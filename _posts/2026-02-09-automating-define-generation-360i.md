---
title: "Automating Define-XML Generation in CDISC 360i"
date: 2026-02-09 09:00:00 -0500
categories: [Standards, Open-source]
tags: [open-source, cdisc, data-exchange]
description: "Update on progress generating Define-XML in CDISC 360i"
---

# Automating Define-XML Generation in CDISC 360i
The big idea behind the 360i Define-XML work is pretty simple: stop hand-crafting define.xml
metadata files and start generating them automatically from standard, reusable metadata
starting with the study design. Less spreadsheet gymnastics. Fewer copy-paste errors.
Increased automation. And a lot more transparency thanks to open-source tools and open
models.

We just completed 360i Phase 1, where we built a new model and working code to automatically
generate a valid SDTM define.xml. As we head into Phase 2, we’re refining what we built in
Phase 1, starting with ADaM define.xml generation and taking another step toward our long-term
360i goal: *end-to-end automation*.

## What we’re trying to do (high-level)
The Define-XML team is focused on four things:
1. **Fully automate generating define.xml** files, shell datasets, and CRFs using published metadata (maximize automation and minimize manual editing).
2. Create a new **Data Definition Specification (DDS)** model designed specifically for automation.
3. Use new metadata sources such as **USDM, Biomedical Concepts (BC), Dataset Specializations (DSS), and Analysis Concepts/Derivation Concepts (AC/DC)**, to produce higher-quality, more consistent define.xml files.
4. Deliver this capability via **open-source software** that any organization can use.

## Why this matters
Today’s define.xml generation process often looks something like this:
1. Grab an Excel metadata spreadsheet,
2. Do lots of cutting and pasting and manual metadata entry,
3. Run a proprietary software tool to convert the spreadsheet metadata into a define.xml file
4. Validate the define.xml file against the schema,
5. Run the stylesheet against the define.xml file,
6. Review the HTML version of the define.xml,
7. Rinse and repeat until you have a complete define.xml file.

It works… but it doesn’t scale well. It’s not exactly automation-friendly, and the quality of
the define.xml file produced suffers.

Our 360i approach focuses on automation using standardized, reusable metadata. We start with a
**USDM-based study design**, pull in BCs and DSSs, populate the **DDS (a JSON-based spec)**,
and then generate define.xml from it without manually authoring metadata. The goal isn’t to
pretend study-specific nuances don’t exist; it’s to generate a complete baseline define.xml
automatically and limit manual edits to only those details that are truly study specific. As
we’ve worked toward this goal, we’ve uncovered some metadata gaps that we’ll need to address
before we achieve our automation ambitions.

## What we delivered in Phase 1
- A working pipeline that generates a **valid SDTM define.xml** from the DDS
- The DDS populated from **USDM, BCs, and DSSs**, with gaps filled from the **CDISC Library** where needed
- A list of **metadata gaps** (e.g., Key Sequence, Repeating) that need to be addressed to reach full automation

Addressing those gaps is front and center in **Phase 2 and is part of 360i overall**.

## What’s next
In Phase 2, we’ll:
- Extend this approach to ADaM define.xml using concepts published by the AC/DC team
- Close metadata gaps identified in Phase 1 and document any new gaps uncovered
- Continue aligning everything around standard models so automation isn’t locked into custom tooling
- Continue to refine the open-source software tool towards a release that can be used in practice

And because we live in the real world, we’re not ignoring today’s reality. Many organizations
aren’t using USDM or BCs yet, so we’re also enabling the software to consume existing metadata
spreadsheets, populate the DDS, and generate the define.xml file using the spreadsheet
metadata.

## Open source, community development
A key goal here is building an **open-source community**. Open-source development lowers
costs, accelerates innovation, and lets us try ideas that might be too risky for commercial
tools. Everyone benefits, including commercial vendors.

The code and models are still evolving as we kick off Phase 2, but we’re planning a **trial
release by the end of the year**. Our next interim release, scheduled for the CDISC Europe
Interchange, focuses on an update to our Phase 1 work that automates SDTM define.xml
generation. In the long term, our goal is to raise the bar for Define-XML generation and make
automation the default, not the exception.

## Sound interesting?
If you’re interested in advancing the current state-of-the-art in Define-XML generation, we’re accepting volunteers interested in contributing. Just head to the [CDISC website volunteer page](https://www.cdisc.org/volunteer/form), select the 360i team, and in the text box specify the 360i Define-XML Team.

If you’re attending the Europe Interchange, our team will be giving a presentation titled Automating Define-XML Generation using a New Metadata Specification Model in the CDISC 360i Program, so make sure you [look for that session in the conference program](https://www.cdisc.org/events/interchange/2026-cdisc-europe-interchange/program).

As we’ll be working with the AC/DC team in Phase 2, I’ll close this by saying *‘For those about to automate define.xml generation, we salute you.’*
