---
title: "Introducing odmlib v0.2.0: A More Developer-Friendly ODM/Define-XML Library"
date: 2026-06-22 09:00:00 -0500
categories: [Standards, Open-source]
tags: [odmlib, open-source, cdisc, data-exchange]
description: "odmlib v0.2.0 updates and the push to v1.0"
---

# Introducing odmlib v0.2.0: A More Developer-Friendly ODM/Define-XML Library

odmlib v0.2.0 is the first major release since v0.1.4. The updates have been motivated by requests
from developers building tools using odmlib, the needs of the CDISC 360i Define-XML/CRF Generation Team, and my own personal wish list. Frankly, the updates were overdue, and the surge in usage made it harder to keep believing otherwise. This release also sets the foundation for the road to v1.0. A published roadmap accompanies v0.2.0 and signals a commitment to sustained odmlib development over the coming year.

odmlib v0.2.0 includes a broad set of updates impacting nearly every aspect of the library, with an emphasis on improving the developer experience. From error handling and validation to developer ergonomics and Pythonic ways of working, odmlib v0.2.0 is a significantly more capable toolkit for working with CDISC ODM, Define-XML, and their extensions. This update is backwards-compatible with v0.1.4, though you may see deprecation warnings where a better
alternative is now available.

I plan to publish a series of articles that highlight odmlib features. This first article provides a list of the major improvements in v0.2.0 and highlights a few of them in more detail.
---

## What is odmlib?

odmlib is a Python library for working with CDISC ODM and Define-XML standards. It provides an object-oriented interface to read and write ODM-based content, which is easier than working directly with XML parsers. odmlib serializes documents as XML, JSON, or Python dictionaries and supports round-tripping between these formats, so you can work in JSON and publish a final document in XML if needed.

odmlib supports many existing ODM extensions and makes it easy to implement your own. It includes conformance checks and schema validation to ensure quality and model compliance.

odmlib is used in several research applications, including the CDISC CORE and the CDISC 360i program. And, because it abstracts away the XML plumbing, odmlib is a good fit for generative AI tools. Assistants like Claude and Copilot produce noticeably better applications using odmlib than they produce when asked to manipulate the underlying XML directly. 

---

## odmlib v0.2.0 Updates at a Glance

- **Structured exception hierarchy** replacing bare `ValueError`/`TypeError` across 70+ raise sites
- **Collect-all-errors validation** so you can see every problem in one pass
- **Permissive loading mode** lets you load non-conformant ODM and Define-XML files for inspection and repair
- **Fluent builder API** for constructing ODM documents with less boilerplate
- **Context managers** for safe load-modify-save workflows
- **Dataset-JSON v1.1 model** to read, write, and convert CDISC Dataset-JSON documents
- **DefineFlattener** produces tabular Define-XML metadata as Dataset-JSON v1.1 datasets
- **ARM 1.0 model** for Analysis Results Metadata, integrated with Define-XML 2.1
- **Expanded ODM v2.0 model** covering Study metadata and AdminData (ClinicalData support targeted for v0.3.0)
- **Valueset regex validation** with reusable `describe()` for documentation and error messages
- **Optional pandas DataFrame integration** for metadata export and flattening features
- **Dynamic OID ref/def checking** via model introspection; works automatically for new models
- **Automatic element ordering on serialization** — output respects the model's declared element order regardless of
  how attributes were assigned
- **Type hints and `.pyi` stubs** for IDE autocomplete and static analysis
- **Expanded and improved documentation** that is more comprehensive and user-friendly
- **Security hardening** removed `eval()` and `exec()` calls from the codebase
- **Modern `pyproject.toml` packaging** with GitHub Actions CI on Python 3.10–3.13
- **AI-ready documentation** includes shipping `CLAUDE.md` with v0.2.0; a dedicated Claude Code skill follows in v0.2.1
- **Community infrastructure** adds `GOVERNANCE.md`, `CONTRIBUTING.md`, `CONTRIBUTORS.md`, and GitHub Discussions
- **>1,200 tests at 94% coverage**, up from 372 tests in the prior release
- **Updated examples** in the odmlib_examples repo include new example programs highlighting v0.2.0 features

With the at-a-glance covered, the rest of this article digs into several of the headline features. 

---

## Structured Error Handling

Prior to v0.2.0, odmlib raised bare `ValueError` and `TypeError` exceptions. If you were building a Define-XML document and made a mistake, you'd get something like:

```
ValueError: ItemOID attribute is required
```

odmlib v0.2.0 introduces a complete exception hierarchy rooted at `OdmlibError` with more targeted exceptions and friendly, helpful messages. The specialized exception classes include:

```python
from odmlib.exceptions import (
    OdmlibError,
    OdmlibValidationError,
    OdmlibRequiredAttributeError,
    OdmlibTypeError,
    OdmlibOIDError,
    OdmlibConformanceError,
    OdmlibElementOrderError,
)
```

Each validation exception carries attributes that help you locate and fix the problem. The string representation gives you a readable message; the structured attributes let you build tooling around them:

```python
try:
    item_ref = ODM.ItemRef(Mandatory="Yes")  # Missing required ItemOID
except OdmlibRequiredAttributeError as e:
    print(e)
    # ItemRef requires the 'ItemOID' attribute. Provide it when constructing
    # the element, e.g., ItemRef(ItemOID="IT.AGE", Mandatory="Yes").
    print(e.attribute)      # "ItemOID"
    print(e.element_type)   # "ItemRef"
```

Type errors now tell you what was expected:

```python
try:
    item = ODM.ItemDef(OID="IT.01", Name="AGE", DataType="integer",
                       Length="not_a_number")
except OdmlibTypeError as e:
    print(e.attribute)      # "Length"
    print(e.expected_type)  # The expected type description
    print(e.actual_value)   # "not_a_number"
```

OID validation, conformance checking, element ordering, namespace errors, parsing errors, and serialization errors each have their own exception class. This means you can write targeted `except` blocks for the kinds of errors you care about.

### Collect-All-Errors Validation

One of my favorite improvements: instead of stopping at the first validation failure, you can now collect all errors in a single pass. Useful when your metadata spreadsheet has, let's say, twenty problems, and you'd rather see them all than discover them one stacktrace at a time:

```python
from odmlib.oid_generator import create_oid_checker

checker = create_oid_checker("odm_1_3_2")
errors = odm.validate(collect_errors=True, oid_checker=checker)
for err in errors:
    print(err)
```

When `collect_errors=False` (the default), behavior is unchanged and the first error raises immediately. When `collect_errors=True`, the method returns a list of all errors found.

---

## Permissive Loading Mode

Structured errors give you better diagnostics, but they don't help if odmlib refuses to load the document in the first place. That's where permissive loading comes in.

A significant new capability in v0.2.0 is the ability to load ODM and Define-XML documents that don't fully conform to their specifications. This addresses a recurring real-world problem: you need to work with a Define-XML file that has missing required attributes, malformed values, or partial metadata.

The new `permissive()` context manager temporarily relaxes validation so the loader will read the document into the object model. Once loaded, you can use the full odmlib API to discover what's wrong, fix it programmatically, and write out a conformant file.

```python
from odmlib import permissive
from odmlib.loader import ODMLoader
from odmlib.odm_loader import XMLDefineLoader

loader = ODMLoader(XMLDefineLoader())

# Strict mode (default) - raises on the first error
# loader.open_odm_document("broken.xml")  # OdmlibRequiredAttributeError

# Permissive mode — loads the document even with errors
with permissive():
    loader.open_odm_document("broken.xml")
    define = loader.root()

# Mode is back to strict outside the context. Now you can inspect:
errors = define.validate(collect_errors=True)
print(f"Found {len(errors)} issues:")
for err in errors:
    print(f"  - {err}")
```

Permissive mode is implemented via a `ValidationMode` flag enum with graduated control. If you only want to skip specific validation categories, say, allow missing required attributes but still enforce type checks. you can combine flags:

```python
from odmlib import permissive
from odmlib.mode import ValidationMode

# Skip required-attribute and valueset checks; keep type enforcement
with permissive(ValidationMode.SKIP_REQUIRED | ValidationMode.SKIP_VALUESET):
    loader.open_odm_document("partial.xml")
```

---

## A More Pythonic Developer Experience

Beyond error handling, v0.2.0 makes the routine workflows more Pythonic.

### The Builder API

Building an ODM document the manual way involves a tree of nested objects, and the local variables to match. The new `ODMBuilder` provides a fluent, chainable alternative:

```python
from odmlib.builder import ODMBuilder

odm = (ODMBuilder("odm_1_3_2")
    .set_file(FileOID="F.001", FileType="Snapshot",
              CreationDateTime="2024-01-01T00:00:00")
    .add_study(OID="S.001",
               study_name="My Study",
               study_description="A phase II study",
               protocol_name="PROT-001")
    .add_metadata_version(OID="MDV.001", Name="Version 1")
    .add_item_group_def(OID="IG.DM", Name="Demographics", Repeating="No")
    .add_item_ref(ItemOID="IT.SUBJID", Mandatory="Yes", OrderNumber=1)
    .add_item_ref(ItemOID="IT.AGE", Mandatory="No", OrderNumber=2)
    .add_item_def(OID="IT.SUBJID", Name="SUBJID", DataType="text")
    .add_item_def(OID="IT.AGE", Name="AGE", DataType="integer")
    .add_code_list(OID="CL.SEX", Name="Sex", DataType="text",
                   items=[{"CodedValue": "M", "Decode": "Male"},
                          {"CodedValue": "F", "Decode": "Female"}])
    .build())

odm.write_xml("study.xml")
```

The builder is purely additive. The existing direct-construction API is unchanged and remains the primary interface. Builders for Define-XML and Dataset-JSON are on the roadmap for v0.4.0, and the ODM builder will be expanded.

### Context Managers for Load-Modify-Save

A common workflow is loading an ODM file, making changes, and writing it back. The new context managers handle the boilerplate:

```python
from odmlib.context import open_odm, open_define

# Load, modify, and save an ODM file
with open_odm("study.xml", output_file="study_updated.xml") as odm:
    mdv = odm.Study[0].MetaDataVersion[0]
    # Add a new ItemGroupDef, modify attributes, etc.
    mdv.ItemGroupDef.append(new_igd)
# File is automatically written on clean exit; not written if an exception occurs

# Works with Define-XML too
with open_define("define.xml", output_file="define_updated.xml") as define:
    mdv = define.Study.MetaDataVersion
    print(f"ItemDefs: {len(mdv.ItemDef)}")
```

Format (XML or JSON) is auto-detected from the file extension, and you can specify a different model package if needed. If an exception propagates out of the `with` block, the file is not written and your source file stays safe.

### Better Element Lookup

The existing `find()` method returns the first match for a given attribute value. When you wanted all matches, you wrote a loop. v0.2.0 adds two new methods that handle the common cases directly:

```python
# Find ALL mandatory ItemRefs (not just the first)
mandatory_refs = igd.find_all("ItemRef", "Mandatory", "Yes")

# Find by multiple criteria at once
ref = igd.find_by("ItemRef", ItemOID="IT.AGE", Mandatory="Yes")
```

`find_all()` returns a list of all matching elements. `find_by()` accepts keyword arguments for multi-attribute matching and returns the first element where all criteria match, or `None`.

---

## Dynamic OID Ref/Def Checking

OID integrity checking is one of odmlib's most valuable and underused features. It verifies that every OID reference in your document points to an actual definition and flags orphaned definitions that nothing references. v0.2.0 now generates these checks dynamically by introspecting the model class definitions themselves:

```python
from odmlib.oid_generator import create_oid_checker

# Create a checker for any supported model
checker = create_oid_checker("odm_1_3_2")

# Use it exactly like before
odm.verify_oids(checker)
checker.check_oid_refs()           # Raises if any ref points to a missing def
```

The practical benefit is that adding OID checking to a new model package, like the expanded ODM v2.0 model or the new ARM 1.0 model, no longer requires a hand-written lookup table.

---

## Final Thoughts

I hope the new features and improvements make odmlib a better Python library for working with CDISC ODM, Define-XML, Dataset-JSON, ARM, and other ODM-based files. For those of you using odmlib today, let me know what you'd like to see next: feature requests, documentation gaps, and example program ideas are all welcome on GitHub Discussions or as issues on the repository.

- odmlib: [github.com/swhume/odmlib](https://github.com/swhume/odmlib)
- Examples: [github.com/swhume/odmlib_examples](https://github.com/swhume/odmlib_examples)

The v0.2.0 release closes one chapter and opens another as odmlib moves toward v1.0. The shorter, more focused follow-up articles will dig into individual features as the road to v1.0 unfolds.
