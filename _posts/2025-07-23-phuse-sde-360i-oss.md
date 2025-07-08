---
marp: true
theme: default
paginate: true
title: Powering Standards with Code - The Role of Open Source in CDISC 360i
description: PHUSE SDE
author: Sam Hume
keywords: 360i, OSS, PHUSE
url: https://swhume.github.io/ 

header: <div><div><img src="https://raw.githubusercontent.com/swhume/swhume.github.io/master/assets/images/360i-logo.png" /> </div> </div>
style: |
    header {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 1fr;
        grid-gap: 10px;
        box-sizing: border-box;
        justify-content: center;
        width: 100%;
    }
    header img {
        height: 125px;
        position: absolute;
        right: 50px;
    }
	
---
# Powering Standards with Code: The Role of Open Source in CDISC 360i
**Sam Hume**
shume@cdisc.org
https://www.linkedin.com/in/sam-hume-dsc
_Opinions are my own_

---
## 360i: Powering Standards with Code
#### _Turning data standards from static specs into dynamic, executable solutions_
1. Standards implementation focus or solutions over specifications
2. Code as part of standards development
3. Code as a communications tool and test framework
4. Consider the HL7 FHIR example

<!--
- Testing standards using open-source applications as part of standards development
- Deliver an executable study package using open-source applications
-->

---
## 360i Deliverables
#### _Publishing executable study packages with open-source software tools_
1. Standards Packages
2. Implementation Cookbooks
3. Example Implementations
4. Executable study package

<!--
1. 	- Linked and executable metadata from study design through analysis results
	- Includes concepts, rules, and sample data
2. 	- Instructions to build standards packages
	- Recipes to implement packages within your processes
3. 	- OSS software enabled example leveraging packages and recipes
	- Library of community-based open-source tools 
-->
---
## CI/CD for CDISC
#### _Treating standards as software: version-controlled, testable, and automatable_
1. Test each standard as it's being developed
2. Test standards in an automated pipeline context
3. Test data is part of standards development
4. Ensure tooling is available when new standards are released

<!--
Consider implementing automated standards updates
Standards models need tooling and tests
Publish models with test data for PR so standards can be tested using tools
-->

---
## 360i Automated Pipeline
![center:75%](https://raw.githubusercontent.com/swhume/swhume.github.io/master/assets/images/automated-pipeline.png)

---
## Why Open-Source Software for 360i?
#### _Driving Standards Implementation Through Shared Tools and Transparent Code_
1. 360i seeks to promote a common set of tools for standards-driven automation
2. Promotes consistency and interoperability while lowering barriers to adoption
3. CDISC brings in volunteers from across the industry, need free tools
4. OSS innovation is strongest in ecosystem-driven industries like life sciences 

<!--
There are all kinds of reasons CDISC should be engaged in open-source, I'll touch on a couple
Historically, CDISC has opted not to fully embrace the tech. That's the rock I've been pushing uphill for the last 
decade plus. But now at least they're convinced that we need to focus on implementation
Common tooling can help deliver common work flows and data flows
 — where the community can prototype, test, and refine standards and tools together
A shared foundation for innovation and collaboration
Honesty, transparency, reproducibility
3. Value transparency, reproducibility, and interoperability
4. Need to collaborate across organizations or borders
2. Need for shared data models and analysis tools
Value standards, reusable components, and collaborative problem-solving
-->

---
## COSA and 360i
#### _Code is becoming a critical part of data standards and standards development_
1. 360i uses COSA tools to demonstrate an automated study pipeline
2. COSA hackathons will help accelerate 360i
3. COSA will add a directory of open-source applications used by 360i
4. Seek to collaborate with Pharmaverse and PHUSE

<!--
360i is creating an automated study data pipeline driven by standards
Pharmaverse collaboration will be especially effective in Phase 2
The hackathons have been very productive. Our Dataset-JSON Viewer hackathon produced some great tools.
New tools and new features
There's more than one way to do it (TMTOWTDI)
Submit your open-source applications
-->

---
## Lucy, you’ve got a lot of explaining to do
#### _360i open-source gives us the bazaar—a messy, fast-moving place where innovation happens._
1. Coding, as with painting, starts with sketching - Paul Graham
2. Open-Source as experimentation and communication: Sandboxes
3. The cathedral and the bazaar - Eric Raymond
4. Plan to throw one away; you will, anyhow - Fred Brooks

---
## Dumbing it Down
#### _Open-Source Is How We Scale Standards Adoption_
1. Code libraries make it simpler to implement complex data standards
2. Abstractions in code are essential to simplifying implementation
3. Code helps reduce the variability in standards implementations
4. See FHIR and OMOP as examples where tooling plays a major role

<!--
Ironic, as a big part of my job or complaints about me have been to dumb it down or take a business focus
Avoid talking about code because that's too techie
Abstractions hide some of the complexities of the CDISC standards
The software, through abstractions, can make the standards easier to implement
Reduces variations in standards representations
May aid in managing standards versioning
-->

---
## OSS and Risk Taking
#### _Open-source lets us explore what commercial vendors often can’t or won’t_
| Factor                | Open-Source | Commercial                    |
|-----------------------|-------------|-------------------------------|
| Speed of Innovation   | Often faster | Slower but more polished      |
| Scope of Innovation   | Broader and grassroots | Focused; customer-driven      |
| Community Involvement | High | Low to none                   |
| Risk Taking | High | Lower (ROI focused) |
| Resource Constraints | May limit scope | Can fund ambitious R&D        |
| UX and Enterprise Fit | Often weaker | Often stronger                |

<!--
This, in part, explains why we're not further along in common automation pipelines
The management class at sponsors and vendors often embody risk avoidance
OSS high risk taking allows exploring edge cases
-->

---
## 360i phase 1 roadmap
![center:80%](https://raw.githubusercontent.com/swhume/swhume.github.io/master/assets/images/360i-phase1-flowchart.png)

---
## Phase 1: Study Design through SDTM Generation
#### _New approaches to old problems_
1. Using USDM + BCs + DSS to drive automated SDTM generation pipeline
2. Identifying and filling gaps in the process
3. Creating recipes that will allow the development of common tools
4. Uses Open Study Builder, sdtm.oak, odmlib, Dataset-JSON tools, etc.

<!-- working through our technical roadmap 
Include a table or list of OSS tools
-->
---
## Phase 2: ADaM through TLF Generation
#### _Phase 2 is where we focus on clinical reporting_
1. Defining Analysis Concepts
2. Makes use of the ARS standard
3. Uses the Phase 1 SDTM datasets as input
4. Will use siera, Admiral, and other Pharmaverse pacakges

<!--
define analysis concepts
-->
---
## Example: Automated SDTM Define-XML Generation
#### _Turning Study Metadata into Define-XML via Open Tools_
1. What's different about 360i: use USDM + BCs + DSSs
2. USDM + BCs + DSSs are not sufficient
3. Plan to create metadata templates available via the Library API
4. Sustaining vs. Disruptive Innovation

<!--
Recipe + Tools for Define-XML Generation
-->

---
## Call to Action
#### _The Future of Standards Depends on Who Shows Up_
1. Participate in 360i: https://www.cdisc.org/cdisc-360i
2. Submit solutions to COSA for listing: https://cosa.cdisc.org
3. Participate in COSA-sponsored hackathons
4. Contribute to content creation

<!--
What hackathons would you be interested in participating in? In helping to lead?
360i end-to-end use cases: RWD, DHT, eDT
Collaborative development for CDISC Biomedical Concepts: https://github.com/cdisc-org/COSMoS/blob/main/bc_starter_package
-->

---
![bg left 80%](https://raw.githubusercontent.com/swhume/swhume.github.io/master/assets/images/question-mark.jpeg)

# Questions?
#### _If we want standards to be usable, they need to be executable, and that starts with us. I’d love to hear your thoughts._
<!--
Seed questions:
-->

---
## Example CDISC 360i Phase 1 OSS 

| Application          | Repository                                                 |
|----------------------|------------------------------------------------------------|
| CDISC Library Client | https://github.com/cdisc-org/cdisc-library-client          |
| CORE                 | https://github.com/cdisc-org/cdisc-rules-engine            |
| CORE Rule Editor     | https://github.com/cdisc-org/conformance-rules-editor      |
| CDISC ODM-XML CRF SDTM Annotations | https://github.com/jmangori/CDISC-Define-XML-SAS-XMLMAP    |

---
## Example CDISC 360i Phase 1 OSS (continued)

| Application          | Repository                                                 |
|----------------------|------------------------------------------------------------|
| Dataset-JSON Conversion (SAS) | https://github.com/lexjansen/dataset-json-sas              |
| Dataset-JSON Conversion (R)   | https://atorus-research.github.io/datasetjson/index.html   |
| Dataset-JSON Viewer | https://github.com/defineEditor/vde-dataset-viewer         |
| Define-XML Stylesheet | https://github.com/lexjansen/define-xml-2.1-stylesheets    |

---
## Example CDISC 360i Phase 1 OSS (continued)

| Application          | Repository                                                 |
|----------------------|------------------------------------------------------------|
| odmlib              | https://github.com/swhume/odmlib                           |
| Open Study Builder  | https://github.com/NovoNordisk-OpenSource/openstudybuilder-solution |
| sdtm.oak            | https://github.com/pharmaverse/sdtm.oak                    |
| Study Definitions Workbench | https://github.com/data4knowledge/study_definitions_workbench |
