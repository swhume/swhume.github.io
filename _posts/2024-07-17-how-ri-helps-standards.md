# How Reference Implementations Benefit Standards

## Introduction

Reference implementations (RIs) accelerate the establishment and adoption of standards. By providing a concrete example of how a standard can be implemented, they facilitate interoperability between different systems and technologies. Developers can refer to an RI to ensure that their implementation aligns with the standard, thus promoting consistency and compatibility. Generally, RIs are designed to demonstrate how a standard works and provide a baseline against which other implementations can be measured.

## Reference Implementation Examples

As CDISC increasingly emphasizes standards implementation and develops standards rooted in logical models and APIs, the need for software tools to automate standards-based data pipelines has grown significantly. Given the necessity of software tools to implement certain data standards, CDISC supports the creation of RIs and open-source applications for its standards through [COSA](https://cosa.cdisc.org/) and software development projects that run parallel to standards development efforts.

For example, the [CDISC Open Rules Engine](https://www.cdisc.org/core), or CORE, provides an RI for software engines that execute the CDISC conformance rules published as part of the CDISC standards. The CDISC Foundational Standards teams’ rule authors use CORE to create and test the rules published with the standards. Thus, the CORE Engine’s interpretation and execution of the rules have been confirmed to match the requirements established by the standards developers.

Other rule engines that run the conformance rules should generate the same results as the CORE Engine. CDISC is creating a certification program to verify that alternative rule engines produce the same results as CORE, making it possible to choose an engine that has been certified to do so.

The CORE Engine is published under the MIT license. Under a permissive license like MIT, the CORE Engine can be embedded in commercial software without requiring the commercial application to be released as open source. It allows developers of other conformance rules engines to examine the code to better understand how to build engines that conform to CORE.

The [Digital Data Flow Study Definition Repository](https://transcelerate.github.io/ddf-home/sdr-ri-codebase-access.html) (SDR) is another RI example that supports a CDISC standard. The SDR is an RI for the Unified Study Definitions Model (USDM) standard that provides an example implementation to facilitate interoperability.

One notable RI example that does not involve a CDISC standard is the Apache HTTP Server. Apache serves as the standard implementation of the HTTP protocol. It provides a reliable and widely accepted reference for developers creating web servers that conform to the HTTP standard.

## Purpose of Reference Implementations

Two of the main purposes fulfilled by RIs in support of standards implementation and adoption are:

1. Demonstrates the implementation of a standard:
    - Clarity: RIs illustrate how a standard should be implemented.
    - Education: RIs serve as a teaching tool, offering a concrete example for developers to learn how to implement the standard correctly.
    - Demonstration: RIs verify that a standard is implementable.
2. Provides a baseline for compliance:
    - Benchmarking: RIs provide a known-good example that other implementations can compare against to ensure they meet the standard.
    - Validation: RIs act as a tool for testing and verifying that other implementations are correct and reliable.
    - Interoperability: RIs support interoperability testing with other implementations.

## Reference Implementation Application Types

The two basic types of applications found in RIs are:

1. Real-world applications:
    - An RI made robust and efficient enough for real-world applications can be particularly useful if the standard is new and no other implementations exist.
    - A usable RI can speed up the adoption of the standard, as developers can use it directly or adapt it to their needs.
    - RIs designed for real-world usage can incorporate features needed for use in regulated industries.
2. Prototype or example-only:
    - An RI might be more of an educational tool than a fully optimized, production-ready solution.
    - By focusing on clarity instead of optimizing it for performance and scalability, the priority might emphasize making the application easy to understand.

Given the importance of RIs to standards, how important is it that an RI works for real-world applications? While it's not always necessary for an RI to be suitable for real-world applications, having one that is can be highly advantageous. It can accelerate adoption, serve as a reliable tool for developers, and provide a concrete example of how a standard should be applied in practice.

As an RI for HTTP Servers, the Apache HTTP Server operates as a real-world, industry-leading solution that helped launch the web. CPython, the Python programming language RI, is an example of a language specification RI that is also the most widely used Python implementation.

## Characteristics of a Good Reference Implementation

Given the purposes RIs serve, here are six characteristics of a good RI:

1. Correctness: It should accurately implement the standard.
2. Clarity: The code should be well-documented and easy to understand.
3. Completeness: It should cover all aspects of the standard.
4. Portability: Ideally, it should run on multiple platforms.
5. Performance: While not always necessary, better performance makes it more useful for real-world applications.
6. Open source: Open-source RIs are particularly common due to the benefits of transparency, community collaboration, and widespread adoption.

By making the RI open-source, developers can study the code, suggest improvements, and contribute to its development. This collaborative approach often leads to faster innovation, broader adoption, and better overall quality.

In practice, RIs are often used by developers as a blueprint for creating their own implementations that adhere to a specific standard. They may serve as a starting point, providing guidance on how to structure code, implement features, and handle edge cases. Developers can refer to the RI to ensure alignment with the standard and to troubleshoot any inconsistencies.

## Conclusion

Overall, software RIs are important tools for standards developers. They foster consistency, compatibility, and innovation in standard implementations. By providing a concrete example of how a standard can be implemented, RIs help drive the adoption of standards and promote interoperability between different systems and technologies. RIs can significantly reduce the time and effort required for developers to support the standard in their own projects. When RIs function as real-world solutions, they provide a valuable resource to implementers. As CDISC focuses increasingly on standards implementation, more RIs and other open-source tools will become available as part of the [COSA Directory](https://cosa.cdisc.org/).
