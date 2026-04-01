-- # Class: AIPackage Description: Specifies an AI package and its associated information.
--     * Slot: id
--     * Slot: informationAboutTraining Description: Describes relevant information about different steps of the training process.
--     * Slot: safetyRiskAssessment Description: Records the results of general safety risk assessment of the AI system.
--     * Slot: useSensitivePersonalInformation Description: Records if sensitive personal information is used during model training orcould be used during the inference.
--     * Slot: limitation Description: Captures a limitation of the AI software.
--     * Slot: autonomyType Description: Indicates whether the system can perform a decision or action without humaninvolvement or guidance.
--     * Slot: informationAboutApplication Description: Provides relevant information about the AI software, not including the modeldescription.
--     * Slot: sourceInfo Description: Records any relevant background information or additional commentsabout the origin of the package.
--     * Slot: homePage Description: A place for the SPDX document creator to record a website that serves as thepackage's home page.
--     * Slot: downloadLocation Description: Identifies the download Uniform Resource Identifier for the package at the timethat the document was created.
--     * Slot: packageVersion Description: Identify the version of a package.
--     * Slot: packageUrl Description: Provides a place for the SPDX data creator to record the package URL string(in accordance with the Package URL specification) for a software Package.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package,File or Snippet, if any.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: energyConsumption_id Description: Indicates the amount of energy consumption incurred by an AI model.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: EnergyConsumption Description: A class for describing the energy consumption incurred by an AI model indifferent stages of its lifecycle.
--     * Slot: id
-- # Class: EnergyConsumptionDescription Description: The class that helps note down the quantity of energy consumption and the unitused for measurement.
--     * Slot: id
--     * Slot: energyQuantity Description: Represents the energy quantity.
--     * Slot: energyUnit Description: Specifies the unit in which energy is measured.
-- # Class: Build Description: Class that describes a build instance of software/artifacts.
--     * Slot: id
--     * Slot: buildType Description: A buildType is a hint that is used to indicate the toolchain, platform, orinfrastructure that the build was invoked on.
--     * Slot: buildEndTime Description: Property that describes the time at which a build stops.
--     * Slot: buildId Description: A buildId is a locally unique identifier used by a builder to identify a uniqueinstance of a build produced by it.
--     * Slot: buildStartTime Description: Property describing the start time of a build.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: Agent Description: Agent represents anything with the potential to act on a system.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Annotation Description: An assertion made in relation to one or more elements.
--     * Slot: id
--     * Slot: contentType Description: Provides information about the content type of an Element or a Property.
--     * Slot: statement Description: Commentary on an assertion that an annotator has made.
--     * Slot: annotationType Description: Describes the type of annotation.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: subject_id Description: An Element an annotator has made an assertion about.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: Artifact Description: A distinct article or unit within the digital domain.
--     * Slot: id
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: Bom Description: A container for a grouping of SPDX-3.0 content characterizing details(provenence, composition, licensing, etc.) about a product.
--     * Slot: id
--     * Slot: context Description: Gives information about the circumstances or unifying propertiesthat Elements of the bundle have been assembled under.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Bundle Description: A collection of Elements that have a shared context.
--     * Slot: id
--     * Slot: context Description: Gives information about the circumstances or unifying propertiesthat Elements of the bundle have been assembled under.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CreationInfo Description: Provides information about the creation of the Element.
--     * Slot: id
--     * Slot: created Description: Identifies when the Element was originally created.
--     * Slot: specVersion Description: Provides a reference number that can be used to understand how to parse andinterpret an Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
-- # Class: DictionaryEntry Description: A key with an associated value.
--     * Slot: id
--     * Slot: value Description: A value used in a generic key-value pair.
--     * Slot: key Description: A key used in a generic key-value pair.
-- # Abstract Class: Element Description: Base domain class from which all other SPDX-3.0 domain classes derive.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: ElementCollection Description: A collection of Elements, not necessarily with unifying context.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ExternalIdentifier Description: A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
--     * Slot: id
--     * Slot: externalIdentifierType Description: Specifies the type of the external identifier.
--     * Slot: issuingAuthority Description: An entity that is authorized to issue identification credentials.
--     * Slot: identifier Description: Uniquely identifies an external element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
-- # Class: ExternalMap Description: A map of Element identifiers that are used within an SpdxDocument but definedexternal to that SpdxDocument.
--     * Slot: id
--     * Slot: locationHint Description: Provides an indication of where to retrieve an external Element.
--     * Slot: externalSpdxId Description: Identifies an external Element used within an SpdxDocument but definedexternal to that SpdxDocument.
--     * Slot: definingArtifact_id Description: Artifact representing a serialization instance of SPDX data containing thedefinition of a particular Element.
-- # Class: ExternalRef Description: A reference to a resource outside the scope of SPDX-3.0 content related to an Element.
--     * Slot: id
--     * Slot: externalRefType Description: Specifies the type of the external reference.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: contentType Description: Provides information about the content type of an Element or a Property.
-- # Class: Hash Description: A mathematically calculated representation of a grouping of data.
--     * Slot: id
--     * Slot: algorithm Description: Specifies the algorithm used for calculating the hash value.
--     * Slot: hashValue Description: The result of applying a hash algorithm to an Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
-- # Class: IndividualElement Description: A concrete subclass of Element used by Individuals in theCore profile.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: IntegrityMethod Description: Provides an independently reproducible mechanism that permits verification of a specific Element.
--     * Slot: id
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
-- # Class: LifecycleScopedRelationship Description: Provide context for a relationship that occurs in the lifecycle.
--     * Slot: id
--     * Slot: scope Description: Capture the scope of information about a specific relationship between elements.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: NamespaceMap Description: A mapping between prefixes and namespace partial URIs.
--     * Slot: id
--     * Slot: prefix Description: A substitute for a URI.
--     * Slot: namespace Description: Provides an unambiguous mechanism for conveying a URI fragment portion of anElement ID.
-- # Class: Organization Description: A group of people who work together in an organized way for a shared purpose.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: PackageVerificationCode Description: An SPDX version 2.X compatible verification method for software packages.
--     * Slot: id
--     * Slot: hashValue Description: The result of applying a hash algorithm to an Element.
--     * Slot: algorithm Description: Specifies the algorithm used for calculating the hash value.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
-- # Class: Person Description: An individual human being.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: PositiveIntegerRange Description: A tuple of two positive integers that define a range.
--     * Slot: id
--     * Slot: endIntegerRange Description: Defines the end of a range.
--     * Slot: beginIntegerRange Description: Defines the beginning of a range.
-- # Class: Relationship Description: Describes a relationship between one or more elements.
--     * Slot: id
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SoftwareAgent Description: A software agent.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SpdxDocument Description: A collection of SPDX Elements that could potentially be serialized.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: dataLicense_id Description: Provides the license under which the SPDX documentation of the Element can beused.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Tool Description: An element of hardware and/or software utilized to carry out a particular function.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: DatasetPackage Description: Specifies a data package and its associated information.
--     * Slot: id
--     * Slot: datasetSize Description: Captures the size of the dataset.
--     * Slot: datasetUpdateMechanism Description: Describes a mechanism to update the dataset.
--     * Slot: dataCollectionProcess Description: Describes how the dataset was collected.
--     * Slot: intendedUse Description: Describes what the given dataset should be used for.
--     * Slot: confidentialityLevel Description: Describes the confidentiality level of the data points contained in the dataset.
--     * Slot: datasetAvailability Description: The field describes the availability of a dataset.
--     * Slot: hasSensitivePersonalInformation Description: Describes if any sensitive personal information is present in the dataset.
--     * Slot: datasetNoise Description: Describes potentially noisy elements of the dataset.
--     * Slot: sourceInfo Description: Records any relevant background information or additional commentsabout the origin of the package.
--     * Slot: homePage Description: A place for the SPDX document creator to record a website that serves as thepackage's home page.
--     * Slot: downloadLocation Description: Identifies the download Uniform Resource Identifier for the package at the timethat the document was created.
--     * Slot: packageVersion Description: Identify the version of a package.
--     * Slot: packageUrl Description: Provides a place for the SPDX data creator to record the package URL string(in accordance with the Package URL specification) for a software Package.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package,File or Snippet, if any.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ConjunctiveLicenseSet Description: Portion of an AnyLicenseInfo representing a set of licensing informationwhere all elements apply.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CustomLicense Description: A license that is not listed on the SPDX License List.
--     * Slot: id
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecatedLicense or LicenseAddition.
--     * Slot: standardLicenseHeader Description: Provides a License author's preferred text to indicate that a file is coveredby the License.
--     * Slot: isFsfLibre Description: Specifies whether the License is listed as free by theFree Software Foundation (FSF).
--     * Slot: isDeprecatedLicenseId Description: Specifies whether a license or additional text identifier has been marked asdeprecated.
--     * Slot: isOsiApproved Description: Specifies whether the License is listed as approved by theOpen Source Initiative (OSI).
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the licenseXML format.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: standardLicenseTemplate Description: Identifies the full text of a License, in SPDX templating format.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CustomLicenseAddition Description: A license addition that is not listed on the SPDX Exceptions List.
--     * Slot: id
--     * Slot: standardAdditionTemplate Description: Identifies the full text of a LicenseAddition, in SPDX templating format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecatedLicense or LicenseAddition.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the licenseXML format.
--     * Slot: isDeprecatedAdditionId Description: Specifies whether an additional text identifier has been marked as deprecated.
--     * Slot: additionText Description: Identifies the full text of a LicenseAddition.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: DisjunctiveLicenseSet Description: Portion of an AnyLicenseInfo representing a set of licensing information whereonly one of the elements applies.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: ExtendableLicense Description: Abstract class representing a License or an OrLaterOperator.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: IndividualLicensingInfo Description: A concrete subclass of AnyLicenseInfo used by Individuals in theExpandedLicensing profile.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: License Description: Abstract class for the portion of an AnyLicenseInfo representing a license.
--     * Slot: id
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecatedLicense or LicenseAddition.
--     * Slot: standardLicenseHeader Description: Provides a License author's preferred text to indicate that a file is coveredby the License.
--     * Slot: isFsfLibre Description: Specifies whether the License is listed as free by theFree Software Foundation (FSF).
--     * Slot: isDeprecatedLicenseId Description: Specifies whether a license or additional text identifier has been marked asdeprecated.
--     * Slot: isOsiApproved Description: Specifies whether the License is listed as approved by theOpen Source Initiative (OSI).
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the licenseXML format.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: standardLicenseTemplate Description: Identifies the full text of a License, in SPDX templating format.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: LicenseAddition Description: Abstract class for additional text intended to be added to a License, butwhich is not itself a standalone License.
--     * Slot: id
--     * Slot: standardAdditionTemplate Description: Identifies the full text of a LicenseAddition, in SPDX templating format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecatedLicense or LicenseAddition.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the licenseXML format.
--     * Slot: isDeprecatedAdditionId Description: Specifies whether an additional text identifier has been marked as deprecated.
--     * Slot: additionText Description: Identifies the full text of a LicenseAddition.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ListedLicense Description: A license that is listed on the SPDX License List.
--     * Slot: id
--     * Slot: deprecatedVersion Description: Specifies the SPDX License List version in which this license or exceptionidentifier was deprecated.
--     * Slot: listVersionAdded Description: Specifies the SPDX License List version in which this ListedLicense orListedLicenseException identifier was first added.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecatedLicense or LicenseAddition.
--     * Slot: standardLicenseHeader Description: Provides a License author's preferred text to indicate that a file is coveredby the License.
--     * Slot: isFsfLibre Description: Specifies whether the License is listed as free by theFree Software Foundation (FSF).
--     * Slot: isDeprecatedLicenseId Description: Specifies whether a license or additional text identifier has been marked asdeprecated.
--     * Slot: isOsiApproved Description: Specifies whether the License is listed as approved by theOpen Source Initiative (OSI).
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the licenseXML format.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: standardLicenseTemplate Description: Identifies the full text of a License, in SPDX templating format.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ListedLicenseException Description: A license exception that is listed on the SPDX Exceptions list.
--     * Slot: id
--     * Slot: listVersionAdded Description: Specifies the SPDX License List version in which this ListedLicense orListedLicenseException identifier was first added.
--     * Slot: deprecatedVersion Description: Specifies the SPDX License List version in which this license or exceptionidentifier was deprecated.
--     * Slot: standardAdditionTemplate Description: Identifies the full text of a LicenseAddition, in SPDX templating format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecatedLicense or LicenseAddition.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the licenseXML format.
--     * Slot: isDeprecatedAdditionId Description: Specifies whether an additional text identifier has been marked as deprecated.
--     * Slot: additionText Description: Identifies the full text of a LicenseAddition.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: OrLaterOperator Description: Portion of an AnyLicenseInfo representing this version, or any later version,of the indicated License.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: subjectLicense_id Description: A License participating in an 'or later' model.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: WithAdditionOperator Description: Portion of an AnyLicenseInfo representing a License which has additionaltext applied to it.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: subjectExtendableLicense_id Description: A License participating in a 'with addition' model.
--     * Slot: subjectAddition_id Description: A LicenseAddition participating in a 'with addition' model.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CdxPropertiesExtension Description: A type of extension consisting of a list of name value pairs.
--     * Slot: id
-- # Class: CdxPropertyEntry Description: A property name with an associated value.
--     * Slot: id
--     * Slot: cdxPropValue Description: A value used in a CdxPropertyEntry name-value pair.
--     * Slot: cdxPropName Description: A name used in a CdxPropertyEntry name-value pair.
-- # Abstract Class: Extension Description: A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
--     * Slot: id
-- # Class: CvssV2VulnAssessmentRelationship Description: Provides a CVSS version 2.0 assessment for a vulnerability.
--     * Slot: id
--     * Slot: vectorString Description: Specifies the CVSS vector string for a vulnerability.
--     * Slot: score Description: Provides a numerical (0-10) representation of the severity of a vulnerability.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CvssV3VulnAssessmentRelationship Description: Provides a CVSS version 3 assessment for a vulnerability.
--     * Slot: id
--     * Slot: severity Description: Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.
--     * Slot: vectorString Description: Specifies the CVSS vector string for a vulnerability.
--     * Slot: score Description: Provides a numerical (0-10) representation of the severity of a vulnerability.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CvssV4VulnAssessmentRelationship Description: Provides a CVSS version 4 assessment for a vulnerability.
--     * Slot: id
--     * Slot: severity Description: Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.
--     * Slot: vectorString Description: Specifies the CVSS vector string for a vulnerability.
--     * Slot: score Description: Provides a numerical (0-10) representation of the severity of a vulnerability.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: EpssVulnAssessmentRelationship Description: Provides an EPSS assessment for a vulnerability.
--     * Slot: id
--     * Slot: percentile Description: The percentile of the current probability score.
--     * Slot: probability Description: A probability score between 0 and 1 of a vulnerability being exploited.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ExploitCatalogVulnAssessmentRelationship Description: Provides an exploit assessment of a vulnerability.
--     * Slot: id
--     * Slot: exploited Description: Describe that a CVE is known to have an exploit because it's been listed in an exploit catalog.
--     * Slot: security_locator Description: Provides the location of an exploit catalog.
--     * Slot: catalogType Description: Specifies the exploit catalog type.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SsvcVulnAssessmentRelationship Description: Provides an SSVC assessment for a vulnerability.
--     * Slot: id
--     * Slot: decisionType Description: Provide the enumeration of possible decisions in the[Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexAffectedVulnAssessmentRelationship Description: Connects a vulnerability and an element designating the element as a productaffected by the vulnerability.
--     * Slot: id
--     * Slot: actionStatement Description: Provides advise on how to mitigate or remediate a vulnerability when a VEX productis affected by it.
--     * Slot: actionStatementTime Description: Records the time when a recommended action was communicated in a VEX statementto mitigate a vulnerability.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexFixedVulnAssessmentRelationship Description: Links a vulnerability and elements representing products (in the VEX sense) wherea fix has been applied and are no longer affected.
--     * Slot: id
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexNotAffectedVulnAssessmentRelationship Description: Links a vulnerability and one or more elements designating the latter as productsnot affected by the vulnerability.
--     * Slot: id
--     * Slot: impactStatementTime Description: Timestamp of impact statement.
--     * Slot: justificationType Description: Impact justification label to be used when linking a vulnerability to an elementrepresenting a VEX product with a VexNotAffectedVulnAssessmentRelationshiprelationship.
--     * Slot: impactStatement Description: Explains why a VEX product is not affected by a vulnerability. It is analternative in VexNotAffectedVulnAssessmentRelationship to the machine-readablejustification label.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship Description: Designates elements as products where the impact of a vulnerability is beinginvestigated.
--     * Slot: id
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: VexVulnAssessmentRelationship Description: Abstract ancestor class for all VEX relationships
--     * Slot: id
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: VulnAssessmentRelationship Description: Abstract ancestor class for all vulnerability assessments
--     * Slot: id
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: assessedElement_id Description: Specifies an Element contained in a piece of software where a vulnerability wasfound.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: from_id Description: References the Element on the left-hand side of a relationship.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Vulnerability Description: Specifies a vulnerability and its associated information.
--     * Slot: id
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: AnyLicenseInfo Description: Abstract class representing a license combination consisting of one or more licenses.
--     * Slot: id
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: LicenseExpression Description: An SPDX Element containing an SPDX license expression string.
--     * Slot: id
--     * Slot: licenseExpression Description: A string in the license expression format.
--     * Slot: licenseListVersion Description: The version of the SPDX License List used in the license expression.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SimpleLicensingText Description: A license or addition that is not listed on the SPDX License List.
--     * Slot: id
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ContentIdentifier Description: A canonical, unique, immutable identifier
--     * Slot: id
--     * Slot: contentIdentifierValue Description: Specifies the value of the content identifier.
--     * Slot: contentIdentifierType Description: Specifies the type of the content identifier.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
-- # Class: File Description: Refers to any object that stores content on a computer.
--     * Slot: id
--     * Slot: fileKind Description: Describes if a given file is a directory or non-directory kind of file.
--     * Slot: contentType Description: Provides information about the content type of an Element or a Property.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package,File or Snippet, if any.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Package Description: Refers to any unit of content that can be associated with a distribution ofsoftware.
--     * Slot: id
--     * Slot: sourceInfo Description: Records any relevant background information or additional commentsabout the origin of the package.
--     * Slot: homePage Description: A place for the SPDX document creator to record a website that serves as thepackage's home page.
--     * Slot: downloadLocation Description: Identifies the download Uniform Resource Identifier for the package at the timethat the document was created.
--     * Slot: packageVersion Description: Identify the version of a package.
--     * Slot: packageUrl Description: Provides a place for the SPDX data creator to record the package URL string(in accordance with the Package URL specification) for a software Package.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package,File or Snippet, if any.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Sbom Description: A collection of SPDX Elements describing a single package.
--     * Slot: id
--     * Slot: context Description: Gives information about the circumstances or unifying propertiesthat Elements of the bundle have been assembled under.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Snippet Description: Describes a certain part of a file.
--     * Slot: id
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package,File or Snippet, if any.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: lineRange_id Description: Defines the line range in the original host file that the snippet informationapplies to.
--     * Slot: snippetFromFile_id Description: Defines the original host file that the snippet information applies to.
--     * Slot: byteRange_id Description: Defines the byte range in the original host file that the snippet informationapplies to.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: SoftwareArtifact Description: A distinct article or unit related to Software.
--     * Slot: id
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package,File or Snippet, if any.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to bereassessed.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about theElement.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: suppliedBy_id Description: Identifies who or what supplied the artifact or VulnAssessmentRelationshipreferenced by the Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: AIPackage_modelDataPreprocessing
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: modelDataPreprocessing Description: Describes all the preprocessing steps applied to the training data before themodel training.
-- # Class: AIPackage_typeOfModel
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: typeOfModel Description: Records the type of the model used in the AI software.
-- # Class: AIPackage_metricDecisionThreshold
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: metricDecisionThreshold_id Description: Captures the threshold that was used for computation of a metric described inthe metric field.
-- # Class: AIPackage_hyperparameter
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: hyperparameter_id Description: Records a hyperparameter used to build the AI model contained in the AIpackage.
-- # Class: AIPackage_domain
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: domain Description: Captures the domain in which the AI package can be used.
-- # Class: AIPackage_modelExplainability
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: modelExplainability Description: Describes methods that can be used to explain the results from the AI model.
-- # Class: AIPackage_metric
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: metric_id Description: Records the measurement of prediction quality of the AI model.
-- # Class: AIPackage_standardCompliance
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: standardCompliance Description: Captures a standard that is being complied with.
-- # Class: AIPackage_attributionText
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text fora software Package, File or Snippet.
-- # Class: AIPackage_additionalPurpose
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: AIPackage_contentIdentifier
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: contentIdentifier_id Description: A canonical, unique, immutable identifier of the artifact content, that may beused for verifying its identity and/or integrity.
-- # Class: AIPackage_standardName
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: AIPackage_supportLevel
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: AIPackage_originatedBy
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: AIPackage_externalIdentifier
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: AIPackage_extension
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: AIPackage_verifiedUsing
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: AIPackage_externalRef
--     * Slot: AIPackage_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: EnergyConsumption_finetuningEnergyConsumption
--     * Slot: EnergyConsumption_id Description: Autocreated FK slot
--     * Slot: finetuningEnergyConsumption_id Description: Specifies the amount of energy consumed when finetuning the AI model that isbeing used in the AI system.
-- # Class: EnergyConsumption_inferenceEnergyConsumption
--     * Slot: EnergyConsumption_id Description: Autocreated FK slot
--     * Slot: inferenceEnergyConsumption_id Description: Specifies the amount of energy consumed during inference time by an AI modelthat is being used in the AI system.
-- # Class: EnergyConsumption_trainingEnergyConsumption
--     * Slot: EnergyConsumption_id Description: Autocreated FK slot
--     * Slot: trainingEnergyConsumption_id Description: Specifies the amount of energy consumed when training the AI model that isbeing used in the AI system.
-- # Class: Build_configSourceDigest
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: configSourceDigest_id Description: Property that describes the digest of the build configuration file used toinvoke a build.
-- # Class: Build_configSourceUri
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: configSourceUri Description: Property that describes the URI of the build configuration source file.
-- # Class: Build_parameter
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: parameter_id Description: Property describing a parameter used in an instance of a build.
-- # Class: Build_configSourceEntrypoint
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: configSourceEntrypoint Description: Property describes the invocation entrypoint of a build.
-- # Class: Build_environment
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: environment_id Description: Property describing the session in which a build is invoked.
-- # Class: Build_externalIdentifier
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Build_extension
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Build_verifiedUsing
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Build_externalRef
--     * Slot: Build_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Agent_externalIdentifier
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Agent_extension
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Agent_verifiedUsing
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Agent_externalRef
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Annotation_externalIdentifier
--     * Slot: Annotation_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Annotation_extension
--     * Slot: Annotation_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Annotation_verifiedUsing
--     * Slot: Annotation_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Annotation_externalRef
--     * Slot: Annotation_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Artifact_standardName
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Artifact_supportLevel
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Artifact_originatedBy
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: Artifact_externalIdentifier
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Artifact_extension
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Artifact_verifiedUsing
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Artifact_externalRef
--     * Slot: Artifact_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Bom_element
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: element_id Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: Bom_profileConformance
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends toconform to.
-- # Class: Bom_rootElement
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: rootElement_id Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: Bom_externalIdentifier
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Bom_extension
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Bom_verifiedUsing
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Bom_externalRef
--     * Slot: Bom_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Bundle_element
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: element_id Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: Bundle_profileConformance
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends toconform to.
-- # Class: Bundle_rootElement
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: rootElement_id Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: Bundle_externalIdentifier
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Bundle_extension
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Bundle_verifiedUsing
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Bundle_externalRef
--     * Slot: Bundle_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: CreationInfo_createdBy
--     * Slot: CreationInfo_id Description: Autocreated FK slot
--     * Slot: createdBy_id Description: Identifies who or what created the Element.
-- # Class: CreationInfo_createdUsing
--     * Slot: CreationInfo_id Description: Autocreated FK slot
--     * Slot: createdUsing_id Description: Identifies the tooling that was used during the creation of the Element.
-- # Class: Element_externalIdentifier
--     * Slot: Element_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Element_extension
--     * Slot: Element_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Element_verifiedUsing
--     * Slot: Element_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Element_externalRef
--     * Slot: Element_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ElementCollection_element
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: element_id Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: ElementCollection_profileConformance
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends toconform to.
-- # Class: ElementCollection_rootElement
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: rootElement_id Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: ElementCollection_externalIdentifier
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: ElementCollection_extension
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: ElementCollection_verifiedUsing
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ElementCollection_externalRef
--     * Slot: ElementCollection_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ExternalIdentifier_identifierLocator
--     * Slot: ExternalIdentifier_id Description: Autocreated FK slot
--     * Slot: identifierLocator Description: Provides the location for more information regarding an external identifier.
-- # Class: ExternalMap_verifiedUsing
--     * Slot: ExternalMap_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ExternalRef_core_locator
--     * Slot: ExternalRef_id Description: Autocreated FK slot
--     * Slot: core_locator Description: Provides the location of an external reference.
-- # Class: IndividualElement_externalIdentifier
--     * Slot: IndividualElement_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: IndividualElement_extension
--     * Slot: IndividualElement_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: IndividualElement_verifiedUsing
--     * Slot: IndividualElement_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: IndividualElement_externalRef
--     * Slot: IndividualElement_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: LifecycleScopedRelationship_to
--     * Slot: LifecycleScopedRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: LifecycleScopedRelationship_externalIdentifier
--     * Slot: LifecycleScopedRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: LifecycleScopedRelationship_extension
--     * Slot: LifecycleScopedRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: LifecycleScopedRelationship_verifiedUsing
--     * Slot: LifecycleScopedRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: LifecycleScopedRelationship_externalRef
--     * Slot: LifecycleScopedRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Organization_externalIdentifier
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Organization_extension
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Organization_verifiedUsing
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Organization_externalRef
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: PackageVerificationCode_packageVerificationCodeExcludedFile
--     * Slot: PackageVerificationCode_id Description: Autocreated FK slot
--     * Slot: packageVerificationCodeExcludedFile Description: The relative file name of a file to be excluded from the`PackageVerificationCode`.
-- # Class: Person_externalIdentifier
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Person_extension
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Person_verifiedUsing
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Person_externalRef
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Relationship_to
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: Relationship_externalIdentifier
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Relationship_extension
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Relationship_verifiedUsing
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Relationship_externalRef
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: SoftwareAgent_externalIdentifier
--     * Slot: SoftwareAgent_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: SoftwareAgent_extension
--     * Slot: SoftwareAgent_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: SoftwareAgent_verifiedUsing
--     * Slot: SoftwareAgent_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: SoftwareAgent_externalRef
--     * Slot: SoftwareAgent_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: SpdxDocument_namespaceMap
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: namespaceMap_id Description: Provides a NamespaceMap of prefixes and associated namespace partial URIs applicable to an SpdxDocument and independent of any specific serialization format or instance.
-- # Class: SpdxDocument_import
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: import_id Description: Provides an ExternalMap of Element identifiers.
-- # Class: SpdxDocument_element
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: element_id Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: SpdxDocument_profileConformance
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends toconform to.
-- # Class: SpdxDocument_rootElement
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: rootElement_id Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: SpdxDocument_externalIdentifier
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: SpdxDocument_extension
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: SpdxDocument_verifiedUsing
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: SpdxDocument_externalRef
--     * Slot: SpdxDocument_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Tool_externalIdentifier
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Tool_extension
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Tool_verifiedUsing
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Tool_externalRef
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: DatasetPackage_datasetType
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: datasetType Description: Describes the type of the given dataset.
-- # Class: DatasetPackage_anonymizationMethodUsed
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: anonymizationMethodUsed Description: Describes the anonymization methods used.
-- # Class: DatasetPackage_knownBias
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: knownBias Description: Records the biases that the dataset is known to encompass.
-- # Class: DatasetPackage_sensor
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: sensor_id Description: Describes a sensor used for collecting the data.
-- # Class: DatasetPackage_dataPreprocessing
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: dataPreprocessing Description: Describes the preprocessing steps that were applied to the raw data to create the given dataset.
-- # Class: DatasetPackage_attributionText
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text fora software Package, File or Snippet.
-- # Class: DatasetPackage_additionalPurpose
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: DatasetPackage_contentIdentifier
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: contentIdentifier_id Description: A canonical, unique, immutable identifier of the artifact content, that may beused for verifying its identity and/or integrity.
-- # Class: DatasetPackage_standardName
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: DatasetPackage_supportLevel
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: DatasetPackage_originatedBy
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: DatasetPackage_externalIdentifier
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: DatasetPackage_extension
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: DatasetPackage_verifiedUsing
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: DatasetPackage_externalRef
--     * Slot: DatasetPackage_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ConjunctiveLicenseSet_member
--     * Slot: ConjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: member_id Description: A license expression participating in a license set.
-- # Class: ConjunctiveLicenseSet_externalIdentifier
--     * Slot: ConjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: ConjunctiveLicenseSet_extension
--     * Slot: ConjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: ConjunctiveLicenseSet_verifiedUsing
--     * Slot: ConjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ConjunctiveLicenseSet_externalRef
--     * Slot: ConjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: CustomLicense_seeAlso
--     * Slot: CustomLicense_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: CustomLicense_externalIdentifier
--     * Slot: CustomLicense_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: CustomLicense_extension
--     * Slot: CustomLicense_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: CustomLicense_verifiedUsing
--     * Slot: CustomLicense_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: CustomLicense_externalRef
--     * Slot: CustomLicense_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: CustomLicenseAddition_seeAlso
--     * Slot: CustomLicenseAddition_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: CustomLicenseAddition_externalIdentifier
--     * Slot: CustomLicenseAddition_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: CustomLicenseAddition_extension
--     * Slot: CustomLicenseAddition_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: CustomLicenseAddition_verifiedUsing
--     * Slot: CustomLicenseAddition_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: CustomLicenseAddition_externalRef
--     * Slot: CustomLicenseAddition_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: DisjunctiveLicenseSet_member
--     * Slot: DisjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: member_id Description: A license expression participating in a license set.
-- # Class: DisjunctiveLicenseSet_externalIdentifier
--     * Slot: DisjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: DisjunctiveLicenseSet_extension
--     * Slot: DisjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: DisjunctiveLicenseSet_verifiedUsing
--     * Slot: DisjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: DisjunctiveLicenseSet_externalRef
--     * Slot: DisjunctiveLicenseSet_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ExtendableLicense_externalIdentifier
--     * Slot: ExtendableLicense_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: ExtendableLicense_extension
--     * Slot: ExtendableLicense_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: ExtendableLicense_verifiedUsing
--     * Slot: ExtendableLicense_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ExtendableLicense_externalRef
--     * Slot: ExtendableLicense_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: IndividualLicensingInfo_externalIdentifier
--     * Slot: IndividualLicensingInfo_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: IndividualLicensingInfo_extension
--     * Slot: IndividualLicensingInfo_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: IndividualLicensingInfo_verifiedUsing
--     * Slot: IndividualLicensingInfo_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: IndividualLicensingInfo_externalRef
--     * Slot: IndividualLicensingInfo_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: License_seeAlso
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: License_externalIdentifier
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: License_extension
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: License_verifiedUsing
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: License_externalRef
--     * Slot: License_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: LicenseAddition_seeAlso
--     * Slot: LicenseAddition_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: LicenseAddition_externalIdentifier
--     * Slot: LicenseAddition_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: LicenseAddition_extension
--     * Slot: LicenseAddition_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: LicenseAddition_verifiedUsing
--     * Slot: LicenseAddition_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: LicenseAddition_externalRef
--     * Slot: LicenseAddition_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ListedLicense_seeAlso
--     * Slot: ListedLicense_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: ListedLicense_externalIdentifier
--     * Slot: ListedLicense_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: ListedLicense_extension
--     * Slot: ListedLicense_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: ListedLicense_verifiedUsing
--     * Slot: ListedLicense_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ListedLicense_externalRef
--     * Slot: ListedLicense_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ListedLicenseException_seeAlso
--     * Slot: ListedLicenseException_id Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: ListedLicenseException_externalIdentifier
--     * Slot: ListedLicenseException_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: ListedLicenseException_extension
--     * Slot: ListedLicenseException_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: ListedLicenseException_verifiedUsing
--     * Slot: ListedLicenseException_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ListedLicenseException_externalRef
--     * Slot: ListedLicenseException_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: OrLaterOperator_externalIdentifier
--     * Slot: OrLaterOperator_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: OrLaterOperator_extension
--     * Slot: OrLaterOperator_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: OrLaterOperator_verifiedUsing
--     * Slot: OrLaterOperator_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: OrLaterOperator_externalRef
--     * Slot: OrLaterOperator_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: WithAdditionOperator_externalIdentifier
--     * Slot: WithAdditionOperator_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: WithAdditionOperator_extension
--     * Slot: WithAdditionOperator_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: WithAdditionOperator_verifiedUsing
--     * Slot: WithAdditionOperator_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: WithAdditionOperator_externalRef
--     * Slot: WithAdditionOperator_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: CdxPropertiesExtension_cdxProperty
--     * Slot: CdxPropertiesExtension_id Description: Autocreated FK slot
--     * Slot: cdxProperty_id Description: Provides a map of a property names to a values.
-- # Class: CvssV2VulnAssessmentRelationship_to
--     * Slot: CvssV2VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: CvssV2VulnAssessmentRelationship_externalIdentifier
--     * Slot: CvssV2VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: CvssV2VulnAssessmentRelationship_extension
--     * Slot: CvssV2VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: CvssV2VulnAssessmentRelationship_verifiedUsing
--     * Slot: CvssV2VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: CvssV2VulnAssessmentRelationship_externalRef
--     * Slot: CvssV2VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: CvssV3VulnAssessmentRelationship_to
--     * Slot: CvssV3VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: CvssV3VulnAssessmentRelationship_externalIdentifier
--     * Slot: CvssV3VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: CvssV3VulnAssessmentRelationship_extension
--     * Slot: CvssV3VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: CvssV3VulnAssessmentRelationship_verifiedUsing
--     * Slot: CvssV3VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: CvssV3VulnAssessmentRelationship_externalRef
--     * Slot: CvssV3VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: CvssV4VulnAssessmentRelationship_to
--     * Slot: CvssV4VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: CvssV4VulnAssessmentRelationship_externalIdentifier
--     * Slot: CvssV4VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: CvssV4VulnAssessmentRelationship_extension
--     * Slot: CvssV4VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: CvssV4VulnAssessmentRelationship_verifiedUsing
--     * Slot: CvssV4VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: CvssV4VulnAssessmentRelationship_externalRef
--     * Slot: CvssV4VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: EpssVulnAssessmentRelationship_to
--     * Slot: EpssVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: EpssVulnAssessmentRelationship_externalIdentifier
--     * Slot: EpssVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: EpssVulnAssessmentRelationship_extension
--     * Slot: EpssVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: EpssVulnAssessmentRelationship_verifiedUsing
--     * Slot: EpssVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: EpssVulnAssessmentRelationship_externalRef
--     * Slot: EpssVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: ExploitCatalogVulnAssessmentRelationship_to
--     * Slot: ExploitCatalogVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: ExploitCatalogVulnAssessmentRelationship_externalIdentifier
--     * Slot: ExploitCatalogVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: ExploitCatalogVulnAssessmentRelationship_extension
--     * Slot: ExploitCatalogVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: ExploitCatalogVulnAssessmentRelationship_verifiedUsing
--     * Slot: ExploitCatalogVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: ExploitCatalogVulnAssessmentRelationship_externalRef
--     * Slot: ExploitCatalogVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: SsvcVulnAssessmentRelationship_to
--     * Slot: SsvcVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: SsvcVulnAssessmentRelationship_externalIdentifier
--     * Slot: SsvcVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: SsvcVulnAssessmentRelationship_extension
--     * Slot: SsvcVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: SsvcVulnAssessmentRelationship_verifiedUsing
--     * Slot: SsvcVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: SsvcVulnAssessmentRelationship_externalRef
--     * Slot: SsvcVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: VexAffectedVulnAssessmentRelationship_to
--     * Slot: VexAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: VexAffectedVulnAssessmentRelationship_externalIdentifier
--     * Slot: VexAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: VexAffectedVulnAssessmentRelationship_extension
--     * Slot: VexAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: VexAffectedVulnAssessmentRelationship_verifiedUsing
--     * Slot: VexAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: VexAffectedVulnAssessmentRelationship_externalRef
--     * Slot: VexAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: VexFixedVulnAssessmentRelationship_to
--     * Slot: VexFixedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: VexFixedVulnAssessmentRelationship_externalIdentifier
--     * Slot: VexFixedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: VexFixedVulnAssessmentRelationship_extension
--     * Slot: VexFixedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: VexFixedVulnAssessmentRelationship_verifiedUsing
--     * Slot: VexFixedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: VexFixedVulnAssessmentRelationship_externalRef
--     * Slot: VexFixedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: VexNotAffectedVulnAssessmentRelationship_to
--     * Slot: VexNotAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: VexNotAffectedVulnAssessmentRelationship_externalIdentifier
--     * Slot: VexNotAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: VexNotAffectedVulnAssessmentRelationship_extension
--     * Slot: VexNotAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: VexNotAffectedVulnAssessmentRelationship_verifiedUsing
--     * Slot: VexNotAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: VexNotAffectedVulnAssessmentRelationship_externalRef
--     * Slot: VexNotAffectedVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship_to
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship_externalIdentifier
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship_extension
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship_verifiedUsing
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship_externalRef
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: VexVulnAssessmentRelationship_to
--     * Slot: VexVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: VexVulnAssessmentRelationship_externalIdentifier
--     * Slot: VexVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: VexVulnAssessmentRelationship_extension
--     * Slot: VexVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: VexVulnAssessmentRelationship_verifiedUsing
--     * Slot: VexVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: VexVulnAssessmentRelationship_externalRef
--     * Slot: VexVulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: VulnAssessmentRelationship_to
--     * Slot: VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: to_id Description: References an Element on the right-hand side of a relationship.
-- # Class: VulnAssessmentRelationship_externalIdentifier
--     * Slot: VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: VulnAssessmentRelationship_extension
--     * Slot: VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: VulnAssessmentRelationship_verifiedUsing
--     * Slot: VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: VulnAssessmentRelationship_externalRef
--     * Slot: VulnAssessmentRelationship_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Vulnerability_standardName
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Vulnerability_supportLevel
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Vulnerability_originatedBy
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: Vulnerability_externalIdentifier
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Vulnerability_extension
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Vulnerability_verifiedUsing
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Vulnerability_externalRef
--     * Slot: Vulnerability_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: AnyLicenseInfo_externalIdentifier
--     * Slot: AnyLicenseInfo_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: AnyLicenseInfo_extension
--     * Slot: AnyLicenseInfo_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: AnyLicenseInfo_verifiedUsing
--     * Slot: AnyLicenseInfo_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: AnyLicenseInfo_externalRef
--     * Slot: AnyLicenseInfo_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: LicenseExpression_customIdToUri
--     * Slot: LicenseExpression_id Description: Autocreated FK slot
--     * Slot: customIdToUri_id Description: Maps a LicenseRef or AdditionRef string for a Custom License or a CustomLicense Addition to its URI ID.
-- # Class: LicenseExpression_externalIdentifier
--     * Slot: LicenseExpression_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: LicenseExpression_extension
--     * Slot: LicenseExpression_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: LicenseExpression_verifiedUsing
--     * Slot: LicenseExpression_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: LicenseExpression_externalRef
--     * Slot: LicenseExpression_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: SimpleLicensingText_externalIdentifier
--     * Slot: SimpleLicensingText_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: SimpleLicensingText_extension
--     * Slot: SimpleLicensingText_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: SimpleLicensingText_verifiedUsing
--     * Slot: SimpleLicensingText_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: SimpleLicensingText_externalRef
--     * Slot: SimpleLicensingText_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: File_attributionText
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text fora software Package, File or Snippet.
-- # Class: File_additionalPurpose
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: File_contentIdentifier
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: contentIdentifier_id Description: A canonical, unique, immutable identifier of the artifact content, that may beused for verifying its identity and/or integrity.
-- # Class: File_standardName
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: File_supportLevel
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: File_originatedBy
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: File_externalIdentifier
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: File_extension
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: File_verifiedUsing
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: File_externalRef
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Package_attributionText
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text fora software Package, File or Snippet.
-- # Class: Package_additionalPurpose
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: Package_contentIdentifier
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: contentIdentifier_id Description: A canonical, unique, immutable identifier of the artifact content, that may beused for verifying its identity and/or integrity.
-- # Class: Package_standardName
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Package_supportLevel
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Package_originatedBy
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: Package_externalIdentifier
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Package_extension
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Package_verifiedUsing
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Package_externalRef
--     * Slot: Package_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Sbom_sbomType
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: sbomType Description: Provides information about the type of an SBOM.
-- # Class: Sbom_element
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: element_id Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: Sbom_profileConformance
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends toconform to.
-- # Class: Sbom_rootElement
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: rootElement_id Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: Sbom_externalIdentifier
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Sbom_extension
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Sbom_verifiedUsing
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Sbom_externalRef
--     * Slot: Sbom_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: Snippet_attributionText
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text fora software Package, File or Snippet.
-- # Class: Snippet_additionalPurpose
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: Snippet_contentIdentifier
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: contentIdentifier_id Description: A canonical, unique, immutable identifier of the artifact content, that may beused for verifying its identity and/or integrity.
-- # Class: Snippet_standardName
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Snippet_supportLevel
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Snippet_originatedBy
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: Snippet_externalIdentifier
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: Snippet_extension
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: Snippet_verifiedUsing
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: Snippet_externalRef
--     * Slot: Snippet_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.
-- # Class: SoftwareArtifact_attributionText
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text fora software Package, File or Snippet.
-- # Class: SoftwareArtifact_additionalPurpose
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: SoftwareArtifact_contentIdentifier
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: contentIdentifier_id Description: A canonical, unique, immutable identifier of the artifact content, that may beused for verifying its identity and/or integrity.
-- # Class: SoftwareArtifact_standardName
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: SoftwareArtifact_supportLevel
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: SoftwareArtifact_originatedBy
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: originatedBy_id Description: Identifies from where or whom the Element originally came.
-- # Class: SoftwareArtifact_externalIdentifier
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: externalIdentifier_id Description: Provides a reference to a resource outside the scope of SPDX-3.0 contentthat uniquely identifies an Element.
-- # Class: SoftwareArtifact_extension
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: extension_id Description: Specifies an Extension characterization of some aspect of an Element.
-- # Class: SoftwareArtifact_verifiedUsing
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: verifiedUsing_id Description: Provides an IntegrityMethod with which the integrity of an Element can beasserted.
-- # Class: SoftwareArtifact_externalRef
--     * Slot: SoftwareArtifact_id Description: Autocreated FK slot
--     * Slot: externalRef_id Description: Points to a resource outside the scope of the SPDX-3.0 contentthat provides additional characteristics of an Element.

CREATE TABLE "EnergyConsumption" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EnergyConsumption_id" ON "EnergyConsumption" (id);

CREATE TABLE "EnergyConsumptionDescription" (
	id INTEGER NOT NULL,
	"energyQuantity" NUMERIC NOT NULL,
	"energyUnit" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EnergyConsumptionDescription_id" ON "EnergyConsumptionDescription" (id);

CREATE TABLE "CreationInfo" (
	id INTEGER NOT NULL,
	created DATETIME NOT NULL,
	"specVersion" TEXT NOT NULL,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CreationInfo_id" ON "CreationInfo" (id);

CREATE TABLE "DictionaryEntry" (
	id INTEGER NOT NULL,
	value TEXT,
	"key" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DictionaryEntry_id" ON "DictionaryEntry" (id);

CREATE TABLE "ExternalIdentifier" (
	id INTEGER NOT NULL,
	"externalIdentifierType" TEXT NOT NULL,
	"issuingAuthority" TEXT,
	identifier TEXT NOT NULL,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ExternalIdentifier_id" ON "ExternalIdentifier" (id);

CREATE TABLE "ExternalRef" (
	id INTEGER NOT NULL,
	"externalRefType" TEXT,
	comment TEXT,
	"contentType" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ExternalRef_id" ON "ExternalRef" (id);

CREATE TABLE "Hash" (
	id INTEGER NOT NULL,
	algorithm TEXT NOT NULL,
	"hashValue" TEXT NOT NULL,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Hash_id" ON "Hash" (id);

CREATE TABLE "IntegrityMethod" (
	id INTEGER NOT NULL,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IntegrityMethod_id" ON "IntegrityMethod" (id);

CREATE TABLE "NamespaceMap" (
	id INTEGER NOT NULL,
	prefix TEXT NOT NULL,
	namespace TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamespaceMap_id" ON "NamespaceMap" (id);

CREATE TABLE "PackageVerificationCode" (
	id INTEGER NOT NULL,
	"hashValue" TEXT NOT NULL,
	algorithm TEXT NOT NULL,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PackageVerificationCode_id" ON "PackageVerificationCode" (id);

CREATE TABLE "PositiveIntegerRange" (
	id INTEGER NOT NULL,
	"endIntegerRange" INTEGER NOT NULL,
	"beginIntegerRange" INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PositiveIntegerRange_id" ON "PositiveIntegerRange" (id);

CREATE TABLE "CdxPropertiesExtension" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CdxPropertiesExtension_id" ON "CdxPropertiesExtension" (id);

CREATE TABLE "CdxPropertyEntry" (
	id INTEGER NOT NULL,
	"cdxPropValue" TEXT,
	"cdxPropName" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CdxPropertyEntry_id" ON "CdxPropertyEntry" (id);

CREATE TABLE "Extension" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Extension_id" ON "Extension" (id);

CREATE TABLE "ContentIdentifier" (
	id INTEGER NOT NULL,
	"contentIdentifierValue" TEXT NOT NULL,
	"contentIdentifierType" VARCHAR(6) NOT NULL,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ContentIdentifier_id" ON "ContentIdentifier" (id);

CREATE TABLE "Build" (
	id INTEGER NOT NULL,
	"buildType" TEXT NOT NULL,
	"buildEndTime" DATETIME,
	"buildId" TEXT,
	"buildStartTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Build_id" ON "Build" (id);

CREATE TABLE "Agent" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Agent_id" ON "Agent" (id);

CREATE TABLE "Bom" (
	id INTEGER NOT NULL,
	context TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Bom_id" ON "Bom" (id);

CREATE TABLE "Bundle" (
	id INTEGER NOT NULL,
	context TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Bundle_id" ON "Bundle" (id);

CREATE TABLE "Element" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Element_id" ON "Element" (id);

CREATE TABLE "ElementCollection" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ElementCollection_id" ON "ElementCollection" (id);

CREATE TABLE "IndividualElement" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_IndividualElement_id" ON "IndividualElement" (id);

CREATE TABLE "Organization" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Organization_id" ON "Organization" (id);

CREATE TABLE "Person" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Person_id" ON "Person" (id);

CREATE TABLE "SoftwareAgent" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SoftwareAgent_id" ON "SoftwareAgent" (id);

CREATE TABLE "Tool" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Tool_id" ON "Tool" (id);

CREATE TABLE "ConjunctiveLicenseSet" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_id" ON "ConjunctiveLicenseSet" (id);

CREATE TABLE "CustomLicense" (
	id INTEGER NOT NULL,
	"obsoletedBy" TEXT,
	"standardLicenseHeader" TEXT,
	"isFsfLibre" BOOLEAN,
	"isDeprecatedLicenseId" BOOLEAN,
	"isOsiApproved" BOOLEAN,
	"licenseXml" TEXT,
	"licenseText" TEXT NOT NULL,
	"standardLicenseTemplate" TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CustomLicense_id" ON "CustomLicense" (id);

CREATE TABLE "CustomLicenseAddition" (
	id INTEGER NOT NULL,
	"standardAdditionTemplate" TEXT,
	"obsoletedBy" TEXT,
	"licenseXml" TEXT,
	"isDeprecatedAdditionId" BOOLEAN,
	"additionText" TEXT NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_id" ON "CustomLicenseAddition" (id);

CREATE TABLE "DisjunctiveLicenseSet" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_id" ON "DisjunctiveLicenseSet" (id);

CREATE TABLE "ExtendableLicense" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ExtendableLicense_id" ON "ExtendableLicense" (id);

CREATE TABLE "IndividualLicensingInfo" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_IndividualLicensingInfo_id" ON "IndividualLicensingInfo" (id);

CREATE TABLE "License" (
	id INTEGER NOT NULL,
	"obsoletedBy" TEXT,
	"standardLicenseHeader" TEXT,
	"isFsfLibre" BOOLEAN,
	"isDeprecatedLicenseId" BOOLEAN,
	"isOsiApproved" BOOLEAN,
	"licenseXml" TEXT,
	"licenseText" TEXT NOT NULL,
	"standardLicenseTemplate" TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_License_id" ON "License" (id);

CREATE TABLE "LicenseAddition" (
	id INTEGER NOT NULL,
	"standardAdditionTemplate" TEXT,
	"obsoletedBy" TEXT,
	"licenseXml" TEXT,
	"isDeprecatedAdditionId" BOOLEAN,
	"additionText" TEXT NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_LicenseAddition_id" ON "LicenseAddition" (id);

CREATE TABLE "ListedLicense" (
	id INTEGER NOT NULL,
	"deprecatedVersion" TEXT,
	"listVersionAdded" TEXT,
	"obsoletedBy" TEXT,
	"standardLicenseHeader" TEXT,
	"isFsfLibre" BOOLEAN,
	"isDeprecatedLicenseId" BOOLEAN,
	"isOsiApproved" BOOLEAN,
	"licenseXml" TEXT,
	"licenseText" TEXT NOT NULL,
	"standardLicenseTemplate" TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ListedLicense_id" ON "ListedLicense" (id);

CREATE TABLE "ListedLicenseException" (
	id INTEGER NOT NULL,
	"listVersionAdded" TEXT,
	"deprecatedVersion" TEXT,
	"standardAdditionTemplate" TEXT,
	"obsoletedBy" TEXT,
	"licenseXml" TEXT,
	"isDeprecatedAdditionId" BOOLEAN,
	"additionText" TEXT NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ListedLicenseException_id" ON "ListedLicenseException" (id);

CREATE TABLE "AnyLicenseInfo" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_AnyLicenseInfo_id" ON "AnyLicenseInfo" (id);

CREATE TABLE "LicenseExpression" (
	id INTEGER NOT NULL,
	"licenseExpression" TEXT NOT NULL,
	"licenseListVersion" TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_LicenseExpression_id" ON "LicenseExpression" (id);

CREATE TABLE "SimpleLicensingText" (
	id INTEGER NOT NULL,
	"licenseText" TEXT NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SimpleLicensingText_id" ON "SimpleLicensingText" (id);

CREATE TABLE "Sbom" (
	id INTEGER NOT NULL,
	context TEXT,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Sbom_id" ON "Sbom" (id);

CREATE TABLE "EnergyConsumption_finetuningEnergyConsumption" (
	"EnergyConsumption_id" INTEGER,
	"finetuningEnergyConsumption_id" INTEGER,
	PRIMARY KEY ("EnergyConsumption_id", "finetuningEnergyConsumption_id"),
	FOREIGN KEY("EnergyConsumption_id") REFERENCES "EnergyConsumption" (id),
	FOREIGN KEY("finetuningEnergyConsumption_id") REFERENCES "EnergyConsumptionDescription" (id)
);
CREATE INDEX "ix_EnergyConsumption_finetuningEnergyConsumption_EnergyConsumption_id" ON "EnergyConsumption_finetuningEnergyConsumption" ("EnergyConsumption_id");
CREATE INDEX "ix_EnergyConsumption_finetuningEnergyConsumption_finetuningEnergyConsumption_id" ON "EnergyConsumption_finetuningEnergyConsumption" ("finetuningEnergyConsumption_id");

CREATE TABLE "EnergyConsumption_inferenceEnergyConsumption" (
	"EnergyConsumption_id" INTEGER,
	"inferenceEnergyConsumption_id" INTEGER,
	PRIMARY KEY ("EnergyConsumption_id", "inferenceEnergyConsumption_id"),
	FOREIGN KEY("EnergyConsumption_id") REFERENCES "EnergyConsumption" (id),
	FOREIGN KEY("inferenceEnergyConsumption_id") REFERENCES "EnergyConsumptionDescription" (id)
);
CREATE INDEX "ix_EnergyConsumption_inferenceEnergyConsumption_inferenceEnergyConsumption_id" ON "EnergyConsumption_inferenceEnergyConsumption" ("inferenceEnergyConsumption_id");
CREATE INDEX "ix_EnergyConsumption_inferenceEnergyConsumption_EnergyConsumption_id" ON "EnergyConsumption_inferenceEnergyConsumption" ("EnergyConsumption_id");

CREATE TABLE "EnergyConsumption_trainingEnergyConsumption" (
	"EnergyConsumption_id" INTEGER,
	"trainingEnergyConsumption_id" INTEGER,
	PRIMARY KEY ("EnergyConsumption_id", "trainingEnergyConsumption_id"),
	FOREIGN KEY("EnergyConsumption_id") REFERENCES "EnergyConsumption" (id),
	FOREIGN KEY("trainingEnergyConsumption_id") REFERENCES "EnergyConsumptionDescription" (id)
);
CREATE INDEX "ix_EnergyConsumption_trainingEnergyConsumption_EnergyConsumption_id" ON "EnergyConsumption_trainingEnergyConsumption" ("EnergyConsumption_id");
CREATE INDEX "ix_EnergyConsumption_trainingEnergyConsumption_trainingEnergyConsumption_id" ON "EnergyConsumption_trainingEnergyConsumption" ("trainingEnergyConsumption_id");

CREATE TABLE "ExternalIdentifier_identifierLocator" (
	"ExternalIdentifier_id" INTEGER,
	"identifierLocator" TEXT,
	PRIMARY KEY ("ExternalIdentifier_id", "identifierLocator"),
	FOREIGN KEY("ExternalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ExternalIdentifier_identifierLocator_identifierLocator" ON "ExternalIdentifier_identifierLocator" ("identifierLocator");
CREATE INDEX "ix_ExternalIdentifier_identifierLocator_ExternalIdentifier_id" ON "ExternalIdentifier_identifierLocator" ("ExternalIdentifier_id");

CREATE TABLE "ExternalRef_core_locator" (
	"ExternalRef_id" INTEGER,
	core_locator TEXT,
	PRIMARY KEY ("ExternalRef_id", core_locator),
	FOREIGN KEY("ExternalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ExternalRef_core_locator_core_locator" ON "ExternalRef_core_locator" (core_locator);
CREATE INDEX "ix_ExternalRef_core_locator_ExternalRef_id" ON "ExternalRef_core_locator" ("ExternalRef_id");

CREATE TABLE "PackageVerificationCode_packageVerificationCodeExcludedFile" (
	"PackageVerificationCode_id" INTEGER,
	"packageVerificationCodeExcludedFile" TEXT,
	PRIMARY KEY ("PackageVerificationCode_id", "packageVerificationCodeExcludedFile"),
	FOREIGN KEY("PackageVerificationCode_id") REFERENCES "PackageVerificationCode" (id)
);
CREATE INDEX "ix_PackageVerificationCode_packageVerificationCodeExcludedFile_PackageVerificationCode_id" ON "PackageVerificationCode_packageVerificationCodeExcludedFile" ("PackageVerificationCode_id");
CREATE INDEX "ix_PackageVerificationCode_packageVerificationCodeExcludedFile_packageVerificationCodeExcludedFile" ON "PackageVerificationCode_packageVerificationCodeExcludedFile" ("packageVerificationCodeExcludedFile");

CREATE TABLE "CdxPropertiesExtension_cdxProperty" (
	"CdxPropertiesExtension_id" INTEGER,
	"cdxProperty_id" INTEGER NOT NULL,
	PRIMARY KEY ("CdxPropertiesExtension_id", "cdxProperty_id"),
	FOREIGN KEY("CdxPropertiesExtension_id") REFERENCES "CdxPropertiesExtension" (id),
	FOREIGN KEY("cdxProperty_id") REFERENCES "CdxPropertyEntry" (id)
);
CREATE INDEX "ix_CdxPropertiesExtension_cdxProperty_cdxProperty_id" ON "CdxPropertiesExtension_cdxProperty" ("cdxProperty_id");
CREATE INDEX "ix_CdxPropertiesExtension_cdxProperty_CdxPropertiesExtension_id" ON "CdxPropertiesExtension_cdxProperty" ("CdxPropertiesExtension_id");

CREATE TABLE "AIPackage" (
	id INTEGER NOT NULL,
	"informationAboutTraining" TEXT,
	"safetyRiskAssessment" VARCHAR(7),
	"useSensitivePersonalInformation" VARCHAR(11),
	limitation TEXT,
	"autonomyType" VARCHAR(11),
	"informationAboutApplication" TEXT,
	"sourceInfo" TEXT,
	"homePage" TEXT,
	"downloadLocation" TEXT,
	"packageVersion" TEXT,
	"packageUrl" TEXT,
	"primaryPurpose" TEXT,
	"copyrightText" TEXT,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"energyConsumption_id" INTEGER,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("energyConsumption_id") REFERENCES "EnergyConsumption" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_AIPackage_id" ON "AIPackage" (id);

CREATE TABLE "Annotation" (
	id INTEGER NOT NULL,
	"contentType" TEXT,
	statement TEXT,
	"annotationType" TEXT NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	subject_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(subject_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Annotation_id" ON "Annotation" (id);

CREATE TABLE "Artifact" (
	id INTEGER NOT NULL,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Artifact_id" ON "Artifact" (id);

CREATE TABLE "LifecycleScopedRelationship" (
	id INTEGER NOT NULL,
	scope TEXT,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_id" ON "LifecycleScopedRelationship" (id);

CREATE TABLE "Relationship" (
	id INTEGER NOT NULL,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Relationship_id" ON "Relationship" (id);

CREATE TABLE "SpdxDocument" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"dataLicense_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("dataLicense_id") REFERENCES "AnyLicenseInfo" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SpdxDocument_id" ON "SpdxDocument" (id);

CREATE TABLE "DatasetPackage" (
	id INTEGER NOT NULL,
	"datasetSize" INTEGER,
	"datasetUpdateMechanism" TEXT,
	"dataCollectionProcess" TEXT,
	"intendedUse" TEXT,
	"confidentialityLevel" VARCHAR(5),
	"datasetAvailability" VARCHAR(14),
	"hasSensitivePersonalInformation" VARCHAR(11),
	"datasetNoise" TEXT,
	"sourceInfo" TEXT,
	"homePage" TEXT,
	"downloadLocation" TEXT,
	"packageVersion" TEXT,
	"packageUrl" TEXT,
	"primaryPurpose" TEXT,
	"copyrightText" TEXT,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_DatasetPackage_id" ON "DatasetPackage" (id);

CREATE TABLE "OrLaterOperator" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"subjectLicense_id" INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("subjectLicense_id") REFERENCES "License" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_OrLaterOperator_id" ON "OrLaterOperator" (id);

CREATE TABLE "WithAdditionOperator" (
	id INTEGER NOT NULL,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"subjectExtendableLicense_id" INTEGER NOT NULL,
	"subjectAddition_id" INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("subjectExtendableLicense_id") REFERENCES "ExtendableLicense" (id),
	FOREIGN KEY("subjectAddition_id") REFERENCES "LicenseAddition" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_WithAdditionOperator_id" ON "WithAdditionOperator" (id);

CREATE TABLE "Vulnerability" (
	id INTEGER NOT NULL,
	"withdrawnTime" DATETIME,
	"modifiedTime" DATETIME,
	"publishedTime" DATETIME,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Vulnerability_id" ON "Vulnerability" (id);

CREATE TABLE "File" (
	id INTEGER NOT NULL,
	"fileKind" VARCHAR(9),
	"contentType" TEXT,
	"primaryPurpose" TEXT,
	"copyrightText" TEXT,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_File_id" ON "File" (id);

CREATE TABLE "Package" (
	id INTEGER NOT NULL,
	"sourceInfo" TEXT,
	"homePage" TEXT,
	"downloadLocation" TEXT,
	"packageVersion" TEXT,
	"packageUrl" TEXT,
	"primaryPurpose" TEXT,
	"copyrightText" TEXT,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Package_id" ON "Package" (id);

CREATE TABLE "SoftwareArtifact" (
	id INTEGER NOT NULL,
	"primaryPurpose" TEXT,
	"copyrightText" TEXT,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SoftwareArtifact_id" ON "SoftwareArtifact" (id);

CREATE TABLE "Build_configSourceDigest" (
	"Build_id" INTEGER,
	"configSourceDigest_id" INTEGER,
	PRIMARY KEY ("Build_id", "configSourceDigest_id"),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY("configSourceDigest_id") REFERENCES "Hash" (id)
);
CREATE INDEX "ix_Build_configSourceDigest_Build_id" ON "Build_configSourceDigest" ("Build_id");
CREATE INDEX "ix_Build_configSourceDigest_configSourceDigest_id" ON "Build_configSourceDigest" ("configSourceDigest_id");

CREATE TABLE "Build_configSourceUri" (
	"Build_id" INTEGER,
	"configSourceUri" TEXT,
	PRIMARY KEY ("Build_id", "configSourceUri"),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id)
);
CREATE INDEX "ix_Build_configSourceUri_Build_id" ON "Build_configSourceUri" ("Build_id");
CREATE INDEX "ix_Build_configSourceUri_configSourceUri" ON "Build_configSourceUri" ("configSourceUri");

CREATE TABLE "Build_parameter" (
	"Build_id" INTEGER,
	parameter_id INTEGER,
	PRIMARY KEY ("Build_id", parameter_id),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY(parameter_id) REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_Build_parameter_Build_id" ON "Build_parameter" ("Build_id");
CREATE INDEX "ix_Build_parameter_parameter_id" ON "Build_parameter" (parameter_id);

CREATE TABLE "Build_configSourceEntrypoint" (
	"Build_id" INTEGER,
	"configSourceEntrypoint" TEXT,
	PRIMARY KEY ("Build_id", "configSourceEntrypoint"),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id)
);
CREATE INDEX "ix_Build_configSourceEntrypoint_configSourceEntrypoint" ON "Build_configSourceEntrypoint" ("configSourceEntrypoint");
CREATE INDEX "ix_Build_configSourceEntrypoint_Build_id" ON "Build_configSourceEntrypoint" ("Build_id");

CREATE TABLE "Build_environment" (
	"Build_id" INTEGER,
	environment_id INTEGER,
	PRIMARY KEY ("Build_id", environment_id),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY(environment_id) REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_Build_environment_environment_id" ON "Build_environment" (environment_id);
CREATE INDEX "ix_Build_environment_Build_id" ON "Build_environment" ("Build_id");

CREATE TABLE "Build_externalIdentifier" (
	"Build_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Build_id", "externalIdentifier_id"),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Build_externalIdentifier_Build_id" ON "Build_externalIdentifier" ("Build_id");
CREATE INDEX "ix_Build_externalIdentifier_externalIdentifier_id" ON "Build_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Build_extension" (
	"Build_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Build_id", extension_id),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Build_extension_Build_id" ON "Build_extension" ("Build_id");
CREATE INDEX "ix_Build_extension_extension_id" ON "Build_extension" (extension_id);

CREATE TABLE "Build_verifiedUsing" (
	"Build_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Build_id", "verifiedUsing_id"),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Build_verifiedUsing_verifiedUsing_id" ON "Build_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Build_verifiedUsing_Build_id" ON "Build_verifiedUsing" ("Build_id");

CREATE TABLE "Build_externalRef" (
	"Build_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Build_id", "externalRef_id"),
	FOREIGN KEY("Build_id") REFERENCES "Build" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Build_externalRef_Build_id" ON "Build_externalRef" ("Build_id");
CREATE INDEX "ix_Build_externalRef_externalRef_id" ON "Build_externalRef" ("externalRef_id");

CREATE TABLE "Agent_externalIdentifier" (
	"Agent_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Agent_id", "externalIdentifier_id"),
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Agent_externalIdentifier_Agent_id" ON "Agent_externalIdentifier" ("Agent_id");
CREATE INDEX "ix_Agent_externalIdentifier_externalIdentifier_id" ON "Agent_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Agent_extension" (
	"Agent_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Agent_id", extension_id),
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Agent_extension_extension_id" ON "Agent_extension" (extension_id);
CREATE INDEX "ix_Agent_extension_Agent_id" ON "Agent_extension" ("Agent_id");

CREATE TABLE "Agent_verifiedUsing" (
	"Agent_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Agent_id", "verifiedUsing_id"),
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Agent_verifiedUsing_verifiedUsing_id" ON "Agent_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Agent_verifiedUsing_Agent_id" ON "Agent_verifiedUsing" ("Agent_id");

CREATE TABLE "Agent_externalRef" (
	"Agent_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Agent_id", "externalRef_id"),
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Agent_externalRef_externalRef_id" ON "Agent_externalRef" ("externalRef_id");
CREATE INDEX "ix_Agent_externalRef_Agent_id" ON "Agent_externalRef" ("Agent_id");

CREATE TABLE "Bom_element" (
	"Bom_id" INTEGER,
	element_id INTEGER,
	PRIMARY KEY ("Bom_id", element_id),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id),
	FOREIGN KEY(element_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_Bom_element_Bom_id" ON "Bom_element" ("Bom_id");
CREATE INDEX "ix_Bom_element_element_id" ON "Bom_element" (element_id);

CREATE TABLE "Bom_profileConformance" (
	"Bom_id" INTEGER,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("Bom_id", "profileConformance"),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id)
);
CREATE INDEX "ix_Bom_profileConformance_Bom_id" ON "Bom_profileConformance" ("Bom_id");
CREATE INDEX "ix_Bom_profileConformance_profileConformance" ON "Bom_profileConformance" ("profileConformance");

CREATE TABLE "Bom_rootElement" (
	"Bom_id" INTEGER,
	"rootElement_id" INTEGER,
	PRIMARY KEY ("Bom_id", "rootElement_id"),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id),
	FOREIGN KEY("rootElement_id") REFERENCES "Element" (id)
);
CREATE INDEX "ix_Bom_rootElement_Bom_id" ON "Bom_rootElement" ("Bom_id");
CREATE INDEX "ix_Bom_rootElement_rootElement_id" ON "Bom_rootElement" ("rootElement_id");

CREATE TABLE "Bom_externalIdentifier" (
	"Bom_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Bom_id", "externalIdentifier_id"),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Bom_externalIdentifier_Bom_id" ON "Bom_externalIdentifier" ("Bom_id");
CREATE INDEX "ix_Bom_externalIdentifier_externalIdentifier_id" ON "Bom_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Bom_extension" (
	"Bom_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Bom_id", extension_id),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Bom_extension_extension_id" ON "Bom_extension" (extension_id);
CREATE INDEX "ix_Bom_extension_Bom_id" ON "Bom_extension" ("Bom_id");

CREATE TABLE "Bom_verifiedUsing" (
	"Bom_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Bom_id", "verifiedUsing_id"),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Bom_verifiedUsing_Bom_id" ON "Bom_verifiedUsing" ("Bom_id");
CREATE INDEX "ix_Bom_verifiedUsing_verifiedUsing_id" ON "Bom_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Bom_externalRef" (
	"Bom_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Bom_id", "externalRef_id"),
	FOREIGN KEY("Bom_id") REFERENCES "Bom" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Bom_externalRef_externalRef_id" ON "Bom_externalRef" ("externalRef_id");
CREATE INDEX "ix_Bom_externalRef_Bom_id" ON "Bom_externalRef" ("Bom_id");

CREATE TABLE "Bundle_element" (
	"Bundle_id" INTEGER,
	element_id INTEGER,
	PRIMARY KEY ("Bundle_id", element_id),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id),
	FOREIGN KEY(element_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_Bundle_element_element_id" ON "Bundle_element" (element_id);
CREATE INDEX "ix_Bundle_element_Bundle_id" ON "Bundle_element" ("Bundle_id");

CREATE TABLE "Bundle_profileConformance" (
	"Bundle_id" INTEGER,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("Bundle_id", "profileConformance"),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id)
);
CREATE INDEX "ix_Bundle_profileConformance_Bundle_id" ON "Bundle_profileConformance" ("Bundle_id");
CREATE INDEX "ix_Bundle_profileConformance_profileConformance" ON "Bundle_profileConformance" ("profileConformance");

CREATE TABLE "Bundle_rootElement" (
	"Bundle_id" INTEGER,
	"rootElement_id" INTEGER,
	PRIMARY KEY ("Bundle_id", "rootElement_id"),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id),
	FOREIGN KEY("rootElement_id") REFERENCES "Element" (id)
);
CREATE INDEX "ix_Bundle_rootElement_rootElement_id" ON "Bundle_rootElement" ("rootElement_id");
CREATE INDEX "ix_Bundle_rootElement_Bundle_id" ON "Bundle_rootElement" ("Bundle_id");

CREATE TABLE "Bundle_externalIdentifier" (
	"Bundle_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Bundle_id", "externalIdentifier_id"),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Bundle_externalIdentifier_Bundle_id" ON "Bundle_externalIdentifier" ("Bundle_id");
CREATE INDEX "ix_Bundle_externalIdentifier_externalIdentifier_id" ON "Bundle_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Bundle_extension" (
	"Bundle_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Bundle_id", extension_id),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Bundle_extension_extension_id" ON "Bundle_extension" (extension_id);
CREATE INDEX "ix_Bundle_extension_Bundle_id" ON "Bundle_extension" ("Bundle_id");

CREATE TABLE "Bundle_verifiedUsing" (
	"Bundle_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Bundle_id", "verifiedUsing_id"),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Bundle_verifiedUsing_Bundle_id" ON "Bundle_verifiedUsing" ("Bundle_id");
CREATE INDEX "ix_Bundle_verifiedUsing_verifiedUsing_id" ON "Bundle_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Bundle_externalRef" (
	"Bundle_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Bundle_id", "externalRef_id"),
	FOREIGN KEY("Bundle_id") REFERENCES "Bundle" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Bundle_externalRef_externalRef_id" ON "Bundle_externalRef" ("externalRef_id");
CREATE INDEX "ix_Bundle_externalRef_Bundle_id" ON "Bundle_externalRef" ("Bundle_id");

CREATE TABLE "CreationInfo_createdBy" (
	"CreationInfo_id" INTEGER,
	"createdBy_id" INTEGER NOT NULL,
	PRIMARY KEY ("CreationInfo_id", "createdBy_id"),
	FOREIGN KEY("CreationInfo_id") REFERENCES "CreationInfo" (id),
	FOREIGN KEY("createdBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_CreationInfo_createdBy_createdBy_id" ON "CreationInfo_createdBy" ("createdBy_id");
CREATE INDEX "ix_CreationInfo_createdBy_CreationInfo_id" ON "CreationInfo_createdBy" ("CreationInfo_id");

CREATE TABLE "CreationInfo_createdUsing" (
	"CreationInfo_id" INTEGER,
	"createdUsing_id" INTEGER,
	PRIMARY KEY ("CreationInfo_id", "createdUsing_id"),
	FOREIGN KEY("CreationInfo_id") REFERENCES "CreationInfo" (id),
	FOREIGN KEY("createdUsing_id") REFERENCES "Tool" (id)
);
CREATE INDEX "ix_CreationInfo_createdUsing_CreationInfo_id" ON "CreationInfo_createdUsing" ("CreationInfo_id");
CREATE INDEX "ix_CreationInfo_createdUsing_createdUsing_id" ON "CreationInfo_createdUsing" ("createdUsing_id");

CREATE TABLE "Element_externalIdentifier" (
	"Element_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Element_id", "externalIdentifier_id"),
	FOREIGN KEY("Element_id") REFERENCES "Element" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Element_externalIdentifier_Element_id" ON "Element_externalIdentifier" ("Element_id");
CREATE INDEX "ix_Element_externalIdentifier_externalIdentifier_id" ON "Element_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Element_extension" (
	"Element_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Element_id", extension_id),
	FOREIGN KEY("Element_id") REFERENCES "Element" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Element_extension_Element_id" ON "Element_extension" ("Element_id");
CREATE INDEX "ix_Element_extension_extension_id" ON "Element_extension" (extension_id);

CREATE TABLE "Element_verifiedUsing" (
	"Element_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Element_id", "verifiedUsing_id"),
	FOREIGN KEY("Element_id") REFERENCES "Element" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Element_verifiedUsing_verifiedUsing_id" ON "Element_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Element_verifiedUsing_Element_id" ON "Element_verifiedUsing" ("Element_id");

CREATE TABLE "Element_externalRef" (
	"Element_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Element_id", "externalRef_id"),
	FOREIGN KEY("Element_id") REFERENCES "Element" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Element_externalRef_externalRef_id" ON "Element_externalRef" ("externalRef_id");
CREATE INDEX "ix_Element_externalRef_Element_id" ON "Element_externalRef" ("Element_id");

CREATE TABLE "ElementCollection_element" (
	"ElementCollection_id" INTEGER,
	element_id INTEGER,
	PRIMARY KEY ("ElementCollection_id", element_id),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id),
	FOREIGN KEY(element_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_ElementCollection_element_element_id" ON "ElementCollection_element" (element_id);
CREATE INDEX "ix_ElementCollection_element_ElementCollection_id" ON "ElementCollection_element" ("ElementCollection_id");

CREATE TABLE "ElementCollection_profileConformance" (
	"ElementCollection_id" INTEGER,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("ElementCollection_id", "profileConformance"),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id)
);
CREATE INDEX "ix_ElementCollection_profileConformance_profileConformance" ON "ElementCollection_profileConformance" ("profileConformance");
CREATE INDEX "ix_ElementCollection_profileConformance_ElementCollection_id" ON "ElementCollection_profileConformance" ("ElementCollection_id");

CREATE TABLE "ElementCollection_rootElement" (
	"ElementCollection_id" INTEGER,
	"rootElement_id" INTEGER,
	PRIMARY KEY ("ElementCollection_id", "rootElement_id"),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id),
	FOREIGN KEY("rootElement_id") REFERENCES "Element" (id)
);
CREATE INDEX "ix_ElementCollection_rootElement_rootElement_id" ON "ElementCollection_rootElement" ("rootElement_id");
CREATE INDEX "ix_ElementCollection_rootElement_ElementCollection_id" ON "ElementCollection_rootElement" ("ElementCollection_id");

CREATE TABLE "ElementCollection_externalIdentifier" (
	"ElementCollection_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("ElementCollection_id", "externalIdentifier_id"),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ElementCollection_externalIdentifier_externalIdentifier_id" ON "ElementCollection_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_ElementCollection_externalIdentifier_ElementCollection_id" ON "ElementCollection_externalIdentifier" ("ElementCollection_id");

CREATE TABLE "ElementCollection_extension" (
	"ElementCollection_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("ElementCollection_id", extension_id),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_ElementCollection_extension_ElementCollection_id" ON "ElementCollection_extension" ("ElementCollection_id");
CREATE INDEX "ix_ElementCollection_extension_extension_id" ON "ElementCollection_extension" (extension_id);

CREATE TABLE "ElementCollection_verifiedUsing" (
	"ElementCollection_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ElementCollection_id", "verifiedUsing_id"),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ElementCollection_verifiedUsing_ElementCollection_id" ON "ElementCollection_verifiedUsing" ("ElementCollection_id");
CREATE INDEX "ix_ElementCollection_verifiedUsing_verifiedUsing_id" ON "ElementCollection_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "ElementCollection_externalRef" (
	"ElementCollection_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("ElementCollection_id", "externalRef_id"),
	FOREIGN KEY("ElementCollection_id") REFERENCES "ElementCollection" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ElementCollection_externalRef_externalRef_id" ON "ElementCollection_externalRef" ("externalRef_id");
CREATE INDEX "ix_ElementCollection_externalRef_ElementCollection_id" ON "ElementCollection_externalRef" ("ElementCollection_id");

CREATE TABLE "IndividualElement_externalIdentifier" (
	"IndividualElement_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("IndividualElement_id", "externalIdentifier_id"),
	FOREIGN KEY("IndividualElement_id") REFERENCES "IndividualElement" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_IndividualElement_externalIdentifier_externalIdentifier_id" ON "IndividualElement_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_IndividualElement_externalIdentifier_IndividualElement_id" ON "IndividualElement_externalIdentifier" ("IndividualElement_id");

CREATE TABLE "IndividualElement_extension" (
	"IndividualElement_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("IndividualElement_id", extension_id),
	FOREIGN KEY("IndividualElement_id") REFERENCES "IndividualElement" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_IndividualElement_extension_IndividualElement_id" ON "IndividualElement_extension" ("IndividualElement_id");
CREATE INDEX "ix_IndividualElement_extension_extension_id" ON "IndividualElement_extension" (extension_id);

CREATE TABLE "IndividualElement_verifiedUsing" (
	"IndividualElement_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("IndividualElement_id", "verifiedUsing_id"),
	FOREIGN KEY("IndividualElement_id") REFERENCES "IndividualElement" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_IndividualElement_verifiedUsing_IndividualElement_id" ON "IndividualElement_verifiedUsing" ("IndividualElement_id");
CREATE INDEX "ix_IndividualElement_verifiedUsing_verifiedUsing_id" ON "IndividualElement_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "IndividualElement_externalRef" (
	"IndividualElement_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("IndividualElement_id", "externalRef_id"),
	FOREIGN KEY("IndividualElement_id") REFERENCES "IndividualElement" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_IndividualElement_externalRef_externalRef_id" ON "IndividualElement_externalRef" ("externalRef_id");
CREATE INDEX "ix_IndividualElement_externalRef_IndividualElement_id" ON "IndividualElement_externalRef" ("IndividualElement_id");

CREATE TABLE "Organization_externalIdentifier" (
	"Organization_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Organization_id", "externalIdentifier_id"),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Organization_externalIdentifier_externalIdentifier_id" ON "Organization_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_Organization_externalIdentifier_Organization_id" ON "Organization_externalIdentifier" ("Organization_id");

CREATE TABLE "Organization_extension" (
	"Organization_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Organization_id", extension_id),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Organization_extension_Organization_id" ON "Organization_extension" ("Organization_id");
CREATE INDEX "ix_Organization_extension_extension_id" ON "Organization_extension" (extension_id);

CREATE TABLE "Organization_verifiedUsing" (
	"Organization_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Organization_id", "verifiedUsing_id"),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Organization_verifiedUsing_verifiedUsing_id" ON "Organization_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Organization_verifiedUsing_Organization_id" ON "Organization_verifiedUsing" ("Organization_id");

CREATE TABLE "Organization_externalRef" (
	"Organization_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Organization_id", "externalRef_id"),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Organization_externalRef_Organization_id" ON "Organization_externalRef" ("Organization_id");
CREATE INDEX "ix_Organization_externalRef_externalRef_id" ON "Organization_externalRef" ("externalRef_id");

CREATE TABLE "Person_externalIdentifier" (
	"Person_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Person_id", "externalIdentifier_id"),
	FOREIGN KEY("Person_id") REFERENCES "Person" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Person_externalIdentifier_Person_id" ON "Person_externalIdentifier" ("Person_id");
CREATE INDEX "ix_Person_externalIdentifier_externalIdentifier_id" ON "Person_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Person_extension" (
	"Person_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Person_id", extension_id),
	FOREIGN KEY("Person_id") REFERENCES "Person" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Person_extension_Person_id" ON "Person_extension" ("Person_id");
CREATE INDEX "ix_Person_extension_extension_id" ON "Person_extension" (extension_id);

CREATE TABLE "Person_verifiedUsing" (
	"Person_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Person_id", "verifiedUsing_id"),
	FOREIGN KEY("Person_id") REFERENCES "Person" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Person_verifiedUsing_Person_id" ON "Person_verifiedUsing" ("Person_id");
CREATE INDEX "ix_Person_verifiedUsing_verifiedUsing_id" ON "Person_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Person_externalRef" (
	"Person_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Person_id", "externalRef_id"),
	FOREIGN KEY("Person_id") REFERENCES "Person" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Person_externalRef_Person_id" ON "Person_externalRef" ("Person_id");
CREATE INDEX "ix_Person_externalRef_externalRef_id" ON "Person_externalRef" ("externalRef_id");

CREATE TABLE "SoftwareAgent_externalIdentifier" (
	"SoftwareAgent_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("SoftwareAgent_id", "externalIdentifier_id"),
	FOREIGN KEY("SoftwareAgent_id") REFERENCES "SoftwareAgent" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_SoftwareAgent_externalIdentifier_externalIdentifier_id" ON "SoftwareAgent_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_SoftwareAgent_externalIdentifier_SoftwareAgent_id" ON "SoftwareAgent_externalIdentifier" ("SoftwareAgent_id");

CREATE TABLE "SoftwareAgent_extension" (
	"SoftwareAgent_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("SoftwareAgent_id", extension_id),
	FOREIGN KEY("SoftwareAgent_id") REFERENCES "SoftwareAgent" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_SoftwareAgent_extension_SoftwareAgent_id" ON "SoftwareAgent_extension" ("SoftwareAgent_id");
CREATE INDEX "ix_SoftwareAgent_extension_extension_id" ON "SoftwareAgent_extension" (extension_id);

CREATE TABLE "SoftwareAgent_verifiedUsing" (
	"SoftwareAgent_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("SoftwareAgent_id", "verifiedUsing_id"),
	FOREIGN KEY("SoftwareAgent_id") REFERENCES "SoftwareAgent" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_SoftwareAgent_verifiedUsing_verifiedUsing_id" ON "SoftwareAgent_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_SoftwareAgent_verifiedUsing_SoftwareAgent_id" ON "SoftwareAgent_verifiedUsing" ("SoftwareAgent_id");

CREATE TABLE "SoftwareAgent_externalRef" (
	"SoftwareAgent_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("SoftwareAgent_id", "externalRef_id"),
	FOREIGN KEY("SoftwareAgent_id") REFERENCES "SoftwareAgent" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_SoftwareAgent_externalRef_SoftwareAgent_id" ON "SoftwareAgent_externalRef" ("SoftwareAgent_id");
CREATE INDEX "ix_SoftwareAgent_externalRef_externalRef_id" ON "SoftwareAgent_externalRef" ("externalRef_id");

CREATE TABLE "Tool_externalIdentifier" (
	"Tool_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Tool_id", "externalIdentifier_id"),
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Tool_externalIdentifier_Tool_id" ON "Tool_externalIdentifier" ("Tool_id");
CREATE INDEX "ix_Tool_externalIdentifier_externalIdentifier_id" ON "Tool_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Tool_extension" (
	"Tool_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Tool_id", extension_id),
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Tool_extension_extension_id" ON "Tool_extension" (extension_id);
CREATE INDEX "ix_Tool_extension_Tool_id" ON "Tool_extension" ("Tool_id");

CREATE TABLE "Tool_verifiedUsing" (
	"Tool_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Tool_id", "verifiedUsing_id"),
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Tool_verifiedUsing_Tool_id" ON "Tool_verifiedUsing" ("Tool_id");
CREATE INDEX "ix_Tool_verifiedUsing_verifiedUsing_id" ON "Tool_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Tool_externalRef" (
	"Tool_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Tool_id", "externalRef_id"),
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Tool_externalRef_Tool_id" ON "Tool_externalRef" ("Tool_id");
CREATE INDEX "ix_Tool_externalRef_externalRef_id" ON "Tool_externalRef" ("externalRef_id");

CREATE TABLE "ConjunctiveLicenseSet_member" (
	"ConjunctiveLicenseSet_id" INTEGER,
	member_id INTEGER NOT NULL,
	PRIMARY KEY ("ConjunctiveLicenseSet_id", member_id),
	FOREIGN KEY("ConjunctiveLicenseSet_id") REFERENCES "ConjunctiveLicenseSet" (id),
	FOREIGN KEY(member_id) REFERENCES "AnyLicenseInfo" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_member_member_id" ON "ConjunctiveLicenseSet_member" (member_id);
CREATE INDEX "ix_ConjunctiveLicenseSet_member_ConjunctiveLicenseSet_id" ON "ConjunctiveLicenseSet_member" ("ConjunctiveLicenseSet_id");

CREATE TABLE "ConjunctiveLicenseSet_externalIdentifier" (
	"ConjunctiveLicenseSet_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("ConjunctiveLicenseSet_id", "externalIdentifier_id"),
	FOREIGN KEY("ConjunctiveLicenseSet_id") REFERENCES "ConjunctiveLicenseSet" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_externalIdentifier_externalIdentifier_id" ON "ConjunctiveLicenseSet_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_ConjunctiveLicenseSet_externalIdentifier_ConjunctiveLicenseSet_id" ON "ConjunctiveLicenseSet_externalIdentifier" ("ConjunctiveLicenseSet_id");

CREATE TABLE "ConjunctiveLicenseSet_extension" (
	"ConjunctiveLicenseSet_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("ConjunctiveLicenseSet_id", extension_id),
	FOREIGN KEY("ConjunctiveLicenseSet_id") REFERENCES "ConjunctiveLicenseSet" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_extension_extension_id" ON "ConjunctiveLicenseSet_extension" (extension_id);
CREATE INDEX "ix_ConjunctiveLicenseSet_extension_ConjunctiveLicenseSet_id" ON "ConjunctiveLicenseSet_extension" ("ConjunctiveLicenseSet_id");

CREATE TABLE "ConjunctiveLicenseSet_verifiedUsing" (
	"ConjunctiveLicenseSet_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ConjunctiveLicenseSet_id", "verifiedUsing_id"),
	FOREIGN KEY("ConjunctiveLicenseSet_id") REFERENCES "ConjunctiveLicenseSet" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_verifiedUsing_ConjunctiveLicenseSet_id" ON "ConjunctiveLicenseSet_verifiedUsing" ("ConjunctiveLicenseSet_id");
CREATE INDEX "ix_ConjunctiveLicenseSet_verifiedUsing_verifiedUsing_id" ON "ConjunctiveLicenseSet_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "ConjunctiveLicenseSet_externalRef" (
	"ConjunctiveLicenseSet_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("ConjunctiveLicenseSet_id", "externalRef_id"),
	FOREIGN KEY("ConjunctiveLicenseSet_id") REFERENCES "ConjunctiveLicenseSet" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_externalRef_externalRef_id" ON "ConjunctiveLicenseSet_externalRef" ("externalRef_id");
CREATE INDEX "ix_ConjunctiveLicenseSet_externalRef_ConjunctiveLicenseSet_id" ON "ConjunctiveLicenseSet_externalRef" ("ConjunctiveLicenseSet_id");

CREATE TABLE "CustomLicense_seeAlso" (
	"CustomLicense_id" INTEGER,
	"seeAlso" TEXT,
	PRIMARY KEY ("CustomLicense_id", "seeAlso"),
	FOREIGN KEY("CustomLicense_id") REFERENCES "CustomLicense" (id)
);
CREATE INDEX "ix_CustomLicense_seeAlso_CustomLicense_id" ON "CustomLicense_seeAlso" ("CustomLicense_id");
CREATE INDEX "ix_CustomLicense_seeAlso_seeAlso" ON "CustomLicense_seeAlso" ("seeAlso");

CREATE TABLE "CustomLicense_externalIdentifier" (
	"CustomLicense_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("CustomLicense_id", "externalIdentifier_id"),
	FOREIGN KEY("CustomLicense_id") REFERENCES "CustomLicense" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_CustomLicense_externalIdentifier_externalIdentifier_id" ON "CustomLicense_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_CustomLicense_externalIdentifier_CustomLicense_id" ON "CustomLicense_externalIdentifier" ("CustomLicense_id");

CREATE TABLE "CustomLicense_extension" (
	"CustomLicense_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("CustomLicense_id", extension_id),
	FOREIGN KEY("CustomLicense_id") REFERENCES "CustomLicense" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_CustomLicense_extension_extension_id" ON "CustomLicense_extension" (extension_id);
CREATE INDEX "ix_CustomLicense_extension_CustomLicense_id" ON "CustomLicense_extension" ("CustomLicense_id");

CREATE TABLE "CustomLicense_verifiedUsing" (
	"CustomLicense_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("CustomLicense_id", "verifiedUsing_id"),
	FOREIGN KEY("CustomLicense_id") REFERENCES "CustomLicense" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_CustomLicense_verifiedUsing_verifiedUsing_id" ON "CustomLicense_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_CustomLicense_verifiedUsing_CustomLicense_id" ON "CustomLicense_verifiedUsing" ("CustomLicense_id");

CREATE TABLE "CustomLicense_externalRef" (
	"CustomLicense_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("CustomLicense_id", "externalRef_id"),
	FOREIGN KEY("CustomLicense_id") REFERENCES "CustomLicense" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_CustomLicense_externalRef_externalRef_id" ON "CustomLicense_externalRef" ("externalRef_id");
CREATE INDEX "ix_CustomLicense_externalRef_CustomLicense_id" ON "CustomLicense_externalRef" ("CustomLicense_id");

CREATE TABLE "CustomLicenseAddition_seeAlso" (
	"CustomLicenseAddition_id" INTEGER,
	"seeAlso" TEXT,
	PRIMARY KEY ("CustomLicenseAddition_id", "seeAlso"),
	FOREIGN KEY("CustomLicenseAddition_id") REFERENCES "CustomLicenseAddition" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_seeAlso_seeAlso" ON "CustomLicenseAddition_seeAlso" ("seeAlso");
CREATE INDEX "ix_CustomLicenseAddition_seeAlso_CustomLicenseAddition_id" ON "CustomLicenseAddition_seeAlso" ("CustomLicenseAddition_id");

CREATE TABLE "CustomLicenseAddition_externalIdentifier" (
	"CustomLicenseAddition_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("CustomLicenseAddition_id", "externalIdentifier_id"),
	FOREIGN KEY("CustomLicenseAddition_id") REFERENCES "CustomLicenseAddition" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_externalIdentifier_externalIdentifier_id" ON "CustomLicenseAddition_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_CustomLicenseAddition_externalIdentifier_CustomLicenseAddition_id" ON "CustomLicenseAddition_externalIdentifier" ("CustomLicenseAddition_id");

CREATE TABLE "CustomLicenseAddition_extension" (
	"CustomLicenseAddition_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("CustomLicenseAddition_id", extension_id),
	FOREIGN KEY("CustomLicenseAddition_id") REFERENCES "CustomLicenseAddition" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_extension_CustomLicenseAddition_id" ON "CustomLicenseAddition_extension" ("CustomLicenseAddition_id");
CREATE INDEX "ix_CustomLicenseAddition_extension_extension_id" ON "CustomLicenseAddition_extension" (extension_id);

CREATE TABLE "CustomLicenseAddition_verifiedUsing" (
	"CustomLicenseAddition_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("CustomLicenseAddition_id", "verifiedUsing_id"),
	FOREIGN KEY("CustomLicenseAddition_id") REFERENCES "CustomLicenseAddition" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_verifiedUsing_verifiedUsing_id" ON "CustomLicenseAddition_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_CustomLicenseAddition_verifiedUsing_CustomLicenseAddition_id" ON "CustomLicenseAddition_verifiedUsing" ("CustomLicenseAddition_id");

CREATE TABLE "CustomLicenseAddition_externalRef" (
	"CustomLicenseAddition_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("CustomLicenseAddition_id", "externalRef_id"),
	FOREIGN KEY("CustomLicenseAddition_id") REFERENCES "CustomLicenseAddition" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_externalRef_externalRef_id" ON "CustomLicenseAddition_externalRef" ("externalRef_id");
CREATE INDEX "ix_CustomLicenseAddition_externalRef_CustomLicenseAddition_id" ON "CustomLicenseAddition_externalRef" ("CustomLicenseAddition_id");

CREATE TABLE "DisjunctiveLicenseSet_member" (
	"DisjunctiveLicenseSet_id" INTEGER,
	member_id INTEGER NOT NULL,
	PRIMARY KEY ("DisjunctiveLicenseSet_id", member_id),
	FOREIGN KEY("DisjunctiveLicenseSet_id") REFERENCES "DisjunctiveLicenseSet" (id),
	FOREIGN KEY(member_id) REFERENCES "AnyLicenseInfo" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_member_DisjunctiveLicenseSet_id" ON "DisjunctiveLicenseSet_member" ("DisjunctiveLicenseSet_id");
CREATE INDEX "ix_DisjunctiveLicenseSet_member_member_id" ON "DisjunctiveLicenseSet_member" (member_id);

CREATE TABLE "DisjunctiveLicenseSet_externalIdentifier" (
	"DisjunctiveLicenseSet_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("DisjunctiveLicenseSet_id", "externalIdentifier_id"),
	FOREIGN KEY("DisjunctiveLicenseSet_id") REFERENCES "DisjunctiveLicenseSet" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_externalIdentifier_externalIdentifier_id" ON "DisjunctiveLicenseSet_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_DisjunctiveLicenseSet_externalIdentifier_DisjunctiveLicenseSet_id" ON "DisjunctiveLicenseSet_externalIdentifier" ("DisjunctiveLicenseSet_id");

CREATE TABLE "DisjunctiveLicenseSet_extension" (
	"DisjunctiveLicenseSet_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("DisjunctiveLicenseSet_id", extension_id),
	FOREIGN KEY("DisjunctiveLicenseSet_id") REFERENCES "DisjunctiveLicenseSet" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_extension_extension_id" ON "DisjunctiveLicenseSet_extension" (extension_id);
CREATE INDEX "ix_DisjunctiveLicenseSet_extension_DisjunctiveLicenseSet_id" ON "DisjunctiveLicenseSet_extension" ("DisjunctiveLicenseSet_id");

CREATE TABLE "DisjunctiveLicenseSet_verifiedUsing" (
	"DisjunctiveLicenseSet_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("DisjunctiveLicenseSet_id", "verifiedUsing_id"),
	FOREIGN KEY("DisjunctiveLicenseSet_id") REFERENCES "DisjunctiveLicenseSet" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_verifiedUsing_verifiedUsing_id" ON "DisjunctiveLicenseSet_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_DisjunctiveLicenseSet_verifiedUsing_DisjunctiveLicenseSet_id" ON "DisjunctiveLicenseSet_verifiedUsing" ("DisjunctiveLicenseSet_id");

CREATE TABLE "DisjunctiveLicenseSet_externalRef" (
	"DisjunctiveLicenseSet_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("DisjunctiveLicenseSet_id", "externalRef_id"),
	FOREIGN KEY("DisjunctiveLicenseSet_id") REFERENCES "DisjunctiveLicenseSet" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_externalRef_DisjunctiveLicenseSet_id" ON "DisjunctiveLicenseSet_externalRef" ("DisjunctiveLicenseSet_id");
CREATE INDEX "ix_DisjunctiveLicenseSet_externalRef_externalRef_id" ON "DisjunctiveLicenseSet_externalRef" ("externalRef_id");

CREATE TABLE "ExtendableLicense_externalIdentifier" (
	"ExtendableLicense_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("ExtendableLicense_id", "externalIdentifier_id"),
	FOREIGN KEY("ExtendableLicense_id") REFERENCES "ExtendableLicense" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ExtendableLicense_externalIdentifier_externalIdentifier_id" ON "ExtendableLicense_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_ExtendableLicense_externalIdentifier_ExtendableLicense_id" ON "ExtendableLicense_externalIdentifier" ("ExtendableLicense_id");

CREATE TABLE "ExtendableLicense_extension" (
	"ExtendableLicense_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("ExtendableLicense_id", extension_id),
	FOREIGN KEY("ExtendableLicense_id") REFERENCES "ExtendableLicense" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_ExtendableLicense_extension_ExtendableLicense_id" ON "ExtendableLicense_extension" ("ExtendableLicense_id");
CREATE INDEX "ix_ExtendableLicense_extension_extension_id" ON "ExtendableLicense_extension" (extension_id);

CREATE TABLE "ExtendableLicense_verifiedUsing" (
	"ExtendableLicense_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ExtendableLicense_id", "verifiedUsing_id"),
	FOREIGN KEY("ExtendableLicense_id") REFERENCES "ExtendableLicense" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ExtendableLicense_verifiedUsing_ExtendableLicense_id" ON "ExtendableLicense_verifiedUsing" ("ExtendableLicense_id");
CREATE INDEX "ix_ExtendableLicense_verifiedUsing_verifiedUsing_id" ON "ExtendableLicense_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "ExtendableLicense_externalRef" (
	"ExtendableLicense_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("ExtendableLicense_id", "externalRef_id"),
	FOREIGN KEY("ExtendableLicense_id") REFERENCES "ExtendableLicense" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ExtendableLicense_externalRef_externalRef_id" ON "ExtendableLicense_externalRef" ("externalRef_id");
CREATE INDEX "ix_ExtendableLicense_externalRef_ExtendableLicense_id" ON "ExtendableLicense_externalRef" ("ExtendableLicense_id");

CREATE TABLE "IndividualLicensingInfo_externalIdentifier" (
	"IndividualLicensingInfo_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("IndividualLicensingInfo_id", "externalIdentifier_id"),
	FOREIGN KEY("IndividualLicensingInfo_id") REFERENCES "IndividualLicensingInfo" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_IndividualLicensingInfo_externalIdentifier_externalIdentifier_id" ON "IndividualLicensingInfo_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_IndividualLicensingInfo_externalIdentifier_IndividualLicensingInfo_id" ON "IndividualLicensingInfo_externalIdentifier" ("IndividualLicensingInfo_id");

CREATE TABLE "IndividualLicensingInfo_extension" (
	"IndividualLicensingInfo_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("IndividualLicensingInfo_id", extension_id),
	FOREIGN KEY("IndividualLicensingInfo_id") REFERENCES "IndividualLicensingInfo" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_IndividualLicensingInfo_extension_extension_id" ON "IndividualLicensingInfo_extension" (extension_id);
CREATE INDEX "ix_IndividualLicensingInfo_extension_IndividualLicensingInfo_id" ON "IndividualLicensingInfo_extension" ("IndividualLicensingInfo_id");

CREATE TABLE "IndividualLicensingInfo_verifiedUsing" (
	"IndividualLicensingInfo_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("IndividualLicensingInfo_id", "verifiedUsing_id"),
	FOREIGN KEY("IndividualLicensingInfo_id") REFERENCES "IndividualLicensingInfo" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_IndividualLicensingInfo_verifiedUsing_verifiedUsing_id" ON "IndividualLicensingInfo_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_IndividualLicensingInfo_verifiedUsing_IndividualLicensingInfo_id" ON "IndividualLicensingInfo_verifiedUsing" ("IndividualLicensingInfo_id");

CREATE TABLE "IndividualLicensingInfo_externalRef" (
	"IndividualLicensingInfo_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("IndividualLicensingInfo_id", "externalRef_id"),
	FOREIGN KEY("IndividualLicensingInfo_id") REFERENCES "IndividualLicensingInfo" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_IndividualLicensingInfo_externalRef_externalRef_id" ON "IndividualLicensingInfo_externalRef" ("externalRef_id");
CREATE INDEX "ix_IndividualLicensingInfo_externalRef_IndividualLicensingInfo_id" ON "IndividualLicensingInfo_externalRef" ("IndividualLicensingInfo_id");

CREATE TABLE "License_seeAlso" (
	"License_id" INTEGER,
	"seeAlso" TEXT,
	PRIMARY KEY ("License_id", "seeAlso"),
	FOREIGN KEY("License_id") REFERENCES "License" (id)
);
CREATE INDEX "ix_License_seeAlso_seeAlso" ON "License_seeAlso" ("seeAlso");
CREATE INDEX "ix_License_seeAlso_License_id" ON "License_seeAlso" ("License_id");

CREATE TABLE "License_externalIdentifier" (
	"License_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("License_id", "externalIdentifier_id"),
	FOREIGN KEY("License_id") REFERENCES "License" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_License_externalIdentifier_License_id" ON "License_externalIdentifier" ("License_id");
CREATE INDEX "ix_License_externalIdentifier_externalIdentifier_id" ON "License_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "License_extension" (
	"License_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("License_id", extension_id),
	FOREIGN KEY("License_id") REFERENCES "License" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_License_extension_License_id" ON "License_extension" ("License_id");
CREATE INDEX "ix_License_extension_extension_id" ON "License_extension" (extension_id);

CREATE TABLE "License_verifiedUsing" (
	"License_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("License_id", "verifiedUsing_id"),
	FOREIGN KEY("License_id") REFERENCES "License" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_License_verifiedUsing_License_id" ON "License_verifiedUsing" ("License_id");
CREATE INDEX "ix_License_verifiedUsing_verifiedUsing_id" ON "License_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "License_externalRef" (
	"License_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("License_id", "externalRef_id"),
	FOREIGN KEY("License_id") REFERENCES "License" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_License_externalRef_externalRef_id" ON "License_externalRef" ("externalRef_id");
CREATE INDEX "ix_License_externalRef_License_id" ON "License_externalRef" ("License_id");

CREATE TABLE "LicenseAddition_seeAlso" (
	"LicenseAddition_id" INTEGER,
	"seeAlso" TEXT,
	PRIMARY KEY ("LicenseAddition_id", "seeAlso"),
	FOREIGN KEY("LicenseAddition_id") REFERENCES "LicenseAddition" (id)
);
CREATE INDEX "ix_LicenseAddition_seeAlso_seeAlso" ON "LicenseAddition_seeAlso" ("seeAlso");
CREATE INDEX "ix_LicenseAddition_seeAlso_LicenseAddition_id" ON "LicenseAddition_seeAlso" ("LicenseAddition_id");

CREATE TABLE "LicenseAddition_externalIdentifier" (
	"LicenseAddition_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("LicenseAddition_id", "externalIdentifier_id"),
	FOREIGN KEY("LicenseAddition_id") REFERENCES "LicenseAddition" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_LicenseAddition_externalIdentifier_externalIdentifier_id" ON "LicenseAddition_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_LicenseAddition_externalIdentifier_LicenseAddition_id" ON "LicenseAddition_externalIdentifier" ("LicenseAddition_id");

CREATE TABLE "LicenseAddition_extension" (
	"LicenseAddition_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("LicenseAddition_id", extension_id),
	FOREIGN KEY("LicenseAddition_id") REFERENCES "LicenseAddition" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_LicenseAddition_extension_extension_id" ON "LicenseAddition_extension" (extension_id);
CREATE INDEX "ix_LicenseAddition_extension_LicenseAddition_id" ON "LicenseAddition_extension" ("LicenseAddition_id");

CREATE TABLE "LicenseAddition_verifiedUsing" (
	"LicenseAddition_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("LicenseAddition_id", "verifiedUsing_id"),
	FOREIGN KEY("LicenseAddition_id") REFERENCES "LicenseAddition" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_LicenseAddition_verifiedUsing_LicenseAddition_id" ON "LicenseAddition_verifiedUsing" ("LicenseAddition_id");
CREATE INDEX "ix_LicenseAddition_verifiedUsing_verifiedUsing_id" ON "LicenseAddition_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "LicenseAddition_externalRef" (
	"LicenseAddition_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("LicenseAddition_id", "externalRef_id"),
	FOREIGN KEY("LicenseAddition_id") REFERENCES "LicenseAddition" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_LicenseAddition_externalRef_externalRef_id" ON "LicenseAddition_externalRef" ("externalRef_id");
CREATE INDEX "ix_LicenseAddition_externalRef_LicenseAddition_id" ON "LicenseAddition_externalRef" ("LicenseAddition_id");

CREATE TABLE "ListedLicense_seeAlso" (
	"ListedLicense_id" INTEGER,
	"seeAlso" TEXT,
	PRIMARY KEY ("ListedLicense_id", "seeAlso"),
	FOREIGN KEY("ListedLicense_id") REFERENCES "ListedLicense" (id)
);
CREATE INDEX "ix_ListedLicense_seeAlso_seeAlso" ON "ListedLicense_seeAlso" ("seeAlso");
CREATE INDEX "ix_ListedLicense_seeAlso_ListedLicense_id" ON "ListedLicense_seeAlso" ("ListedLicense_id");

CREATE TABLE "ListedLicense_externalIdentifier" (
	"ListedLicense_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("ListedLicense_id", "externalIdentifier_id"),
	FOREIGN KEY("ListedLicense_id") REFERENCES "ListedLicense" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ListedLicense_externalIdentifier_externalIdentifier_id" ON "ListedLicense_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_ListedLicense_externalIdentifier_ListedLicense_id" ON "ListedLicense_externalIdentifier" ("ListedLicense_id");

CREATE TABLE "ListedLicense_extension" (
	"ListedLicense_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("ListedLicense_id", extension_id),
	FOREIGN KEY("ListedLicense_id") REFERENCES "ListedLicense" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_ListedLicense_extension_extension_id" ON "ListedLicense_extension" (extension_id);
CREATE INDEX "ix_ListedLicense_extension_ListedLicense_id" ON "ListedLicense_extension" ("ListedLicense_id");

CREATE TABLE "ListedLicense_verifiedUsing" (
	"ListedLicense_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ListedLicense_id", "verifiedUsing_id"),
	FOREIGN KEY("ListedLicense_id") REFERENCES "ListedLicense" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ListedLicense_verifiedUsing_verifiedUsing_id" ON "ListedLicense_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_ListedLicense_verifiedUsing_ListedLicense_id" ON "ListedLicense_verifiedUsing" ("ListedLicense_id");

CREATE TABLE "ListedLicense_externalRef" (
	"ListedLicense_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("ListedLicense_id", "externalRef_id"),
	FOREIGN KEY("ListedLicense_id") REFERENCES "ListedLicense" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ListedLicense_externalRef_ListedLicense_id" ON "ListedLicense_externalRef" ("ListedLicense_id");
CREATE INDEX "ix_ListedLicense_externalRef_externalRef_id" ON "ListedLicense_externalRef" ("externalRef_id");

CREATE TABLE "ListedLicenseException_seeAlso" (
	"ListedLicenseException_id" INTEGER,
	"seeAlso" TEXT,
	PRIMARY KEY ("ListedLicenseException_id", "seeAlso"),
	FOREIGN KEY("ListedLicenseException_id") REFERENCES "ListedLicenseException" (id)
);
CREATE INDEX "ix_ListedLicenseException_seeAlso_ListedLicenseException_id" ON "ListedLicenseException_seeAlso" ("ListedLicenseException_id");
CREATE INDEX "ix_ListedLicenseException_seeAlso_seeAlso" ON "ListedLicenseException_seeAlso" ("seeAlso");

CREATE TABLE "ListedLicenseException_externalIdentifier" (
	"ListedLicenseException_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("ListedLicenseException_id", "externalIdentifier_id"),
	FOREIGN KEY("ListedLicenseException_id") REFERENCES "ListedLicenseException" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ListedLicenseException_externalIdentifier_externalIdentifier_id" ON "ListedLicenseException_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_ListedLicenseException_externalIdentifier_ListedLicenseException_id" ON "ListedLicenseException_externalIdentifier" ("ListedLicenseException_id");

CREATE TABLE "ListedLicenseException_extension" (
	"ListedLicenseException_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("ListedLicenseException_id", extension_id),
	FOREIGN KEY("ListedLicenseException_id") REFERENCES "ListedLicenseException" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_ListedLicenseException_extension_ListedLicenseException_id" ON "ListedLicenseException_extension" ("ListedLicenseException_id");
CREATE INDEX "ix_ListedLicenseException_extension_extension_id" ON "ListedLicenseException_extension" (extension_id);

CREATE TABLE "ListedLicenseException_verifiedUsing" (
	"ListedLicenseException_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ListedLicenseException_id", "verifiedUsing_id"),
	FOREIGN KEY("ListedLicenseException_id") REFERENCES "ListedLicenseException" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ListedLicenseException_verifiedUsing_ListedLicenseException_id" ON "ListedLicenseException_verifiedUsing" ("ListedLicenseException_id");
CREATE INDEX "ix_ListedLicenseException_verifiedUsing_verifiedUsing_id" ON "ListedLicenseException_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "ListedLicenseException_externalRef" (
	"ListedLicenseException_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("ListedLicenseException_id", "externalRef_id"),
	FOREIGN KEY("ListedLicenseException_id") REFERENCES "ListedLicenseException" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ListedLicenseException_externalRef_externalRef_id" ON "ListedLicenseException_externalRef" ("externalRef_id");
CREATE INDEX "ix_ListedLicenseException_externalRef_ListedLicenseException_id" ON "ListedLicenseException_externalRef" ("ListedLicenseException_id");

CREATE TABLE "AnyLicenseInfo_externalIdentifier" (
	"AnyLicenseInfo_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("AnyLicenseInfo_id", "externalIdentifier_id"),
	FOREIGN KEY("AnyLicenseInfo_id") REFERENCES "AnyLicenseInfo" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_AnyLicenseInfo_externalIdentifier_AnyLicenseInfo_id" ON "AnyLicenseInfo_externalIdentifier" ("AnyLicenseInfo_id");
CREATE INDEX "ix_AnyLicenseInfo_externalIdentifier_externalIdentifier_id" ON "AnyLicenseInfo_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "AnyLicenseInfo_extension" (
	"AnyLicenseInfo_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("AnyLicenseInfo_id", extension_id),
	FOREIGN KEY("AnyLicenseInfo_id") REFERENCES "AnyLicenseInfo" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_AnyLicenseInfo_extension_extension_id" ON "AnyLicenseInfo_extension" (extension_id);
CREATE INDEX "ix_AnyLicenseInfo_extension_AnyLicenseInfo_id" ON "AnyLicenseInfo_extension" ("AnyLicenseInfo_id");

CREATE TABLE "AnyLicenseInfo_verifiedUsing" (
	"AnyLicenseInfo_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("AnyLicenseInfo_id", "verifiedUsing_id"),
	FOREIGN KEY("AnyLicenseInfo_id") REFERENCES "AnyLicenseInfo" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_AnyLicenseInfo_verifiedUsing_verifiedUsing_id" ON "AnyLicenseInfo_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_AnyLicenseInfo_verifiedUsing_AnyLicenseInfo_id" ON "AnyLicenseInfo_verifiedUsing" ("AnyLicenseInfo_id");

CREATE TABLE "AnyLicenseInfo_externalRef" (
	"AnyLicenseInfo_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("AnyLicenseInfo_id", "externalRef_id"),
	FOREIGN KEY("AnyLicenseInfo_id") REFERENCES "AnyLicenseInfo" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_AnyLicenseInfo_externalRef_AnyLicenseInfo_id" ON "AnyLicenseInfo_externalRef" ("AnyLicenseInfo_id");
CREATE INDEX "ix_AnyLicenseInfo_externalRef_externalRef_id" ON "AnyLicenseInfo_externalRef" ("externalRef_id");

CREATE TABLE "LicenseExpression_customIdToUri" (
	"LicenseExpression_id" INTEGER,
	"customIdToUri_id" INTEGER,
	PRIMARY KEY ("LicenseExpression_id", "customIdToUri_id"),
	FOREIGN KEY("LicenseExpression_id") REFERENCES "LicenseExpression" (id),
	FOREIGN KEY("customIdToUri_id") REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_LicenseExpression_customIdToUri_LicenseExpression_id" ON "LicenseExpression_customIdToUri" ("LicenseExpression_id");
CREATE INDEX "ix_LicenseExpression_customIdToUri_customIdToUri_id" ON "LicenseExpression_customIdToUri" ("customIdToUri_id");

CREATE TABLE "LicenseExpression_externalIdentifier" (
	"LicenseExpression_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("LicenseExpression_id", "externalIdentifier_id"),
	FOREIGN KEY("LicenseExpression_id") REFERENCES "LicenseExpression" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_LicenseExpression_externalIdentifier_externalIdentifier_id" ON "LicenseExpression_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_LicenseExpression_externalIdentifier_LicenseExpression_id" ON "LicenseExpression_externalIdentifier" ("LicenseExpression_id");

CREATE TABLE "LicenseExpression_extension" (
	"LicenseExpression_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("LicenseExpression_id", extension_id),
	FOREIGN KEY("LicenseExpression_id") REFERENCES "LicenseExpression" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_LicenseExpression_extension_LicenseExpression_id" ON "LicenseExpression_extension" ("LicenseExpression_id");
CREATE INDEX "ix_LicenseExpression_extension_extension_id" ON "LicenseExpression_extension" (extension_id);

CREATE TABLE "LicenseExpression_verifiedUsing" (
	"LicenseExpression_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("LicenseExpression_id", "verifiedUsing_id"),
	FOREIGN KEY("LicenseExpression_id") REFERENCES "LicenseExpression" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_LicenseExpression_verifiedUsing_LicenseExpression_id" ON "LicenseExpression_verifiedUsing" ("LicenseExpression_id");
CREATE INDEX "ix_LicenseExpression_verifiedUsing_verifiedUsing_id" ON "LicenseExpression_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "LicenseExpression_externalRef" (
	"LicenseExpression_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("LicenseExpression_id", "externalRef_id"),
	FOREIGN KEY("LicenseExpression_id") REFERENCES "LicenseExpression" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_LicenseExpression_externalRef_externalRef_id" ON "LicenseExpression_externalRef" ("externalRef_id");
CREATE INDEX "ix_LicenseExpression_externalRef_LicenseExpression_id" ON "LicenseExpression_externalRef" ("LicenseExpression_id");

CREATE TABLE "SimpleLicensingText_externalIdentifier" (
	"SimpleLicensingText_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("SimpleLicensingText_id", "externalIdentifier_id"),
	FOREIGN KEY("SimpleLicensingText_id") REFERENCES "SimpleLicensingText" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_SimpleLicensingText_externalIdentifier_externalIdentifier_id" ON "SimpleLicensingText_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_SimpleLicensingText_externalIdentifier_SimpleLicensingText_id" ON "SimpleLicensingText_externalIdentifier" ("SimpleLicensingText_id");

CREATE TABLE "SimpleLicensingText_extension" (
	"SimpleLicensingText_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("SimpleLicensingText_id", extension_id),
	FOREIGN KEY("SimpleLicensingText_id") REFERENCES "SimpleLicensingText" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_SimpleLicensingText_extension_extension_id" ON "SimpleLicensingText_extension" (extension_id);
CREATE INDEX "ix_SimpleLicensingText_extension_SimpleLicensingText_id" ON "SimpleLicensingText_extension" ("SimpleLicensingText_id");

CREATE TABLE "SimpleLicensingText_verifiedUsing" (
	"SimpleLicensingText_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("SimpleLicensingText_id", "verifiedUsing_id"),
	FOREIGN KEY("SimpleLicensingText_id") REFERENCES "SimpleLicensingText" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_SimpleLicensingText_verifiedUsing_SimpleLicensingText_id" ON "SimpleLicensingText_verifiedUsing" ("SimpleLicensingText_id");
CREATE INDEX "ix_SimpleLicensingText_verifiedUsing_verifiedUsing_id" ON "SimpleLicensingText_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "SimpleLicensingText_externalRef" (
	"SimpleLicensingText_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("SimpleLicensingText_id", "externalRef_id"),
	FOREIGN KEY("SimpleLicensingText_id") REFERENCES "SimpleLicensingText" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_SimpleLicensingText_externalRef_externalRef_id" ON "SimpleLicensingText_externalRef" ("externalRef_id");
CREATE INDEX "ix_SimpleLicensingText_externalRef_SimpleLicensingText_id" ON "SimpleLicensingText_externalRef" ("SimpleLicensingText_id");

CREATE TABLE "Sbom_sbomType" (
	"Sbom_id" INTEGER,
	"sbomType" VARCHAR(8),
	PRIMARY KEY ("Sbom_id", "sbomType"),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id)
);
CREATE INDEX "ix_Sbom_sbomType_Sbom_id" ON "Sbom_sbomType" ("Sbom_id");
CREATE INDEX "ix_Sbom_sbomType_sbomType" ON "Sbom_sbomType" ("sbomType");

CREATE TABLE "Sbom_element" (
	"Sbom_id" INTEGER,
	element_id INTEGER,
	PRIMARY KEY ("Sbom_id", element_id),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id),
	FOREIGN KEY(element_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_Sbom_element_element_id" ON "Sbom_element" (element_id);
CREATE INDEX "ix_Sbom_element_Sbom_id" ON "Sbom_element" ("Sbom_id");

CREATE TABLE "Sbom_profileConformance" (
	"Sbom_id" INTEGER,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("Sbom_id", "profileConformance"),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id)
);
CREATE INDEX "ix_Sbom_profileConformance_Sbom_id" ON "Sbom_profileConformance" ("Sbom_id");
CREATE INDEX "ix_Sbom_profileConformance_profileConformance" ON "Sbom_profileConformance" ("profileConformance");

CREATE TABLE "Sbom_rootElement" (
	"Sbom_id" INTEGER,
	"rootElement_id" INTEGER,
	PRIMARY KEY ("Sbom_id", "rootElement_id"),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id),
	FOREIGN KEY("rootElement_id") REFERENCES "Element" (id)
);
CREATE INDEX "ix_Sbom_rootElement_rootElement_id" ON "Sbom_rootElement" ("rootElement_id");
CREATE INDEX "ix_Sbom_rootElement_Sbom_id" ON "Sbom_rootElement" ("Sbom_id");

CREATE TABLE "Sbom_externalIdentifier" (
	"Sbom_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Sbom_id", "externalIdentifier_id"),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Sbom_externalIdentifier_Sbom_id" ON "Sbom_externalIdentifier" ("Sbom_id");
CREATE INDEX "ix_Sbom_externalIdentifier_externalIdentifier_id" ON "Sbom_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Sbom_extension" (
	"Sbom_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Sbom_id", extension_id),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Sbom_extension_extension_id" ON "Sbom_extension" (extension_id);
CREATE INDEX "ix_Sbom_extension_Sbom_id" ON "Sbom_extension" ("Sbom_id");

CREATE TABLE "Sbom_verifiedUsing" (
	"Sbom_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Sbom_id", "verifiedUsing_id"),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Sbom_verifiedUsing_Sbom_id" ON "Sbom_verifiedUsing" ("Sbom_id");
CREATE INDEX "ix_Sbom_verifiedUsing_verifiedUsing_id" ON "Sbom_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Sbom_externalRef" (
	"Sbom_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Sbom_id", "externalRef_id"),
	FOREIGN KEY("Sbom_id") REFERENCES "Sbom" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Sbom_externalRef_externalRef_id" ON "Sbom_externalRef" ("externalRef_id");
CREATE INDEX "ix_Sbom_externalRef_Sbom_id" ON "Sbom_externalRef" ("Sbom_id");

CREATE TABLE "ExternalMap" (
	id INTEGER NOT NULL,
	"locationHint" TEXT,
	"externalSpdxId" TEXT NOT NULL,
	"definingArtifact_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("definingArtifact_id") REFERENCES "Artifact" (id)
);
CREATE INDEX "ix_ExternalMap_id" ON "ExternalMap" (id);

CREATE TABLE "CvssV2VulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"vectorString" TEXT NOT NULL,
	score NUMERIC NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_id" ON "CvssV2VulnAssessmentRelationship" (id);

CREATE TABLE "CvssV3VulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	severity VARCHAR(8) NOT NULL,
	"vectorString" TEXT NOT NULL,
	score NUMERIC NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_id" ON "CvssV3VulnAssessmentRelationship" (id);

CREATE TABLE "CvssV4VulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	severity VARCHAR(8) NOT NULL,
	"vectorString" TEXT NOT NULL,
	score NUMERIC NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_id" ON "CvssV4VulnAssessmentRelationship" (id);

CREATE TABLE "EpssVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	percentile NUMERIC NOT NULL,
	probability NUMERIC NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_id" ON "EpssVulnAssessmentRelationship" (id);

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	exploited BOOLEAN NOT NULL,
	security_locator TEXT NOT NULL,
	"catalogType" TEXT NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_id" ON "ExploitCatalogVulnAssessmentRelationship" (id);

CREATE TABLE "SsvcVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"decisionType" VARCHAR(9) NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_id" ON "SsvcVulnAssessmentRelationship" (id);

CREATE TABLE "VexAffectedVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"actionStatement" TEXT NOT NULL,
	"actionStatementTime" DATETIME,
	"vexVersion" TEXT,
	"statusNotes" TEXT,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_id" ON "VexAffectedVulnAssessmentRelationship" (id);

CREATE TABLE "VexFixedVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"vexVersion" TEXT,
	"statusNotes" TEXT,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_id" ON "VexFixedVulnAssessmentRelationship" (id);

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"impactStatementTime" DATETIME,
	"justificationType" VARCHAR(43),
	"impactStatement" TEXT,
	"vexVersion" TEXT,
	"statusNotes" TEXT,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_id" ON "VexNotAffectedVulnAssessmentRelationship" (id);

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"vexVersion" TEXT,
	"statusNotes" TEXT,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_id" ON "VexUnderInvestigationVulnAssessmentRelationship" (id);

CREATE TABLE "VexVulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"vexVersion" TEXT,
	"statusNotes" TEXT,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_id" ON "VexVulnAssessmentRelationship" (id);

CREATE TABLE "VulnAssessmentRelationship" (
	id INTEGER NOT NULL,
	"withdrawnTime" DATETIME,
	"publishedTime" DATETIME,
	"modifiedTime" DATETIME,
	completeness VARCHAR(11),
	"startTime" DATETIME,
	"relationshipType" TEXT NOT NULL,
	"endTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"assessedElement_id" INTEGER,
	"suppliedBy_id" INTEGER,
	from_id INTEGER NOT NULL,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("assessedElement_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY(from_id) REFERENCES "Element" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_id" ON "VulnAssessmentRelationship" (id);

CREATE TABLE "Snippet" (
	id INTEGER NOT NULL,
	"primaryPurpose" TEXT,
	"copyrightText" TEXT,
	"builtTime" DATETIME,
	"validUntilTime" DATETIME,
	"releaseTime" DATETIME,
	summary TEXT,
	description TEXT,
	comment TEXT,
	name TEXT,
	"lineRange_id" INTEGER,
	"snippetFromFile_id" INTEGER NOT NULL,
	"byteRange_id" INTEGER,
	"suppliedBy_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("lineRange_id") REFERENCES "PositiveIntegerRange" (id),
	FOREIGN KEY("snippetFromFile_id") REFERENCES "File" (id),
	FOREIGN KEY("byteRange_id") REFERENCES "PositiveIntegerRange" (id),
	FOREIGN KEY("suppliedBy_id") REFERENCES "Agent" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Snippet_id" ON "Snippet" (id);

CREATE TABLE "AIPackage_modelDataPreprocessing" (
	"AIPackage_id" INTEGER,
	"modelDataPreprocessing" TEXT,
	PRIMARY KEY ("AIPackage_id", "modelDataPreprocessing"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_modelDataPreprocessing_AIPackage_id" ON "AIPackage_modelDataPreprocessing" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_modelDataPreprocessing_modelDataPreprocessing" ON "AIPackage_modelDataPreprocessing" ("modelDataPreprocessing");

CREATE TABLE "AIPackage_typeOfModel" (
	"AIPackage_id" INTEGER,
	"typeOfModel" TEXT,
	PRIMARY KEY ("AIPackage_id", "typeOfModel"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_typeOfModel_typeOfModel" ON "AIPackage_typeOfModel" ("typeOfModel");
CREATE INDEX "ix_AIPackage_typeOfModel_AIPackage_id" ON "AIPackage_typeOfModel" ("AIPackage_id");

CREATE TABLE "AIPackage_metricDecisionThreshold" (
	"AIPackage_id" INTEGER,
	"metricDecisionThreshold_id" INTEGER,
	PRIMARY KEY ("AIPackage_id", "metricDecisionThreshold_id"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY("metricDecisionThreshold_id") REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_AIPackage_metricDecisionThreshold_AIPackage_id" ON "AIPackage_metricDecisionThreshold" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_metricDecisionThreshold_metricDecisionThreshold_id" ON "AIPackage_metricDecisionThreshold" ("metricDecisionThreshold_id");

CREATE TABLE "AIPackage_hyperparameter" (
	"AIPackage_id" INTEGER,
	hyperparameter_id INTEGER,
	PRIMARY KEY ("AIPackage_id", hyperparameter_id),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY(hyperparameter_id) REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_AIPackage_hyperparameter_hyperparameter_id" ON "AIPackage_hyperparameter" (hyperparameter_id);
CREATE INDEX "ix_AIPackage_hyperparameter_AIPackage_id" ON "AIPackage_hyperparameter" ("AIPackage_id");

CREATE TABLE "AIPackage_domain" (
	"AIPackage_id" INTEGER,
	domain TEXT,
	PRIMARY KEY ("AIPackage_id", domain),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_domain_AIPackage_id" ON "AIPackage_domain" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_domain_domain" ON "AIPackage_domain" (domain);

CREATE TABLE "AIPackage_modelExplainability" (
	"AIPackage_id" INTEGER,
	"modelExplainability" TEXT,
	PRIMARY KEY ("AIPackage_id", "modelExplainability"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_modelExplainability_AIPackage_id" ON "AIPackage_modelExplainability" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_modelExplainability_modelExplainability" ON "AIPackage_modelExplainability" ("modelExplainability");

CREATE TABLE "AIPackage_metric" (
	"AIPackage_id" INTEGER,
	metric_id INTEGER,
	PRIMARY KEY ("AIPackage_id", metric_id),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY(metric_id) REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_AIPackage_metric_metric_id" ON "AIPackage_metric" (metric_id);
CREATE INDEX "ix_AIPackage_metric_AIPackage_id" ON "AIPackage_metric" ("AIPackage_id");

CREATE TABLE "AIPackage_standardCompliance" (
	"AIPackage_id" INTEGER,
	"standardCompliance" TEXT,
	PRIMARY KEY ("AIPackage_id", "standardCompliance"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_standardCompliance_standardCompliance" ON "AIPackage_standardCompliance" ("standardCompliance");
CREATE INDEX "ix_AIPackage_standardCompliance_AIPackage_id" ON "AIPackage_standardCompliance" ("AIPackage_id");

CREATE TABLE "AIPackage_attributionText" (
	"AIPackage_id" INTEGER,
	"attributionText" TEXT,
	PRIMARY KEY ("AIPackage_id", "attributionText"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_attributionText_attributionText" ON "AIPackage_attributionText" ("attributionText");
CREATE INDEX "ix_AIPackage_attributionText_AIPackage_id" ON "AIPackage_attributionText" ("AIPackage_id");

CREATE TABLE "AIPackage_additionalPurpose" (
	"AIPackage_id" INTEGER,
	"additionalPurpose" TEXT,
	PRIMARY KEY ("AIPackage_id", "additionalPurpose"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_additionalPurpose_additionalPurpose" ON "AIPackage_additionalPurpose" ("additionalPurpose");
CREATE INDEX "ix_AIPackage_additionalPurpose_AIPackage_id" ON "AIPackage_additionalPurpose" ("AIPackage_id");

CREATE TABLE "AIPackage_contentIdentifier" (
	"AIPackage_id" INTEGER,
	"contentIdentifier_id" INTEGER,
	PRIMARY KEY ("AIPackage_id", "contentIdentifier_id"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY("contentIdentifier_id") REFERENCES "ContentIdentifier" (id)
);
CREATE INDEX "ix_AIPackage_contentIdentifier_contentIdentifier_id" ON "AIPackage_contentIdentifier" ("contentIdentifier_id");
CREATE INDEX "ix_AIPackage_contentIdentifier_AIPackage_id" ON "AIPackage_contentIdentifier" ("AIPackage_id");

CREATE TABLE "AIPackage_standardName" (
	"AIPackage_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("AIPackage_id", "standardName"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_standardName_AIPackage_id" ON "AIPackage_standardName" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_standardName_standardName" ON "AIPackage_standardName" ("standardName");

CREATE TABLE "AIPackage_supportLevel" (
	"AIPackage_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("AIPackage_id", "supportLevel"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id)
);
CREATE INDEX "ix_AIPackage_supportLevel_supportLevel" ON "AIPackage_supportLevel" ("supportLevel");
CREATE INDEX "ix_AIPackage_supportLevel_AIPackage_id" ON "AIPackage_supportLevel" ("AIPackage_id");

CREATE TABLE "AIPackage_originatedBy" (
	"AIPackage_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("AIPackage_id", "originatedBy_id"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_AIPackage_originatedBy_originatedBy_id" ON "AIPackage_originatedBy" ("originatedBy_id");
CREATE INDEX "ix_AIPackage_originatedBy_AIPackage_id" ON "AIPackage_originatedBy" ("AIPackage_id");

CREATE TABLE "AIPackage_externalIdentifier" (
	"AIPackage_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("AIPackage_id", "externalIdentifier_id"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_AIPackage_externalIdentifier_externalIdentifier_id" ON "AIPackage_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_AIPackage_externalIdentifier_AIPackage_id" ON "AIPackage_externalIdentifier" ("AIPackage_id");

CREATE TABLE "AIPackage_extension" (
	"AIPackage_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("AIPackage_id", extension_id),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_AIPackage_extension_AIPackage_id" ON "AIPackage_extension" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_extension_extension_id" ON "AIPackage_extension" (extension_id);

CREATE TABLE "AIPackage_verifiedUsing" (
	"AIPackage_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("AIPackage_id", "verifiedUsing_id"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_AIPackage_verifiedUsing_verifiedUsing_id" ON "AIPackage_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_AIPackage_verifiedUsing_AIPackage_id" ON "AIPackage_verifiedUsing" ("AIPackage_id");

CREATE TABLE "AIPackage_externalRef" (
	"AIPackage_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("AIPackage_id", "externalRef_id"),
	FOREIGN KEY("AIPackage_id") REFERENCES "AIPackage" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_AIPackage_externalRef_AIPackage_id" ON "AIPackage_externalRef" ("AIPackage_id");
CREATE INDEX "ix_AIPackage_externalRef_externalRef_id" ON "AIPackage_externalRef" ("externalRef_id");

CREATE TABLE "Annotation_externalIdentifier" (
	"Annotation_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Annotation_id", "externalIdentifier_id"),
	FOREIGN KEY("Annotation_id") REFERENCES "Annotation" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Annotation_externalIdentifier_externalIdentifier_id" ON "Annotation_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_Annotation_externalIdentifier_Annotation_id" ON "Annotation_externalIdentifier" ("Annotation_id");

CREATE TABLE "Annotation_extension" (
	"Annotation_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Annotation_id", extension_id),
	FOREIGN KEY("Annotation_id") REFERENCES "Annotation" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Annotation_extension_Annotation_id" ON "Annotation_extension" ("Annotation_id");
CREATE INDEX "ix_Annotation_extension_extension_id" ON "Annotation_extension" (extension_id);

CREATE TABLE "Annotation_verifiedUsing" (
	"Annotation_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Annotation_id", "verifiedUsing_id"),
	FOREIGN KEY("Annotation_id") REFERENCES "Annotation" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Annotation_verifiedUsing_Annotation_id" ON "Annotation_verifiedUsing" ("Annotation_id");
CREATE INDEX "ix_Annotation_verifiedUsing_verifiedUsing_id" ON "Annotation_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Annotation_externalRef" (
	"Annotation_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Annotation_id", "externalRef_id"),
	FOREIGN KEY("Annotation_id") REFERENCES "Annotation" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Annotation_externalRef_externalRef_id" ON "Annotation_externalRef" ("externalRef_id");
CREATE INDEX "ix_Annotation_externalRef_Annotation_id" ON "Annotation_externalRef" ("Annotation_id");

CREATE TABLE "Artifact_standardName" (
	"Artifact_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("Artifact_id", "standardName"),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id)
);
CREATE INDEX "ix_Artifact_standardName_standardName" ON "Artifact_standardName" ("standardName");
CREATE INDEX "ix_Artifact_standardName_Artifact_id" ON "Artifact_standardName" ("Artifact_id");

CREATE TABLE "Artifact_supportLevel" (
	"Artifact_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Artifact_id", "supportLevel"),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id)
);
CREATE INDEX "ix_Artifact_supportLevel_supportLevel" ON "Artifact_supportLevel" ("supportLevel");
CREATE INDEX "ix_Artifact_supportLevel_Artifact_id" ON "Artifact_supportLevel" ("Artifact_id");

CREATE TABLE "Artifact_originatedBy" (
	"Artifact_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("Artifact_id", "originatedBy_id"),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Artifact_originatedBy_originatedBy_id" ON "Artifact_originatedBy" ("originatedBy_id");
CREATE INDEX "ix_Artifact_originatedBy_Artifact_id" ON "Artifact_originatedBy" ("Artifact_id");

CREATE TABLE "Artifact_externalIdentifier" (
	"Artifact_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Artifact_id", "externalIdentifier_id"),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Artifact_externalIdentifier_externalIdentifier_id" ON "Artifact_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_Artifact_externalIdentifier_Artifact_id" ON "Artifact_externalIdentifier" ("Artifact_id");

CREATE TABLE "Artifact_extension" (
	"Artifact_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Artifact_id", extension_id),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Artifact_extension_Artifact_id" ON "Artifact_extension" ("Artifact_id");
CREATE INDEX "ix_Artifact_extension_extension_id" ON "Artifact_extension" (extension_id);

CREATE TABLE "Artifact_verifiedUsing" (
	"Artifact_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Artifact_id", "verifiedUsing_id"),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Artifact_verifiedUsing_verifiedUsing_id" ON "Artifact_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Artifact_verifiedUsing_Artifact_id" ON "Artifact_verifiedUsing" ("Artifact_id");

CREATE TABLE "Artifact_externalRef" (
	"Artifact_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Artifact_id", "externalRef_id"),
	FOREIGN KEY("Artifact_id") REFERENCES "Artifact" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Artifact_externalRef_Artifact_id" ON "Artifact_externalRef" ("Artifact_id");
CREATE INDEX "ix_Artifact_externalRef_externalRef_id" ON "Artifact_externalRef" ("externalRef_id");

CREATE TABLE "LifecycleScopedRelationship_to" (
	"LifecycleScopedRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("LifecycleScopedRelationship_id", to_id),
	FOREIGN KEY("LifecycleScopedRelationship_id") REFERENCES "LifecycleScopedRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_to_to_id" ON "LifecycleScopedRelationship_to" (to_id);
CREATE INDEX "ix_LifecycleScopedRelationship_to_LifecycleScopedRelationship_id" ON "LifecycleScopedRelationship_to" ("LifecycleScopedRelationship_id");

CREATE TABLE "LifecycleScopedRelationship_externalIdentifier" (
	"LifecycleScopedRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("LifecycleScopedRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("LifecycleScopedRelationship_id") REFERENCES "LifecycleScopedRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_externalIdentifier_externalIdentifier_id" ON "LifecycleScopedRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_LifecycleScopedRelationship_externalIdentifier_LifecycleScopedRelationship_id" ON "LifecycleScopedRelationship_externalIdentifier" ("LifecycleScopedRelationship_id");

CREATE TABLE "LifecycleScopedRelationship_extension" (
	"LifecycleScopedRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("LifecycleScopedRelationship_id", extension_id),
	FOREIGN KEY("LifecycleScopedRelationship_id") REFERENCES "LifecycleScopedRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_extension_extension_id" ON "LifecycleScopedRelationship_extension" (extension_id);
CREATE INDEX "ix_LifecycleScopedRelationship_extension_LifecycleScopedRelationship_id" ON "LifecycleScopedRelationship_extension" ("LifecycleScopedRelationship_id");

CREATE TABLE "LifecycleScopedRelationship_verifiedUsing" (
	"LifecycleScopedRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("LifecycleScopedRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("LifecycleScopedRelationship_id") REFERENCES "LifecycleScopedRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_verifiedUsing_verifiedUsing_id" ON "LifecycleScopedRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_LifecycleScopedRelationship_verifiedUsing_LifecycleScopedRelationship_id" ON "LifecycleScopedRelationship_verifiedUsing" ("LifecycleScopedRelationship_id");

CREATE TABLE "LifecycleScopedRelationship_externalRef" (
	"LifecycleScopedRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("LifecycleScopedRelationship_id", "externalRef_id"),
	FOREIGN KEY("LifecycleScopedRelationship_id") REFERENCES "LifecycleScopedRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_externalRef_externalRef_id" ON "LifecycleScopedRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_LifecycleScopedRelationship_externalRef_LifecycleScopedRelationship_id" ON "LifecycleScopedRelationship_externalRef" ("LifecycleScopedRelationship_id");

CREATE TABLE "Relationship_to" (
	"Relationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("Relationship_id", to_id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_Relationship_to_Relationship_id" ON "Relationship_to" ("Relationship_id");
CREATE INDEX "ix_Relationship_to_to_id" ON "Relationship_to" (to_id);

CREATE TABLE "Relationship_externalIdentifier" (
	"Relationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Relationship_id", "externalIdentifier_id"),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Relationship_externalIdentifier_externalIdentifier_id" ON "Relationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_Relationship_externalIdentifier_Relationship_id" ON "Relationship_externalIdentifier" ("Relationship_id");

CREATE TABLE "Relationship_extension" (
	"Relationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Relationship_id", extension_id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Relationship_extension_extension_id" ON "Relationship_extension" (extension_id);
CREATE INDEX "ix_Relationship_extension_Relationship_id" ON "Relationship_extension" ("Relationship_id");

CREATE TABLE "Relationship_verifiedUsing" (
	"Relationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Relationship_id", "verifiedUsing_id"),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Relationship_verifiedUsing_Relationship_id" ON "Relationship_verifiedUsing" ("Relationship_id");
CREATE INDEX "ix_Relationship_verifiedUsing_verifiedUsing_id" ON "Relationship_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Relationship_externalRef" (
	"Relationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Relationship_id", "externalRef_id"),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Relationship_externalRef_Relationship_id" ON "Relationship_externalRef" ("Relationship_id");
CREATE INDEX "ix_Relationship_externalRef_externalRef_id" ON "Relationship_externalRef" ("externalRef_id");

CREATE TABLE "SpdxDocument_namespaceMap" (
	"SpdxDocument_id" INTEGER,
	"namespaceMap_id" INTEGER,
	PRIMARY KEY ("SpdxDocument_id", "namespaceMap_id"),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY("namespaceMap_id") REFERENCES "NamespaceMap" (id)
);
CREATE INDEX "ix_SpdxDocument_namespaceMap_namespaceMap_id" ON "SpdxDocument_namespaceMap" ("namespaceMap_id");
CREATE INDEX "ix_SpdxDocument_namespaceMap_SpdxDocument_id" ON "SpdxDocument_namespaceMap" ("SpdxDocument_id");

CREATE TABLE "SpdxDocument_element" (
	"SpdxDocument_id" INTEGER,
	element_id INTEGER,
	PRIMARY KEY ("SpdxDocument_id", element_id),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY(element_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_SpdxDocument_element_element_id" ON "SpdxDocument_element" (element_id);
CREATE INDEX "ix_SpdxDocument_element_SpdxDocument_id" ON "SpdxDocument_element" ("SpdxDocument_id");

CREATE TABLE "SpdxDocument_profileConformance" (
	"SpdxDocument_id" INTEGER,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("SpdxDocument_id", "profileConformance"),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id)
);
CREATE INDEX "ix_SpdxDocument_profileConformance_profileConformance" ON "SpdxDocument_profileConformance" ("profileConformance");
CREATE INDEX "ix_SpdxDocument_profileConformance_SpdxDocument_id" ON "SpdxDocument_profileConformance" ("SpdxDocument_id");

CREATE TABLE "SpdxDocument_rootElement" (
	"SpdxDocument_id" INTEGER,
	"rootElement_id" INTEGER,
	PRIMARY KEY ("SpdxDocument_id", "rootElement_id"),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY("rootElement_id") REFERENCES "Element" (id)
);
CREATE INDEX "ix_SpdxDocument_rootElement_SpdxDocument_id" ON "SpdxDocument_rootElement" ("SpdxDocument_id");
CREATE INDEX "ix_SpdxDocument_rootElement_rootElement_id" ON "SpdxDocument_rootElement" ("rootElement_id");

CREATE TABLE "SpdxDocument_externalIdentifier" (
	"SpdxDocument_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("SpdxDocument_id", "externalIdentifier_id"),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_SpdxDocument_externalIdentifier_externalIdentifier_id" ON "SpdxDocument_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_SpdxDocument_externalIdentifier_SpdxDocument_id" ON "SpdxDocument_externalIdentifier" ("SpdxDocument_id");

CREATE TABLE "SpdxDocument_extension" (
	"SpdxDocument_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("SpdxDocument_id", extension_id),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_SpdxDocument_extension_extension_id" ON "SpdxDocument_extension" (extension_id);
CREATE INDEX "ix_SpdxDocument_extension_SpdxDocument_id" ON "SpdxDocument_extension" ("SpdxDocument_id");

CREATE TABLE "SpdxDocument_verifiedUsing" (
	"SpdxDocument_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("SpdxDocument_id", "verifiedUsing_id"),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_SpdxDocument_verifiedUsing_verifiedUsing_id" ON "SpdxDocument_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_SpdxDocument_verifiedUsing_SpdxDocument_id" ON "SpdxDocument_verifiedUsing" ("SpdxDocument_id");

CREATE TABLE "SpdxDocument_externalRef" (
	"SpdxDocument_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("SpdxDocument_id", "externalRef_id"),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_SpdxDocument_externalRef_SpdxDocument_id" ON "SpdxDocument_externalRef" ("SpdxDocument_id");
CREATE INDEX "ix_SpdxDocument_externalRef_externalRef_id" ON "SpdxDocument_externalRef" ("externalRef_id");

CREATE TABLE "DatasetPackage_datasetType" (
	"DatasetPackage_id" INTEGER,
	"datasetType" TEXT NOT NULL,
	PRIMARY KEY ("DatasetPackage_id", "datasetType"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_datasetType_DatasetPackage_id" ON "DatasetPackage_datasetType" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_datasetType_datasetType" ON "DatasetPackage_datasetType" ("datasetType");

CREATE TABLE "DatasetPackage_anonymizationMethodUsed" (
	"DatasetPackage_id" INTEGER,
	"anonymizationMethodUsed" TEXT,
	PRIMARY KEY ("DatasetPackage_id", "anonymizationMethodUsed"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_anonymizationMethodUsed_DatasetPackage_id" ON "DatasetPackage_anonymizationMethodUsed" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_anonymizationMethodUsed_anonymizationMethodUsed" ON "DatasetPackage_anonymizationMethodUsed" ("anonymizationMethodUsed");

CREATE TABLE "DatasetPackage_knownBias" (
	"DatasetPackage_id" INTEGER,
	"knownBias" TEXT,
	PRIMARY KEY ("DatasetPackage_id", "knownBias"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_knownBias_DatasetPackage_id" ON "DatasetPackage_knownBias" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_knownBias_knownBias" ON "DatasetPackage_knownBias" ("knownBias");

CREATE TABLE "DatasetPackage_sensor" (
	"DatasetPackage_id" INTEGER,
	sensor_id INTEGER,
	PRIMARY KEY ("DatasetPackage_id", sensor_id),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY(sensor_id) REFERENCES "DictionaryEntry" (id)
);
CREATE INDEX "ix_DatasetPackage_sensor_DatasetPackage_id" ON "DatasetPackage_sensor" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_sensor_sensor_id" ON "DatasetPackage_sensor" (sensor_id);

CREATE TABLE "DatasetPackage_dataPreprocessing" (
	"DatasetPackage_id" INTEGER,
	"dataPreprocessing" TEXT,
	PRIMARY KEY ("DatasetPackage_id", "dataPreprocessing"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_dataPreprocessing_dataPreprocessing" ON "DatasetPackage_dataPreprocessing" ("dataPreprocessing");
CREATE INDEX "ix_DatasetPackage_dataPreprocessing_DatasetPackage_id" ON "DatasetPackage_dataPreprocessing" ("DatasetPackage_id");

CREATE TABLE "DatasetPackage_attributionText" (
	"DatasetPackage_id" INTEGER,
	"attributionText" TEXT,
	PRIMARY KEY ("DatasetPackage_id", "attributionText"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_attributionText_DatasetPackage_id" ON "DatasetPackage_attributionText" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_attributionText_attributionText" ON "DatasetPackage_attributionText" ("attributionText");

CREATE TABLE "DatasetPackage_additionalPurpose" (
	"DatasetPackage_id" INTEGER,
	"additionalPurpose" TEXT,
	PRIMARY KEY ("DatasetPackage_id", "additionalPurpose"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_additionalPurpose_DatasetPackage_id" ON "DatasetPackage_additionalPurpose" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_additionalPurpose_additionalPurpose" ON "DatasetPackage_additionalPurpose" ("additionalPurpose");

CREATE TABLE "DatasetPackage_contentIdentifier" (
	"DatasetPackage_id" INTEGER,
	"contentIdentifier_id" INTEGER,
	PRIMARY KEY ("DatasetPackage_id", "contentIdentifier_id"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY("contentIdentifier_id") REFERENCES "ContentIdentifier" (id)
);
CREATE INDEX "ix_DatasetPackage_contentIdentifier_DatasetPackage_id" ON "DatasetPackage_contentIdentifier" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_contentIdentifier_contentIdentifier_id" ON "DatasetPackage_contentIdentifier" ("contentIdentifier_id");

CREATE TABLE "DatasetPackage_standardName" (
	"DatasetPackage_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("DatasetPackage_id", "standardName"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_standardName_DatasetPackage_id" ON "DatasetPackage_standardName" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_standardName_standardName" ON "DatasetPackage_standardName" ("standardName");

CREATE TABLE "DatasetPackage_supportLevel" (
	"DatasetPackage_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("DatasetPackage_id", "supportLevel"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id)
);
CREATE INDEX "ix_DatasetPackage_supportLevel_DatasetPackage_id" ON "DatasetPackage_supportLevel" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_supportLevel_supportLevel" ON "DatasetPackage_supportLevel" ("supportLevel");

CREATE TABLE "DatasetPackage_originatedBy" (
	"DatasetPackage_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("DatasetPackage_id", "originatedBy_id"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_DatasetPackage_originatedBy_originatedBy_id" ON "DatasetPackage_originatedBy" ("originatedBy_id");
CREATE INDEX "ix_DatasetPackage_originatedBy_DatasetPackage_id" ON "DatasetPackage_originatedBy" ("DatasetPackage_id");

CREATE TABLE "DatasetPackage_externalIdentifier" (
	"DatasetPackage_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("DatasetPackage_id", "externalIdentifier_id"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_DatasetPackage_externalIdentifier_DatasetPackage_id" ON "DatasetPackage_externalIdentifier" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_externalIdentifier_externalIdentifier_id" ON "DatasetPackage_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "DatasetPackage_extension" (
	"DatasetPackage_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("DatasetPackage_id", extension_id),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_DatasetPackage_extension_extension_id" ON "DatasetPackage_extension" (extension_id);
CREATE INDEX "ix_DatasetPackage_extension_DatasetPackage_id" ON "DatasetPackage_extension" ("DatasetPackage_id");

CREATE TABLE "DatasetPackage_verifiedUsing" (
	"DatasetPackage_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("DatasetPackage_id", "verifiedUsing_id"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_DatasetPackage_verifiedUsing_DatasetPackage_id" ON "DatasetPackage_verifiedUsing" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_verifiedUsing_verifiedUsing_id" ON "DatasetPackage_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "DatasetPackage_externalRef" (
	"DatasetPackage_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("DatasetPackage_id", "externalRef_id"),
	FOREIGN KEY("DatasetPackage_id") REFERENCES "DatasetPackage" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_DatasetPackage_externalRef_DatasetPackage_id" ON "DatasetPackage_externalRef" ("DatasetPackage_id");
CREATE INDEX "ix_DatasetPackage_externalRef_externalRef_id" ON "DatasetPackage_externalRef" ("externalRef_id");

CREATE TABLE "OrLaterOperator_externalIdentifier" (
	"OrLaterOperator_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("OrLaterOperator_id", "externalIdentifier_id"),
	FOREIGN KEY("OrLaterOperator_id") REFERENCES "OrLaterOperator" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_OrLaterOperator_externalIdentifier_externalIdentifier_id" ON "OrLaterOperator_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_OrLaterOperator_externalIdentifier_OrLaterOperator_id" ON "OrLaterOperator_externalIdentifier" ("OrLaterOperator_id");

CREATE TABLE "OrLaterOperator_extension" (
	"OrLaterOperator_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("OrLaterOperator_id", extension_id),
	FOREIGN KEY("OrLaterOperator_id") REFERENCES "OrLaterOperator" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_OrLaterOperator_extension_extension_id" ON "OrLaterOperator_extension" (extension_id);
CREATE INDEX "ix_OrLaterOperator_extension_OrLaterOperator_id" ON "OrLaterOperator_extension" ("OrLaterOperator_id");

CREATE TABLE "OrLaterOperator_verifiedUsing" (
	"OrLaterOperator_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("OrLaterOperator_id", "verifiedUsing_id"),
	FOREIGN KEY("OrLaterOperator_id") REFERENCES "OrLaterOperator" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_OrLaterOperator_verifiedUsing_verifiedUsing_id" ON "OrLaterOperator_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_OrLaterOperator_verifiedUsing_OrLaterOperator_id" ON "OrLaterOperator_verifiedUsing" ("OrLaterOperator_id");

CREATE TABLE "OrLaterOperator_externalRef" (
	"OrLaterOperator_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("OrLaterOperator_id", "externalRef_id"),
	FOREIGN KEY("OrLaterOperator_id") REFERENCES "OrLaterOperator" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_OrLaterOperator_externalRef_OrLaterOperator_id" ON "OrLaterOperator_externalRef" ("OrLaterOperator_id");
CREATE INDEX "ix_OrLaterOperator_externalRef_externalRef_id" ON "OrLaterOperator_externalRef" ("externalRef_id");

CREATE TABLE "WithAdditionOperator_externalIdentifier" (
	"WithAdditionOperator_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("WithAdditionOperator_id", "externalIdentifier_id"),
	FOREIGN KEY("WithAdditionOperator_id") REFERENCES "WithAdditionOperator" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_WithAdditionOperator_externalIdentifier_WithAdditionOperator_id" ON "WithAdditionOperator_externalIdentifier" ("WithAdditionOperator_id");
CREATE INDEX "ix_WithAdditionOperator_externalIdentifier_externalIdentifier_id" ON "WithAdditionOperator_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "WithAdditionOperator_extension" (
	"WithAdditionOperator_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("WithAdditionOperator_id", extension_id),
	FOREIGN KEY("WithAdditionOperator_id") REFERENCES "WithAdditionOperator" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_WithAdditionOperator_extension_extension_id" ON "WithAdditionOperator_extension" (extension_id);
CREATE INDEX "ix_WithAdditionOperator_extension_WithAdditionOperator_id" ON "WithAdditionOperator_extension" ("WithAdditionOperator_id");

CREATE TABLE "WithAdditionOperator_verifiedUsing" (
	"WithAdditionOperator_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("WithAdditionOperator_id", "verifiedUsing_id"),
	FOREIGN KEY("WithAdditionOperator_id") REFERENCES "WithAdditionOperator" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_WithAdditionOperator_verifiedUsing_verifiedUsing_id" ON "WithAdditionOperator_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_WithAdditionOperator_verifiedUsing_WithAdditionOperator_id" ON "WithAdditionOperator_verifiedUsing" ("WithAdditionOperator_id");

CREATE TABLE "WithAdditionOperator_externalRef" (
	"WithAdditionOperator_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("WithAdditionOperator_id", "externalRef_id"),
	FOREIGN KEY("WithAdditionOperator_id") REFERENCES "WithAdditionOperator" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_WithAdditionOperator_externalRef_WithAdditionOperator_id" ON "WithAdditionOperator_externalRef" ("WithAdditionOperator_id");
CREATE INDEX "ix_WithAdditionOperator_externalRef_externalRef_id" ON "WithAdditionOperator_externalRef" ("externalRef_id");

CREATE TABLE "Vulnerability_standardName" (
	"Vulnerability_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("Vulnerability_id", "standardName"),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id)
);
CREATE INDEX "ix_Vulnerability_standardName_Vulnerability_id" ON "Vulnerability_standardName" ("Vulnerability_id");
CREATE INDEX "ix_Vulnerability_standardName_standardName" ON "Vulnerability_standardName" ("standardName");

CREATE TABLE "Vulnerability_supportLevel" (
	"Vulnerability_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Vulnerability_id", "supportLevel"),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id)
);
CREATE INDEX "ix_Vulnerability_supportLevel_Vulnerability_id" ON "Vulnerability_supportLevel" ("Vulnerability_id");
CREATE INDEX "ix_Vulnerability_supportLevel_supportLevel" ON "Vulnerability_supportLevel" ("supportLevel");

CREATE TABLE "Vulnerability_originatedBy" (
	"Vulnerability_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("Vulnerability_id", "originatedBy_id"),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Vulnerability_originatedBy_originatedBy_id" ON "Vulnerability_originatedBy" ("originatedBy_id");
CREATE INDEX "ix_Vulnerability_originatedBy_Vulnerability_id" ON "Vulnerability_originatedBy" ("Vulnerability_id");

CREATE TABLE "Vulnerability_externalIdentifier" (
	"Vulnerability_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Vulnerability_id", "externalIdentifier_id"),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Vulnerability_externalIdentifier_Vulnerability_id" ON "Vulnerability_externalIdentifier" ("Vulnerability_id");
CREATE INDEX "ix_Vulnerability_externalIdentifier_externalIdentifier_id" ON "Vulnerability_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Vulnerability_extension" (
	"Vulnerability_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Vulnerability_id", extension_id),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Vulnerability_extension_extension_id" ON "Vulnerability_extension" (extension_id);
CREATE INDEX "ix_Vulnerability_extension_Vulnerability_id" ON "Vulnerability_extension" ("Vulnerability_id");

CREATE TABLE "Vulnerability_verifiedUsing" (
	"Vulnerability_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Vulnerability_id", "verifiedUsing_id"),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Vulnerability_verifiedUsing_verifiedUsing_id" ON "Vulnerability_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Vulnerability_verifiedUsing_Vulnerability_id" ON "Vulnerability_verifiedUsing" ("Vulnerability_id");

CREATE TABLE "Vulnerability_externalRef" (
	"Vulnerability_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Vulnerability_id", "externalRef_id"),
	FOREIGN KEY("Vulnerability_id") REFERENCES "Vulnerability" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Vulnerability_externalRef_externalRef_id" ON "Vulnerability_externalRef" ("externalRef_id");
CREATE INDEX "ix_Vulnerability_externalRef_Vulnerability_id" ON "Vulnerability_externalRef" ("Vulnerability_id");

CREATE TABLE "File_attributionText" (
	"File_id" INTEGER,
	"attributionText" TEXT,
	PRIMARY KEY ("File_id", "attributionText"),
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE INDEX "ix_File_attributionText_attributionText" ON "File_attributionText" ("attributionText");
CREATE INDEX "ix_File_attributionText_File_id" ON "File_attributionText" ("File_id");

CREATE TABLE "File_additionalPurpose" (
	"File_id" INTEGER,
	"additionalPurpose" TEXT,
	PRIMARY KEY ("File_id", "additionalPurpose"),
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE INDEX "ix_File_additionalPurpose_File_id" ON "File_additionalPurpose" ("File_id");
CREATE INDEX "ix_File_additionalPurpose_additionalPurpose" ON "File_additionalPurpose" ("additionalPurpose");

CREATE TABLE "File_contentIdentifier" (
	"File_id" INTEGER,
	"contentIdentifier_id" INTEGER,
	PRIMARY KEY ("File_id", "contentIdentifier_id"),
	FOREIGN KEY("File_id") REFERENCES "File" (id),
	FOREIGN KEY("contentIdentifier_id") REFERENCES "ContentIdentifier" (id)
);
CREATE INDEX "ix_File_contentIdentifier_contentIdentifier_id" ON "File_contentIdentifier" ("contentIdentifier_id");
CREATE INDEX "ix_File_contentIdentifier_File_id" ON "File_contentIdentifier" ("File_id");

CREATE TABLE "File_standardName" (
	"File_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("File_id", "standardName"),
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE INDEX "ix_File_standardName_File_id" ON "File_standardName" ("File_id");
CREATE INDEX "ix_File_standardName_standardName" ON "File_standardName" ("standardName");

CREATE TABLE "File_supportLevel" (
	"File_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("File_id", "supportLevel"),
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE INDEX "ix_File_supportLevel_supportLevel" ON "File_supportLevel" ("supportLevel");
CREATE INDEX "ix_File_supportLevel_File_id" ON "File_supportLevel" ("File_id");

CREATE TABLE "File_originatedBy" (
	"File_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("File_id", "originatedBy_id"),
	FOREIGN KEY("File_id") REFERENCES "File" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_File_originatedBy_File_id" ON "File_originatedBy" ("File_id");
CREATE INDEX "ix_File_originatedBy_originatedBy_id" ON "File_originatedBy" ("originatedBy_id");

CREATE TABLE "File_externalIdentifier" (
	"File_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("File_id", "externalIdentifier_id"),
	FOREIGN KEY("File_id") REFERENCES "File" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_File_externalIdentifier_File_id" ON "File_externalIdentifier" ("File_id");
CREATE INDEX "ix_File_externalIdentifier_externalIdentifier_id" ON "File_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "File_extension" (
	"File_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("File_id", extension_id),
	FOREIGN KEY("File_id") REFERENCES "File" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_File_extension_extension_id" ON "File_extension" (extension_id);
CREATE INDEX "ix_File_extension_File_id" ON "File_extension" ("File_id");

CREATE TABLE "File_verifiedUsing" (
	"File_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("File_id", "verifiedUsing_id"),
	FOREIGN KEY("File_id") REFERENCES "File" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_File_verifiedUsing_verifiedUsing_id" ON "File_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_File_verifiedUsing_File_id" ON "File_verifiedUsing" ("File_id");

CREATE TABLE "File_externalRef" (
	"File_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("File_id", "externalRef_id"),
	FOREIGN KEY("File_id") REFERENCES "File" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_File_externalRef_File_id" ON "File_externalRef" ("File_id");
CREATE INDEX "ix_File_externalRef_externalRef_id" ON "File_externalRef" ("externalRef_id");

CREATE TABLE "Package_attributionText" (
	"Package_id" INTEGER,
	"attributionText" TEXT,
	PRIMARY KEY ("Package_id", "attributionText"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id)
);
CREATE INDEX "ix_Package_attributionText_attributionText" ON "Package_attributionText" ("attributionText");
CREATE INDEX "ix_Package_attributionText_Package_id" ON "Package_attributionText" ("Package_id");

CREATE TABLE "Package_additionalPurpose" (
	"Package_id" INTEGER,
	"additionalPurpose" TEXT,
	PRIMARY KEY ("Package_id", "additionalPurpose"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id)
);
CREATE INDEX "ix_Package_additionalPurpose_Package_id" ON "Package_additionalPurpose" ("Package_id");
CREATE INDEX "ix_Package_additionalPurpose_additionalPurpose" ON "Package_additionalPurpose" ("additionalPurpose");

CREATE TABLE "Package_contentIdentifier" (
	"Package_id" INTEGER,
	"contentIdentifier_id" INTEGER,
	PRIMARY KEY ("Package_id", "contentIdentifier_id"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id),
	FOREIGN KEY("contentIdentifier_id") REFERENCES "ContentIdentifier" (id)
);
CREATE INDEX "ix_Package_contentIdentifier_Package_id" ON "Package_contentIdentifier" ("Package_id");
CREATE INDEX "ix_Package_contentIdentifier_contentIdentifier_id" ON "Package_contentIdentifier" ("contentIdentifier_id");

CREATE TABLE "Package_standardName" (
	"Package_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("Package_id", "standardName"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id)
);
CREATE INDEX "ix_Package_standardName_Package_id" ON "Package_standardName" ("Package_id");
CREATE INDEX "ix_Package_standardName_standardName" ON "Package_standardName" ("standardName");

CREATE TABLE "Package_supportLevel" (
	"Package_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Package_id", "supportLevel"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id)
);
CREATE INDEX "ix_Package_supportLevel_Package_id" ON "Package_supportLevel" ("Package_id");
CREATE INDEX "ix_Package_supportLevel_supportLevel" ON "Package_supportLevel" ("supportLevel");

CREATE TABLE "Package_originatedBy" (
	"Package_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("Package_id", "originatedBy_id"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Package_originatedBy_Package_id" ON "Package_originatedBy" ("Package_id");
CREATE INDEX "ix_Package_originatedBy_originatedBy_id" ON "Package_originatedBy" ("originatedBy_id");

CREATE TABLE "Package_externalIdentifier" (
	"Package_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Package_id", "externalIdentifier_id"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Package_externalIdentifier_Package_id" ON "Package_externalIdentifier" ("Package_id");
CREATE INDEX "ix_Package_externalIdentifier_externalIdentifier_id" ON "Package_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Package_extension" (
	"Package_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Package_id", extension_id),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Package_extension_Package_id" ON "Package_extension" ("Package_id");
CREATE INDEX "ix_Package_extension_extension_id" ON "Package_extension" (extension_id);

CREATE TABLE "Package_verifiedUsing" (
	"Package_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Package_id", "verifiedUsing_id"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Package_verifiedUsing_Package_id" ON "Package_verifiedUsing" ("Package_id");
CREATE INDEX "ix_Package_verifiedUsing_verifiedUsing_id" ON "Package_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "Package_externalRef" (
	"Package_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Package_id", "externalRef_id"),
	FOREIGN KEY("Package_id") REFERENCES "Package" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Package_externalRef_Package_id" ON "Package_externalRef" ("Package_id");
CREATE INDEX "ix_Package_externalRef_externalRef_id" ON "Package_externalRef" ("externalRef_id");

CREATE TABLE "SoftwareArtifact_attributionText" (
	"SoftwareArtifact_id" INTEGER,
	"attributionText" TEXT,
	PRIMARY KEY ("SoftwareArtifact_id", "attributionText"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id)
);
CREATE INDEX "ix_SoftwareArtifact_attributionText_attributionText" ON "SoftwareArtifact_attributionText" ("attributionText");
CREATE INDEX "ix_SoftwareArtifact_attributionText_SoftwareArtifact_id" ON "SoftwareArtifact_attributionText" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_additionalPurpose" (
	"SoftwareArtifact_id" INTEGER,
	"additionalPurpose" TEXT,
	PRIMARY KEY ("SoftwareArtifact_id", "additionalPurpose"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id)
);
CREATE INDEX "ix_SoftwareArtifact_additionalPurpose_SoftwareArtifact_id" ON "SoftwareArtifact_additionalPurpose" ("SoftwareArtifact_id");
CREATE INDEX "ix_SoftwareArtifact_additionalPurpose_additionalPurpose" ON "SoftwareArtifact_additionalPurpose" ("additionalPurpose");

CREATE TABLE "SoftwareArtifact_contentIdentifier" (
	"SoftwareArtifact_id" INTEGER,
	"contentIdentifier_id" INTEGER,
	PRIMARY KEY ("SoftwareArtifact_id", "contentIdentifier_id"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("contentIdentifier_id") REFERENCES "ContentIdentifier" (id)
);
CREATE INDEX "ix_SoftwareArtifact_contentIdentifier_contentIdentifier_id" ON "SoftwareArtifact_contentIdentifier" ("contentIdentifier_id");
CREATE INDEX "ix_SoftwareArtifact_contentIdentifier_SoftwareArtifact_id" ON "SoftwareArtifact_contentIdentifier" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_standardName" (
	"SoftwareArtifact_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("SoftwareArtifact_id", "standardName"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id)
);
CREATE INDEX "ix_SoftwareArtifact_standardName_standardName" ON "SoftwareArtifact_standardName" ("standardName");
CREATE INDEX "ix_SoftwareArtifact_standardName_SoftwareArtifact_id" ON "SoftwareArtifact_standardName" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_supportLevel" (
	"SoftwareArtifact_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("SoftwareArtifact_id", "supportLevel"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id)
);
CREATE INDEX "ix_SoftwareArtifact_supportLevel_supportLevel" ON "SoftwareArtifact_supportLevel" ("supportLevel");
CREATE INDEX "ix_SoftwareArtifact_supportLevel_SoftwareArtifact_id" ON "SoftwareArtifact_supportLevel" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_originatedBy" (
	"SoftwareArtifact_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("SoftwareArtifact_id", "originatedBy_id"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_SoftwareArtifact_originatedBy_SoftwareArtifact_id" ON "SoftwareArtifact_originatedBy" ("SoftwareArtifact_id");
CREATE INDEX "ix_SoftwareArtifact_originatedBy_originatedBy_id" ON "SoftwareArtifact_originatedBy" ("originatedBy_id");

CREATE TABLE "SoftwareArtifact_externalIdentifier" (
	"SoftwareArtifact_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("SoftwareArtifact_id", "externalIdentifier_id"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_SoftwareArtifact_externalIdentifier_externalIdentifier_id" ON "SoftwareArtifact_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_SoftwareArtifact_externalIdentifier_SoftwareArtifact_id" ON "SoftwareArtifact_externalIdentifier" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_extension" (
	"SoftwareArtifact_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("SoftwareArtifact_id", extension_id),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_SoftwareArtifact_extension_extension_id" ON "SoftwareArtifact_extension" (extension_id);
CREATE INDEX "ix_SoftwareArtifact_extension_SoftwareArtifact_id" ON "SoftwareArtifact_extension" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_verifiedUsing" (
	"SoftwareArtifact_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("SoftwareArtifact_id", "verifiedUsing_id"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_SoftwareArtifact_verifiedUsing_verifiedUsing_id" ON "SoftwareArtifact_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_SoftwareArtifact_verifiedUsing_SoftwareArtifact_id" ON "SoftwareArtifact_verifiedUsing" ("SoftwareArtifact_id");

CREATE TABLE "SoftwareArtifact_externalRef" (
	"SoftwareArtifact_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("SoftwareArtifact_id", "externalRef_id"),
	FOREIGN KEY("SoftwareArtifact_id") REFERENCES "SoftwareArtifact" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_SoftwareArtifact_externalRef_externalRef_id" ON "SoftwareArtifact_externalRef" ("externalRef_id");
CREATE INDEX "ix_SoftwareArtifact_externalRef_SoftwareArtifact_id" ON "SoftwareArtifact_externalRef" ("SoftwareArtifact_id");

CREATE TABLE "ExternalMap_verifiedUsing" (
	"ExternalMap_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ExternalMap_id", "verifiedUsing_id"),
	FOREIGN KEY("ExternalMap_id") REFERENCES "ExternalMap" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ExternalMap_verifiedUsing_verifiedUsing_id" ON "ExternalMap_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_ExternalMap_verifiedUsing_ExternalMap_id" ON "ExternalMap_verifiedUsing" ("ExternalMap_id");

CREATE TABLE "SpdxDocument_import" (
	"SpdxDocument_id" INTEGER,
	import_id INTEGER,
	PRIMARY KEY ("SpdxDocument_id", import_id),
	FOREIGN KEY("SpdxDocument_id") REFERENCES "SpdxDocument" (id),
	FOREIGN KEY(import_id) REFERENCES "ExternalMap" (id)
);
CREATE INDEX "ix_SpdxDocument_import_SpdxDocument_id" ON "SpdxDocument_import" ("SpdxDocument_id");
CREATE INDEX "ix_SpdxDocument_import_import_id" ON "SpdxDocument_import" (import_id);

CREATE TABLE "CvssV2VulnAssessmentRelationship_to" (
	"CvssV2VulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("CvssV2VulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_id") REFERENCES "CvssV2VulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_to_CvssV2VulnAssessmentRelationship_id" ON "CvssV2VulnAssessmentRelationship_to" ("CvssV2VulnAssessmentRelationship_id");
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_to_to_id" ON "CvssV2VulnAssessmentRelationship_to" (to_id);

CREATE TABLE "CvssV2VulnAssessmentRelationship_externalIdentifier" (
	"CvssV2VulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("CvssV2VulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_id") REFERENCES "CvssV2VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_externalIdentifier_CvssV2VulnAssessmentRelationship_id" ON "CvssV2VulnAssessmentRelationship_externalIdentifier" ("CvssV2VulnAssessmentRelationship_id");
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "CvssV2VulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "CvssV2VulnAssessmentRelationship_extension" (
	"CvssV2VulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("CvssV2VulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_id") REFERENCES "CvssV2VulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_extension_extension_id" ON "CvssV2VulnAssessmentRelationship_extension" (extension_id);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_extension_CvssV2VulnAssessmentRelationship_id" ON "CvssV2VulnAssessmentRelationship_extension" ("CvssV2VulnAssessmentRelationship_id");

CREATE TABLE "CvssV2VulnAssessmentRelationship_verifiedUsing" (
	"CvssV2VulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("CvssV2VulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_id") REFERENCES "CvssV2VulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "CvssV2VulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_verifiedUsing_CvssV2VulnAssessmentRelationship_id" ON "CvssV2VulnAssessmentRelationship_verifiedUsing" ("CvssV2VulnAssessmentRelationship_id");

CREATE TABLE "CvssV2VulnAssessmentRelationship_externalRef" (
	"CvssV2VulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("CvssV2VulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_id") REFERENCES "CvssV2VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_externalRef_externalRef_id" ON "CvssV2VulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_externalRef_CvssV2VulnAssessmentRelationship_id" ON "CvssV2VulnAssessmentRelationship_externalRef" ("CvssV2VulnAssessmentRelationship_id");

CREATE TABLE "CvssV3VulnAssessmentRelationship_to" (
	"CvssV3VulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("CvssV3VulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_id") REFERENCES "CvssV3VulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_to_to_id" ON "CvssV3VulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_to_CvssV3VulnAssessmentRelationship_id" ON "CvssV3VulnAssessmentRelationship_to" ("CvssV3VulnAssessmentRelationship_id");

CREATE TABLE "CvssV3VulnAssessmentRelationship_externalIdentifier" (
	"CvssV3VulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("CvssV3VulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_id") REFERENCES "CvssV3VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_externalIdentifier_CvssV3VulnAssessmentRelationship_id" ON "CvssV3VulnAssessmentRelationship_externalIdentifier" ("CvssV3VulnAssessmentRelationship_id");
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "CvssV3VulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "CvssV3VulnAssessmentRelationship_extension" (
	"CvssV3VulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("CvssV3VulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_id") REFERENCES "CvssV3VulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_extension_CvssV3VulnAssessmentRelationship_id" ON "CvssV3VulnAssessmentRelationship_extension" ("CvssV3VulnAssessmentRelationship_id");
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_extension_extension_id" ON "CvssV3VulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "CvssV3VulnAssessmentRelationship_verifiedUsing" (
	"CvssV3VulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("CvssV3VulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_id") REFERENCES "CvssV3VulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "CvssV3VulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_verifiedUsing_CvssV3VulnAssessmentRelationship_id" ON "CvssV3VulnAssessmentRelationship_verifiedUsing" ("CvssV3VulnAssessmentRelationship_id");

CREATE TABLE "CvssV3VulnAssessmentRelationship_externalRef" (
	"CvssV3VulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("CvssV3VulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_id") REFERENCES "CvssV3VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_externalRef_externalRef_id" ON "CvssV3VulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_externalRef_CvssV3VulnAssessmentRelationship_id" ON "CvssV3VulnAssessmentRelationship_externalRef" ("CvssV3VulnAssessmentRelationship_id");

CREATE TABLE "CvssV4VulnAssessmentRelationship_to" (
	"CvssV4VulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("CvssV4VulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_id") REFERENCES "CvssV4VulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_to_to_id" ON "CvssV4VulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_to_CvssV4VulnAssessmentRelationship_id" ON "CvssV4VulnAssessmentRelationship_to" ("CvssV4VulnAssessmentRelationship_id");

CREATE TABLE "CvssV4VulnAssessmentRelationship_externalIdentifier" (
	"CvssV4VulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("CvssV4VulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_id") REFERENCES "CvssV4VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "CvssV4VulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_externalIdentifier_CvssV4VulnAssessmentRelationship_id" ON "CvssV4VulnAssessmentRelationship_externalIdentifier" ("CvssV4VulnAssessmentRelationship_id");

CREATE TABLE "CvssV4VulnAssessmentRelationship_extension" (
	"CvssV4VulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("CvssV4VulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_id") REFERENCES "CvssV4VulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_extension_extension_id" ON "CvssV4VulnAssessmentRelationship_extension" (extension_id);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_extension_CvssV4VulnAssessmentRelationship_id" ON "CvssV4VulnAssessmentRelationship_extension" ("CvssV4VulnAssessmentRelationship_id");

CREATE TABLE "CvssV4VulnAssessmentRelationship_verifiedUsing" (
	"CvssV4VulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("CvssV4VulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_id") REFERENCES "CvssV4VulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "CvssV4VulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_verifiedUsing_CvssV4VulnAssessmentRelationship_id" ON "CvssV4VulnAssessmentRelationship_verifiedUsing" ("CvssV4VulnAssessmentRelationship_id");

CREATE TABLE "CvssV4VulnAssessmentRelationship_externalRef" (
	"CvssV4VulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("CvssV4VulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_id") REFERENCES "CvssV4VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_externalRef_CvssV4VulnAssessmentRelationship_id" ON "CvssV4VulnAssessmentRelationship_externalRef" ("CvssV4VulnAssessmentRelationship_id");
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_externalRef_externalRef_id" ON "CvssV4VulnAssessmentRelationship_externalRef" ("externalRef_id");

CREATE TABLE "EpssVulnAssessmentRelationship_to" (
	"EpssVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("EpssVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("EpssVulnAssessmentRelationship_id") REFERENCES "EpssVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_to_EpssVulnAssessmentRelationship_id" ON "EpssVulnAssessmentRelationship_to" ("EpssVulnAssessmentRelationship_id");
CREATE INDEX "ix_EpssVulnAssessmentRelationship_to_to_id" ON "EpssVulnAssessmentRelationship_to" (to_id);

CREATE TABLE "EpssVulnAssessmentRelationship_externalIdentifier" (
	"EpssVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("EpssVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_id") REFERENCES "EpssVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "EpssVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_EpssVulnAssessmentRelationship_externalIdentifier_EpssVulnAssessmentRelationship_id" ON "EpssVulnAssessmentRelationship_externalIdentifier" ("EpssVulnAssessmentRelationship_id");

CREATE TABLE "EpssVulnAssessmentRelationship_extension" (
	"EpssVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("EpssVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("EpssVulnAssessmentRelationship_id") REFERENCES "EpssVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_extension_EpssVulnAssessmentRelationship_id" ON "EpssVulnAssessmentRelationship_extension" ("EpssVulnAssessmentRelationship_id");
CREATE INDEX "ix_EpssVulnAssessmentRelationship_extension_extension_id" ON "EpssVulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "EpssVulnAssessmentRelationship_verifiedUsing" (
	"EpssVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("EpssVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_id") REFERENCES "EpssVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "EpssVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_EpssVulnAssessmentRelationship_verifiedUsing_EpssVulnAssessmentRelationship_id" ON "EpssVulnAssessmentRelationship_verifiedUsing" ("EpssVulnAssessmentRelationship_id");

CREATE TABLE "EpssVulnAssessmentRelationship_externalRef" (
	"EpssVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("EpssVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_id") REFERENCES "EpssVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_externalRef_EpssVulnAssessmentRelationship_id" ON "EpssVulnAssessmentRelationship_externalRef" ("EpssVulnAssessmentRelationship_id");
CREATE INDEX "ix_EpssVulnAssessmentRelationship_externalRef_externalRef_id" ON "EpssVulnAssessmentRelationship_externalRef" ("externalRef_id");

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship_to" (
	"ExploitCatalogVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("ExploitCatalogVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_id") REFERENCES "ExploitCatalogVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_to_to_id" ON "ExploitCatalogVulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_to_ExploitCatalogVulnAssessmentRelationship_id" ON "ExploitCatalogVulnAssessmentRelationship_to" ("ExploitCatalogVulnAssessmentRelationship_id");

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship_externalIdentifier" (
	"ExploitCatalogVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("ExploitCatalogVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_id") REFERENCES "ExploitCatalogVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_externalIdentifier_ExploitCatalogVulnAssessmentRelationship_id" ON "ExploitCatalogVulnAssessmentRelationship_externalIdentifier" ("ExploitCatalogVulnAssessmentRelationship_id");
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "ExploitCatalogVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship_extension" (
	"ExploitCatalogVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("ExploitCatalogVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_id") REFERENCES "ExploitCatalogVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_extension_ExploitCatalogVulnAssessmentRelationship_id" ON "ExploitCatalogVulnAssessmentRelationship_extension" ("ExploitCatalogVulnAssessmentRelationship_id");
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_extension_extension_id" ON "ExploitCatalogVulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship_verifiedUsing" (
	"ExploitCatalogVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("ExploitCatalogVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_id") REFERENCES "ExploitCatalogVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "ExploitCatalogVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_verifiedUsing_ExploitCatalogVulnAssessmentRelationship_id" ON "ExploitCatalogVulnAssessmentRelationship_verifiedUsing" ("ExploitCatalogVulnAssessmentRelationship_id");

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship_externalRef" (
	"ExploitCatalogVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("ExploitCatalogVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_id") REFERENCES "ExploitCatalogVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_externalRef_externalRef_id" ON "ExploitCatalogVulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_externalRef_ExploitCatalogVulnAssessmentRelationship_id" ON "ExploitCatalogVulnAssessmentRelationship_externalRef" ("ExploitCatalogVulnAssessmentRelationship_id");

CREATE TABLE "SsvcVulnAssessmentRelationship_to" (
	"SsvcVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("SsvcVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_id") REFERENCES "SsvcVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_to_SsvcVulnAssessmentRelationship_id" ON "SsvcVulnAssessmentRelationship_to" ("SsvcVulnAssessmentRelationship_id");
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_to_to_id" ON "SsvcVulnAssessmentRelationship_to" (to_id);

CREATE TABLE "SsvcVulnAssessmentRelationship_externalIdentifier" (
	"SsvcVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("SsvcVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_id") REFERENCES "SsvcVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "SsvcVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_externalIdentifier_SsvcVulnAssessmentRelationship_id" ON "SsvcVulnAssessmentRelationship_externalIdentifier" ("SsvcVulnAssessmentRelationship_id");

CREATE TABLE "SsvcVulnAssessmentRelationship_extension" (
	"SsvcVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("SsvcVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_id") REFERENCES "SsvcVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_extension_extension_id" ON "SsvcVulnAssessmentRelationship_extension" (extension_id);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_extension_SsvcVulnAssessmentRelationship_id" ON "SsvcVulnAssessmentRelationship_extension" ("SsvcVulnAssessmentRelationship_id");

CREATE TABLE "SsvcVulnAssessmentRelationship_verifiedUsing" (
	"SsvcVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("SsvcVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_id") REFERENCES "SsvcVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_verifiedUsing_SsvcVulnAssessmentRelationship_id" ON "SsvcVulnAssessmentRelationship_verifiedUsing" ("SsvcVulnAssessmentRelationship_id");
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "SsvcVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "SsvcVulnAssessmentRelationship_externalRef" (
	"SsvcVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("SsvcVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_id") REFERENCES "SsvcVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_externalRef_externalRef_id" ON "SsvcVulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_externalRef_SsvcVulnAssessmentRelationship_id" ON "SsvcVulnAssessmentRelationship_externalRef" ("SsvcVulnAssessmentRelationship_id");

CREATE TABLE "VexAffectedVulnAssessmentRelationship_to" (
	"VexAffectedVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("VexAffectedVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_id") REFERENCES "VexAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_to_VexAffectedVulnAssessmentRelationship_id" ON "VexAffectedVulnAssessmentRelationship_to" ("VexAffectedVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_to_to_id" ON "VexAffectedVulnAssessmentRelationship_to" (to_id);

CREATE TABLE "VexAffectedVulnAssessmentRelationship_externalIdentifier" (
	"VexAffectedVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("VexAffectedVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_id") REFERENCES "VexAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "VexAffectedVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_externalIdentifier_VexAffectedVulnAssessmentRelationship_id" ON "VexAffectedVulnAssessmentRelationship_externalIdentifier" ("VexAffectedVulnAssessmentRelationship_id");

CREATE TABLE "VexAffectedVulnAssessmentRelationship_extension" (
	"VexAffectedVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("VexAffectedVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_id") REFERENCES "VexAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_extension_VexAffectedVulnAssessmentRelationship_id" ON "VexAffectedVulnAssessmentRelationship_extension" ("VexAffectedVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_extension_extension_id" ON "VexAffectedVulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "VexAffectedVulnAssessmentRelationship_verifiedUsing" (
	"VexAffectedVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("VexAffectedVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_id") REFERENCES "VexAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_verifiedUsing_VexAffectedVulnAssessmentRelationship_id" ON "VexAffectedVulnAssessmentRelationship_verifiedUsing" ("VexAffectedVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "VexAffectedVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "VexAffectedVulnAssessmentRelationship_externalRef" (
	"VexAffectedVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("VexAffectedVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_id") REFERENCES "VexAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_externalRef_externalRef_id" ON "VexAffectedVulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_externalRef_VexAffectedVulnAssessmentRelationship_id" ON "VexAffectedVulnAssessmentRelationship_externalRef" ("VexAffectedVulnAssessmentRelationship_id");

CREATE TABLE "VexFixedVulnAssessmentRelationship_to" (
	"VexFixedVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("VexFixedVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_id") REFERENCES "VexFixedVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_to_to_id" ON "VexFixedVulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_to_VexFixedVulnAssessmentRelationship_id" ON "VexFixedVulnAssessmentRelationship_to" ("VexFixedVulnAssessmentRelationship_id");

CREATE TABLE "VexFixedVulnAssessmentRelationship_externalIdentifier" (
	"VexFixedVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("VexFixedVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_id") REFERENCES "VexFixedVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "VexFixedVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_externalIdentifier_VexFixedVulnAssessmentRelationship_id" ON "VexFixedVulnAssessmentRelationship_externalIdentifier" ("VexFixedVulnAssessmentRelationship_id");

CREATE TABLE "VexFixedVulnAssessmentRelationship_extension" (
	"VexFixedVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("VexFixedVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_id") REFERENCES "VexFixedVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_extension_VexFixedVulnAssessmentRelationship_id" ON "VexFixedVulnAssessmentRelationship_extension" ("VexFixedVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_extension_extension_id" ON "VexFixedVulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "VexFixedVulnAssessmentRelationship_verifiedUsing" (
	"VexFixedVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("VexFixedVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_id") REFERENCES "VexFixedVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_verifiedUsing_VexFixedVulnAssessmentRelationship_id" ON "VexFixedVulnAssessmentRelationship_verifiedUsing" ("VexFixedVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "VexFixedVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");

CREATE TABLE "VexFixedVulnAssessmentRelationship_externalRef" (
	"VexFixedVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("VexFixedVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_id") REFERENCES "VexFixedVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_externalRef_externalRef_id" ON "VexFixedVulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_externalRef_VexFixedVulnAssessmentRelationship_id" ON "VexFixedVulnAssessmentRelationship_externalRef" ("VexFixedVulnAssessmentRelationship_id");

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship_to" (
	"VexNotAffectedVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("VexNotAffectedVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_id") REFERENCES "VexNotAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_to_to_id" ON "VexNotAffectedVulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_to_VexNotAffectedVulnAssessmentRelationship_id" ON "VexNotAffectedVulnAssessmentRelationship_to" ("VexNotAffectedVulnAssessmentRelationship_id");

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship_externalIdentifier" (
	"VexNotAffectedVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("VexNotAffectedVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_id") REFERENCES "VexNotAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "VexNotAffectedVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_externalIdentifier_VexNotAffectedVulnAssessmentRelationship_id" ON "VexNotAffectedVulnAssessmentRelationship_externalIdentifier" ("VexNotAffectedVulnAssessmentRelationship_id");

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship_extension" (
	"VexNotAffectedVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("VexNotAffectedVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_id") REFERENCES "VexNotAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_extension_VexNotAffectedVulnAssessmentRelationship_id" ON "VexNotAffectedVulnAssessmentRelationship_extension" ("VexNotAffectedVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_extension_extension_id" ON "VexNotAffectedVulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship_verifiedUsing" (
	"VexNotAffectedVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("VexNotAffectedVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_id") REFERENCES "VexNotAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "VexNotAffectedVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_verifiedUsing_VexNotAffectedVulnAssessmentRelationship_id" ON "VexNotAffectedVulnAssessmentRelationship_verifiedUsing" ("VexNotAffectedVulnAssessmentRelationship_id");

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship_externalRef" (
	"VexNotAffectedVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("VexNotAffectedVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_id") REFERENCES "VexNotAffectedVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_externalRef_externalRef_id" ON "VexNotAffectedVulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_externalRef_VexNotAffectedVulnAssessmentRelationship_id" ON "VexNotAffectedVulnAssessmentRelationship_externalRef" ("VexNotAffectedVulnAssessmentRelationship_id");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship_to" (
	"VexUnderInvestigationVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("VexUnderInvestigationVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_id") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_to_to_id" ON "VexUnderInvestigationVulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_to_VexUnderInvestigationVulnAssessmentRelationship_id" ON "VexUnderInvestigationVulnAssessmentRelationship_to" ("VexUnderInvestigationVulnAssessmentRelationship_id");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship_externalIdentifier" (
	"VexUnderInvestigationVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("VexUnderInvestigationVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_id") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "VexUnderInvestigationVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_externalIdentifier_VexUnderInvestigationVulnAssessmentRelationship_id" ON "VexUnderInvestigationVulnAssessmentRelationship_externalIdentifier" ("VexUnderInvestigationVulnAssessmentRelationship_id");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship_extension" (
	"VexUnderInvestigationVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("VexUnderInvestigationVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_id") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_extension_extension_id" ON "VexUnderInvestigationVulnAssessmentRelationship_extension" (extension_id);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_extension_VexUnderInvestigationVulnAssessmentRelationship_id" ON "VexUnderInvestigationVulnAssessmentRelationship_extension" ("VexUnderInvestigationVulnAssessmentRelationship_id");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship_verifiedUsing" (
	"VexUnderInvestigationVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("VexUnderInvestigationVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_id") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "VexUnderInvestigationVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_verifiedUsing_VexUnderInvestigationVulnAssessmentRelationship_id" ON "VexUnderInvestigationVulnAssessmentRelationship_verifiedUsing" ("VexUnderInvestigationVulnAssessmentRelationship_id");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship_externalRef" (
	"VexUnderInvestigationVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("VexUnderInvestigationVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_id") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_externalRef_externalRef_id" ON "VexUnderInvestigationVulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_externalRef_VexUnderInvestigationVulnAssessmentRelationship_id" ON "VexUnderInvestigationVulnAssessmentRelationship_externalRef" ("VexUnderInvestigationVulnAssessmentRelationship_id");

CREATE TABLE "VexVulnAssessmentRelationship_to" (
	"VexVulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("VexVulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("VexVulnAssessmentRelationship_id") REFERENCES "VexVulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_to_VexVulnAssessmentRelationship_id" ON "VexVulnAssessmentRelationship_to" ("VexVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexVulnAssessmentRelationship_to_to_id" ON "VexVulnAssessmentRelationship_to" (to_id);

CREATE TABLE "VexVulnAssessmentRelationship_externalIdentifier" (
	"VexVulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("VexVulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("VexVulnAssessmentRelationship_id") REFERENCES "VexVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "VexVulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_VexVulnAssessmentRelationship_externalIdentifier_VexVulnAssessmentRelationship_id" ON "VexVulnAssessmentRelationship_externalIdentifier" ("VexVulnAssessmentRelationship_id");

CREATE TABLE "VexVulnAssessmentRelationship_extension" (
	"VexVulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("VexVulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("VexVulnAssessmentRelationship_id") REFERENCES "VexVulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_extension_VexVulnAssessmentRelationship_id" ON "VexVulnAssessmentRelationship_extension" ("VexVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexVulnAssessmentRelationship_extension_extension_id" ON "VexVulnAssessmentRelationship_extension" (extension_id);

CREATE TABLE "VexVulnAssessmentRelationship_verifiedUsing" (
	"VexVulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("VexVulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("VexVulnAssessmentRelationship_id") REFERENCES "VexVulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "VexVulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_VexVulnAssessmentRelationship_verifiedUsing_VexVulnAssessmentRelationship_id" ON "VexVulnAssessmentRelationship_verifiedUsing" ("VexVulnAssessmentRelationship_id");

CREATE TABLE "VexVulnAssessmentRelationship_externalRef" (
	"VexVulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("VexVulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("VexVulnAssessmentRelationship_id") REFERENCES "VexVulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_externalRef_VexVulnAssessmentRelationship_id" ON "VexVulnAssessmentRelationship_externalRef" ("VexVulnAssessmentRelationship_id");
CREATE INDEX "ix_VexVulnAssessmentRelationship_externalRef_externalRef_id" ON "VexVulnAssessmentRelationship_externalRef" ("externalRef_id");

CREATE TABLE "VulnAssessmentRelationship_to" (
	"VulnAssessmentRelationship_id" INTEGER,
	to_id INTEGER NOT NULL,
	PRIMARY KEY ("VulnAssessmentRelationship_id", to_id),
	FOREIGN KEY("VulnAssessmentRelationship_id") REFERENCES "VulnAssessmentRelationship" (id),
	FOREIGN KEY(to_id) REFERENCES "Element" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_to_to_id" ON "VulnAssessmentRelationship_to" (to_id);
CREATE INDEX "ix_VulnAssessmentRelationship_to_VulnAssessmentRelationship_id" ON "VulnAssessmentRelationship_to" ("VulnAssessmentRelationship_id");

CREATE TABLE "VulnAssessmentRelationship_externalIdentifier" (
	"VulnAssessmentRelationship_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("VulnAssessmentRelationship_id", "externalIdentifier_id"),
	FOREIGN KEY("VulnAssessmentRelationship_id") REFERENCES "VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_externalIdentifier_externalIdentifier_id" ON "VulnAssessmentRelationship_externalIdentifier" ("externalIdentifier_id");
CREATE INDEX "ix_VulnAssessmentRelationship_externalIdentifier_VulnAssessmentRelationship_id" ON "VulnAssessmentRelationship_externalIdentifier" ("VulnAssessmentRelationship_id");

CREATE TABLE "VulnAssessmentRelationship_extension" (
	"VulnAssessmentRelationship_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("VulnAssessmentRelationship_id", extension_id),
	FOREIGN KEY("VulnAssessmentRelationship_id") REFERENCES "VulnAssessmentRelationship" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_extension_extension_id" ON "VulnAssessmentRelationship_extension" (extension_id);
CREATE INDEX "ix_VulnAssessmentRelationship_extension_VulnAssessmentRelationship_id" ON "VulnAssessmentRelationship_extension" ("VulnAssessmentRelationship_id");

CREATE TABLE "VulnAssessmentRelationship_verifiedUsing" (
	"VulnAssessmentRelationship_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("VulnAssessmentRelationship_id", "verifiedUsing_id"),
	FOREIGN KEY("VulnAssessmentRelationship_id") REFERENCES "VulnAssessmentRelationship" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_verifiedUsing_verifiedUsing_id" ON "VulnAssessmentRelationship_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_VulnAssessmentRelationship_verifiedUsing_VulnAssessmentRelationship_id" ON "VulnAssessmentRelationship_verifiedUsing" ("VulnAssessmentRelationship_id");

CREATE TABLE "VulnAssessmentRelationship_externalRef" (
	"VulnAssessmentRelationship_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("VulnAssessmentRelationship_id", "externalRef_id"),
	FOREIGN KEY("VulnAssessmentRelationship_id") REFERENCES "VulnAssessmentRelationship" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_externalRef_externalRef_id" ON "VulnAssessmentRelationship_externalRef" ("externalRef_id");
CREATE INDEX "ix_VulnAssessmentRelationship_externalRef_VulnAssessmentRelationship_id" ON "VulnAssessmentRelationship_externalRef" ("VulnAssessmentRelationship_id");

CREATE TABLE "Snippet_attributionText" (
	"Snippet_id" INTEGER,
	"attributionText" TEXT,
	PRIMARY KEY ("Snippet_id", "attributionText"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id)
);
CREATE INDEX "ix_Snippet_attributionText_attributionText" ON "Snippet_attributionText" ("attributionText");
CREATE INDEX "ix_Snippet_attributionText_Snippet_id" ON "Snippet_attributionText" ("Snippet_id");

CREATE TABLE "Snippet_additionalPurpose" (
	"Snippet_id" INTEGER,
	"additionalPurpose" TEXT,
	PRIMARY KEY ("Snippet_id", "additionalPurpose"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id)
);
CREATE INDEX "ix_Snippet_additionalPurpose_Snippet_id" ON "Snippet_additionalPurpose" ("Snippet_id");
CREATE INDEX "ix_Snippet_additionalPurpose_additionalPurpose" ON "Snippet_additionalPurpose" ("additionalPurpose");

CREATE TABLE "Snippet_contentIdentifier" (
	"Snippet_id" INTEGER,
	"contentIdentifier_id" INTEGER,
	PRIMARY KEY ("Snippet_id", "contentIdentifier_id"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id),
	FOREIGN KEY("contentIdentifier_id") REFERENCES "ContentIdentifier" (id)
);
CREATE INDEX "ix_Snippet_contentIdentifier_Snippet_id" ON "Snippet_contentIdentifier" ("Snippet_id");
CREATE INDEX "ix_Snippet_contentIdentifier_contentIdentifier_id" ON "Snippet_contentIdentifier" ("contentIdentifier_id");

CREATE TABLE "Snippet_standardName" (
	"Snippet_id" INTEGER,
	"standardName" TEXT,
	PRIMARY KEY ("Snippet_id", "standardName"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id)
);
CREATE INDEX "ix_Snippet_standardName_Snippet_id" ON "Snippet_standardName" ("Snippet_id");
CREATE INDEX "ix_Snippet_standardName_standardName" ON "Snippet_standardName" ("standardName");

CREATE TABLE "Snippet_supportLevel" (
	"Snippet_id" INTEGER,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Snippet_id", "supportLevel"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id)
);
CREATE INDEX "ix_Snippet_supportLevel_Snippet_id" ON "Snippet_supportLevel" ("Snippet_id");
CREATE INDEX "ix_Snippet_supportLevel_supportLevel" ON "Snippet_supportLevel" ("supportLevel");

CREATE TABLE "Snippet_originatedBy" (
	"Snippet_id" INTEGER,
	"originatedBy_id" INTEGER,
	PRIMARY KEY ("Snippet_id", "originatedBy_id"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id),
	FOREIGN KEY("originatedBy_id") REFERENCES "Agent" (id)
);
CREATE INDEX "ix_Snippet_originatedBy_Snippet_id" ON "Snippet_originatedBy" ("Snippet_id");
CREATE INDEX "ix_Snippet_originatedBy_originatedBy_id" ON "Snippet_originatedBy" ("originatedBy_id");

CREATE TABLE "Snippet_externalIdentifier" (
	"Snippet_id" INTEGER,
	"externalIdentifier_id" INTEGER,
	PRIMARY KEY ("Snippet_id", "externalIdentifier_id"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id),
	FOREIGN KEY("externalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_Snippet_externalIdentifier_Snippet_id" ON "Snippet_externalIdentifier" ("Snippet_id");
CREATE INDEX "ix_Snippet_externalIdentifier_externalIdentifier_id" ON "Snippet_externalIdentifier" ("externalIdentifier_id");

CREATE TABLE "Snippet_extension" (
	"Snippet_id" INTEGER,
	extension_id INTEGER,
	PRIMARY KEY ("Snippet_id", extension_id),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id),
	FOREIGN KEY(extension_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Snippet_extension_Snippet_id" ON "Snippet_extension" ("Snippet_id");
CREATE INDEX "ix_Snippet_extension_extension_id" ON "Snippet_extension" (extension_id);

CREATE TABLE "Snippet_verifiedUsing" (
	"Snippet_id" INTEGER,
	"verifiedUsing_id" INTEGER,
	PRIMARY KEY ("Snippet_id", "verifiedUsing_id"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id),
	FOREIGN KEY("verifiedUsing_id") REFERENCES "IntegrityMethod" (id)
);
CREATE INDEX "ix_Snippet_verifiedUsing_verifiedUsing_id" ON "Snippet_verifiedUsing" ("verifiedUsing_id");
CREATE INDEX "ix_Snippet_verifiedUsing_Snippet_id" ON "Snippet_verifiedUsing" ("Snippet_id");

CREATE TABLE "Snippet_externalRef" (
	"Snippet_id" INTEGER,
	"externalRef_id" INTEGER,
	PRIMARY KEY ("Snippet_id", "externalRef_id"),
	FOREIGN KEY("Snippet_id") REFERENCES "Snippet" (id),
	FOREIGN KEY("externalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_Snippet_externalRef_Snippet_id" ON "Snippet_externalRef" ("Snippet_id");
CREATE INDEX "ix_Snippet_externalRef_externalRef_id" ON "Snippet_externalRef" ("externalRef_id");
