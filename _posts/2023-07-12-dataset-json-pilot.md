# No More XPT? Piloting New Dataset-JSON For FDA Submissions

Orignally published in [Clinical Leader on July 12, 2023](https://www.clinicalleader.com/doc/no-more-xpt-piloting-new-dataset-json-for-fda-submissions-0001)

## Introduction

When submitting study datasets, the FDA requires organizations to use the SAS V5 XPORT (XPT), a format that dates back to 1989. Originally 
announced in the FDA’s 1999 
[_Guidance for Industry – Providing Regulatory Submissions in Electronic Format; General Considerations_](https://www.fda.gov/media/71200/download), 
the XPT requirement set the format for representing datasets in the CDISC Foundational Standards. Since then, many aspects of the submission 
process have improved, yet the XPT requirement has remained. The 
[outdated XPT format](https://www.cdisc.org/sites/default/files/2023-05/Transport-for-the-Next-Generation-Version-1.0.pdf) imposes restrictions 
on submission data, including limited data types, no Unicode support, variable name and field size constraints, inefficient use of storage space, 
lack of extensibility, and insufficient metadata. Moreover, XPT’s binary format limits its utility for use in many modern data exchange scenarios.

CDISC developed Dataset-JSON, a new dataset exchange format, to replace XPT. Working with the FDA and industry participants, CDISC and PHUSE 
lead a new pilot project to test Dataset-JSON for use in regulatory submissions as well as other dataset exchange scenarios. 
Dataset-JSON is part of the CDISC ODM v2.0 standard, which will be published in August 2023. It has already been the subject of a 
[successful hackathon that produced a number of open-source tools](https://cosa.cdisc.org/hackathons/datasetJson), including software 
to convert Dataset-JSON to dataset formats, such as SAS datasets, R data frames, and Python data frames. The project, _Dataset-JSON as 
an alternative transport format for regulatory submissions_, begins in the fall of 2023 and incorporates a two-phased evaluation (1) an 
FDA proof-of-concept using existing pre-clinical datasets, followed by (2) an FDA pilot using clinical data. The results of the pilot will 
be published in the first quarter of 2024 and shared at the 2024 PHUSE CSS conference. This project also includes Dataset-JSON focused workshops 
and hackathons sponsored by PHUSE and the CDISC Open-Source Alliance (COSA).

## About Dataset-JSON And Its Benefits

Dataset-JSON is a modern dataset format designed to meet the regulatory requirements for submission datasets as well as support other 
data exchange scenarios. It is based on the 
[CDISC Dataset-XML v1.0 specification](https://www.cdisc.org/standards/foundational/dataset-xml/dataset-xml-v10) with important 
enhancements, including much smaller file sizes and additional metadata. In fact, Dataset-JSON file sizes are smaller than XPT and Dataset-XML. 
Dataset-JSON links to a Define-XML file for more complete metadata. It will be published under the MIT open-source license.

Dataset-JSON is based on [JSON](https://www.json.org/json-en.html), a widely used, easy to implement, 
[lightweight data exchange format](https://www.lexjansen.com/pharmasug/2022/AD/PharmaSUG-2022-AD-150.pdf) that uses human-readable 
text to store and transmit data objects consisting of attribute–value pairs and arrays. JSON is the de facto standard data format for 
data exchange using application programming interfaces (APIs).

Dataset-JSON, as a vendor and technology-neutral standard, works well with a broad range of programming languages and technology stacks. 
Many programming languages include built-in libraries for working with JSON data. Transforming Dataset-JSON into SAS datasets, R data 
frames, or Python Pandas data frames for analysis proves to be a simple task as was demonstrated in CDISC’s 2022 Dataset-JSON hackathon. 
For most programming languages, Dataset-JSON is a straightforward format to process. As the default data exchange format for most APIs, 
a JSON-based standard makes possible the use of modern data exchange technologies for regulatory submissions.

Overcoming the limitations imposed by XPT will initially benefit the regulators and others engaged in dataset exchange. 
The longer-term, more significant benefits will emerge as the constraints imposed on the CDISC Foundational Standards by XPT are removed, 
allowing new standards versions to take advantage of Dataset-JSON’s enhanced capabilities.

## New Software Tools To Support Dataset-JSON

In addition to the JSON support already available in nearly every programming language, a number of new software tools that 
support Dataset-JSON are emerging, including those created as part of our Dataset-JSON Hackathon. These open-source tools perform 
tasks fundamental to a data exchange standard like Dataset-JSON by converting to and from datasets in other formats. The 
hackathon included viewers, streaming features, REST API examples, and other useful tools. Additionally, some existing tool 
makers have committed to natively supporting the Dataset-JSON format, including software solutions like JMP Clinical and 
[CORE](https://www.cdisc.org/core).

Software tools are an essential part of the FDA pilot as they are necessary to convert the Dataset-JSON files into SAS 
datasets and R data frames so that Dataset-JSON can be used as a drop-in replacement for SAS XPT. The FDA pilot will largely 
focus on the use of Dataset-JSON within existing processes with the goal of adding Dataset-JSON to the Data Standards Catalog 
as a standard accepted for regulatory submissions.

PHUSE and COSA plan to host a series of workshops and hackathons to expand the number of open-source software 
tools available that support Dataset-JSON as well as to help developers learn to use Dataset-JSON through hands-on 
experience. Dataset-JSON will be the theme of the 2023 PHUSE CSS conference in September.

## The FDA Pilot: Determining Whether Dataset-JSON Satisfies The FDA And Industry

The challenge in moving from XPT to Dataset-JSON for regulatory submissions is two-fold:
1. ensure that regulatory authorities have sufficient confidence in Dataset-JSON to accept it as an alternative to XPT and
2. ensure that industry can transition to Dataset-JSON with no impact on the submission process.

The workshops, hackathons, and pilot will seek to demonstrate that the above challenges are met. The FDA pilot, as 
currently defined, addresses two primary objectives that will take place in phases.

Phase 1 targets the short-term goal of establishing Dataset-JSON as a drop-in replacement for XPT. This case comprises two 
formats that contain the same data, which can be used interchangeably for regulatory submissions: same content, different suitcase. 
This phase ensures no disruption to existing processes that use XPT today. The objective of this phase is for the FDA to accept 
Dataset-JSON as an alternative transport format for regulatory submissions in addition to the current XPT standard. Sponsors can use 
either XPT or Dataset-JSON with the understanding that support for XPT will eventually be phased out.

Phase 2 targets the longer-term goal of enhancing new versions of the CDISC Foundational Standards to move beyond the XPT restrictions 
that have impacted them. This phase will include developing a new version of Define-XML called Define-JSON based on ODM v2.0, as well as 
creating enhanced conformance rules for each CDISC Foundational Standard. The objective of phase 2 is to deprecate XPT and make Dataset-JSON 
the transport format for regulatory submissions.

The pilot deliverables include:
- a report on the outcomes and findings of the Dataset-JSON submission pilots,
- a business case to highlight the increased usability, flexibility, and other meaningful benefits derived from using Dataset-JSON for data exchange, including for regulatory submissions, and
- a strategy for future development of the CDISC Foundational Standards to leverage the features of Dataset-JSON.

## Getting More Information

The Dataset-JSON specification has been finalized and is available on the [CDISC web site](https://www.cdisc.org/dataset-json). 
The schemas and example datasets are available in a public [GitHub repository](https://github.com/cdisc-org/DataExchange-DatasetJson). 
Software tools created during the Dataset-JSON hackathon are available via the [COSA Directory](https://cosa.cdisc.org/hackathons/datasetJson). 
A curated subset of the hackathon tools will be selected for inclusion in the FDA pilot, though pilot participants may use other tools. 
Information on the PHUSE and COSA workshops and hackathons to help industry prepare to transition to using Dataset-JSON will be announced once 
plans are finalized. Those interested in participating in the pilot should contact [workinggroups@phuse.global](mailto:workinggroups@phuse.global).

### About The Author

Sam Hume leads CDISC’s data science team, which develops tools and standards that support clinical and translational research. 
Sam directs delivery of the CDISC Library, co-leads the Data Exchange Standards team, and serves as a leader of CORE. Additionally, 
he oversees the CDISC Open-Source Alliance (COSA), which supports CDISC-related open-source software projects. Sam has 30 years’ 
experience working in clinical research informatics and has held several senior-level technology positions in the biopharmaceutical industry. 
He holds a doctorate in information systems.
