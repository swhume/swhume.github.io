# The CDISC Open Rules Engine (CORE): Open-Source Software For Clinical Research

Oringally published in 
[Clinical Leader on April 29, 2023](https://www.clinicalleader.com/doc/the-cdisc-open-rules-engine-core-open-source-software-for-clinical-0001)

Open-source software development, widely used across most industries globally, has recently been gaining ground in clinical research. 
Substantial advantages in cost, the pace of innovation, and delivery options have long been acknowledged as strengths of open-source 
software. However, regulated clinical research places additional demands on software, including validation requirements and ensuring 
results are accurate and reproducible. These regulatory burdens hindered the movement of open-source software solutions into clinical 
research, but increasingly industry recognizes that the value generated though a collaborative open-source development approach outweighs 
the challenges introduced by this development model. Faster rates of innovation, at lower total cost of ownership through collaborative 
implementation of industry best practices, benefit the software itself and can yield similar advantages for the documentation, testing, 
and validation of the software.

Open source democratizes innovation for software developers as well as for implementers using the software. Given the growing 
interest in the benefits of open-source, it’s not surprising to see the emergence of industry-led initiatives supporting open-source 
software development, including the [CDISC Open-Source Alliance (COSA)](https://www.cdisc.org/cosa), 
[pharmaverse](https://pharmaverse.org/), [openpharma](https://www.openpharma.blog/), and the 
[PHUSE Data Visualization and Open Source Technology](https://advance.phuse.global/pages/viewpage.action?pageId=327777) working group. 
This article highlights a specific COSA project, the [CDISC Open Rules Engine (CORE) software.](https://www.cdisc.org/core)

## Creating And Testing Rules With The CORE Engine

CORE delivers a governed set of unambiguous and executable Conformance Rules as part of each CDISC Foundational Standard 
and provides an open-source conformance rule execution engine as a reference implementation. The CORE Engine is considered 
a reference implementation because it is the software used by the CDISC Foundational Standards teams’ rule authors to 
create and test the rules. This means that the CORE Engine’s interpretation and execution of the rule has been confirmed to 
match the requirements established by the standards developers. Other rule engines that run the conformance rules should 
achieve the same results as CORE Engine. CDISC is creating a certification program to verify that alternative rule engines 
produce the same results as CORE, opening the conformance rule engine market to alternative solutions.

The CORE software includes the previously mentioned Engine that executes the rules as well as a web-based 
[Rule Editor](https://github.com/cdisc-org/conformance-rules-editor) for authoring and testing rules. 
The Rule Editor uses the rule engine to test Conformance Rules using test data created by the rule author. 
The Rule Editor aids rule authors by providing an interactive development environment that includes features such as 
code completion, syntax checking, and integrated testing. A conformance rule schema defines the structure, and in some 
cases content for the Conformance Rules. The process of developing and testing unambiguous Conformance Rules during 
Foundational Standard development improves the overall quality of the standards themselves.

## Sharing Standardized Clinical Research Datasets Made Easy With Conformance Rules

Running conformance rules against study datasets helps parties exchanging data to understand the state of the datasets. 
This represents a necessary step in asserting that the datasets meet an established, accepted threshold for standards conformance. 
For these reasons, Conformance Rules play a critical role in the regulatory submission process. Beyond submissions, executable 
conformance rules make it easier to share standardized clinical research datasets for all studies and throughout the duration of a 
study. Rule sets used to test for conformance can be modified to address the needs of a specific study and those rule sets may vary 
over the course of the study as the datasets get closer to being finalized.

CDISC initiated the CORE project in response to an industry need for an unambiguous set of Conformance Rules developed and tested by 
the CDISC Standards Development teams. Since the Conformance Rules are part of a Foundational Standard, they will be published in the 
[CDISC Library standards metadata repository](https://www.cdisc.org/cdisc-library) with the Foundational Standard and available via the 
Library API for any rule engine to execute. In addition to being used by our community of volunteer standards developers to author and 
test the rules, the Engine and Rule Editor software fill the need for an open, low-cost software solution that can be used by all of the 
CDISC community.

Prior to CORE, Foundational Standards teams created rule specifications that required implementers of CDISC Foundational Standards to create 
their own executable versions of the rules from the specification. Interpreting the rule specification was a necessary step to transform 
that specification into an executable rule. These interpretations were not always consistent with the standards development team's intention.

Conformance Rule authors create the executable rules in YAML, a human-readable data format, using the Rule Editor software. The rules are 
defined using metadata specified within the YAML schema, creating a low-code approach to rule development. Programming experience is not 
required to author rules, and many non-programmers have successfully authored rules. In fact, many rule authors are first-time CDISC volunteers. 
CDISC provides [Rule Editor training for all volunteers](https://www.cdisc.org/events/webinar/core-volunteer-onboarding-training-webinar) seeking 
to join the team.

The Rule Editor software is deployed in the CDISC Azure platform to make it accessible to the volunteers participating in rule development 
without the need to install software. Completed and tested Conformance Rules are published in the CDISC Library, and software tools can 
access them via its API, which is freely available for all who set up an account. The Rule Editor software is available on the 
[project’s public GitHub repository](https://github.com/cdisc-org/conformance-rules-editor).

## Open To All: Using CORE In Your Own Workflow

Since the first Minimal Viable Product (MVP) of the CORE Engine in April 2022, iterative CORE Engine releases that feature a 
command-line interface have been made available from the project’s GitHub repository. Vendors have begun developing a desktop version 
of CORE that’s easy to deploy and features a user interface of their own design. These simple to install and use desktop versions will 
make it easier to evaluate the CORE Engine without IT support. Vendors have also expressed an interest in integrating the CORE Engine 
into their products, since most software that generates standardized datasets would benefit from an integrated ability to test the datasets 
for standards conformance and data quality.

The CORE Engine supports the ingestion of a variety of dataset formats, including SAS v5 XPORT, Dataset-JSON (a CDISC data exchange 
standard for tabular datasets), and CSV. As an open-source application, vendors can extend CORE to add support for additional dataset 
formats.

The CORE Engine provides a framework to plug in new rule types developed by the CORE team or by other implementers who have the need 
for additional rules not yet supported by the Engine. In addition to using CDISC Conformance Rules, custom conformance rules can be 
authored to test study-specific standards implementations.

The CORE Engine and Rule Editor software are released under [the MIT license](https://opensource.org/license/mit/). The MIT license is 
among the more permissive and widely used open-source licenses. It is also among the simplest. The MIT license requires that developers 
provide attribution by including copyright and permission notices. It also states that the software is provided as-is without warranty.
Developers who use MIT-licensed software are free to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the licensed
software including redistributing the code in proprietary applications without requiring the source code for that application to be released as
open source. Basically, it allows developers to do anything they want with the code as long as they provide attribution and do not hold the 
authors liable. CORE benefits from this type of permissive licensing by removing licensing restrictions as a barrier to using the software.

## Adopting CORE Across The Clinical Research Community

The CORE project maintains values fundamental to open standards as well as to open-source software: transparency, participation, 
and efficacy. The degree to which CORE succeeds at meeting the evolving requirements of the clinical research community depends on 
the level of engagement across the global CDISC community. Continued active participation from a growing group of contributing 
volunteers is needed to develop the complete set of Conformance Rules as well as to add new features and tests to the CORE Engine 
and Rule Editor software.

CDISC leads the development of the CORE software to ensure that the means to create and test Conformance Rules exists for 
anyone interested in using it. Although not all the Conformance Rule sets are available today, organizations have started using 
CORE with the rules currently available and have reported successful outcomes. A number of commercial software providers have 
expressed interest in incorporating CORE into their products so that conformance rule checking becomes a feature of their platform. 
Vendors have also committed to making CORE available to their customers. Open-source software products, such as the 
[Smart Submission Dataset Viewer,](https://sourceforge.net/projects/smart-submission-dataset-viewe/) have incorporated 
CORE into the application. Because CORE is open-source, and conformance checking is a necessary step in creating and sharing standard 
datasets, there will be a variety of options available from vendors seeking to offer conformance checking services.

## Using Conformance Rules Throughout The Study Life Cycle

Data quality is essential throughout the study lifecycle, not just during submission preparation. Conformance rule sets can be created 
to assess standards data conformance and quality at different phases in the research lifecycle. Assessing data quality early in a study 
can improve overall data quality and limit the work needed to achieve conformance at the end of the study lifecycle. The ability for each 
organization to develop its own conformance rules to complement the CDISC Foundational Standards’ Conformance Rules, combined with a
variety of CORE Engine deployment options, increases the feasibility of continuously running quality and conformance checks throughout the 
study lifecycle.

## Validating And Testing The CORE Engine

CDISC will provide a validation package for CORE that implementers can extend to offer a fully validated solution. CDISC leads a 
testing and validation team who will create a suite of automated system tests, along with the validation documentation needed to 
support the deployment of a validated CORE instance. The system testing complements the unit tests created by the development team. 
While CDISC will lead the system testing and validation effort, a team of volunteers with software validation and auditing expertise will 
contribute to the deliverables. System tests and validation documentation will be published in a GitHub repository.

## Regulatory Authorities And Conformance Testing

A frequently asked question regarding CORE involves the participation and commitment of regulatory authorities. Since CDISC Conformance 
Rules are published as part of our Foundational Standards, CDISC anticipates that regulatory agencies will use these Rules for their 
conformance testing. A benefit of a CORE certification program will be that different conformance rule engines can be tested to show that 
the engine interprets the rules correctly and consistently, making it possible for regulators and submitting sponsors to choose from a 
variety of software engines.

## Looking Ahead To A New Release In 2023

Currently, we are working toward completing the executable Conformance Rules for our Foundational Standards as well as the 
regulatory business rule sets. As new conformance rule requirements emerge, the CORE Engine and Rule Editor will be updated to 
add new functionality.

As a community-driven project, the pace at which these milestones are achieved is based largely on the number of volunteers 
actively working to develop the necessary Conformance Rules. CDISC is targeting a CORE v1.0 release with a complete set of Conformance
Rules by the end of 2023.

Active volunteers make CDISC work, and CORE is no exception. For those interested in participating in CORE rule authoring or 
software development, please visit the [CORE page on the CDISC website](https://www.cdisc.org/core) for more information.

### About The Author

Sam Hume leads CDISC’s Data Science team who develops tools and standards that support clinical and translational research. 
Sam directs delivery of the CDISC Library, co-leads the Data Exchange Standards team, and serves as a leader of CORE. 
Additionally, he oversees the CDISC Open-Source Alliance (COSA), which supports CDISC-related open-source software projects. 
Sam has 30 years’ experience working in clinical research informatics and has held several senior-level technology positions 
in the biopharmaceutical industry. He holds a doctorate in Information Systems.
