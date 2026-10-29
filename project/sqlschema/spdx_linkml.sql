-- # Class: Agent Description: Agent represents anything with the potential to act on a system.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Annotation Description: An assertion made in relation to one or more elements.
--     * Slot: contentType Description: Provides information about the content type of an Element or a Property.
--     * Slot: annotationType Description: Describes the type of annotation.
--     * Slot: statement Description: Commentary on an assertion that an annotator has made.
--     * Slot: subject Description: An Element an annotator has made an assertion about.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: AnyLicenseInfo Description: Abstract class representing a license combination consisting of one or more licenses.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: Artifact Description: A distinct article or unit within the digital domain.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Bom Description: A container for a grouping of SPDX-3.0 content characterizing details (provenence, composition, licensing, etc.) about a product.
--     * Slot: context Description: Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Bundle Description: A collection of Elements that have a shared context.
--     * Slot: context Description: Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CreationInfo Description: Provides information about the creation of the Element.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: created Description: Identifies when the Element was originally created.
--     * Slot: specVersion Description: Provides a reference number that can be used to understand how to parse and interpret an Element.
-- # Class: DictionaryEntry Description: A key with an associated value.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: key Description: A key used in a generic key-value pair.
--     * Slot: value Description: A value used in a generic key-value pair.
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: LicenseExpression_spdxId Description: Autocreated FK slot
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
-- # Abstract Class: Element Description: Base domain class from which all other SPDX-3.0 domain classes derive.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: ElementCollection Description: A collection of Elements, not necessarily with unifying context.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: Extension Description: A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: Agent_spdxId Description: Autocreated FK slot
--     * Slot: Annotation_spdxId Description: Autocreated FK slot
--     * Slot: AnyLicenseInfo_spdxId Description: Autocreated FK slot
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: Element_spdxId Description: Autocreated FK slot
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: IndividualElement_spdxId Description: Autocreated FK slot
--     * Slot: LifecycleScopedRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Organization_spdxId Description: Autocreated FK slot
--     * Slot: Person_spdxId Description: Autocreated FK slot
--     * Slot: Relationship_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareAgent_spdxId Description: Autocreated FK slot
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: Tool_spdxId Description: Autocreated FK slot
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: LicenseExpression_spdxId Description: Autocreated FK slot
--     * Slot: SimpleLicensingText_spdxId Description: Autocreated FK slot
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: ConjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicense_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: DisjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: ExtendableLicense_spdxId Description: Autocreated FK slot
--     * Slot: IndividualLicensingInfo_spdxId Description: Autocreated FK slot
--     * Slot: License_spdxId Description: Autocreated FK slot
--     * Slot: LicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicense_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicenseException_spdxId Description: Autocreated FK slot
--     * Slot: OrLaterOperator_spdxId Description: Autocreated FK slot
--     * Slot: WithAdditionOperator_spdxId Description: Autocreated FK slot
--     * Slot: CvssV2VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV3VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV4VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: EpssVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: ExploitCatalogVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: SsvcVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexFixedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexNotAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
-- # Class: ExternalIdentifier Description: A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: externalIdentifierType Description: Specifies the type of the external identifier.
--     * Slot: identifier Description: Uniquely identifies an external element.
--     * Slot: issuingAuthority Description: An entity that is authorized to issue identification credentials.
--     * Slot: Agent_spdxId Description: Autocreated FK slot
--     * Slot: Annotation_spdxId Description: Autocreated FK slot
--     * Slot: AnyLicenseInfo_spdxId Description: Autocreated FK slot
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: Element_spdxId Description: Autocreated FK slot
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: IndividualElement_spdxId Description: Autocreated FK slot
--     * Slot: LifecycleScopedRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Organization_spdxId Description: Autocreated FK slot
--     * Slot: Person_spdxId Description: Autocreated FK slot
--     * Slot: Relationship_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareAgent_spdxId Description: Autocreated FK slot
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: Tool_spdxId Description: Autocreated FK slot
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: LicenseExpression_spdxId Description: Autocreated FK slot
--     * Slot: SimpleLicensingText_spdxId Description: Autocreated FK slot
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: ConjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicense_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: DisjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: ExtendableLicense_spdxId Description: Autocreated FK slot
--     * Slot: IndividualLicensingInfo_spdxId Description: Autocreated FK slot
--     * Slot: License_spdxId Description: Autocreated FK slot
--     * Slot: LicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicense_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicenseException_spdxId Description: Autocreated FK slot
--     * Slot: OrLaterOperator_spdxId Description: Autocreated FK slot
--     * Slot: WithAdditionOperator_spdxId Description: Autocreated FK slot
--     * Slot: CvssV2VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV3VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV4VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: EpssVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: ExploitCatalogVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: SsvcVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexFixedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexNotAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
-- # Class: ExternalMap Description: A map of Element identifiers that are used within an SpdxDocument but defined external to that SpdxDocument.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: definingArtifact Description: Artifact representing a serialization instance of SPDX data containing the definition of a particular Element.
--     * Slot: externalSpdxId Description: Identifies an external Element used within an SpdxDocument but defined external to that SpdxDocument.
--     * Slot: locationHint Description: Provides an indication of where to retrieve an external Element.
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
-- # Class: ExternalRef Description: A reference to a resource outside the scope of SPDX-3.0 content related to an Element.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: contentType Description: Provides information about the content type of an Element or a Property.
--     * Slot: externalRefType Description: Specifies the type of the external reference.
--     * Slot: Agent_spdxId Description: Autocreated FK slot
--     * Slot: Annotation_spdxId Description: Autocreated FK slot
--     * Slot: AnyLicenseInfo_spdxId Description: Autocreated FK slot
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: Element_spdxId Description: Autocreated FK slot
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: IndividualElement_spdxId Description: Autocreated FK slot
--     * Slot: LifecycleScopedRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Organization_spdxId Description: Autocreated FK slot
--     * Slot: Person_spdxId Description: Autocreated FK slot
--     * Slot: Relationship_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareAgent_spdxId Description: Autocreated FK slot
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: Tool_spdxId Description: Autocreated FK slot
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: LicenseExpression_spdxId Description: Autocreated FK slot
--     * Slot: SimpleLicensingText_spdxId Description: Autocreated FK slot
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: ConjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicense_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: DisjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: ExtendableLicense_spdxId Description: Autocreated FK slot
--     * Slot: IndividualLicensingInfo_spdxId Description: Autocreated FK slot
--     * Slot: License_spdxId Description: Autocreated FK slot
--     * Slot: LicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicense_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicenseException_spdxId Description: Autocreated FK slot
--     * Slot: OrLaterOperator_spdxId Description: Autocreated FK slot
--     * Slot: WithAdditionOperator_spdxId Description: Autocreated FK slot
--     * Slot: CvssV2VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV3VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV4VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: EpssVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: ExploitCatalogVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: SsvcVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexFixedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexNotAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
-- # Class: Hash Description: A mathematically calculated representation of a grouping of data.
--     * Slot: id
--     * Slot: algorithm Description: Specifies the algorithm used for calculating the hash value.
--     * Slot: hashValue Description: The result of applying a hash algorithm to an Element.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: Build_spdxId Description: Autocreated FK slot
-- # Class: IndividualElement Description: A concrete subclass of Element used by Individuals in the Core profile.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: IntegrityMethod Description: Provides an independently reproducible mechanism that permits verification of a specific Element.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: Agent_spdxId Description: Autocreated FK slot
--     * Slot: Annotation_spdxId Description: Autocreated FK slot
--     * Slot: AnyLicenseInfo_spdxId Description: Autocreated FK slot
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: Element_spdxId Description: Autocreated FK slot
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: ExternalMap_id Description: Autocreated FK slot
--     * Slot: IndividualElement_spdxId Description: Autocreated FK slot
--     * Slot: LifecycleScopedRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Organization_spdxId Description: Autocreated FK slot
--     * Slot: Person_spdxId Description: Autocreated FK slot
--     * Slot: Relationship_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareAgent_spdxId Description: Autocreated FK slot
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: Tool_spdxId Description: Autocreated FK slot
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: LicenseExpression_spdxId Description: Autocreated FK slot
--     * Slot: SimpleLicensingText_spdxId Description: Autocreated FK slot
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: ConjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicense_spdxId Description: Autocreated FK slot
--     * Slot: CustomLicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: DisjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: ExtendableLicense_spdxId Description: Autocreated FK slot
--     * Slot: IndividualLicensingInfo_spdxId Description: Autocreated FK slot
--     * Slot: License_spdxId Description: Autocreated FK slot
--     * Slot: LicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicense_spdxId Description: Autocreated FK slot
--     * Slot: ListedLicenseException_spdxId Description: Autocreated FK slot
--     * Slot: OrLaterOperator_spdxId Description: Autocreated FK slot
--     * Slot: WithAdditionOperator_spdxId Description: Autocreated FK slot
--     * Slot: CvssV2VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV3VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: CvssV4VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: EpssVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: ExploitCatalogVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: SsvcVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexFixedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexNotAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VexVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
-- # Class: LifecycleScopedRelationship Description: Provide context for a relationship that occurs in the lifecycle.
--     * Slot: scope Description: Capture the scope of information about a specific relationship between elements.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: NamespaceMap Description: A mapping between prefixes and namespace partial URIs.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: namespace Description: Provides an unambiguous mechanism for conveying a URI fragment portion of an Element ID.
--     * Slot: prefix Description: A substitute for a URI.
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
-- # Class: Organization Description: A group of people who work together in an organized way for a shared purpose.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: PackageVerificationCode Description: An SPDX version 2.X compatible verification method for software packages.
--     * Slot: id
--     * Slot: algorithm Description: Specifies the algorithm used for calculating the hash value.
--     * Slot: hashValue Description: The result of applying a hash algorithm to an Element.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
-- # Class: Person Description: An individual human being.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: PositiveIntegerRange Description: A tuple of two positive integers that define a range.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: beginIntegerRange Description: Defines the beginning of a range.
--     * Slot: endIntegerRange Description: Defines the end of a range.
-- # Class: Relationship Description: Describes a relationship between one or more elements.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SoftwareAgent Description: A software agent.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SpdxDocument Description: A collection of SPDX Elements that could potentially be serialized.
--     * Slot: dataLicense Description: Provides the license under which the SPDX documentation of the Element can be used.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Tool Description: An element of hardware and/or software utilized to carry out a particular function.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Build Description: Class that describes a build instance of software/artifacts.
--     * Slot: buildEndTime Description: Property that describes the time at which a build stops.
--     * Slot: buildId Description: A buildId is a locally unique identifier used by a builder to identify a unique instance of a build produced by it.
--     * Slot: buildStartTime Description: Property describing the start time of a build.
--     * Slot: buildType Description: A buildType is a hint that is used to indicate the toolchain, platform, or infrastructure that the build was invoked on.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CdxPropertiesExtension Description: A type of extension consisting of a list of name value pairs.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
-- # Class: CdxPropertyEntry Description: A property name with an associated value.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: cdxPropName Description: A name used in a CdxPropertyEntry name-value pair.
--     * Slot: cdxPropValue Description: A value used in a CdxPropertyEntry name-value pair.
--     * Slot: CdxPropertiesExtension_id Description: Autocreated FK slot
-- # Class: LicenseExpression Description: An SPDX Element containing an SPDX license expression string.
--     * Slot: licenseExpression Description: A string in the license expression format.
--     * Slot: licenseListVersion Description: The version of the SPDX License List used in the license expression.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SimpleLicensingText Description: A license or addition that is not listed on the SPDX License List.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ContentIdentifier Description: A canonical, unique, immutable identifier
--     * Slot: id
--     * Slot: contentIdentifierType Description: Specifies the type of the content identifier.
--     * Slot: contentIdentifierValue Description: Specifies the value of the content identifier.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
-- # Class: File Description: Refers to any object that stores content on a computer.
--     * Slot: contentType Description: Provides information about the content type of an Element or a Property.
--     * Slot: fileKind Description: Describes if a given file is a directory or non-directory kind of file.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Package Description: Refers to any unit of content that can be associated with a distribution of software.
--     * Slot: downloadLocation Description: Identifies the download Uniform Resource Identifier for the package at the time that the document was created.
--     * Slot: homePage Description: A place for the SPDX document creator to record a website that serves as the package's home page.
--     * Slot: packageUrl Description: Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.
--     * Slot: packageVersion Description: Identify the version of a package.
--     * Slot: sourceInfo Description: Records any relevant background information or additional comments about the origin of the package.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Sbom Description: A collection of SPDX Elements describing a single package.
--     * Slot: context Description: Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Snippet Description: Describes a certain part of a file.
--     * Slot: snippetFromFile Description: Defines the original host file that the snippet information applies to.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: byteRange_id Description: Defines the byte range in the original host file that the snippet information applies to.
--     * Slot: lineRange_id Description: Defines the line range in the original host file that the snippet information applies to.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: SoftwareArtifact Description: A distinct article or unit related to Software.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: AIPackage Description: Specifies an AI package and its associated information.
--     * Slot: autonomyType Description: Indicates whether the system can perform a decision or action without human involvement or guidance.
--     * Slot: informationAboutApplication Description: Provides relevant information about the AI software, not including the model description.
--     * Slot: informationAboutTraining Description: Describes relevant information about different steps of the training process.
--     * Slot: limitation Description: Captures a limitation of the AI software.
--     * Slot: safetyRiskAssessment Description: Records the results of general safety risk assessment of the AI system.
--     * Slot: useSensitivePersonalInformation Description: Records if sensitive personal information is used during model training or could be used during the inference.
--     * Slot: downloadLocation Description: Identifies the download Uniform Resource Identifier for the package at the time that the document was created.
--     * Slot: homePage Description: A place for the SPDX document creator to record a website that serves as the package's home page.
--     * Slot: packageUrl Description: Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.
--     * Slot: packageVersion Description: Identify the version of a package.
--     * Slot: sourceInfo Description: Records any relevant background information or additional comments about the origin of the package.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: energyConsumption_id Description: Indicates the amount of energy consumption incurred by an AI model.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: EnergyConsumption Description: A class for describing the energy consumption incurred by an AI model in different stages of its lifecycle.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
-- # Class: EnergyConsumptionDescription Description: The class that helps note down the quantity of energy consumption and the unit used for measurement.
--     * Slot: id
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: energyQuantity Description: Represents the energy quantity.
--     * Slot: energyUnit Description: Specifies the unit in which energy is measured.
--     * Slot: EnergyConsumption_id Description: Autocreated FK slot
-- # Class: DatasetPackage Description: Specifies a data package and its associated information.
--     * Slot: confidentialityLevel Description: Describes the confidentiality level of the data points contained in the dataset.
--     * Slot: dataCollectionProcess Description: Describes how the dataset was collected.
--     * Slot: datasetAvailability Description: The field describes the availability of a dataset.
--     * Slot: datasetNoise Description: Describes potentially noisy elements of the dataset.
--     * Slot: datasetSize Description: Captures the size of the dataset.
--     * Slot: datasetUpdateMechanism Description: Describes a mechanism to update the dataset.
--     * Slot: hasSensitivePersonalInformation Description: Describes if any sensitive personal information is present in the dataset.
--     * Slot: intendedUse Description: Describes what the given dataset should be used for.
--     * Slot: downloadLocation Description: Identifies the download Uniform Resource Identifier for the package at the time that the document was created.
--     * Slot: homePage Description: A place for the SPDX document creator to record a website that serves as the package's home page.
--     * Slot: packageUrl Description: Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.
--     * Slot: packageVersion Description: Identify the version of a package.
--     * Slot: sourceInfo Description: Records any relevant background information or additional comments about the origin of the package.
--     * Slot: copyrightText Description: Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.
--     * Slot: primaryPurpose Description: Provides information about the primary purpose of the software artifact.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ConjunctiveLicenseSet Description: Portion of an AnyLicenseInfo representing a set of licensing information where all elements apply.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CustomLicense Description: A license that is not listed on the SPDX License List.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the license XML format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.
--     * Slot: isDeprecatedLicenseId Description: Specifies whether a license or additional text identifier has been marked as deprecated.
--     * Slot: isFsfLibre Description: Specifies whether the License is listed as free by the Free Software Foundation (FSF).
--     * Slot: isOsiApproved Description: Specifies whether the License is listed as approved by the Open Source Initiative (OSI).
--     * Slot: standardLicenseHeader Description: Provides a License author's preferred text to indicate that a file is covered by the License.
--     * Slot: standardLicenseTemplate Description: Identifies the full text of a License, in SPDX templating format.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CustomLicenseAddition Description: A license addition that is not listed on the SPDX Exceptions List.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the license XML format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.
--     * Slot: additionText Description: Identifies the full text of a LicenseAddition.
--     * Slot: isDeprecatedAdditionId Description: Specifies whether an additional text identifier has been marked as deprecated.
--     * Slot: standardAdditionTemplate Description: Identifies the full text of a LicenseAddition, in SPDX templating format.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: DisjunctiveLicenseSet Description: Portion of an AnyLicenseInfo representing a set of licensing information where only one of the elements applies.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: ExtendableLicense Description: Abstract class representing a License or an OrLaterOperator.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: IndividualLicensingInfo Description: A concrete subclass of AnyLicenseInfo used by Individuals in the ExpandedLicensing profile.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: License Description: Abstract class for the portion of an AnyLicenseInfo representing a license.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the license XML format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.
--     * Slot: isDeprecatedLicenseId Description: Specifies whether a license or additional text identifier has been marked as deprecated.
--     * Slot: isFsfLibre Description: Specifies whether the License is listed as free by the Free Software Foundation (FSF).
--     * Slot: isOsiApproved Description: Specifies whether the License is listed as approved by the Open Source Initiative (OSI).
--     * Slot: standardLicenseHeader Description: Provides a License author's preferred text to indicate that a file is covered by the License.
--     * Slot: standardLicenseTemplate Description: Identifies the full text of a License, in SPDX templating format.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: LicenseAddition Description: Abstract class for additional text intended to be added to a License, but which is not itself a standalone License.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the license XML format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.
--     * Slot: additionText Description: Identifies the full text of a LicenseAddition.
--     * Slot: isDeprecatedAdditionId Description: Specifies whether an additional text identifier has been marked as deprecated.
--     * Slot: standardAdditionTemplate Description: Identifies the full text of a LicenseAddition, in SPDX templating format.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ListedLicense Description: A license that is listed on the SPDX License List.
--     * Slot: deprecatedVersion Description: Specifies the SPDX License List version in which this license or exception identifier was deprecated.
--     * Slot: listVersionAdded Description: Specifies the SPDX License List version in which this ListedLicense or ListedLicenseException identifier was first added.
--     * Slot: licenseText Description: Identifies the full text of a License or Addition.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the license XML format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.
--     * Slot: isDeprecatedLicenseId Description: Specifies whether a license or additional text identifier has been marked as deprecated.
--     * Slot: isFsfLibre Description: Specifies whether the License is listed as free by the Free Software Foundation (FSF).
--     * Slot: isOsiApproved Description: Specifies whether the License is listed as approved by the Open Source Initiative (OSI).
--     * Slot: standardLicenseHeader Description: Provides a License author's preferred text to indicate that a file is covered by the License.
--     * Slot: standardLicenseTemplate Description: Identifies the full text of a License, in SPDX templating format.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ListedLicenseException Description: A license exception that is listed on the SPDX Exceptions list.
--     * Slot: deprecatedVersion Description: Specifies the SPDX License List version in which this license or exception identifier was deprecated.
--     * Slot: listVersionAdded Description: Specifies the SPDX License List version in which this ListedLicense or ListedLicenseException identifier was first added.
--     * Slot: licenseXml Description: Identifies all the text and metadata associated with a license in the license XML format.
--     * Slot: obsoletedBy Description: Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.
--     * Slot: additionText Description: Identifies the full text of a LicenseAddition.
--     * Slot: isDeprecatedAdditionId Description: Specifies whether an additional text identifier has been marked as deprecated.
--     * Slot: standardAdditionTemplate Description: Identifies the full text of a LicenseAddition, in SPDX templating format.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: OrLaterOperator Description: Portion of an AnyLicenseInfo representing this version, or any later version, of the indicated License.
--     * Slot: subjectLicense Description: A License participating in an 'or later' model.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: WithAdditionOperator Description: Portion of an AnyLicenseInfo representing a License which has additional text applied to it.
--     * Slot: subjectAddition Description: A LicenseAddition participating in a 'with addition' model.
--     * Slot: subjectExtendableLicense Description: A License participating in a 'with addition' model.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CvssV2VulnAssessmentRelationship Description: Provides a CVSS version 2.0 assessment for a vulnerability.
--     * Slot: score Description: Provides a numerical (0-10) representation of the severity of a vulnerability.
--     * Slot: vectorString Description: Specifies the CVSS vector string for a vulnerability.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CvssV3VulnAssessmentRelationship Description: Provides a CVSS version 3 assessment for a vulnerability.
--     * Slot: score Description: Provides a numerical (0-10) representation of the severity of a vulnerability.
--     * Slot: severity Description: Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.
--     * Slot: vectorString Description: Specifies the CVSS vector string for a vulnerability.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: CvssV4VulnAssessmentRelationship Description: Provides a CVSS version 4 assessment for a vulnerability.
--     * Slot: score Description: Provides a numerical (0-10) representation of the severity of a vulnerability.
--     * Slot: severity Description: Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.
--     * Slot: vectorString Description: Specifies the CVSS vector string for a vulnerability.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: EpssVulnAssessmentRelationship Description: Provides an EPSS assessment for a vulnerability.
--     * Slot: percentile Description: The percentile of the current probability score.
--     * Slot: probability Description: A probability score between 0 and 1 of a vulnerability being exploited.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: ExploitCatalogVulnAssessmentRelationship Description: Provides an exploit assessment of a vulnerability.
--     * Slot: catalogType Description: Specifies the exploit catalog type.
--     * Slot: exploited Description: Describe that a CVE is known to have an exploit because it's been listed in an exploit catalog.
--     * Slot: security_locator Description: Provides the location of an exploit catalog.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: SsvcVulnAssessmentRelationship Description: Provides an SSVC assessment for a vulnerability.
--     * Slot: decisionType Description: Provide the enumeration of possible decisions in the [Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexAffectedVulnAssessmentRelationship Description: Connects a vulnerability and an element designating the element as a product affected by the vulnerability.
--     * Slot: actionStatement Description: Provides advise on how to mitigate or remediate a vulnerability when a VEX product is affected by it.
--     * Slot: actionStatementTime Description: Records the time when a recommended action was communicated in a VEX statement to mitigate a vulnerability.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexFixedVulnAssessmentRelationship Description: Links a vulnerability and elements representing products (in the VEX sense) where a fix has been applied and are no longer affected.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexNotAffectedVulnAssessmentRelationship Description: Links a vulnerability and one or more elements designating the latter as products not affected by the vulnerability.
--     * Slot: impactStatement Description: Explains why a VEX product is not affected by a vulnerability. It is an alternative in VexNotAffectedVulnAssessmentRelationship to the machine-readable justification label.
--     * Slot: impactStatementTime Description: Timestamp of impact statement.
--     * Slot: justificationType Description: Impact justification label to be used when linking a vulnerability to an element representing a VEX product with a VexNotAffectedVulnAssessmentRelationship relationship.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship Description: Designates elements as products where the impact of a vulnerability is being investigated.
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: VexVulnAssessmentRelationship Description: Abstract ancestor class for all VEX relationships
--     * Slot: statusNotes Description: Conveys information about how VEX status was determined.
--     * Slot: vexVersion Description: Specifies the version of a VEX statement.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Abstract Class: VulnAssessmentRelationship Description: Abstract ancestor class for all vulnerability assessments
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: assessedElement Description: Specifies an Element contained in a piece of software where a vulnerability was found.
--     * Slot: completeness Description: Provides information about the completeness of relationships.
--     * Slot: endTime Description: Specifies the time from which an element is no longer applicable / valid.
--     * Slot: from Description: References the Element on the left-hand side of a relationship.
--     * Slot: relationshipType Description: Information about the relationship between two Elements.
--     * Slot: startTime Description: Specifies the time from which an element is applicable / valid.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Vulnerability Description: Specifies a vulnerability and its associated information.
--     * Slot: modifiedTime Description: Specifies a time when a vulnerability assessment was modified
--     * Slot: publishedTime Description: Specifies the time when a vulnerability was published.
--     * Slot: withdrawnTime Description: Specified the time and date when a vulnerability was withdrawn.
--     * Slot: suppliedBy Description: Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.
--     * Slot: builtTime Description: Specifies the time an artifact was built.
--     * Slot: releaseTime Description: Specifies the time an artifact was released.
--     * Slot: validUntilTime Description: Specifies until when the artifact can be used before its usage needs to be reassessed.
--     * Slot: type Description: The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.
--     * Slot: comment Description: Provide consumers with comments by the creator of the Element about the Element.
--     * Slot: spdxId Description: The IRI that identifies this Element. A reference to an Element from any field is this IRI.
--     * Slot: description Description: Provides a detailed description of the Element.
--     * Slot: name Description: Identifies the name of an Element as designated by the creator.
--     * Slot: summary Description: A short description of an Element.
--     * Slot: creationInfo_id Description: Provides information about the creation of the Element.
-- # Class: Artifact_originatedBy
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: Artifact_standardName
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Artifact_supportLevel
--     * Slot: Artifact_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Bom_element
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: element_spdxId Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: Bom_profileConformance
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends to conform to.
-- # Class: Bom_rootElement
--     * Slot: Bom_spdxId Description: Autocreated FK slot
--     * Slot: rootElement_spdxId Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: Bundle_element
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: element_spdxId Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: Bundle_profileConformance
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends to conform to.
-- # Class: Bundle_rootElement
--     * Slot: Bundle_spdxId Description: Autocreated FK slot
--     * Slot: rootElement_spdxId Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: CreationInfo_createdBy
--     * Slot: CreationInfo_id Description: Autocreated FK slot
--     * Slot: createdBy_spdxId Description: Identifies who or what created the Element.
-- # Class: CreationInfo_createdUsing
--     * Slot: CreationInfo_id Description: Autocreated FK slot
--     * Slot: createdUsing_spdxId Description: Identifies the tooling that was used during the creation of the Element.
-- # Class: ElementCollection_element
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: element_spdxId Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: ElementCollection_profileConformance
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends to conform to.
-- # Class: ElementCollection_rootElement
--     * Slot: ElementCollection_spdxId Description: Autocreated FK slot
--     * Slot: rootElement_spdxId Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: ExternalIdentifier_identifierLocator
--     * Slot: ExternalIdentifier_id Description: Autocreated FK slot
--     * Slot: identifierLocator Description: Provides the location for more information regarding an external identifier.
-- # Class: ExternalRef_locator
--     * Slot: ExternalRef_id Description: Autocreated FK slot
--     * Slot: locator Description: Provides the location of an external reference.
-- # Class: LifecycleScopedRelationship_to
--     * Slot: LifecycleScopedRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: PackageVerificationCode_packageVerificationCodeExcludedFile
--     * Slot: PackageVerificationCode_id Description: Autocreated FK slot
--     * Slot: packageVerificationCodeExcludedFile Description: The relative file name of a file to be excluded from the `PackageVerificationCode`.
-- # Class: Relationship_to
--     * Slot: Relationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: SpdxDocument_element
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: element_spdxId Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: SpdxDocument_profileConformance
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends to conform to.
-- # Class: SpdxDocument_rootElement
--     * Slot: SpdxDocument_spdxId Description: Autocreated FK slot
--     * Slot: rootElement_spdxId Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: Build_configSourceEntrypoint
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: configSourceEntrypoint Description: Property describes the invocation entrypoint of a build.
-- # Class: Build_configSourceUri
--     * Slot: Build_spdxId Description: Autocreated FK slot
--     * Slot: configSourceUri Description: Property that describes the URI of the build configuration source file.
-- # Class: File_additionalPurpose
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: File_attributionText
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.
-- # Class: File_originatedBy
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: File_standardName
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: File_supportLevel
--     * Slot: File_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Package_additionalPurpose
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: Package_attributionText
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.
-- # Class: Package_originatedBy
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: Package_standardName
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Package_supportLevel
--     * Slot: Package_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: Sbom_sbomType
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: sbomType Description: Provides information about the type of an SBOM.
-- # Class: Sbom_element
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: element_spdxId Description: Refers to one or more Elements that are part of an ElementCollection.
-- # Class: Sbom_profileConformance
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: profileConformance Description: Describes one a profile which the creator of this ElementCollection intends to conform to.
-- # Class: Sbom_rootElement
--     * Slot: Sbom_spdxId Description: Autocreated FK slot
--     * Slot: rootElement_spdxId Description: This property is used to denote the root Element(s) of a tree of elements contained in a BOM.
-- # Class: Snippet_additionalPurpose
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: Snippet_attributionText
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.
-- # Class: Snippet_originatedBy
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: Snippet_standardName
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Snippet_supportLevel
--     * Slot: Snippet_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: SoftwareArtifact_additionalPurpose
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: SoftwareArtifact_attributionText
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.
-- # Class: SoftwareArtifact_originatedBy
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: SoftwareArtifact_standardName
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: SoftwareArtifact_supportLevel
--     * Slot: SoftwareArtifact_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: AIPackage_domain
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: domain Description: Captures the domain in which the AI package can be used.
-- # Class: AIPackage_modelDataPreprocessing
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: modelDataPreprocessing Description: Describes all the preprocessing steps applied to the training data before the model training.
-- # Class: AIPackage_modelExplainability
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: modelExplainability Description: Describes methods that can be used to explain the results from the AI model.
-- # Class: AIPackage_standardCompliance
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: standardCompliance Description: Captures a standard that is being complied with.
-- # Class: AIPackage_typeOfModel
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: typeOfModel Description: Records the type of the model used in the AI software.
-- # Class: AIPackage_additionalPurpose
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: AIPackage_attributionText
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.
-- # Class: AIPackage_originatedBy
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: AIPackage_standardName
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: AIPackage_supportLevel
--     * Slot: AIPackage_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: DatasetPackage_anonymizationMethodUsed
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: anonymizationMethodUsed Description: Describes the anonymization methods used.
-- # Class: DatasetPackage_dataPreprocessing
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: dataPreprocessing Description: Describes the preprocessing steps that were applied to the raw data to create the given dataset.
-- # Class: DatasetPackage_datasetType
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: datasetType Description: Describes the type of the given dataset.
-- # Class: DatasetPackage_knownBias
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: knownBias Description: Records the biases that the dataset is known to encompass.
-- # Class: DatasetPackage_additionalPurpose
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: additionalPurpose Description: Provides additional purpose information of the software artifact.
-- # Class: DatasetPackage_attributionText
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: attributionText Description: Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.
-- # Class: DatasetPackage_originatedBy
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: DatasetPackage_standardName
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: DatasetPackage_supportLevel
--     * Slot: DatasetPackage_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.
-- # Class: ConjunctiveLicenseSet_member
--     * Slot: ConjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: member_spdxId Description: A license expression participating in a license set.
-- # Class: CustomLicense_seeAlso
--     * Slot: CustomLicense_spdxId Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: CustomLicenseAddition_seeAlso
--     * Slot: CustomLicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: DisjunctiveLicenseSet_member
--     * Slot: DisjunctiveLicenseSet_spdxId Description: Autocreated FK slot
--     * Slot: member_spdxId Description: A license expression participating in a license set.
-- # Class: License_seeAlso
--     * Slot: License_spdxId Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: LicenseAddition_seeAlso
--     * Slot: LicenseAddition_spdxId Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: ListedLicense_seeAlso
--     * Slot: ListedLicense_spdxId Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: ListedLicenseException_seeAlso
--     * Slot: ListedLicenseException_spdxId Description: Autocreated FK slot
--     * Slot: seeAlso Description: Contains a URL where the License or LicenseAddition can be found in use.
-- # Class: CvssV2VulnAssessmentRelationship_to
--     * Slot: CvssV2VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: CvssV3VulnAssessmentRelationship_to
--     * Slot: CvssV3VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: CvssV4VulnAssessmentRelationship_to
--     * Slot: CvssV4VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: EpssVulnAssessmentRelationship_to
--     * Slot: EpssVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: ExploitCatalogVulnAssessmentRelationship_to
--     * Slot: ExploitCatalogVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: SsvcVulnAssessmentRelationship_to
--     * Slot: SsvcVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: VexAffectedVulnAssessmentRelationship_to
--     * Slot: VexAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: VexFixedVulnAssessmentRelationship_to
--     * Slot: VexFixedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: VexNotAffectedVulnAssessmentRelationship_to
--     * Slot: VexNotAffectedVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: VexUnderInvestigationVulnAssessmentRelationship_to
--     * Slot: VexUnderInvestigationVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: VexVulnAssessmentRelationship_to
--     * Slot: VexVulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: VulnAssessmentRelationship_to
--     * Slot: VulnAssessmentRelationship_spdxId Description: Autocreated FK slot
--     * Slot: to_spdxId Description: References an Element on the right-hand side of a relationship.
-- # Class: Vulnerability_originatedBy
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
--     * Slot: originatedBy_spdxId Description: Identifies from where or whom the Element originally came.
-- # Class: Vulnerability_standardName
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
--     * Slot: standardName Description: The name of a relevant standard that may apply to an artifact.
-- # Class: Vulnerability_supportLevel
--     * Slot: Vulnerability_spdxId Description: Autocreated FK slot
--     * Slot: supportLevel Description: Specifies the level of support associated with an artifact.

CREATE TABLE "CreationInfo" (
	id INTEGER NOT NULL,
	type TEXT,
	comment TEXT,
	created TEXT NOT NULL,
	"specVersion" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CreationInfo_id" ON "CreationInfo" (id);

CREATE TABLE "PackageVerificationCode" (
	id INTEGER NOT NULL,
	algorithm VARCHAR(17) NOT NULL,
	"hashValue" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PackageVerificationCode_id" ON "PackageVerificationCode" (id);

CREATE TABLE "PositiveIntegerRange" (
	id INTEGER NOT NULL,
	type TEXT,
	"beginIntegerRange" INTEGER NOT NULL,
	"endIntegerRange" INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PositiveIntegerRange_id" ON "PositiveIntegerRange" (id);

CREATE TABLE "CdxPropertiesExtension" (
	id INTEGER NOT NULL,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CdxPropertiesExtension_id" ON "CdxPropertiesExtension" (id);

CREATE TABLE "EnergyConsumption" (
	id INTEGER NOT NULL,
	type TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EnergyConsumption_id" ON "EnergyConsumption" (id);

CREATE TABLE "Agent" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Agent_spdxId" ON "Agent" ("spdxId");

CREATE TABLE "AnyLicenseInfo" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_AnyLicenseInfo_spdxId" ON "AnyLicenseInfo" ("spdxId");

CREATE TABLE "Bom" (
	context TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Bom_spdxId" ON "Bom" ("spdxId");

CREATE TABLE "Bundle" (
	context TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Bundle_spdxId" ON "Bundle" ("spdxId");

CREATE TABLE "Element" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Element_spdxId" ON "Element" ("spdxId");

CREATE TABLE "ElementCollection" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ElementCollection_spdxId" ON "ElementCollection" ("spdxId");

CREATE TABLE "IndividualElement" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_IndividualElement_spdxId" ON "IndividualElement" ("spdxId");

CREATE TABLE "Organization" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Organization_spdxId" ON "Organization" ("spdxId");

CREATE TABLE "Person" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Person_spdxId" ON "Person" ("spdxId");

CREATE TABLE "SoftwareAgent" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SoftwareAgent_spdxId" ON "SoftwareAgent" ("spdxId");

CREATE TABLE "Tool" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Tool_spdxId" ON "Tool" ("spdxId");

CREATE TABLE "Build" (
	"buildEndTime" TEXT,
	"buildId" TEXT,
	"buildStartTime" TEXT,
	"buildType" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Build_spdxId" ON "Build" ("spdxId");

CREATE TABLE "CdxPropertyEntry" (
	id INTEGER NOT NULL,
	type TEXT,
	"cdxPropName" TEXT NOT NULL,
	"cdxPropValue" TEXT,
	"CdxPropertiesExtension_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CdxPropertiesExtension_id") REFERENCES "CdxPropertiesExtension" (id)
);
CREATE INDEX "ix_CdxPropertyEntry_id" ON "CdxPropertyEntry" (id);

CREATE TABLE "LicenseExpression" (
	"licenseExpression" TEXT NOT NULL,
	"licenseListVersion" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_LicenseExpression_spdxId" ON "LicenseExpression" ("spdxId");

CREATE TABLE "SimpleLicensingText" (
	"licenseText" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SimpleLicensingText_spdxId" ON "SimpleLicensingText" ("spdxId");

CREATE TABLE "Sbom" (
	context TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Sbom_spdxId" ON "Sbom" ("spdxId");

CREATE TABLE "EnergyConsumptionDescription" (
	id INTEGER NOT NULL,
	type TEXT,
	"energyQuantity" NUMERIC NOT NULL,
	"energyUnit" VARCHAR(12) NOT NULL,
	"EnergyConsumption_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("EnergyConsumption_id") REFERENCES "EnergyConsumption" (id)
);
CREATE INDEX "ix_EnergyConsumptionDescription_id" ON "EnergyConsumptionDescription" (id);

CREATE TABLE "ConjunctiveLicenseSet" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ConjunctiveLicenseSet_spdxId" ON "ConjunctiveLicenseSet" ("spdxId");

CREATE TABLE "CustomLicense" (
	"licenseText" TEXT NOT NULL,
	"licenseXml" TEXT,
	"obsoletedBy" TEXT,
	"isDeprecatedLicenseId" BOOLEAN,
	"isFsfLibre" BOOLEAN,
	"isOsiApproved" BOOLEAN,
	"standardLicenseHeader" TEXT,
	"standardLicenseTemplate" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CustomLicense_spdxId" ON "CustomLicense" ("spdxId");

CREATE TABLE "CustomLicenseAddition" (
	"licenseXml" TEXT,
	"obsoletedBy" TEXT,
	"additionText" TEXT NOT NULL,
	"isDeprecatedAdditionId" BOOLEAN,
	"standardAdditionTemplate" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CustomLicenseAddition_spdxId" ON "CustomLicenseAddition" ("spdxId");

CREATE TABLE "DisjunctiveLicenseSet" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_DisjunctiveLicenseSet_spdxId" ON "DisjunctiveLicenseSet" ("spdxId");

CREATE TABLE "ExtendableLicense" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ExtendableLicense_spdxId" ON "ExtendableLicense" ("spdxId");

CREATE TABLE "IndividualLicensingInfo" (
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_IndividualLicensingInfo_spdxId" ON "IndividualLicensingInfo" ("spdxId");

CREATE TABLE "License" (
	"licenseText" TEXT NOT NULL,
	"licenseXml" TEXT,
	"obsoletedBy" TEXT,
	"isDeprecatedLicenseId" BOOLEAN,
	"isFsfLibre" BOOLEAN,
	"isOsiApproved" BOOLEAN,
	"standardLicenseHeader" TEXT,
	"standardLicenseTemplate" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_License_spdxId" ON "License" ("spdxId");

CREATE TABLE "LicenseAddition" (
	"licenseXml" TEXT,
	"obsoletedBy" TEXT,
	"additionText" TEXT NOT NULL,
	"isDeprecatedAdditionId" BOOLEAN,
	"standardAdditionTemplate" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_LicenseAddition_spdxId" ON "LicenseAddition" ("spdxId");

CREATE TABLE "ListedLicense" (
	"deprecatedVersion" TEXT,
	"listVersionAdded" TEXT,
	"licenseText" TEXT NOT NULL,
	"licenseXml" TEXT,
	"obsoletedBy" TEXT,
	"isDeprecatedLicenseId" BOOLEAN,
	"isFsfLibre" BOOLEAN,
	"isOsiApproved" BOOLEAN,
	"standardLicenseHeader" TEXT,
	"standardLicenseTemplate" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ListedLicense_spdxId" ON "ListedLicense" ("spdxId");

CREATE TABLE "ListedLicenseException" (
	"deprecatedVersion" TEXT,
	"listVersionAdded" TEXT,
	"licenseXml" TEXT,
	"obsoletedBy" TEXT,
	"additionText" TEXT NOT NULL,
	"isDeprecatedAdditionId" BOOLEAN,
	"standardAdditionTemplate" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ListedLicenseException_spdxId" ON "ListedLicenseException" ("spdxId");

CREATE TABLE "PackageVerificationCode_packageVerificationCodeExcludedFile" (
	"PackageVerificationCode_id" INTEGER,
	"packageVerificationCodeExcludedFile" TEXT,
	PRIMARY KEY ("PackageVerificationCode_id", "packageVerificationCodeExcludedFile"),
	FOREIGN KEY("PackageVerificationCode_id") REFERENCES "PackageVerificationCode" (id)
);
CREATE INDEX "ix_PackageVerificationCode_packageVerificationCodeExcludedFile_PackageVerificationCode_id" ON "PackageVerificationCode_packageVerificationCodeExcludedFile" ("PackageVerificationCode_id");
CREATE INDEX "ix_PackageVerificationCode_packageVerificationCodeExcludedFile_packageVerificationCodeExcludedFile" ON "PackageVerificationCode_packageVerificationCodeExcludedFile" ("packageVerificationCodeExcludedFile");

CREATE TABLE "Annotation" (
	"contentType" TEXT,
	"annotationType" VARCHAR(6) NOT NULL,
	statement TEXT,
	subject TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY(subject) REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Annotation_spdxId" ON "Annotation" ("spdxId");

CREATE TABLE "Artifact" (
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Artifact_spdxId" ON "Artifact" ("spdxId");

CREATE TABLE "Hash" (
	id INTEGER NOT NULL,
	algorithm VARCHAR(17) NOT NULL,
	"hashValue" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"Build_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId")
);
CREATE INDEX "ix_Hash_id" ON "Hash" (id);

CREATE TABLE "LifecycleScopedRelationship" (
	scope VARCHAR(11),
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_LifecycleScopedRelationship_spdxId" ON "LifecycleScopedRelationship" ("spdxId");

CREATE TABLE "Relationship" (
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Relationship_spdxId" ON "Relationship" ("spdxId");

CREATE TABLE "SpdxDocument" (
	"dataLicense" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("dataLicense") REFERENCES "AnyLicenseInfo" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SpdxDocument_spdxId" ON "SpdxDocument" ("spdxId");

CREATE TABLE "File" (
	"contentType" TEXT,
	"fileKind" VARCHAR(9),
	"copyrightText" TEXT,
	"primaryPurpose" VARCHAR(15),
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_File_spdxId" ON "File" ("spdxId");

CREATE TABLE "Package" (
	"downloadLocation" TEXT,
	"homePage" TEXT,
	"packageUrl" TEXT,
	"packageVersion" TEXT,
	"sourceInfo" TEXT,
	"copyrightText" TEXT,
	"primaryPurpose" VARCHAR(15),
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Package_spdxId" ON "Package" ("spdxId");

CREATE TABLE "SoftwareArtifact" (
	"copyrightText" TEXT,
	"primaryPurpose" VARCHAR(15),
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SoftwareArtifact_spdxId" ON "SoftwareArtifact" ("spdxId");

CREATE TABLE "AIPackage" (
	"autonomyType" VARCHAR(11),
	"informationAboutApplication" TEXT,
	"informationAboutTraining" TEXT,
	limitation TEXT,
	"safetyRiskAssessment" VARCHAR(7),
	"useSensitivePersonalInformation" VARCHAR(11),
	"downloadLocation" TEXT,
	"homePage" TEXT,
	"packageUrl" TEXT,
	"packageVersion" TEXT,
	"sourceInfo" TEXT,
	"copyrightText" TEXT,
	"primaryPurpose" VARCHAR(15),
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"energyConsumption_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("energyConsumption_id") REFERENCES "EnergyConsumption" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_AIPackage_spdxId" ON "AIPackage" ("spdxId");

CREATE TABLE "DatasetPackage" (
	"confidentialityLevel" VARCHAR(5),
	"dataCollectionProcess" TEXT,
	"datasetAvailability" VARCHAR(14),
	"datasetNoise" TEXT,
	"datasetSize" INTEGER,
	"datasetUpdateMechanism" TEXT,
	"hasSensitivePersonalInformation" VARCHAR(11),
	"intendedUse" TEXT,
	"downloadLocation" TEXT,
	"homePage" TEXT,
	"packageUrl" TEXT,
	"packageVersion" TEXT,
	"sourceInfo" TEXT,
	"copyrightText" TEXT,
	"primaryPurpose" VARCHAR(15),
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_DatasetPackage_spdxId" ON "DatasetPackage" ("spdxId");

CREATE TABLE "OrLaterOperator" (
	"subjectLicense" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("subjectLicense") REFERENCES "License" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_OrLaterOperator_spdxId" ON "OrLaterOperator" ("spdxId");

CREATE TABLE "WithAdditionOperator" (
	"subjectAddition" TEXT NOT NULL,
	"subjectExtendableLicense" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("subjectAddition") REFERENCES "LicenseAddition" ("spdxId"),
	FOREIGN KEY("subjectExtendableLicense") REFERENCES "ExtendableLicense" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_WithAdditionOperator_spdxId" ON "WithAdditionOperator" ("spdxId");

CREATE TABLE "Vulnerability" (
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"withdrawnTime" TEXT,
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Vulnerability_spdxId" ON "Vulnerability" ("spdxId");

CREATE TABLE "Bom_element" (
	"Bom_spdxId" TEXT,
	"element_spdxId" TEXT,
	PRIMARY KEY ("Bom_spdxId", "element_spdxId"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId"),
	FOREIGN KEY("element_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Bom_element_element_spdxId" ON "Bom_element" ("element_spdxId");
CREATE INDEX "ix_Bom_element_Bom_spdxId" ON "Bom_element" ("Bom_spdxId");

CREATE TABLE "Bom_profileConformance" (
	"Bom_spdxId" TEXT,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("Bom_spdxId", "profileConformance"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId")
);
CREATE INDEX "ix_Bom_profileConformance_Bom_spdxId" ON "Bom_profileConformance" ("Bom_spdxId");
CREATE INDEX "ix_Bom_profileConformance_profileConformance" ON "Bom_profileConformance" ("profileConformance");

CREATE TABLE "Bom_rootElement" (
	"Bom_spdxId" TEXT,
	"rootElement_spdxId" TEXT,
	PRIMARY KEY ("Bom_spdxId", "rootElement_spdxId"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId"),
	FOREIGN KEY("rootElement_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Bom_rootElement_rootElement_spdxId" ON "Bom_rootElement" ("rootElement_spdxId");
CREATE INDEX "ix_Bom_rootElement_Bom_spdxId" ON "Bom_rootElement" ("Bom_spdxId");

CREATE TABLE "Bundle_element" (
	"Bundle_spdxId" TEXT,
	"element_spdxId" TEXT,
	PRIMARY KEY ("Bundle_spdxId", "element_spdxId"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId"),
	FOREIGN KEY("element_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Bundle_element_element_spdxId" ON "Bundle_element" ("element_spdxId");
CREATE INDEX "ix_Bundle_element_Bundle_spdxId" ON "Bundle_element" ("Bundle_spdxId");

CREATE TABLE "Bundle_profileConformance" (
	"Bundle_spdxId" TEXT,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("Bundle_spdxId", "profileConformance"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId")
);
CREATE INDEX "ix_Bundle_profileConformance_profileConformance" ON "Bundle_profileConformance" ("profileConformance");
CREATE INDEX "ix_Bundle_profileConformance_Bundle_spdxId" ON "Bundle_profileConformance" ("Bundle_spdxId");

CREATE TABLE "Bundle_rootElement" (
	"Bundle_spdxId" TEXT,
	"rootElement_spdxId" TEXT,
	PRIMARY KEY ("Bundle_spdxId", "rootElement_spdxId"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId"),
	FOREIGN KEY("rootElement_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Bundle_rootElement_Bundle_spdxId" ON "Bundle_rootElement" ("Bundle_spdxId");
CREATE INDEX "ix_Bundle_rootElement_rootElement_spdxId" ON "Bundle_rootElement" ("rootElement_spdxId");

CREATE TABLE "CreationInfo_createdBy" (
	"CreationInfo_id" INTEGER,
	"createdBy_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("CreationInfo_id", "createdBy_spdxId"),
	FOREIGN KEY("CreationInfo_id") REFERENCES "CreationInfo" (id),
	FOREIGN KEY("createdBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_CreationInfo_createdBy_CreationInfo_id" ON "CreationInfo_createdBy" ("CreationInfo_id");
CREATE INDEX "ix_CreationInfo_createdBy_createdBy_spdxId" ON "CreationInfo_createdBy" ("createdBy_spdxId");

CREATE TABLE "CreationInfo_createdUsing" (
	"CreationInfo_id" INTEGER,
	"createdUsing_spdxId" TEXT,
	PRIMARY KEY ("CreationInfo_id", "createdUsing_spdxId"),
	FOREIGN KEY("CreationInfo_id") REFERENCES "CreationInfo" (id),
	FOREIGN KEY("createdUsing_spdxId") REFERENCES "Tool" ("spdxId")
);
CREATE INDEX "ix_CreationInfo_createdUsing_CreationInfo_id" ON "CreationInfo_createdUsing" ("CreationInfo_id");
CREATE INDEX "ix_CreationInfo_createdUsing_createdUsing_spdxId" ON "CreationInfo_createdUsing" ("createdUsing_spdxId");

CREATE TABLE "ElementCollection_element" (
	"ElementCollection_spdxId" TEXT,
	"element_spdxId" TEXT,
	PRIMARY KEY ("ElementCollection_spdxId", "element_spdxId"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId"),
	FOREIGN KEY("element_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_ElementCollection_element_ElementCollection_spdxId" ON "ElementCollection_element" ("ElementCollection_spdxId");
CREATE INDEX "ix_ElementCollection_element_element_spdxId" ON "ElementCollection_element" ("element_spdxId");

CREATE TABLE "ElementCollection_profileConformance" (
	"ElementCollection_spdxId" TEXT,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("ElementCollection_spdxId", "profileConformance"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId")
);
CREATE INDEX "ix_ElementCollection_profileConformance_ElementCollection_spdxId" ON "ElementCollection_profileConformance" ("ElementCollection_spdxId");
CREATE INDEX "ix_ElementCollection_profileConformance_profileConformance" ON "ElementCollection_profileConformance" ("profileConformance");

CREATE TABLE "ElementCollection_rootElement" (
	"ElementCollection_spdxId" TEXT,
	"rootElement_spdxId" TEXT,
	PRIMARY KEY ("ElementCollection_spdxId", "rootElement_spdxId"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId"),
	FOREIGN KEY("rootElement_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_ElementCollection_rootElement_rootElement_spdxId" ON "ElementCollection_rootElement" ("rootElement_spdxId");
CREATE INDEX "ix_ElementCollection_rootElement_ElementCollection_spdxId" ON "ElementCollection_rootElement" ("ElementCollection_spdxId");

CREATE TABLE "Build_configSourceEntrypoint" (
	"Build_spdxId" TEXT,
	"configSourceEntrypoint" TEXT,
	PRIMARY KEY ("Build_spdxId", "configSourceEntrypoint"),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId")
);
CREATE INDEX "ix_Build_configSourceEntrypoint_Build_spdxId" ON "Build_configSourceEntrypoint" ("Build_spdxId");
CREATE INDEX "ix_Build_configSourceEntrypoint_configSourceEntrypoint" ON "Build_configSourceEntrypoint" ("configSourceEntrypoint");

CREATE TABLE "Build_configSourceUri" (
	"Build_spdxId" TEXT,
	"configSourceUri" TEXT,
	PRIMARY KEY ("Build_spdxId", "configSourceUri"),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId")
);
CREATE INDEX "ix_Build_configSourceUri_Build_spdxId" ON "Build_configSourceUri" ("Build_spdxId");
CREATE INDEX "ix_Build_configSourceUri_configSourceUri" ON "Build_configSourceUri" ("configSourceUri");

CREATE TABLE "Sbom_sbomType" (
	"Sbom_spdxId" TEXT,
	"sbomType" VARCHAR(8),
	PRIMARY KEY ("Sbom_spdxId", "sbomType"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId")
);
CREATE INDEX "ix_Sbom_sbomType_sbomType" ON "Sbom_sbomType" ("sbomType");
CREATE INDEX "ix_Sbom_sbomType_Sbom_spdxId" ON "Sbom_sbomType" ("Sbom_spdxId");

CREATE TABLE "Sbom_element" (
	"Sbom_spdxId" TEXT,
	"element_spdxId" TEXT,
	PRIMARY KEY ("Sbom_spdxId", "element_spdxId"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId"),
	FOREIGN KEY("element_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Sbom_element_element_spdxId" ON "Sbom_element" ("element_spdxId");
CREATE INDEX "ix_Sbom_element_Sbom_spdxId" ON "Sbom_element" ("Sbom_spdxId");

CREATE TABLE "Sbom_profileConformance" (
	"Sbom_spdxId" TEXT,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("Sbom_spdxId", "profileConformance"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId")
);
CREATE INDEX "ix_Sbom_profileConformance_Sbom_spdxId" ON "Sbom_profileConformance" ("Sbom_spdxId");
CREATE INDEX "ix_Sbom_profileConformance_profileConformance" ON "Sbom_profileConformance" ("profileConformance");

CREATE TABLE "Sbom_rootElement" (
	"Sbom_spdxId" TEXT,
	"rootElement_spdxId" TEXT,
	PRIMARY KEY ("Sbom_spdxId", "rootElement_spdxId"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId"),
	FOREIGN KEY("rootElement_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Sbom_rootElement_rootElement_spdxId" ON "Sbom_rootElement" ("rootElement_spdxId");
CREATE INDEX "ix_Sbom_rootElement_Sbom_spdxId" ON "Sbom_rootElement" ("Sbom_spdxId");

CREATE TABLE "ConjunctiveLicenseSet_member" (
	"ConjunctiveLicenseSet_spdxId" TEXT,
	"member_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("ConjunctiveLicenseSet_spdxId", "member_spdxId"),
	FOREIGN KEY("ConjunctiveLicenseSet_spdxId") REFERENCES "ConjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("member_spdxId") REFERENCES "AnyLicenseInfo" ("spdxId")
);
CREATE INDEX "ix_ConjunctiveLicenseSet_member_ConjunctiveLicenseSet_spdxId" ON "ConjunctiveLicenseSet_member" ("ConjunctiveLicenseSet_spdxId");
CREATE INDEX "ix_ConjunctiveLicenseSet_member_member_spdxId" ON "ConjunctiveLicenseSet_member" ("member_spdxId");

CREATE TABLE "CustomLicense_seeAlso" (
	"CustomLicense_spdxId" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("CustomLicense_spdxId", "seeAlso"),
	FOREIGN KEY("CustomLicense_spdxId") REFERENCES "CustomLicense" ("spdxId")
);
CREATE INDEX "ix_CustomLicense_seeAlso_CustomLicense_spdxId" ON "CustomLicense_seeAlso" ("CustomLicense_spdxId");
CREATE INDEX "ix_CustomLicense_seeAlso_seeAlso" ON "CustomLicense_seeAlso" ("seeAlso");

CREATE TABLE "CustomLicenseAddition_seeAlso" (
	"CustomLicenseAddition_spdxId" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("CustomLicenseAddition_spdxId", "seeAlso"),
	FOREIGN KEY("CustomLicenseAddition_spdxId") REFERENCES "CustomLicenseAddition" ("spdxId")
);
CREATE INDEX "ix_CustomLicenseAddition_seeAlso_CustomLicenseAddition_spdxId" ON "CustomLicenseAddition_seeAlso" ("CustomLicenseAddition_spdxId");
CREATE INDEX "ix_CustomLicenseAddition_seeAlso_seeAlso" ON "CustomLicenseAddition_seeAlso" ("seeAlso");

CREATE TABLE "DisjunctiveLicenseSet_member" (
	"DisjunctiveLicenseSet_spdxId" TEXT,
	"member_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("DisjunctiveLicenseSet_spdxId", "member_spdxId"),
	FOREIGN KEY("DisjunctiveLicenseSet_spdxId") REFERENCES "DisjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("member_spdxId") REFERENCES "AnyLicenseInfo" ("spdxId")
);
CREATE INDEX "ix_DisjunctiveLicenseSet_member_member_spdxId" ON "DisjunctiveLicenseSet_member" ("member_spdxId");
CREATE INDEX "ix_DisjunctiveLicenseSet_member_DisjunctiveLicenseSet_spdxId" ON "DisjunctiveLicenseSet_member" ("DisjunctiveLicenseSet_spdxId");

CREATE TABLE "License_seeAlso" (
	"License_spdxId" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("License_spdxId", "seeAlso"),
	FOREIGN KEY("License_spdxId") REFERENCES "License" ("spdxId")
);
CREATE INDEX "ix_License_seeAlso_License_spdxId" ON "License_seeAlso" ("License_spdxId");
CREATE INDEX "ix_License_seeAlso_seeAlso" ON "License_seeAlso" ("seeAlso");

CREATE TABLE "LicenseAddition_seeAlso" (
	"LicenseAddition_spdxId" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("LicenseAddition_spdxId", "seeAlso"),
	FOREIGN KEY("LicenseAddition_spdxId") REFERENCES "LicenseAddition" ("spdxId")
);
CREATE INDEX "ix_LicenseAddition_seeAlso_LicenseAddition_spdxId" ON "LicenseAddition_seeAlso" ("LicenseAddition_spdxId");
CREATE INDEX "ix_LicenseAddition_seeAlso_seeAlso" ON "LicenseAddition_seeAlso" ("seeAlso");

CREATE TABLE "ListedLicense_seeAlso" (
	"ListedLicense_spdxId" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("ListedLicense_spdxId", "seeAlso"),
	FOREIGN KEY("ListedLicense_spdxId") REFERENCES "ListedLicense" ("spdxId")
);
CREATE INDEX "ix_ListedLicense_seeAlso_ListedLicense_spdxId" ON "ListedLicense_seeAlso" ("ListedLicense_spdxId");
CREATE INDEX "ix_ListedLicense_seeAlso_seeAlso" ON "ListedLicense_seeAlso" ("seeAlso");

CREATE TABLE "ListedLicenseException_seeAlso" (
	"ListedLicenseException_spdxId" TEXT,
	"seeAlso" TEXT,
	PRIMARY KEY ("ListedLicenseException_spdxId", "seeAlso"),
	FOREIGN KEY("ListedLicenseException_spdxId") REFERENCES "ListedLicenseException" ("spdxId")
);
CREATE INDEX "ix_ListedLicenseException_seeAlso_ListedLicenseException_spdxId" ON "ListedLicenseException_seeAlso" ("ListedLicenseException_spdxId");
CREATE INDEX "ix_ListedLicenseException_seeAlso_seeAlso" ON "ListedLicenseException_seeAlso" ("seeAlso");

CREATE TABLE "DictionaryEntry" (
	id INTEGER NOT NULL,
	type TEXT,
	"key" TEXT NOT NULL,
	value TEXT,
	"Build_spdxId" TEXT,
	"LicenseExpression_spdxId" TEXT,
	"AIPackage_spdxId" TEXT,
	"DatasetPackage_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId"),
	FOREIGN KEY("LicenseExpression_spdxId") REFERENCES "LicenseExpression" ("spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DictionaryEntry_id" ON "DictionaryEntry" (id);

CREATE TABLE "ExternalMap" (
	id INTEGER NOT NULL,
	type TEXT,
	"definingArtifact" TEXT,
	"externalSpdxId" TEXT NOT NULL,
	"locationHint" TEXT,
	"SpdxDocument_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("definingArtifact") REFERENCES "Artifact" ("spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId")
);
CREATE INDEX "ix_ExternalMap_id" ON "ExternalMap" (id);

CREATE TABLE "NamespaceMap" (
	id INTEGER NOT NULL,
	type TEXT,
	namespace TEXT NOT NULL,
	prefix TEXT NOT NULL,
	"SpdxDocument_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId")
);
CREATE INDEX "ix_NamespaceMap_id" ON "NamespaceMap" (id);

CREATE TABLE "Snippet" (
	"snippetFromFile" TEXT NOT NULL,
	"copyrightText" TEXT,
	"primaryPurpose" VARCHAR(15),
	"suppliedBy" TEXT,
	"builtTime" TEXT,
	"releaseTime" TEXT,
	"validUntilTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"byteRange_id" INTEGER,
	"lineRange_id" INTEGER,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("snippetFromFile") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("byteRange_id") REFERENCES "PositiveIntegerRange" (id),
	FOREIGN KEY("lineRange_id") REFERENCES "PositiveIntegerRange" (id),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_Snippet_spdxId" ON "Snippet" ("spdxId");

CREATE TABLE "CvssV2VulnAssessmentRelationship" (
	score NUMERIC NOT NULL,
	"vectorString" TEXT NOT NULL,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_spdxId" ON "CvssV2VulnAssessmentRelationship" ("spdxId");

CREATE TABLE "CvssV3VulnAssessmentRelationship" (
	score NUMERIC NOT NULL,
	severity VARCHAR(8) NOT NULL,
	"vectorString" TEXT NOT NULL,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_spdxId" ON "CvssV3VulnAssessmentRelationship" ("spdxId");

CREATE TABLE "CvssV4VulnAssessmentRelationship" (
	score NUMERIC NOT NULL,
	severity VARCHAR(8) NOT NULL,
	"vectorString" TEXT NOT NULL,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_spdxId" ON "CvssV4VulnAssessmentRelationship" ("spdxId");

CREATE TABLE "EpssVulnAssessmentRelationship" (
	percentile NUMERIC NOT NULL,
	probability NUMERIC NOT NULL,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_spdxId" ON "EpssVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship" (
	"catalogType" VARCHAR(5) NOT NULL,
	exploited BOOLEAN NOT NULL,
	security_locator TEXT NOT NULL,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_spdxId" ON "ExploitCatalogVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "SsvcVulnAssessmentRelationship" (
	"decisionType" VARCHAR(9) NOT NULL,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_spdxId" ON "SsvcVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "VexAffectedVulnAssessmentRelationship" (
	"actionStatement" TEXT NOT NULL,
	"actionStatementTime" TEXT,
	"statusNotes" TEXT,
	"vexVersion" TEXT,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_spdxId" ON "VexAffectedVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "VexFixedVulnAssessmentRelationship" (
	"statusNotes" TEXT,
	"vexVersion" TEXT,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_spdxId" ON "VexFixedVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship" (
	"impactStatement" TEXT,
	"impactStatementTime" TEXT,
	"justificationType" VARCHAR(43),
	"statusNotes" TEXT,
	"vexVersion" TEXT,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_spdxId" ON "VexNotAffectedVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship" (
	"statusNotes" TEXT,
	"vexVersion" TEXT,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_spdxId" ON "VexUnderInvestigationVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "VexVulnAssessmentRelationship" (
	"statusNotes" TEXT,
	"vexVersion" TEXT,
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_spdxId" ON "VexVulnAssessmentRelationship" ("spdxId");

CREATE TABLE "VulnAssessmentRelationship" (
	"modifiedTime" TEXT,
	"publishedTime" TEXT,
	"suppliedBy" TEXT,
	"withdrawnTime" TEXT,
	"assessedElement" TEXT,
	completeness VARCHAR(11),
	"endTime" TEXT,
	"from" TEXT NOT NULL,
	"relationshipType" VARCHAR(26) NOT NULL,
	"startTime" TEXT,
	type TEXT,
	comment TEXT,
	"spdxId" TEXT NOT NULL,
	description TEXT,
	name TEXT,
	summary TEXT,
	"creationInfo_id" INTEGER NOT NULL,
	PRIMARY KEY ("spdxId"),
	FOREIGN KEY("suppliedBy") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("assessedElement") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("from") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("creationInfo_id") REFERENCES "CreationInfo" (id)
);
CREATE INDEX "ix_VulnAssessmentRelationship_spdxId" ON "VulnAssessmentRelationship" ("spdxId");

CREATE TABLE "Artifact_originatedBy" (
	"Artifact_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("Artifact_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_Artifact_originatedBy_originatedBy_spdxId" ON "Artifact_originatedBy" ("originatedBy_spdxId");
CREATE INDEX "ix_Artifact_originatedBy_Artifact_spdxId" ON "Artifact_originatedBy" ("Artifact_spdxId");

CREATE TABLE "Artifact_standardName" (
	"Artifact_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("Artifact_spdxId", "standardName"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId")
);
CREATE INDEX "ix_Artifact_standardName_Artifact_spdxId" ON "Artifact_standardName" ("Artifact_spdxId");
CREATE INDEX "ix_Artifact_standardName_standardName" ON "Artifact_standardName" ("standardName");

CREATE TABLE "Artifact_supportLevel" (
	"Artifact_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Artifact_spdxId", "supportLevel"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId")
);
CREATE INDEX "ix_Artifact_supportLevel_supportLevel" ON "Artifact_supportLevel" ("supportLevel");
CREATE INDEX "ix_Artifact_supportLevel_Artifact_spdxId" ON "Artifact_supportLevel" ("Artifact_spdxId");

CREATE TABLE "LifecycleScopedRelationship_to" (
	"LifecycleScopedRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("LifecycleScopedRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("LifecycleScopedRelationship_spdxId") REFERENCES "LifecycleScopedRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_LifecycleScopedRelationship_to_LifecycleScopedRelationship_spdxId" ON "LifecycleScopedRelationship_to" ("LifecycleScopedRelationship_spdxId");
CREATE INDEX "ix_LifecycleScopedRelationship_to_to_spdxId" ON "LifecycleScopedRelationship_to" ("to_spdxId");

CREATE TABLE "Relationship_to" (
	"Relationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("Relationship_spdxId", "to_spdxId"),
	FOREIGN KEY("Relationship_spdxId") REFERENCES "Relationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_Relationship_to_Relationship_spdxId" ON "Relationship_to" ("Relationship_spdxId");
CREATE INDEX "ix_Relationship_to_to_spdxId" ON "Relationship_to" ("to_spdxId");

CREATE TABLE "SpdxDocument_element" (
	"SpdxDocument_spdxId" TEXT,
	"element_spdxId" TEXT,
	PRIMARY KEY ("SpdxDocument_spdxId", "element_spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId"),
	FOREIGN KEY("element_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_SpdxDocument_element_element_spdxId" ON "SpdxDocument_element" ("element_spdxId");
CREATE INDEX "ix_SpdxDocument_element_SpdxDocument_spdxId" ON "SpdxDocument_element" ("SpdxDocument_spdxId");

CREATE TABLE "SpdxDocument_profileConformance" (
	"SpdxDocument_spdxId" TEXT,
	"profileConformance" VARCHAR(17),
	PRIMARY KEY ("SpdxDocument_spdxId", "profileConformance"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId")
);
CREATE INDEX "ix_SpdxDocument_profileConformance_SpdxDocument_spdxId" ON "SpdxDocument_profileConformance" ("SpdxDocument_spdxId");
CREATE INDEX "ix_SpdxDocument_profileConformance_profileConformance" ON "SpdxDocument_profileConformance" ("profileConformance");

CREATE TABLE "SpdxDocument_rootElement" (
	"SpdxDocument_spdxId" TEXT,
	"rootElement_spdxId" TEXT,
	PRIMARY KEY ("SpdxDocument_spdxId", "rootElement_spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId"),
	FOREIGN KEY("rootElement_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_SpdxDocument_rootElement_SpdxDocument_spdxId" ON "SpdxDocument_rootElement" ("SpdxDocument_spdxId");
CREATE INDEX "ix_SpdxDocument_rootElement_rootElement_spdxId" ON "SpdxDocument_rootElement" ("rootElement_spdxId");

CREATE TABLE "File_additionalPurpose" (
	"File_spdxId" TEXT,
	"additionalPurpose" VARCHAR(15),
	PRIMARY KEY ("File_spdxId", "additionalPurpose"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId")
);
CREATE INDEX "ix_File_additionalPurpose_additionalPurpose" ON "File_additionalPurpose" ("additionalPurpose");
CREATE INDEX "ix_File_additionalPurpose_File_spdxId" ON "File_additionalPurpose" ("File_spdxId");

CREATE TABLE "File_attributionText" (
	"File_spdxId" TEXT,
	"attributionText" TEXT,
	PRIMARY KEY ("File_spdxId", "attributionText"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId")
);
CREATE INDEX "ix_File_attributionText_File_spdxId" ON "File_attributionText" ("File_spdxId");
CREATE INDEX "ix_File_attributionText_attributionText" ON "File_attributionText" ("attributionText");

CREATE TABLE "File_originatedBy" (
	"File_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("File_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_File_originatedBy_File_spdxId" ON "File_originatedBy" ("File_spdxId");
CREATE INDEX "ix_File_originatedBy_originatedBy_spdxId" ON "File_originatedBy" ("originatedBy_spdxId");

CREATE TABLE "File_standardName" (
	"File_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("File_spdxId", "standardName"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId")
);
CREATE INDEX "ix_File_standardName_standardName" ON "File_standardName" ("standardName");
CREATE INDEX "ix_File_standardName_File_spdxId" ON "File_standardName" ("File_spdxId");

CREATE TABLE "File_supportLevel" (
	"File_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("File_spdxId", "supportLevel"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId")
);
CREATE INDEX "ix_File_supportLevel_File_spdxId" ON "File_supportLevel" ("File_spdxId");
CREATE INDEX "ix_File_supportLevel_supportLevel" ON "File_supportLevel" ("supportLevel");

CREATE TABLE "Package_additionalPurpose" (
	"Package_spdxId" TEXT,
	"additionalPurpose" VARCHAR(15),
	PRIMARY KEY ("Package_spdxId", "additionalPurpose"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId")
);
CREATE INDEX "ix_Package_additionalPurpose_Package_spdxId" ON "Package_additionalPurpose" ("Package_spdxId");
CREATE INDEX "ix_Package_additionalPurpose_additionalPurpose" ON "Package_additionalPurpose" ("additionalPurpose");

CREATE TABLE "Package_attributionText" (
	"Package_spdxId" TEXT,
	"attributionText" TEXT,
	PRIMARY KEY ("Package_spdxId", "attributionText"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId")
);
CREATE INDEX "ix_Package_attributionText_attributionText" ON "Package_attributionText" ("attributionText");
CREATE INDEX "ix_Package_attributionText_Package_spdxId" ON "Package_attributionText" ("Package_spdxId");

CREATE TABLE "Package_originatedBy" (
	"Package_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("Package_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_Package_originatedBy_originatedBy_spdxId" ON "Package_originatedBy" ("originatedBy_spdxId");
CREATE INDEX "ix_Package_originatedBy_Package_spdxId" ON "Package_originatedBy" ("Package_spdxId");

CREATE TABLE "Package_standardName" (
	"Package_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("Package_spdxId", "standardName"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId")
);
CREATE INDEX "ix_Package_standardName_standardName" ON "Package_standardName" ("standardName");
CREATE INDEX "ix_Package_standardName_Package_spdxId" ON "Package_standardName" ("Package_spdxId");

CREATE TABLE "Package_supportLevel" (
	"Package_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Package_spdxId", "supportLevel"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId")
);
CREATE INDEX "ix_Package_supportLevel_Package_spdxId" ON "Package_supportLevel" ("Package_spdxId");
CREATE INDEX "ix_Package_supportLevel_supportLevel" ON "Package_supportLevel" ("supportLevel");

CREATE TABLE "SoftwareArtifact_additionalPurpose" (
	"SoftwareArtifact_spdxId" TEXT,
	"additionalPurpose" VARCHAR(15),
	PRIMARY KEY ("SoftwareArtifact_spdxId", "additionalPurpose"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId")
);
CREATE INDEX "ix_SoftwareArtifact_additionalPurpose_SoftwareArtifact_spdxId" ON "SoftwareArtifact_additionalPurpose" ("SoftwareArtifact_spdxId");
CREATE INDEX "ix_SoftwareArtifact_additionalPurpose_additionalPurpose" ON "SoftwareArtifact_additionalPurpose" ("additionalPurpose");

CREATE TABLE "SoftwareArtifact_attributionText" (
	"SoftwareArtifact_spdxId" TEXT,
	"attributionText" TEXT,
	PRIMARY KEY ("SoftwareArtifact_spdxId", "attributionText"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId")
);
CREATE INDEX "ix_SoftwareArtifact_attributionText_attributionText" ON "SoftwareArtifact_attributionText" ("attributionText");
CREATE INDEX "ix_SoftwareArtifact_attributionText_SoftwareArtifact_spdxId" ON "SoftwareArtifact_attributionText" ("SoftwareArtifact_spdxId");

CREATE TABLE "SoftwareArtifact_originatedBy" (
	"SoftwareArtifact_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("SoftwareArtifact_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_SoftwareArtifact_originatedBy_originatedBy_spdxId" ON "SoftwareArtifact_originatedBy" ("originatedBy_spdxId");
CREATE INDEX "ix_SoftwareArtifact_originatedBy_SoftwareArtifact_spdxId" ON "SoftwareArtifact_originatedBy" ("SoftwareArtifact_spdxId");

CREATE TABLE "SoftwareArtifact_standardName" (
	"SoftwareArtifact_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("SoftwareArtifact_spdxId", "standardName"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId")
);
CREATE INDEX "ix_SoftwareArtifact_standardName_standardName" ON "SoftwareArtifact_standardName" ("standardName");
CREATE INDEX "ix_SoftwareArtifact_standardName_SoftwareArtifact_spdxId" ON "SoftwareArtifact_standardName" ("SoftwareArtifact_spdxId");

CREATE TABLE "SoftwareArtifact_supportLevel" (
	"SoftwareArtifact_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("SoftwareArtifact_spdxId", "supportLevel"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId")
);
CREATE INDEX "ix_SoftwareArtifact_supportLevel_SoftwareArtifact_spdxId" ON "SoftwareArtifact_supportLevel" ("SoftwareArtifact_spdxId");
CREATE INDEX "ix_SoftwareArtifact_supportLevel_supportLevel" ON "SoftwareArtifact_supportLevel" ("supportLevel");

CREATE TABLE "AIPackage_domain" (
	"AIPackage_spdxId" TEXT,
	domain TEXT,
	PRIMARY KEY ("AIPackage_spdxId", domain),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_domain_domain" ON "AIPackage_domain" (domain);
CREATE INDEX "ix_AIPackage_domain_AIPackage_spdxId" ON "AIPackage_domain" ("AIPackage_spdxId");

CREATE TABLE "AIPackage_modelDataPreprocessing" (
	"AIPackage_spdxId" TEXT,
	"modelDataPreprocessing" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "modelDataPreprocessing"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_modelDataPreprocessing_AIPackage_spdxId" ON "AIPackage_modelDataPreprocessing" ("AIPackage_spdxId");
CREATE INDEX "ix_AIPackage_modelDataPreprocessing_modelDataPreprocessing" ON "AIPackage_modelDataPreprocessing" ("modelDataPreprocessing");

CREATE TABLE "AIPackage_modelExplainability" (
	"AIPackage_spdxId" TEXT,
	"modelExplainability" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "modelExplainability"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_modelExplainability_modelExplainability" ON "AIPackage_modelExplainability" ("modelExplainability");
CREATE INDEX "ix_AIPackage_modelExplainability_AIPackage_spdxId" ON "AIPackage_modelExplainability" ("AIPackage_spdxId");

CREATE TABLE "AIPackage_standardCompliance" (
	"AIPackage_spdxId" TEXT,
	"standardCompliance" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "standardCompliance"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_standardCompliance_AIPackage_spdxId" ON "AIPackage_standardCompliance" ("AIPackage_spdxId");
CREATE INDEX "ix_AIPackage_standardCompliance_standardCompliance" ON "AIPackage_standardCompliance" ("standardCompliance");

CREATE TABLE "AIPackage_typeOfModel" (
	"AIPackage_spdxId" TEXT,
	"typeOfModel" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "typeOfModel"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_typeOfModel_AIPackage_spdxId" ON "AIPackage_typeOfModel" ("AIPackage_spdxId");
CREATE INDEX "ix_AIPackage_typeOfModel_typeOfModel" ON "AIPackage_typeOfModel" ("typeOfModel");

CREATE TABLE "AIPackage_additionalPurpose" (
	"AIPackage_spdxId" TEXT,
	"additionalPurpose" VARCHAR(15),
	PRIMARY KEY ("AIPackage_spdxId", "additionalPurpose"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_additionalPurpose_additionalPurpose" ON "AIPackage_additionalPurpose" ("additionalPurpose");
CREATE INDEX "ix_AIPackage_additionalPurpose_AIPackage_spdxId" ON "AIPackage_additionalPurpose" ("AIPackage_spdxId");

CREATE TABLE "AIPackage_attributionText" (
	"AIPackage_spdxId" TEXT,
	"attributionText" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "attributionText"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_attributionText_attributionText" ON "AIPackage_attributionText" ("attributionText");
CREATE INDEX "ix_AIPackage_attributionText_AIPackage_spdxId" ON "AIPackage_attributionText" ("AIPackage_spdxId");

CREATE TABLE "AIPackage_originatedBy" (
	"AIPackage_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_AIPackage_originatedBy_originatedBy_spdxId" ON "AIPackage_originatedBy" ("originatedBy_spdxId");
CREATE INDEX "ix_AIPackage_originatedBy_AIPackage_spdxId" ON "AIPackage_originatedBy" ("AIPackage_spdxId");

CREATE TABLE "AIPackage_standardName" (
	"AIPackage_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("AIPackage_spdxId", "standardName"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_standardName_standardName" ON "AIPackage_standardName" ("standardName");
CREATE INDEX "ix_AIPackage_standardName_AIPackage_spdxId" ON "AIPackage_standardName" ("AIPackage_spdxId");

CREATE TABLE "AIPackage_supportLevel" (
	"AIPackage_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("AIPackage_spdxId", "supportLevel"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId")
);
CREATE INDEX "ix_AIPackage_supportLevel_supportLevel" ON "AIPackage_supportLevel" ("supportLevel");
CREATE INDEX "ix_AIPackage_supportLevel_AIPackage_spdxId" ON "AIPackage_supportLevel" ("AIPackage_spdxId");

CREATE TABLE "DatasetPackage_anonymizationMethodUsed" (
	"DatasetPackage_spdxId" TEXT,
	"anonymizationMethodUsed" TEXT,
	PRIMARY KEY ("DatasetPackage_spdxId", "anonymizationMethodUsed"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_anonymizationMethodUsed_anonymizationMethodUsed" ON "DatasetPackage_anonymizationMethodUsed" ("anonymizationMethodUsed");
CREATE INDEX "ix_DatasetPackage_anonymizationMethodUsed_DatasetPackage_spdxId" ON "DatasetPackage_anonymizationMethodUsed" ("DatasetPackage_spdxId");

CREATE TABLE "DatasetPackage_dataPreprocessing" (
	"DatasetPackage_spdxId" TEXT,
	"dataPreprocessing" TEXT,
	PRIMARY KEY ("DatasetPackage_spdxId", "dataPreprocessing"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_dataPreprocessing_DatasetPackage_spdxId" ON "DatasetPackage_dataPreprocessing" ("DatasetPackage_spdxId");
CREATE INDEX "ix_DatasetPackage_dataPreprocessing_dataPreprocessing" ON "DatasetPackage_dataPreprocessing" ("dataPreprocessing");

CREATE TABLE "DatasetPackage_datasetType" (
	"DatasetPackage_spdxId" TEXT,
	"datasetType" VARCHAR(11) NOT NULL,
	PRIMARY KEY ("DatasetPackage_spdxId", "datasetType"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_datasetType_datasetType" ON "DatasetPackage_datasetType" ("datasetType");
CREATE INDEX "ix_DatasetPackage_datasetType_DatasetPackage_spdxId" ON "DatasetPackage_datasetType" ("DatasetPackage_spdxId");

CREATE TABLE "DatasetPackage_knownBias" (
	"DatasetPackage_spdxId" TEXT,
	"knownBias" TEXT,
	PRIMARY KEY ("DatasetPackage_spdxId", "knownBias"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_knownBias_knownBias" ON "DatasetPackage_knownBias" ("knownBias");
CREATE INDEX "ix_DatasetPackage_knownBias_DatasetPackage_spdxId" ON "DatasetPackage_knownBias" ("DatasetPackage_spdxId");

CREATE TABLE "DatasetPackage_additionalPurpose" (
	"DatasetPackage_spdxId" TEXT,
	"additionalPurpose" VARCHAR(15),
	PRIMARY KEY ("DatasetPackage_spdxId", "additionalPurpose"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_additionalPurpose_DatasetPackage_spdxId" ON "DatasetPackage_additionalPurpose" ("DatasetPackage_spdxId");
CREATE INDEX "ix_DatasetPackage_additionalPurpose_additionalPurpose" ON "DatasetPackage_additionalPurpose" ("additionalPurpose");

CREATE TABLE "DatasetPackage_attributionText" (
	"DatasetPackage_spdxId" TEXT,
	"attributionText" TEXT,
	PRIMARY KEY ("DatasetPackage_spdxId", "attributionText"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_attributionText_DatasetPackage_spdxId" ON "DatasetPackage_attributionText" ("DatasetPackage_spdxId");
CREATE INDEX "ix_DatasetPackage_attributionText_attributionText" ON "DatasetPackage_attributionText" ("attributionText");

CREATE TABLE "DatasetPackage_originatedBy" (
	"DatasetPackage_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("DatasetPackage_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_originatedBy_DatasetPackage_spdxId" ON "DatasetPackage_originatedBy" ("DatasetPackage_spdxId");
CREATE INDEX "ix_DatasetPackage_originatedBy_originatedBy_spdxId" ON "DatasetPackage_originatedBy" ("originatedBy_spdxId");

CREATE TABLE "DatasetPackage_standardName" (
	"DatasetPackage_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("DatasetPackage_spdxId", "standardName"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_standardName_standardName" ON "DatasetPackage_standardName" ("standardName");
CREATE INDEX "ix_DatasetPackage_standardName_DatasetPackage_spdxId" ON "DatasetPackage_standardName" ("DatasetPackage_spdxId");

CREATE TABLE "DatasetPackage_supportLevel" (
	"DatasetPackage_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("DatasetPackage_spdxId", "supportLevel"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_DatasetPackage_supportLevel_DatasetPackage_spdxId" ON "DatasetPackage_supportLevel" ("DatasetPackage_spdxId");
CREATE INDEX "ix_DatasetPackage_supportLevel_supportLevel" ON "DatasetPackage_supportLevel" ("supportLevel");

CREATE TABLE "Vulnerability_originatedBy" (
	"Vulnerability_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("Vulnerability_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_Vulnerability_originatedBy_originatedBy_spdxId" ON "Vulnerability_originatedBy" ("originatedBy_spdxId");
CREATE INDEX "ix_Vulnerability_originatedBy_Vulnerability_spdxId" ON "Vulnerability_originatedBy" ("Vulnerability_spdxId");

CREATE TABLE "Vulnerability_standardName" (
	"Vulnerability_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("Vulnerability_spdxId", "standardName"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId")
);
CREATE INDEX "ix_Vulnerability_standardName_standardName" ON "Vulnerability_standardName" ("standardName");
CREATE INDEX "ix_Vulnerability_standardName_Vulnerability_spdxId" ON "Vulnerability_standardName" ("Vulnerability_spdxId");

CREATE TABLE "Vulnerability_supportLevel" (
	"Vulnerability_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Vulnerability_spdxId", "supportLevel"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId")
);
CREATE INDEX "ix_Vulnerability_supportLevel_Vulnerability_spdxId" ON "Vulnerability_supportLevel" ("Vulnerability_spdxId");
CREATE INDEX "ix_Vulnerability_supportLevel_supportLevel" ON "Vulnerability_supportLevel" ("supportLevel");

CREATE TABLE "Extension" (
	id INTEGER NOT NULL,
	type TEXT,
	"Agent_spdxId" TEXT,
	"Annotation_spdxId" TEXT,
	"AnyLicenseInfo_spdxId" TEXT,
	"Artifact_spdxId" TEXT,
	"Bom_spdxId" TEXT,
	"Bundle_spdxId" TEXT,
	"Element_spdxId" TEXT,
	"ElementCollection_spdxId" TEXT,
	"IndividualElement_spdxId" TEXT,
	"LifecycleScopedRelationship_spdxId" TEXT,
	"Organization_spdxId" TEXT,
	"Person_spdxId" TEXT,
	"Relationship_spdxId" TEXT,
	"SoftwareAgent_spdxId" TEXT,
	"SpdxDocument_spdxId" TEXT,
	"Tool_spdxId" TEXT,
	"Build_spdxId" TEXT,
	"LicenseExpression_spdxId" TEXT,
	"SimpleLicensingText_spdxId" TEXT,
	"File_spdxId" TEXT,
	"Package_spdxId" TEXT,
	"Sbom_spdxId" TEXT,
	"Snippet_spdxId" TEXT,
	"SoftwareArtifact_spdxId" TEXT,
	"AIPackage_spdxId" TEXT,
	"DatasetPackage_spdxId" TEXT,
	"ConjunctiveLicenseSet_spdxId" TEXT,
	"CustomLicense_spdxId" TEXT,
	"CustomLicenseAddition_spdxId" TEXT,
	"DisjunctiveLicenseSet_spdxId" TEXT,
	"ExtendableLicense_spdxId" TEXT,
	"IndividualLicensingInfo_spdxId" TEXT,
	"License_spdxId" TEXT,
	"LicenseAddition_spdxId" TEXT,
	"ListedLicense_spdxId" TEXT,
	"ListedLicenseException_spdxId" TEXT,
	"OrLaterOperator_spdxId" TEXT,
	"WithAdditionOperator_spdxId" TEXT,
	"CvssV2VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV3VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV4VulnAssessmentRelationship_spdxId" TEXT,
	"EpssVulnAssessmentRelationship_spdxId" TEXT,
	"ExploitCatalogVulnAssessmentRelationship_spdxId" TEXT,
	"SsvcVulnAssessmentRelationship_spdxId" TEXT,
	"VexAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexFixedVulnAssessmentRelationship_spdxId" TEXT,
	"VexNotAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexUnderInvestigationVulnAssessmentRelationship_spdxId" TEXT,
	"VexVulnAssessmentRelationship_spdxId" TEXT,
	"VulnAssessmentRelationship_spdxId" TEXT,
	"Vulnerability_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Agent_spdxId") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("Annotation_spdxId") REFERENCES "Annotation" ("spdxId"),
	FOREIGN KEY("AnyLicenseInfo_spdxId") REFERENCES "AnyLicenseInfo" ("spdxId"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId"),
	FOREIGN KEY("Element_spdxId") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId"),
	FOREIGN KEY("IndividualElement_spdxId") REFERENCES "IndividualElement" ("spdxId"),
	FOREIGN KEY("LifecycleScopedRelationship_spdxId") REFERENCES "LifecycleScopedRelationship" ("spdxId"),
	FOREIGN KEY("Organization_spdxId") REFERENCES "Organization" ("spdxId"),
	FOREIGN KEY("Person_spdxId") REFERENCES "Person" ("spdxId"),
	FOREIGN KEY("Relationship_spdxId") REFERENCES "Relationship" ("spdxId"),
	FOREIGN KEY("SoftwareAgent_spdxId") REFERENCES "SoftwareAgent" ("spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId"),
	FOREIGN KEY("Tool_spdxId") REFERENCES "Tool" ("spdxId"),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId"),
	FOREIGN KEY("LicenseExpression_spdxId") REFERENCES "LicenseExpression" ("spdxId"),
	FOREIGN KEY("SimpleLicensingText_spdxId") REFERENCES "SimpleLicensingText" ("spdxId"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId"),
	FOREIGN KEY("ConjunctiveLicenseSet_spdxId") REFERENCES "ConjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("CustomLicense_spdxId") REFERENCES "CustomLicense" ("spdxId"),
	FOREIGN KEY("CustomLicenseAddition_spdxId") REFERENCES "CustomLicenseAddition" ("spdxId"),
	FOREIGN KEY("DisjunctiveLicenseSet_spdxId") REFERENCES "DisjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("ExtendableLicense_spdxId") REFERENCES "ExtendableLicense" ("spdxId"),
	FOREIGN KEY("IndividualLicensingInfo_spdxId") REFERENCES "IndividualLicensingInfo" ("spdxId"),
	FOREIGN KEY("License_spdxId") REFERENCES "License" ("spdxId"),
	FOREIGN KEY("LicenseAddition_spdxId") REFERENCES "LicenseAddition" ("spdxId"),
	FOREIGN KEY("ListedLicense_spdxId") REFERENCES "ListedLicense" ("spdxId"),
	FOREIGN KEY("ListedLicenseException_spdxId") REFERENCES "ListedLicenseException" ("spdxId"),
	FOREIGN KEY("OrLaterOperator_spdxId") REFERENCES "OrLaterOperator" ("spdxId"),
	FOREIGN KEY("WithAdditionOperator_spdxId") REFERENCES "WithAdditionOperator" ("spdxId"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_spdxId") REFERENCES "CvssV2VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_spdxId") REFERENCES "CvssV3VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_spdxId") REFERENCES "CvssV4VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_spdxId") REFERENCES "EpssVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_spdxId") REFERENCES "ExploitCatalogVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_spdxId") REFERENCES "SsvcVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_spdxId") REFERENCES "VexFixedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexNotAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_spdxId") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexVulnAssessmentRelationship_spdxId") REFERENCES "VexVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VulnAssessmentRelationship_spdxId") REFERENCES "VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId")
);
CREATE INDEX "ix_Extension_id" ON "Extension" (id);

CREATE TABLE "ExternalIdentifier" (
	id INTEGER NOT NULL,
	type TEXT,
	comment TEXT,
	"externalIdentifierType" VARCHAR(13) NOT NULL,
	identifier TEXT NOT NULL,
	"issuingAuthority" TEXT,
	"Agent_spdxId" TEXT,
	"Annotation_spdxId" TEXT,
	"AnyLicenseInfo_spdxId" TEXT,
	"Artifact_spdxId" TEXT,
	"Bom_spdxId" TEXT,
	"Bundle_spdxId" TEXT,
	"Element_spdxId" TEXT,
	"ElementCollection_spdxId" TEXT,
	"IndividualElement_spdxId" TEXT,
	"LifecycleScopedRelationship_spdxId" TEXT,
	"Organization_spdxId" TEXT,
	"Person_spdxId" TEXT,
	"Relationship_spdxId" TEXT,
	"SoftwareAgent_spdxId" TEXT,
	"SpdxDocument_spdxId" TEXT,
	"Tool_spdxId" TEXT,
	"Build_spdxId" TEXT,
	"LicenseExpression_spdxId" TEXT,
	"SimpleLicensingText_spdxId" TEXT,
	"File_spdxId" TEXT,
	"Package_spdxId" TEXT,
	"Sbom_spdxId" TEXT,
	"Snippet_spdxId" TEXT,
	"SoftwareArtifact_spdxId" TEXT,
	"AIPackage_spdxId" TEXT,
	"DatasetPackage_spdxId" TEXT,
	"ConjunctiveLicenseSet_spdxId" TEXT,
	"CustomLicense_spdxId" TEXT,
	"CustomLicenseAddition_spdxId" TEXT,
	"DisjunctiveLicenseSet_spdxId" TEXT,
	"ExtendableLicense_spdxId" TEXT,
	"IndividualLicensingInfo_spdxId" TEXT,
	"License_spdxId" TEXT,
	"LicenseAddition_spdxId" TEXT,
	"ListedLicense_spdxId" TEXT,
	"ListedLicenseException_spdxId" TEXT,
	"OrLaterOperator_spdxId" TEXT,
	"WithAdditionOperator_spdxId" TEXT,
	"CvssV2VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV3VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV4VulnAssessmentRelationship_spdxId" TEXT,
	"EpssVulnAssessmentRelationship_spdxId" TEXT,
	"ExploitCatalogVulnAssessmentRelationship_spdxId" TEXT,
	"SsvcVulnAssessmentRelationship_spdxId" TEXT,
	"VexAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexFixedVulnAssessmentRelationship_spdxId" TEXT,
	"VexNotAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexUnderInvestigationVulnAssessmentRelationship_spdxId" TEXT,
	"VexVulnAssessmentRelationship_spdxId" TEXT,
	"VulnAssessmentRelationship_spdxId" TEXT,
	"Vulnerability_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Agent_spdxId") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("Annotation_spdxId") REFERENCES "Annotation" ("spdxId"),
	FOREIGN KEY("AnyLicenseInfo_spdxId") REFERENCES "AnyLicenseInfo" ("spdxId"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId"),
	FOREIGN KEY("Element_spdxId") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId"),
	FOREIGN KEY("IndividualElement_spdxId") REFERENCES "IndividualElement" ("spdxId"),
	FOREIGN KEY("LifecycleScopedRelationship_spdxId") REFERENCES "LifecycleScopedRelationship" ("spdxId"),
	FOREIGN KEY("Organization_spdxId") REFERENCES "Organization" ("spdxId"),
	FOREIGN KEY("Person_spdxId") REFERENCES "Person" ("spdxId"),
	FOREIGN KEY("Relationship_spdxId") REFERENCES "Relationship" ("spdxId"),
	FOREIGN KEY("SoftwareAgent_spdxId") REFERENCES "SoftwareAgent" ("spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId"),
	FOREIGN KEY("Tool_spdxId") REFERENCES "Tool" ("spdxId"),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId"),
	FOREIGN KEY("LicenseExpression_spdxId") REFERENCES "LicenseExpression" ("spdxId"),
	FOREIGN KEY("SimpleLicensingText_spdxId") REFERENCES "SimpleLicensingText" ("spdxId"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId"),
	FOREIGN KEY("ConjunctiveLicenseSet_spdxId") REFERENCES "ConjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("CustomLicense_spdxId") REFERENCES "CustomLicense" ("spdxId"),
	FOREIGN KEY("CustomLicenseAddition_spdxId") REFERENCES "CustomLicenseAddition" ("spdxId"),
	FOREIGN KEY("DisjunctiveLicenseSet_spdxId") REFERENCES "DisjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("ExtendableLicense_spdxId") REFERENCES "ExtendableLicense" ("spdxId"),
	FOREIGN KEY("IndividualLicensingInfo_spdxId") REFERENCES "IndividualLicensingInfo" ("spdxId"),
	FOREIGN KEY("License_spdxId") REFERENCES "License" ("spdxId"),
	FOREIGN KEY("LicenseAddition_spdxId") REFERENCES "LicenseAddition" ("spdxId"),
	FOREIGN KEY("ListedLicense_spdxId") REFERENCES "ListedLicense" ("spdxId"),
	FOREIGN KEY("ListedLicenseException_spdxId") REFERENCES "ListedLicenseException" ("spdxId"),
	FOREIGN KEY("OrLaterOperator_spdxId") REFERENCES "OrLaterOperator" ("spdxId"),
	FOREIGN KEY("WithAdditionOperator_spdxId") REFERENCES "WithAdditionOperator" ("spdxId"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_spdxId") REFERENCES "CvssV2VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_spdxId") REFERENCES "CvssV3VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_spdxId") REFERENCES "CvssV4VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_spdxId") REFERENCES "EpssVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_spdxId") REFERENCES "ExploitCatalogVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_spdxId") REFERENCES "SsvcVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_spdxId") REFERENCES "VexFixedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexNotAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_spdxId") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexVulnAssessmentRelationship_spdxId") REFERENCES "VexVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VulnAssessmentRelationship_spdxId") REFERENCES "VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId")
);
CREATE INDEX "ix_ExternalIdentifier_id" ON "ExternalIdentifier" (id);

CREATE TABLE "ExternalRef" (
	id INTEGER NOT NULL,
	type TEXT,
	comment TEXT,
	"contentType" TEXT,
	"externalRefType" VARCHAR(37),
	"Agent_spdxId" TEXT,
	"Annotation_spdxId" TEXT,
	"AnyLicenseInfo_spdxId" TEXT,
	"Artifact_spdxId" TEXT,
	"Bom_spdxId" TEXT,
	"Bundle_spdxId" TEXT,
	"Element_spdxId" TEXT,
	"ElementCollection_spdxId" TEXT,
	"IndividualElement_spdxId" TEXT,
	"LifecycleScopedRelationship_spdxId" TEXT,
	"Organization_spdxId" TEXT,
	"Person_spdxId" TEXT,
	"Relationship_spdxId" TEXT,
	"SoftwareAgent_spdxId" TEXT,
	"SpdxDocument_spdxId" TEXT,
	"Tool_spdxId" TEXT,
	"Build_spdxId" TEXT,
	"LicenseExpression_spdxId" TEXT,
	"SimpleLicensingText_spdxId" TEXT,
	"File_spdxId" TEXT,
	"Package_spdxId" TEXT,
	"Sbom_spdxId" TEXT,
	"Snippet_spdxId" TEXT,
	"SoftwareArtifact_spdxId" TEXT,
	"AIPackage_spdxId" TEXT,
	"DatasetPackage_spdxId" TEXT,
	"ConjunctiveLicenseSet_spdxId" TEXT,
	"CustomLicense_spdxId" TEXT,
	"CustomLicenseAddition_spdxId" TEXT,
	"DisjunctiveLicenseSet_spdxId" TEXT,
	"ExtendableLicense_spdxId" TEXT,
	"IndividualLicensingInfo_spdxId" TEXT,
	"License_spdxId" TEXT,
	"LicenseAddition_spdxId" TEXT,
	"ListedLicense_spdxId" TEXT,
	"ListedLicenseException_spdxId" TEXT,
	"OrLaterOperator_spdxId" TEXT,
	"WithAdditionOperator_spdxId" TEXT,
	"CvssV2VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV3VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV4VulnAssessmentRelationship_spdxId" TEXT,
	"EpssVulnAssessmentRelationship_spdxId" TEXT,
	"ExploitCatalogVulnAssessmentRelationship_spdxId" TEXT,
	"SsvcVulnAssessmentRelationship_spdxId" TEXT,
	"VexAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexFixedVulnAssessmentRelationship_spdxId" TEXT,
	"VexNotAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexUnderInvestigationVulnAssessmentRelationship_spdxId" TEXT,
	"VexVulnAssessmentRelationship_spdxId" TEXT,
	"VulnAssessmentRelationship_spdxId" TEXT,
	"Vulnerability_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Agent_spdxId") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("Annotation_spdxId") REFERENCES "Annotation" ("spdxId"),
	FOREIGN KEY("AnyLicenseInfo_spdxId") REFERENCES "AnyLicenseInfo" ("spdxId"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId"),
	FOREIGN KEY("Element_spdxId") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId"),
	FOREIGN KEY("IndividualElement_spdxId") REFERENCES "IndividualElement" ("spdxId"),
	FOREIGN KEY("LifecycleScopedRelationship_spdxId") REFERENCES "LifecycleScopedRelationship" ("spdxId"),
	FOREIGN KEY("Organization_spdxId") REFERENCES "Organization" ("spdxId"),
	FOREIGN KEY("Person_spdxId") REFERENCES "Person" ("spdxId"),
	FOREIGN KEY("Relationship_spdxId") REFERENCES "Relationship" ("spdxId"),
	FOREIGN KEY("SoftwareAgent_spdxId") REFERENCES "SoftwareAgent" ("spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId"),
	FOREIGN KEY("Tool_spdxId") REFERENCES "Tool" ("spdxId"),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId"),
	FOREIGN KEY("LicenseExpression_spdxId") REFERENCES "LicenseExpression" ("spdxId"),
	FOREIGN KEY("SimpleLicensingText_spdxId") REFERENCES "SimpleLicensingText" ("spdxId"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId"),
	FOREIGN KEY("ConjunctiveLicenseSet_spdxId") REFERENCES "ConjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("CustomLicense_spdxId") REFERENCES "CustomLicense" ("spdxId"),
	FOREIGN KEY("CustomLicenseAddition_spdxId") REFERENCES "CustomLicenseAddition" ("spdxId"),
	FOREIGN KEY("DisjunctiveLicenseSet_spdxId") REFERENCES "DisjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("ExtendableLicense_spdxId") REFERENCES "ExtendableLicense" ("spdxId"),
	FOREIGN KEY("IndividualLicensingInfo_spdxId") REFERENCES "IndividualLicensingInfo" ("spdxId"),
	FOREIGN KEY("License_spdxId") REFERENCES "License" ("spdxId"),
	FOREIGN KEY("LicenseAddition_spdxId") REFERENCES "LicenseAddition" ("spdxId"),
	FOREIGN KEY("ListedLicense_spdxId") REFERENCES "ListedLicense" ("spdxId"),
	FOREIGN KEY("ListedLicenseException_spdxId") REFERENCES "ListedLicenseException" ("spdxId"),
	FOREIGN KEY("OrLaterOperator_spdxId") REFERENCES "OrLaterOperator" ("spdxId"),
	FOREIGN KEY("WithAdditionOperator_spdxId") REFERENCES "WithAdditionOperator" ("spdxId"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_spdxId") REFERENCES "CvssV2VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_spdxId") REFERENCES "CvssV3VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_spdxId") REFERENCES "CvssV4VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_spdxId") REFERENCES "EpssVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_spdxId") REFERENCES "ExploitCatalogVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_spdxId") REFERENCES "SsvcVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_spdxId") REFERENCES "VexFixedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexNotAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_spdxId") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexVulnAssessmentRelationship_spdxId") REFERENCES "VexVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VulnAssessmentRelationship_spdxId") REFERENCES "VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId")
);
CREATE INDEX "ix_ExternalRef_id" ON "ExternalRef" (id);

CREATE TABLE "IntegrityMethod" (
	id INTEGER NOT NULL,
	type TEXT,
	comment TEXT,
	"Agent_spdxId" TEXT,
	"Annotation_spdxId" TEXT,
	"AnyLicenseInfo_spdxId" TEXT,
	"Artifact_spdxId" TEXT,
	"Bom_spdxId" TEXT,
	"Bundle_spdxId" TEXT,
	"Element_spdxId" TEXT,
	"ElementCollection_spdxId" TEXT,
	"ExternalMap_id" INTEGER,
	"IndividualElement_spdxId" TEXT,
	"LifecycleScopedRelationship_spdxId" TEXT,
	"Organization_spdxId" TEXT,
	"Person_spdxId" TEXT,
	"Relationship_spdxId" TEXT,
	"SoftwareAgent_spdxId" TEXT,
	"SpdxDocument_spdxId" TEXT,
	"Tool_spdxId" TEXT,
	"Build_spdxId" TEXT,
	"LicenseExpression_spdxId" TEXT,
	"SimpleLicensingText_spdxId" TEXT,
	"File_spdxId" TEXT,
	"Package_spdxId" TEXT,
	"Sbom_spdxId" TEXT,
	"Snippet_spdxId" TEXT,
	"SoftwareArtifact_spdxId" TEXT,
	"AIPackage_spdxId" TEXT,
	"DatasetPackage_spdxId" TEXT,
	"ConjunctiveLicenseSet_spdxId" TEXT,
	"CustomLicense_spdxId" TEXT,
	"CustomLicenseAddition_spdxId" TEXT,
	"DisjunctiveLicenseSet_spdxId" TEXT,
	"ExtendableLicense_spdxId" TEXT,
	"IndividualLicensingInfo_spdxId" TEXT,
	"License_spdxId" TEXT,
	"LicenseAddition_spdxId" TEXT,
	"ListedLicense_spdxId" TEXT,
	"ListedLicenseException_spdxId" TEXT,
	"OrLaterOperator_spdxId" TEXT,
	"WithAdditionOperator_spdxId" TEXT,
	"CvssV2VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV3VulnAssessmentRelationship_spdxId" TEXT,
	"CvssV4VulnAssessmentRelationship_spdxId" TEXT,
	"EpssVulnAssessmentRelationship_spdxId" TEXT,
	"ExploitCatalogVulnAssessmentRelationship_spdxId" TEXT,
	"SsvcVulnAssessmentRelationship_spdxId" TEXT,
	"VexAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexFixedVulnAssessmentRelationship_spdxId" TEXT,
	"VexNotAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"VexUnderInvestigationVulnAssessmentRelationship_spdxId" TEXT,
	"VexVulnAssessmentRelationship_spdxId" TEXT,
	"VulnAssessmentRelationship_spdxId" TEXT,
	"Vulnerability_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Agent_spdxId") REFERENCES "Agent" ("spdxId"),
	FOREIGN KEY("Annotation_spdxId") REFERENCES "Annotation" ("spdxId"),
	FOREIGN KEY("AnyLicenseInfo_spdxId") REFERENCES "AnyLicenseInfo" ("spdxId"),
	FOREIGN KEY("Artifact_spdxId") REFERENCES "Artifact" ("spdxId"),
	FOREIGN KEY("Bom_spdxId") REFERENCES "Bom" ("spdxId"),
	FOREIGN KEY("Bundle_spdxId") REFERENCES "Bundle" ("spdxId"),
	FOREIGN KEY("Element_spdxId") REFERENCES "Element" ("spdxId"),
	FOREIGN KEY("ElementCollection_spdxId") REFERENCES "ElementCollection" ("spdxId"),
	FOREIGN KEY("ExternalMap_id") REFERENCES "ExternalMap" (id),
	FOREIGN KEY("IndividualElement_spdxId") REFERENCES "IndividualElement" ("spdxId"),
	FOREIGN KEY("LifecycleScopedRelationship_spdxId") REFERENCES "LifecycleScopedRelationship" ("spdxId"),
	FOREIGN KEY("Organization_spdxId") REFERENCES "Organization" ("spdxId"),
	FOREIGN KEY("Person_spdxId") REFERENCES "Person" ("spdxId"),
	FOREIGN KEY("Relationship_spdxId") REFERENCES "Relationship" ("spdxId"),
	FOREIGN KEY("SoftwareAgent_spdxId") REFERENCES "SoftwareAgent" ("spdxId"),
	FOREIGN KEY("SpdxDocument_spdxId") REFERENCES "SpdxDocument" ("spdxId"),
	FOREIGN KEY("Tool_spdxId") REFERENCES "Tool" ("spdxId"),
	FOREIGN KEY("Build_spdxId") REFERENCES "Build" ("spdxId"),
	FOREIGN KEY("LicenseExpression_spdxId") REFERENCES "LicenseExpression" ("spdxId"),
	FOREIGN KEY("SimpleLicensingText_spdxId") REFERENCES "SimpleLicensingText" ("spdxId"),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId"),
	FOREIGN KEY("Sbom_spdxId") REFERENCES "Sbom" ("spdxId"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId"),
	FOREIGN KEY("ConjunctiveLicenseSet_spdxId") REFERENCES "ConjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("CustomLicense_spdxId") REFERENCES "CustomLicense" ("spdxId"),
	FOREIGN KEY("CustomLicenseAddition_spdxId") REFERENCES "CustomLicenseAddition" ("spdxId"),
	FOREIGN KEY("DisjunctiveLicenseSet_spdxId") REFERENCES "DisjunctiveLicenseSet" ("spdxId"),
	FOREIGN KEY("ExtendableLicense_spdxId") REFERENCES "ExtendableLicense" ("spdxId"),
	FOREIGN KEY("IndividualLicensingInfo_spdxId") REFERENCES "IndividualLicensingInfo" ("spdxId"),
	FOREIGN KEY("License_spdxId") REFERENCES "License" ("spdxId"),
	FOREIGN KEY("LicenseAddition_spdxId") REFERENCES "LicenseAddition" ("spdxId"),
	FOREIGN KEY("ListedLicense_spdxId") REFERENCES "ListedLicense" ("spdxId"),
	FOREIGN KEY("ListedLicenseException_spdxId") REFERENCES "ListedLicenseException" ("spdxId"),
	FOREIGN KEY("OrLaterOperator_spdxId") REFERENCES "OrLaterOperator" ("spdxId"),
	FOREIGN KEY("WithAdditionOperator_spdxId") REFERENCES "WithAdditionOperator" ("spdxId"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_spdxId") REFERENCES "CvssV2VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_spdxId") REFERENCES "CvssV3VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_spdxId") REFERENCES "CvssV4VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_spdxId") REFERENCES "EpssVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_spdxId") REFERENCES "ExploitCatalogVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_spdxId") REFERENCES "SsvcVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_spdxId") REFERENCES "VexFixedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexNotAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_spdxId") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VexVulnAssessmentRelationship_spdxId") REFERENCES "VexVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("VulnAssessmentRelationship_spdxId") REFERENCES "VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("Vulnerability_spdxId") REFERENCES "Vulnerability" ("spdxId")
);
CREATE INDEX "ix_IntegrityMethod_id" ON "IntegrityMethod" (id);

CREATE TABLE "ContentIdentifier" (
	id INTEGER NOT NULL,
	"contentIdentifierType" VARCHAR(6) NOT NULL,
	"contentIdentifierValue" TEXT NOT NULL,
	type TEXT,
	comment TEXT,
	"File_spdxId" TEXT,
	"Package_spdxId" TEXT,
	"Snippet_spdxId" TEXT,
	"SoftwareArtifact_spdxId" TEXT,
	"AIPackage_spdxId" TEXT,
	"DatasetPackage_spdxId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("File_spdxId") REFERENCES "File" ("spdxId"),
	FOREIGN KEY("Package_spdxId") REFERENCES "Package" ("spdxId"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId"),
	FOREIGN KEY("SoftwareArtifact_spdxId") REFERENCES "SoftwareArtifact" ("spdxId"),
	FOREIGN KEY("AIPackage_spdxId") REFERENCES "AIPackage" ("spdxId"),
	FOREIGN KEY("DatasetPackage_spdxId") REFERENCES "DatasetPackage" ("spdxId")
);
CREATE INDEX "ix_ContentIdentifier_id" ON "ContentIdentifier" (id);

CREATE TABLE "Snippet_additionalPurpose" (
	"Snippet_spdxId" TEXT,
	"additionalPurpose" VARCHAR(15),
	PRIMARY KEY ("Snippet_spdxId", "additionalPurpose"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId")
);
CREATE INDEX "ix_Snippet_additionalPurpose_additionalPurpose" ON "Snippet_additionalPurpose" ("additionalPurpose");
CREATE INDEX "ix_Snippet_additionalPurpose_Snippet_spdxId" ON "Snippet_additionalPurpose" ("Snippet_spdxId");

CREATE TABLE "Snippet_attributionText" (
	"Snippet_spdxId" TEXT,
	"attributionText" TEXT,
	PRIMARY KEY ("Snippet_spdxId", "attributionText"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId")
);
CREATE INDEX "ix_Snippet_attributionText_attributionText" ON "Snippet_attributionText" ("attributionText");
CREATE INDEX "ix_Snippet_attributionText_Snippet_spdxId" ON "Snippet_attributionText" ("Snippet_spdxId");

CREATE TABLE "Snippet_originatedBy" (
	"Snippet_spdxId" TEXT,
	"originatedBy_spdxId" TEXT,
	PRIMARY KEY ("Snippet_spdxId", "originatedBy_spdxId"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId"),
	FOREIGN KEY("originatedBy_spdxId") REFERENCES "Agent" ("spdxId")
);
CREATE INDEX "ix_Snippet_originatedBy_Snippet_spdxId" ON "Snippet_originatedBy" ("Snippet_spdxId");
CREATE INDEX "ix_Snippet_originatedBy_originatedBy_spdxId" ON "Snippet_originatedBy" ("originatedBy_spdxId");

CREATE TABLE "Snippet_standardName" (
	"Snippet_spdxId" TEXT,
	"standardName" TEXT,
	PRIMARY KEY ("Snippet_spdxId", "standardName"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId")
);
CREATE INDEX "ix_Snippet_standardName_Snippet_spdxId" ON "Snippet_standardName" ("Snippet_spdxId");
CREATE INDEX "ix_Snippet_standardName_standardName" ON "Snippet_standardName" ("standardName");

CREATE TABLE "Snippet_supportLevel" (
	"Snippet_spdxId" TEXT,
	"supportLevel" VARCHAR(14),
	PRIMARY KEY ("Snippet_spdxId", "supportLevel"),
	FOREIGN KEY("Snippet_spdxId") REFERENCES "Snippet" ("spdxId")
);
CREATE INDEX "ix_Snippet_supportLevel_Snippet_spdxId" ON "Snippet_supportLevel" ("Snippet_spdxId");
CREATE INDEX "ix_Snippet_supportLevel_supportLevel" ON "Snippet_supportLevel" ("supportLevel");

CREATE TABLE "CvssV2VulnAssessmentRelationship_to" (
	"CvssV2VulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("CvssV2VulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("CvssV2VulnAssessmentRelationship_spdxId") REFERENCES "CvssV2VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_to_CvssV2VulnAssessmentRelationship_spdxId" ON "CvssV2VulnAssessmentRelationship_to" ("CvssV2VulnAssessmentRelationship_spdxId");
CREATE INDEX "ix_CvssV2VulnAssessmentRelationship_to_to_spdxId" ON "CvssV2VulnAssessmentRelationship_to" ("to_spdxId");

CREATE TABLE "CvssV3VulnAssessmentRelationship_to" (
	"CvssV3VulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("CvssV3VulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("CvssV3VulnAssessmentRelationship_spdxId") REFERENCES "CvssV3VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_to_to_spdxId" ON "CvssV3VulnAssessmentRelationship_to" ("to_spdxId");
CREATE INDEX "ix_CvssV3VulnAssessmentRelationship_to_CvssV3VulnAssessmentRelationship_spdxId" ON "CvssV3VulnAssessmentRelationship_to" ("CvssV3VulnAssessmentRelationship_spdxId");

CREATE TABLE "CvssV4VulnAssessmentRelationship_to" (
	"CvssV4VulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("CvssV4VulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("CvssV4VulnAssessmentRelationship_spdxId") REFERENCES "CvssV4VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_to_to_spdxId" ON "CvssV4VulnAssessmentRelationship_to" ("to_spdxId");
CREATE INDEX "ix_CvssV4VulnAssessmentRelationship_to_CvssV4VulnAssessmentRelationship_spdxId" ON "CvssV4VulnAssessmentRelationship_to" ("CvssV4VulnAssessmentRelationship_spdxId");

CREATE TABLE "EpssVulnAssessmentRelationship_to" (
	"EpssVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("EpssVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("EpssVulnAssessmentRelationship_spdxId") REFERENCES "EpssVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_EpssVulnAssessmentRelationship_to_EpssVulnAssessmentRelationship_spdxId" ON "EpssVulnAssessmentRelationship_to" ("EpssVulnAssessmentRelationship_spdxId");
CREATE INDEX "ix_EpssVulnAssessmentRelationship_to_to_spdxId" ON "EpssVulnAssessmentRelationship_to" ("to_spdxId");

CREATE TABLE "ExploitCatalogVulnAssessmentRelationship_to" (
	"ExploitCatalogVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("ExploitCatalogVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("ExploitCatalogVulnAssessmentRelationship_spdxId") REFERENCES "ExploitCatalogVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_to_ExploitCatalogVulnAssessmentRelationship_spdxId" ON "ExploitCatalogVulnAssessmentRelationship_to" ("ExploitCatalogVulnAssessmentRelationship_spdxId");
CREATE INDEX "ix_ExploitCatalogVulnAssessmentRelationship_to_to_spdxId" ON "ExploitCatalogVulnAssessmentRelationship_to" ("to_spdxId");

CREATE TABLE "SsvcVulnAssessmentRelationship_to" (
	"SsvcVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("SsvcVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("SsvcVulnAssessmentRelationship_spdxId") REFERENCES "SsvcVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_to_to_spdxId" ON "SsvcVulnAssessmentRelationship_to" ("to_spdxId");
CREATE INDEX "ix_SsvcVulnAssessmentRelationship_to_SsvcVulnAssessmentRelationship_spdxId" ON "SsvcVulnAssessmentRelationship_to" ("SsvcVulnAssessmentRelationship_spdxId");

CREATE TABLE "VexAffectedVulnAssessmentRelationship_to" (
	"VexAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("VexAffectedVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("VexAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_to_to_spdxId" ON "VexAffectedVulnAssessmentRelationship_to" ("to_spdxId");
CREATE INDEX "ix_VexAffectedVulnAssessmentRelationship_to_VexAffectedVulnAssessmentRelationship_spdxId" ON "VexAffectedVulnAssessmentRelationship_to" ("VexAffectedVulnAssessmentRelationship_spdxId");

CREATE TABLE "VexFixedVulnAssessmentRelationship_to" (
	"VexFixedVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("VexFixedVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("VexFixedVulnAssessmentRelationship_spdxId") REFERENCES "VexFixedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_to_VexFixedVulnAssessmentRelationship_spdxId" ON "VexFixedVulnAssessmentRelationship_to" ("VexFixedVulnAssessmentRelationship_spdxId");
CREATE INDEX "ix_VexFixedVulnAssessmentRelationship_to_to_spdxId" ON "VexFixedVulnAssessmentRelationship_to" ("to_spdxId");

CREATE TABLE "VexNotAffectedVulnAssessmentRelationship_to" (
	"VexNotAffectedVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("VexNotAffectedVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("VexNotAffectedVulnAssessmentRelationship_spdxId") REFERENCES "VexNotAffectedVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_to_VexNotAffectedVulnAssessmentRelationship_spdxId" ON "VexNotAffectedVulnAssessmentRelationship_to" ("VexNotAffectedVulnAssessmentRelationship_spdxId");
CREATE INDEX "ix_VexNotAffectedVulnAssessmentRelationship_to_to_spdxId" ON "VexNotAffectedVulnAssessmentRelationship_to" ("to_spdxId");

CREATE TABLE "VexUnderInvestigationVulnAssessmentRelationship_to" (
	"VexUnderInvestigationVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("VexUnderInvestigationVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("VexUnderInvestigationVulnAssessmentRelationship_spdxId") REFERENCES "VexUnderInvestigationVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_to_to_spdxId" ON "VexUnderInvestigationVulnAssessmentRelationship_to" ("to_spdxId");
CREATE INDEX "ix_VexUnderInvestigationVulnAssessmentRelationship_to_VexUnderInvestigationVulnAssessmentRelationship_spdxId" ON "VexUnderInvestigationVulnAssessmentRelationship_to" ("VexUnderInvestigationVulnAssessmentRelationship_spdxId");

CREATE TABLE "VexVulnAssessmentRelationship_to" (
	"VexVulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("VexVulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("VexVulnAssessmentRelationship_spdxId") REFERENCES "VexVulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_VexVulnAssessmentRelationship_to_to_spdxId" ON "VexVulnAssessmentRelationship_to" ("to_spdxId");
CREATE INDEX "ix_VexVulnAssessmentRelationship_to_VexVulnAssessmentRelationship_spdxId" ON "VexVulnAssessmentRelationship_to" ("VexVulnAssessmentRelationship_spdxId");

CREATE TABLE "VulnAssessmentRelationship_to" (
	"VulnAssessmentRelationship_spdxId" TEXT,
	"to_spdxId" TEXT NOT NULL,
	PRIMARY KEY ("VulnAssessmentRelationship_spdxId", "to_spdxId"),
	FOREIGN KEY("VulnAssessmentRelationship_spdxId") REFERENCES "VulnAssessmentRelationship" ("spdxId"),
	FOREIGN KEY("to_spdxId") REFERENCES "Element" ("spdxId")
);
CREATE INDEX "ix_VulnAssessmentRelationship_to_VulnAssessmentRelationship_spdxId" ON "VulnAssessmentRelationship_to" ("VulnAssessmentRelationship_spdxId");
CREATE INDEX "ix_VulnAssessmentRelationship_to_to_spdxId" ON "VulnAssessmentRelationship_to" ("to_spdxId");

CREATE TABLE "ExternalIdentifier_identifierLocator" (
	"ExternalIdentifier_id" INTEGER,
	"identifierLocator" TEXT,
	PRIMARY KEY ("ExternalIdentifier_id", "identifierLocator"),
	FOREIGN KEY("ExternalIdentifier_id") REFERENCES "ExternalIdentifier" (id)
);
CREATE INDEX "ix_ExternalIdentifier_identifierLocator_identifierLocator" ON "ExternalIdentifier_identifierLocator" ("identifierLocator");
CREATE INDEX "ix_ExternalIdentifier_identifierLocator_ExternalIdentifier_id" ON "ExternalIdentifier_identifierLocator" ("ExternalIdentifier_id");

CREATE TABLE "ExternalRef_locator" (
	"ExternalRef_id" INTEGER,
	locator TEXT,
	PRIMARY KEY ("ExternalRef_id", locator),
	FOREIGN KEY("ExternalRef_id") REFERENCES "ExternalRef" (id)
);
CREATE INDEX "ix_ExternalRef_locator_ExternalRef_id" ON "ExternalRef_locator" ("ExternalRef_id");
CREATE INDEX "ix_ExternalRef_locator_locator" ON "ExternalRef_locator" (locator);
