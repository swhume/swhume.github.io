# Top 10 Reasons for Using Dataset-JSON over Parquet for Data Exchange

One frequently asked question regarding Dataset-JSON is: Why not Apache Parquet? Parquet is not the most widely used 
format by statistical programmers in our industry, that remains SAS7BDAT, but it is a standard format that's growing 
in popularity, particularly among R programmers. There's very little debate regarding the need to replace SAS V5 XPT 
with something released in this century. While some programmers have gravitated towards the idea of a standardized 
binary dataset format like Parquet, here's why Dataset-JSON is the better choice for clinical research data exchange.

## 1. It's in the DNA: JSON for Exchange, Parquet for Analytics

Dataset-JSON is a data exchange standard representing tabular datasets as JSON or NDJSON. JSON is the de facto 
standard for data exchange, especially via RESTful APIs, and NDJSON provides a streamable alternative that accommodates 
large datasets. Importantly, the JSON specification itself is stable and unchanging, so you won't wake up to breaking changes like "JSON 3.0" that deprecates your code. Dataset-JSON as a standard, however, is versioned to evolve with industry needs.

Text-based standards like JSON offer key advantages for data exchange: they're human-readable, suitable for long-term 
archival, and work seamlessly with version control systems like Git, making it easy to track dataset changes over time.

Apache Parquet, currently on version 2.12.0, is a binary format optimized for data analytics, specifically for 
efficient storage and retrieval in analytical workflows. Different purpose, different design.

## 2. An FDA Evaluation Selected JSON

In 2022, the FDA evaluated alternatives to replace SAS V5 XPT and selected JSON as the preferred data exchange format. 
You'll find a reference to this in the [Federal Register Notice](https://www.federalregister.gov/documents/2025/04/09/2025-06051/electronic-study-data-submission-data-standards-clinical-data-interchange-standards-consortium) 
requesting comments on the Dataset-JSON standard.

## 3. We Have a Standard Ready Now

We've developed, published, tested, and piloted the Dataset-JSON standard. It's ready to use today. Dataset-JSON is 
our best and fastest path to replacing SAS V5 XPT. The collaborative pilot between CDISC, PHUSE, and the FDA 
demonstrated that Dataset-JSON functions as a drop-in replacement for XPT. The pilot included FDA testing and 
submitting datasets through the test ESG. Dataset-JSON is ready to support your tabular data exchange needs, today.

## 4. API-Based Exchange Is the Future

Dataset-JSON was designed to support both API and file-based data exchange. API-based exchange is expected to become 
the primary method by transaction volume, with the standard API specification supporting pagination, compression, and 
streaming for good performance.

Here's where it gets interesting: for many API use cases, implementers never read or write Dataset-JSON files. The 
server reads data from a datastore, formats it as Dataset-JSON on-the-fly, and sends it to the client. The client 
receives it and may write it to a native format like Parquet or SAS7BDAT. The format excels as the _transfer medium_.

## 5. NDJSON: Streaming Power for Large Datasets

NDJSON (Newline Delimited JSON) provides an alternative Dataset-JSON format that makes it simple to process large 
datasets. Applications can read or write one row of JSON at a time. Some JSON libraries attempt to read entire datasets 
into memory, which doesn't work for very large datasets. NDJSON solves this elegantly: any JSON library can read/write 
Dataset-JSON datasets without exceeding system resources. It also provides a natural format for streaming datasets via 
the standard API.

The Dataset-JSON standard doesn't stipulate when to use JSON versus NDJSON, but many prefer NDJSON for file processing 
and JSON for API data transfers.

## 6. Optimized for What Matters in Data Exchange

Dataset-JSON optimizes for what matters in data exchange: reliability, compatibility, and simplicity, rather than raw 
I/O speed. Since exchange datasets are typically read once and transformed into operational formats, obsessing over 
read/write performance misses the point. It's like optimizing a delivery truck for drag racing.

Many Dataset-JSON exchanges never touch a physical file. When using file-based exchange, the dataset is transformed 
into an operational format where all subsequent operations occur. The exchange format's job is to reliably get data 
from point A to point B in a way that's agnostic to the technology stack used by A or B.

## 7. Simple to Implement with Minimal Dependencies

Despite being a relatively new standard, many applications have implemented Dataset-JSON. Developers consistently note 
the ease and speed of developing tools that work with Dataset-JSON. The CDISC Open-Source Alliance (COSA) has hosted 
two hackathons to build Dataset-JSON software, resulting in numerous high-quality open-source tools including 
conversion utilities, viewers, conformance checkers, APIs, and more.

Here's a practical win for developers: JSON libraries tend to have minimal dependencies. Python developers? The json 
module comes built-in; no pip install, no dependency hell. Parquet, on the other hand, tends to require Apache Arrow 
C++ bindings, a whole different beast to manage. JSON is supported by nearly every programming language and platform. 
Many software applications already import or export JSON-formatted data.

## 8. Beyond Submissions: Supporting the Full Data Ecosystem

Dataset-JSON was developed to address a broad range of data exchange scenarios beyond those traditionally supported by 
statistical programming environments. This includes data exchange involving EDC systems, ePRO platforms, labs, and 
other raw data sources. Dataset-JSON supports any scenario that involves exchanging tabular datasets. Regulatory 
submissions are just one use case.

Some organizations have started including Dataset-JSON datasets as part of their data lake solutions because it 
provides a neutral format easily implemented by any system that generates tabular data. The Compressed Dataset-JSON 
format provides an alternative that significantly reduces dataset size for storage and transfer.

## 9. Aligned with Healthcare Standards (HL7 FHIR)

The use of JSON for data exchange aligns perfectly with those working with HL7 FHIR. HL7 FHIR data is primarily 
exchanged using JSON via APIs. Bulk FHIR transfers use NDJSON to make processing large data files easier. This 
alignment matters significantly to regulatory authorities and those working with Real World Data (RWD). Speaking the 
same data language reduces integration friction across healthcare and research systems.

## 10. Part of the CDISC Ecosystem

Dataset-JSON aligns with CDISC's broad use of JSON for data exchange. The Unified Study Definition Model (USDM) for 
digitized protocol and study design has a standard API that implements the JSON media type. The Analysis Results 
Standard, CORE, CDISC Library, ODM v2.0, and other standards support JSON-based data exchange. Using Dataset-JSON means 
you're working with the grain of the ecosystem, not against it.

## Why the Parquet Appeal?

It's worth acknowledging why some R programmers gravitate toward Parquet. For analytical workloads, Parquet offers 
real advantages: columnar storage means faster queries when you're analyzing specific variables across millions of 
records, efficient compression reduces storage costs, and read/write speeds are optimized for analytical patterns. 
These are genuine strengths.

But here's the key distinction: those strengths are optimized for _analytics_, not _exchange_. Once you've received 
data via Dataset-JSON, you're free to convert it to Parquet, or SAS7BDAT, or other formats for use in your analytical 
pipeline. The exchange format and the analytics format serve different masters.

## The Bottom Line

While Parquet excels as an analytics format, Dataset-JSON was purpose-built for the data exchange challenges we face 
in clinical research. It's API-ready, backed by a rapidly growing ecosystem of tools, and a proven drop-in replacement 
for SAS V5 XPT in regulatory submissions. More importantly, it's ready to use today.