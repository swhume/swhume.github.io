# The Dataset-JSON API

This post builds on my [previous Dataset-JSON post](https://www.linkedin.com/posts/sam-hume-dsc_cdisc-phuse-activity-7152706741992890368-7MqT) and covers
a [draft Dataset-JSON API specification](https://github.com/cdisc-org/DataExchange-DatasetJson-API) created during a [COSA](https://cosa.cdisc.org/) 
Hackathon.

The CDISC Open-Source Alliance (COSA) initiated a second COSA Dataset-JSON Hackathon to create a draft REST API specification for exchanging 
Dataset-JSON datasets. With input from hackathon participants, I drafted an API specification using the machine-readable 
[Open API Specification (OAS) 3.1 standard](https://github.com/OAI/OpenAPI-Specification). API specifications in OAS format can be used 
to generate documentation as well as to generate code for API clients. Check out this [list of OAS tools](https://openapi.tools/). For those 
interested in data exchange using Dataset-JSON, please review and comment on the 
[draft specification in the associated GitHub repository](https://github.com/cdisc-org/DataExchange-DatasetJson-API).

**Table 1** shows the endpoints and associated HTTP verbs that form the API. The hackathon participants agreed that the API should support 
CRUD operations, and the HTTP verbs reflect that. Implementing a read-only API using only the GET verbs provides a valid API instance. 
Read-only APIs may be implemented for systems, such as an EDC system, where sponsors can retrieve content, but posting and updating content is 
not supported. Systems that implement the API standard may expand the API’s features by adding supplementary, non-standard endpoints. 
The standard API has been kept intentionally simple for easy implementation and conformance to the standard.

**Table 1. Dataset-JSON API Endpoints**

| **Endpoint** | **HTTP Verb** | **Description** |
| --- | --- | --- |
| /studies | GET | Get the list of available studies |
|  | POST | Create a new study |
| /studies/{studyOID} | GET | Get a study |
|  | PUT | Update a study |
|  | DELETE | Remove a study |
| /studies/{studyOID}/datasets | GET | Get the list of datasets for a study |
|  | POST | Create a new dataset |
| /studies/{studyOID}/datasets/{datasetOID} | GET | Get a dataset |
|  | PUT | Update a dataset |
|  | PATCH | Append records to a dataset |
|  | DELETE | Remove a dataset |
| /docs | GET | Get API OAS documentation |

The API uses the _studyOID_ and _datasetOID_ as keys as they are identifiers in ODM-based standards like Dataset-JSON. Ideally, these keys 
will exclude characters not supported for use in URLs, though the API will generate a legal representation of the keys for use in a URL.

The API specification includes pagination and compression features to improve performance and to support the transfer of large datasets. 
Similar to the way browsers manage compressed data, the Dataset-JSON API software performs the compression and decompression using gzip or 
brotli transparently in the background.

Clients may filter the list of datasets returned for a study by setting the _If-Modified-Since_ header to a specific datetime. If 
the _If-Modified-Since_ header is set, the API returns all datasets with creationDateTime attribute values on or after the datetime specified 
in the header. This allows clients to request datasets that were changed or added since the last time the datasets were retrieved. Clients 
may filter on a specific standard, such as SDTMIG, by setting the _standard_ query parameter.

The draft API specification uses the _application/json_ media type. In the same way the _application/odm+xml_ media type exists for the ODM 
standard, CDISC plans to register a specific Dataset-JSON media type with the IANA, possibly _application/dataset+json_.

In addition to producing a draft API specification, the draft API also seeks to support the PHUSE/CDISC/FDA 
[_Dataset-JSON as Alternative Transport Format for Regulatory Submissions_](https://advance.phuse.global/display/WEL/Dataset-JSON+as+Alternative+Transport+Format+for+Regulatory+Submissions) 
pilot project by highlighting the fact that, as a data exchange standard, Dataset-JSON datasets will be exchanged using APIs more than by file 
transfer. Testing the API for data exchange is out of scope for the pilot since regulatory submissions will continue to use the same file transfer 
method that has been used with SAS XPT datasets.

Using the findings from the _Dataset-JSON as Alternative Transport Format for Regulatory Submissions_ pilot, the CDISC Dataset-JSON standards 
development team has started developing Dataset-JSON v1.1. Once this version of the standard is complete, the Dataset-JSON API specification 
will be updated to reflect the changes.

While the primary purpose of the COSA Hackathon was to create a draft REST API specification for Dataset-JSON, a secondary objective 
was to develop a proof-of-concept implementation of the API. The proof-of-concept implementation helps developers to review and comment 
on the API specification in a more meaningful way. At least one proof-of-concept implementation will be made available for reviewers to 
try out before the end of Q2 2024 and will be featured in a future blog post.

Please use the [CDISC DataExchange-DatasetJson-API GitHub repository](https://github.com/cdisc-org/DataExchange-DatasetJson-API) to add API 
specification issues or comments for discussion.
