# Managing Model Releases

As CDISC develops new and increasingly sophisticated models as the basis for our data standards, it places growing importance on elevating our model release management game. These model-based CDISC standards require software tools to implement the standard effectively. Software developers must get involved in the standards development process to ensure that the model release management process supports the efficient implementation and maintenance of applications based on these models. Standards developers will need to factor the impact of software maintenance into release planning. Ideally, open-source software tools will be available to test each standard before its release, as this will improve the standard and help ensure that other software tools can process it.

### Dataset-JSON v1.1

[Dataset-JSON v1.1](https://wiki.cdisc.org/display/DSJSON1DOT1/Dataset-JSON+v1.1) provides a simple example. As we finalized Dataset-JSON v1.0, we ran a [COSA](https://cosa.cdisc.org/hackathons/datasetJson) Hackathon and initiated the [_Dataset-JSON as an Alternative Transport Format for Regulatory Submissions_](https://phuse.s3.eu-central-1.amazonaws.com/Deliverables/Optimizing+the+Use+of+Data+Standards/WP-88+Dataset-JSON+Report.pdf​) pilot. Software tools have been a part of the Dataset-JSON story from the beginning, and we could not have run the pilot without them. Software development activities complemented our standards development work by providing a feedback mechanism and a way to demonstrate that Dataset-JSON satisfied its target use cases.

The pilot was successful because we proved that Dataset-JSON supported the requirements for regulatory submissions. We also learned several ways to simplify and improve the standard, triggering the Dataset-JSON v1.1 project we completed over the summer. Feedback from the pilot also helped the conversion tool developers improve their software.

Dataset-JSON v1.1 includes a number of changes to the model. As we wrap up the Dataset-JSON v1.1 Public Review work, it’s a good time to remind developers that there is no need to continue to support Dataset-JSON v1.0. Dataset-JSON v1.1 will be the first production version of the standard that developers should support. This decision simplifies the development and maintenance of Dataset-JSON tools. Software tools are necessary to drive the adoption of the standard, and starting from a clean baseline version that’s undergone a significant review period helps ensure the stability of the model and the software tools that implement it.

### Models for Standards

Logical data models, APIs, and JSON data exchange have increasingly become part of the CDISC standards development landscape. Standards projects, such as the [DDF](https://www.cdisc.org/ddf) and [ARS](https://www.cdisc.org/standards/foundational/analysis-results-standard), include relatively sophisticated logical models at the heart of the standard. These standards require software tools to be implemented effectively. The software tools need stable models and maintenance schemes. Once a stable model has been published, software maintenance must be part of the standards release management planning process.

Standard models broadly and consistently implemented by industry provide the best way to enable end-to-end, standards-driven automation. This is the only way to ensure there are COTS and open-source software tools for sponsors and CROs to implement. The current environment, where every sponsor implements their own flavor of the standards, makes developing software tools that any sponsor could implement without significant customization and configuration unfeasible. CDISC plans to improve the current state-of-the-art as part of the CDISC 360i initiative, but more on that in a future post.

### ODM Versioning and Release Management

ODM, a standard typically built into software products, uses numerous release management tactics to aid developers. Many of these tactics apply to releasing new versions of the ODM model, while others apply to managing metadata versions within a study.

The following table highlights tactics the ODM standard uses to help with version management.

| **Tactic** | **Description of ODM Support** |
| --- | --- |
| Include model version | ODM content includes the _ODMVersion_ attribute, which holds the model version number. |
| Manage study metadata versions | ODM uses _MetaDataVersion_ to manage versioning within a study. |
| External semantics | ODM uses the _Coding_ element to enable content to reference externally maintained semantics, allowing the model to carry a wide range of content using a small set of entities. It also creates a separation of concerns where the semantic standards content can be created and managed independently of ODM. |
| Separation of content and structure | ODM carries content defined by other standards, such as CDASH, and this separation of concerns minimizes the need for ODM to be updated to accommodate new releases of the content standards. |
| Extensibility | ODM’s widely used extension mechanism allows users to add new types of content to ODM without necessitating a new ODM version. Senders and receivers must follow specific requirements for creating and processing extensions. This benefits implementers by providing one base model that supports a wide range of implementations. This flexibility must be managed to ensure that it doesn’t, in practice, create many one-off standards implementations that impede interoperability. It’s an important balancing act. CDISC has used ODM’s extension mechanism to create Define-XML and other ODM-based data exchange standards. |
| Deprecation | ODM typically deprecates elements before removing them from a new standard version. |
| Conformance rules | Conformance rules, more often used for Define-XML, provide the means to constrain a model without changing the version. This enables the model to maintain the flexibility needed to support a variety of use cases while using different sets of conformance rules to apply the necessary constraints. Moving constraints to the conformance rules enables the model to maintain a higher degree of flexibility. This is another example where a separation of concerns minimizes the need to update a model. |
| Semantic versioning | Governance practices and semantic versioning minimize the frequency of publishing ODM versions that break backward compatibility. Importantly, it provides a mechanism for patching standards and their associated models when fixes are needed that do not break backward compatibility. It also signals to developers when a new release that breaks backward compatibility is planned. |
| Schema components | The ODM and Define models are implemented as schemas consisting of components that isolate changes and extensions. For example, the Define-XML 2.1 schema maintains enumerations in a separate schema that can be updated with new controlled terminology without impacting the main schema. The separation of concerns enables certain parts of the model to evolve while the main structure remains unchanged. |
| Flexible model | ODM's general model is highly flexible, allowing it to represent a wide variety of data types and structures. This flexibility is beneficial when working with complex or novel types of clinical data. Novel content can be represented in ODM without necessitating a new or updated model. |
| Certification | ODM certification provides a mechanism to ensure that software tools implementing ODM conform to the standard specification. As new versions are released, software tools must be re-certified to show that they conform to the updated specification. |

As we begin work on CDISC 360i, we will create tools and tactics for migrating ODM v1.3.2 implementations to ODM v2.0. We will also publish best practices to help implementers manage ODM v2.0’s metadata modeling flexibility. I’ll expand on these as we get into the 360i project.

In addition to the ODM version management tactics listed above, many other tactics can be applied to help minimize the impact of new versions of ODM or other standard models. General release and version management tactics cover much more ground than I intend to include in this post, but here are a handful of example tactics that minimize the impact of model changes on the systems that implement them:

| **Tactic** | **Description of Other Tactics** |
| --- | --- |
| Migration tools | Use a migration script and other tools to port older versions of the model to the newer version. |
| Test cases | Maintain a robust test case library to facilitate updating software to use newer versions of a model. |
| API Versioning | Use API versioning to enable applications to use different versions of a model. |
| Adaptors | Create adapters so that applications can adapt to other versions of a model. |
| Profiles | Use profiles to adapt models to specific usage scenarios. |
| Feature flags | Use feature flags to enable or disable new features so that software can work with older versions of a model. |
| Code generation | Generate code based on the model to ensure software can work with newer versions. For example, GraphQL can generate types and resolvers based on a schema, reducing manual coding efforts when the schema changes. |
| Schema evolution | Design your schemas to be backward and forward-compatible. This means new schema versions can read data written by older versions and vice versa. For example, Avro supports schema evolution. |

As CDISC develops increasingly connected standards that seek to enable automated processes, managing model releases and providing tools to support up-versioning will become a growing part of standards development. While ODM uses practical model release management tactics, newer and more complex models, like those published by the DDF and ARS standards, will need even more sophisticated practices and a community to help implement them.