# Introducing odmlib

As a Python developer I’ve had an interest in an ODM library that makes it easy to work with ODM and Define-XML 
documents. During the CDISC 360 project, I worked on generating ODM and Define-XML documents using an object-oriented 
approach. As I moved on from development work on the project, I decided to start developing a Python package that I 
could re-use on future projects and satisfy my personal interest in an object-oriented library for creating and 
processing ODM documents and its extensions. This package, named odmlib, remains under development but can be used for 
basic metadata processing.

Odmlib simplifies working with the CDISC ODM data exchange standard and its extensions in Python. It supports an 
object-oriented approach and serializations in XML and JSON. Odmlib also supports conformance checks and schema 
validation to ensure quality and standards compliance.

You can find [odmlib on Github](https://github.com/swhume/odmlib). If you’re interested in experimenting with it, I 
would recommend trying out one of the [example applications](https://github.com/swhume/odmlib_examples). The best place 
to start is the get_started application to create and process a basic ODM file.

To get acquainted with odmlib, let’s take a look at what amounts to the “hello, world” of ODM file creation. Before 
you can use odmlib, you’ll need to install it. Although it’s still under development, a version of odmlib is available 
on PyPI. Although not the most up-to-date, it’s the easiest to install:
```
pip install odmlib
```

Since it’s still in development, if you want the latest version, to keep up with updates, or to contribute to its 
development you’ll need to install it from the source. See the Getting Started section in the README.md in the odmlib 
repository for details.

Now, let’s create the ODM root element. To create the root object, the object name is the same as the element name and 
the attributes are set as part of object creation:
```python
root = ODM.ODM(
	FileOID="ODM.DEMO.001", 
	Granularity="Metadata", 
	AsOfDateTime=current_datetime, 
	CreationDateTime=current_datetime, 
	ODMVersion="1.3.2", 
	FileType="Snapshot", 
	Originator="Hume Data Labs", 
	SourceSystem="odmlib", 
	SourceSystemVersion="0.1"
)
```

Now the variable root is set to the ODM object. All that remains is to create the child elements by instantiating and 
appending them in the right order. For example, the Study element is created next and appended to ODM as follows:
```python
root.Study.append(ODM.Study(OID="ODM.GET.STARTED"))
```

A Study object is created with the OID set to “ODM.GET.STARTED” and appended to root.Study. When there can be multiple 
instances of an element, as is the case with Study, use a list to represent that element. The ODM standard specifies 
that there can be 0 or more Study elements under the parent ODM element, as shown below:
```python
ODM(Study*, AdminData*, ReferenceData*, ClinicalData*, ...)
```

Follow this same approach to create the rest of this simple ODM file. Keep in mind the order in which you add elements 
should match the order in the ODM specification. For example:
```python
root.Study[0].GlobalVariables = ODM.GlobalVariables()
root.Study[0].GlobalVariables.StudyName = 
ODM.StudyName(_content="Get Started with ODM XML")
root.Study[0].GlobalVariables.StudyDescription = 
ODM.StudyDescription(_content="Getting started with odmlib")
root.Study[0].GlobalVariables.ProtocolName = 
ODM.ProtocolName(_content="ODM XML Get Started")
```

This basic process is repeated to complete building the ODM file. Once all the content has been created, the ODM file 
can be generated as XML and written to a file as follows:
```python
root.write_xml("./data/simple_create.xml")
```

If you want to generate JSON instead of XML, root can be serialized as JSON as follows:
```python
root.write_json(“./data/simple_create.json”)
```

Now you’ve got an ODM XML file. Here’s the entire example that shows creating a very simple ODM file in XML.
```python
import odmlib.odm_1_3_2.model as ODM
import datetime

ODM_XML_FILE = "./data/simple_create.xml"
ODM_JSON_FILE = "./data/simple_create.json"

current_datetime = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
root = ODM.ODM(FileOID="ODM.DEMO.001", Granularity="Metadata", AsOfDateTime=current_datetime,
               CreationDateTime=current_datetime, ODMVersion="1.3.2", FileType="Snapshot",
               Originator="swhume", SourceSystem="odmlib", SourceSystemVersion="0.1")

# create Study and add to ODM
root.Study.append(ODM.Study(OID="ODM.GET.STARTED"))

# create the global variables
root.Study[0].GlobalVariables = ODM.GlobalVariables()
root.Study[0].GlobalVariables.StudyName = ODM.StudyName(_content="Get Started with ODM XML")
root.Study[0].GlobalVariables.StudyDescription = ODM.StudyDescription(_content="Demo to get started with odmlib")
root.Study[0].GlobalVariables.ProtocolName = ODM.ProtocolName(_content="ODM XML Get Started")

# create the MetaDataVersion
root.Study[0].MetaDataVersion.append(ODM.MetaDataVersion(OID="MDV.DEMO-ODM-01", Name="Get Started MDV",
                                                         Description="Get Started Demo"))
# create Protocol
p = ODM.Protocol()
p.Description = ODM.Description()
p.Description.TranslatedText.append(ODM.TranslatedText(_content="Get Started Protocol", lang="en"))
p.StudyEventRef.append(ODM.StudyEventRef(StudyEventOID="BASELINE", OrderNumber=1, Mandatory="Yes"))
root.Study[0].MetaDataVersion[0].Protocol = p

# create a StudyEventDef
sed = ODM.StudyEventDef(OID="BASELINE", Name="Baseline Visit", Repeating="No", Type="Scheduled")
sed.FormRef.append(ODM.FormRef(FormOID="ODM.F.DM", Mandatory="Yes", OrderNumber=1))
root.Study[0].MetaDataVersion[0].StudyEventDef.append(sed)

# create a FormDef
fd = ODM.FormDef(OID="ODM.F.DM", Name="Demographics", Repeating="No")
fd.ItemGroupRef.append(ODM.ItemGroupRef(ItemGroupOID="ODM.IG.DM", Mandatory="Yes", OrderNumber=2))
root.Study[0].MetaDataVersion[0].FormDef.append(fd)

# create an ItemGroupDef
igd = ODM.ItemGroupDef(OID="ODM.IG.DM", Name="Demographics", Repeating="No")
igd.ItemRef.append(ODM.ItemRef(ItemOID="ODM.IT.DM.BRTHYR", Mandatory="Yes"))
root.Study[0].MetaDataVersion[0].ItemGroupDef.append(igd)

# create an ItemDef
itd = ODM.ItemDef(OID="ODM.IT.DM.BRTHYR", Name="Birth Year", DataType="integer")
itd.Description = ODM.Description()
itd.Description.TranslatedText.append(ODM.TranslatedText(_content="Year of the subject's birth", lang="en"))
itd.Question = ODM.Question()
itd.Question.TranslatedText.append(ODM.TranslatedText(_content="Birth Year", lang="en"))
itd.Alias.append(ODM.Alias(Context="CDASH", Name="BRTHYR"))
itd.Alias.append(ODM.Alias(Context="SDTM", Name="BRTHDTC"))
root.Study[0].MetaDataVersion[0].ItemDef.append(itd)

# save the new ODM document to an ODM XML file
root.write_xml(ODM_XML_FILE)

# save the same ODM document to a JSON file
root.write_json(ODM_JSON_FILE)
```

That’s a very basic introduction to creating a simple ODM file using odmlib. Next post will cover reading and 
processing this file. I’ll cover working with Define-XML in future posts.