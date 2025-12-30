# Powering Standards With Code: The Role Of Open Source In CDISC 360i

This year marks CDISC's 25th anniversary as a standards development organization. Over the last quarter-century, 
CDISC has built a diverse portfolio of widely adopted data standards that have advanced clinical research worldwide. 
Yet one challenge persists: how to implement those standards in automated research data pipelines that are fast, 
scalable, and reliable.

To address this longstanding challenge, CDISC launched CDISC 360i, a strategic initiative focused on transforming the   
way we implement standards. At the heart of 360i lies a powerful idea: standards should not exist merely as static 
specifications; they should exist as part of a solution. The goal is simple but transformative: make standards 
executable so they can power automation across the research data life cycle.

The launch of 360i coincides with a dynamic new trend: the rise of open-source software (OSS) in regulated research. 
Once rare in regulated research, the adoption of OSS is accelerating among sponsors, CROs, and academic research 
centers. Two other emerging forces have helped accelerate this trend:

- New model-based standards. Model-based standards, such as the Unified Study Definitions Model (USDM) for study design and the Analysis Results Standard (ARS) for reporting, require automation to fully implement. When combined with semantic definitions such as Biomedical Concepts (BCs) and Analysis Concepts (ACs), these new models enable the development of sophisticated software tools that can more comprehensively automate clinical research data processes.
- The arrival of generative AI. Generative AI enables the development of a new class of software tools that accelerate standards development, testing, and implementation.

The OSS development model shares many common attributes with the standards development process, creating a foundation 
for automation that is practical, flexible, and community-driven

## What Is CDISC 360i?

CDISC 360i transforms static standards into dynamic, executable assets. The "i" stands for implementation, signaling 
CDISC's expanded focus from standards specifications to standards-driven automation. Standards specifications require 
community members to determine how to implement them, while 360i provides implementation-ready solutions.

The vision is an automated research data pipeline that runs from digital study design through analysis results, built 
from:

- model-based standards like USDM and ARS
- semantically rich metadata such as BCs, ACs, and Dataset Specializations (DSS)
- integrated OSS tools to automate each step of the pipeline
- synthetic, fit-for-purpose test data.

The result is a preconfigured downloadable study package, complete with metadata, test data, and runnable software 
showing exactly how a standardized study can operate from start to finish.

## Why Open Source Is Central To 360i

### From Specification To Solution

A standard on paper doesn't guarantee automation. Implementers require executable examples that demonstrate the 
standard's effectiveness in practice. With OSS, 360i delivers runnable study packages that:

- demonstrate the standard functioning inside a research data pipeline
- run in any environment without licensing restrictions
- provide common processing methods that improve interoperability and reduce variability.

### Reducing Barriers To Adoption

Many smaller sponsors, CROs, and academic groups face cost and complexity hurdles in adopting standards. OSS lowers 
both by offering:

- free, community-supported tools
- prebuilt best practices for handling CDISC metadata and data
- freedom from vendor lock-in.

### Driving Innovation

OSS fosters a "bazaar" (to borrow software developer Eric Raymond's phrase) ideal for sharing new ideas openly, 
testing them quickly, and collaborating broadly. It makes OSS ideal for:

- filling tooling gaps where no solutions yet exist
- taking risks to explore new approaches
- feeding recommendations for improvements back into the standards themselves.

### Sustainable Development And Maintenance

Because OSS projects draw contributors from many organizations, they:

- spread costs and effort broadly
- evolve continuously with regular updates
- offer transparent, reusable code vetted by the community.

## Models And OSS

The availability of new standards models, such as USDM and ARS, eases the development of software tools. Models provide 
the relationships and semantics necessary to enable the automation of processes with appropriate rigor and quality. 
They facilitate the development of common software tools.

Models often benefit from reference implementations. Reference implementations provide an exemplar software 
implementation of a model endorsed by the model developers. In most cases, reference implementations are OSS.

## Treating Standards Like Code

360i applies modern software development practices to standards development, including:

- Version Control: Store and track changes to standards metadata in GitHub, which allows collaborative editing, branching, and rollbacks.
- Continuous Integration/Deployment (CI/CD): Automatically test draft standards against OSS tools and publish approved versions to the CDISC Library. Think of CI/CD as an assembly line that checks quality at every step before shipping.
- Automated Testing: Run test suites for each change made, ensuring compatibility both for a single standard and for the full end-to-end pipeline.
- Machine-Readable Formats: Publish standards in API-accessible formats so they can be consumed directly by software without manual conversion.

Standards also benefit from code libraries that implement them. Code libraries make it easier for other developers to 
build software tools that automate standards-based data processing. Code libraries often embed the schema or model for 
the standard they implement, making them especially useful for the CDISC Data Exchange Standards.

Treating standards like code turns standards into configurable and testable digital assets, ensuring they are ready for 
automation the moment they are published.

## How OSS Changes Standards Development

With OSS, developers don't just write standards, they prove them in action during the development process. In 360i:

- New standards are tested with executable code and test data before release.
- Feedback loops between implementers and standard developers are shorter and richer.
- Ideally, standards are delivered with tooling in place, not years later.

## OSS As An Enabler Of Scale

Scaling the adoption of standards means lowering both technical and financial barriers. OSS helps by:

- providing code libraries that abstract away complexity so others can build on them easily
- implementing default configurations to reduce the learning curve
- ensuring consistency with common tools for metadata processing.

When paired with open standards, OSS can reach more users, in more settings, with less friction.

## Open Source Vs. Commercial: A Balanced Ecosystem

360i recognizes the value of both OSS and commercial tools. However, in the context of 360i, OSS offers unique 
advantages that commercial models may struggle to match, such as high community engagement, risk-taking, and rapid 
innovation. Commercial software often benefits from OSS, as almost all commercial software contains OSS components. 
Thus, the availability of OSS will stimulate closed-source commercial software development. Successful standards 
automation requires a healthy ecosystem with both OSS and closed-source commercial alternatives.

## The OSS Toolbox For 360i

Many of the OSS tools used in 360i are already available via [CDISC COSA](https://cosa.cdisc.org/) and GitHub. 
Some originated from hackathons, while others emerged from community collaborations. Where gaps exist, 360i teams 
write new code, often starting as sandbox repositories before becoming official assets in 
the [360i GitHub repository](https://github.com/cdisc-org/360i).

COSA hackathons will continue to address automation gaps, ensuring a steady pipeline of practical, freely available 
tools.

## The Road Ahead: A Call to Action

360i is an open invitation to anyone passionate about advancing research automation:

- **Join a 360i team:** Shape tools and standards with your domain expertise.
- **Submit OSS tools to COSA:** Share your work so the whole community benefits.
- **Participate in hackathons:** Help solve critical automation challenges.
- **Contribute to standards content:** Refine and expand CDISC metadata to improve interoperability.

Visit [CDISC.org/360i](https://www.cdisc.org/cdisc-360i) to get involved. The future of standards is defined by 
those who show up.

## Conclusion

360i aims to accelerate processes, reduce manual effort, and unlock new levels of scalability and consistency across 
the entire clinical research data life cycle. 360i seeks to evolve standards from static definitions to 
machine-readable, executable resources that are configurable and testable. Ideally, the availability of common 
software tools and processes makes using the CDISC standards the path of least resistance, meaning it's simpler and 
more efficient to use the standards and their associated tools than it is to use proprietary metadata and software to 
run studies.

CDISC 360i is more than an initiative; it's a pivot. It's a recognition that to maximize the impact of standards, 
they must be executable, testable, and usable. Open-source software is not only a delivery mechanism; it also provides 
a collaborative language that bridges the standards developers, software developers, and standards implementers. 
CDISC 360i offers a practical foundation, built on OSS, to unlock the next era of clinical research automation. 
The community that builds it defines it.

This article was originally published in [Clinical Tech Leader](https://www.clinicaltechleader.com/doc/powering-standards-with-code-the-role-of-open-source-in-cdisc-i-0001) on September 26, 2025.