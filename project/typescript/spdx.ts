/**
* Specifies the unit of energy consumption.
*/
export enum EnergyUnitType {
    
    /** Kilowatt-hour. */
    kilowattHour = "kilowattHour",
    /** Megajoule. */
    megajoule = "megajoule",
    /** Any other units of energy measurement. */
    other = "other",
};
/**
* Specifies the safety risk level.
*/
export enum SafetyRiskAssessmentType {
    
    /** The second-highest level of risk posed by an AI system. */
    high = "high",
    /** Low/no risk is posed by an AI system. */
    low = "low",
    /** The third-highest level of risk posed by an AI system. */
    medium = "medium",
    /** The highest level of risk posed by an AI system. */
    serious = "serious",
};
/**
* Specifies the type of an annotation.
*/
export enum AnnotationType {
    
    /** Used to store extra information about an Element which is not part of a review (e.g. extra information provided during the creation of the Element). */
    other = "other",
    /** Used when someone reviews the Element. */
    review = "review",
};
/**
* Specifies the type of an external identifier.
*/
export enum ExternalIdentifierType {
    
    /** [Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf) */
    cpe22 = "cpe22",
    /** [Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final) */
    cpe23 = "cpe23",
    /** Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id). */
    cve = "cve",
    /** Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3986/) Section 3. */
    email = "email",
    /** [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg). */
    gitoid = "gitoid",
    /** Used when the type does not match any of the other options. */
    other = "other",
    /** Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this specification. */
    packageUrl = "packageUrl",
    /** Used when there is a security related identifier of unspecified type. */
    securityOther = "securityOther",
    /** SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`. */
    swhid = "swhid",
    /** Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3. */
    swid = "swid",
    /** [Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource. */
    urlScheme = "urlScheme",
};
/**
* Specifies the type of an external reference.
*/
export enum ExternalRefType {
    
    /** A reference to an alternative download location. */
    altDownloadLocation = "altDownloadLocation",
    /** A reference to an alternative web page. */
    altWebPage = "altWebPage",
    /** A reference to binary artifacts related to a package. */
    binaryArtifact = "binaryArtifact",
    /** A reference to a Bower package. The package locator format, looks like `package#version`, is defined in the "install" section of [Bower API documentation](https://bower.io/docs/api/#install). */
    bower = "bower",
    /** A reference build metadata related to a published package. */
    buildMeta = "buildMeta",
    /** A reference build system used to create or publish the package. */
    buildSystem = "buildSystem",
    /** A reference to a certification report for a package from an accredited/independent body. */
    certificationReport = "certificationReport",
    /** A reference to the instant messaging system used by the maintainer for a package. */
    chat = "chat",
    /** A reference to a Software Composition Analysis (SCA) report. */
    componentAnalysisReport = "componentAnalysisReport",
    /** [Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/). */
    cwe = "cwe",
    /** A reference to the documentation for a package. */
    documentation = "documentation",
    /** A reference to a dynamic analysis report for a package. */
    dynamicAnalysisReport = "dynamicAnalysisReport",
    /** A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package. */
    eolNotice = "eolNotice",
    /** A reference to a export control assessment for a package. */
    exportControlAssessment = "exportControlAssessment",
    /** A reference to funding information related to a package. */
    funding = "funding",
    /** A reference to the issue tracker for a package. */
    issueTracker = "issueTracker",
    /** A reference to additional license information related to an artifact. */
    license = "license",
    /** A reference to the mailing list used by the maintainer for a package. */
    mailingList = "mailingList",
    /** A reference to a Maven repository artifact. The artifact locator format is defined in the [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html) and looks like `groupId:artifactId[:version]`. */
    mavenCentral = "mavenCentral",
    /** A reference to metrics related to package such as OpenSSF scorecards. */
    metrics = "metrics",
    /** A reference to an npm package. The package locator format is defined in the [npm documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and looks like `package@version`. */
    npm = "npm",
    /** A reference to a NuGet package. The package locator format is defined in the [NuGet documentation](https://docs.nuget.org) and looks like `package/version`. */
    nuget = "nuget",
    /** Used when the type does not match any of the other options. */
    other = "other",
    /** A reference to a privacy assessment for a package. */
    privacyAssessment = "privacyAssessment",
    /** A reference to additional product metadata such as reference within organization's product catalog. */
    productMetadata = "productMetadata",
    /** A reference to a purchase order for a package. */
    purchaseOrder = "purchaseOrder",
    /** A reference to a quality assessment for a package. */
    qualityAssessmentReport = "qualityAssessmentReport",
    /** A reference to a published list of releases for a package. */
    releaseHistory = "releaseHistory",
    /** A reference to the release notes for a package. */
    releaseNotes = "releaseNotes",
    /** A reference to a risk assessment for a package. */
    riskAssessment = "riskAssessment",
    /** A reference to a runtime analysis report for a package. */
    runtimeAnalysisReport = "runtimeAnalysisReport",
    /** A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form). */
    secureSoftwareAttestation = "secureSoftwareAttestation",
    /** A reference to the security adversary model for a package. */
    securityAdversaryModel = "securityAdversaryModel",
    /** A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries. */
    securityAdvisory = "securityAdvisory",
    /** A reference to the patch or source code that fixes a vulnerability. */
    securityFix = "securityFix",
    /** A reference to related security information of unspecified type. */
    securityOther = "securityOther",
    /** A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package. */
    securityPenTestReport = "securityPenTestReport",
    /** A reference to instructions for reporting newly discovered security vulnerabilities for a package. */
    securityPolicy = "securityPolicy",
    /** A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package. */
    securityThreatModel = "securityThreatModel",
    /** A reference to a social media channel for a package. */
    socialMedia = "socialMedia",
    /** A reference to an artifact containing the sources for a package. */
    sourceArtifact = "sourceArtifact",
    /** A reference to a static analysis report for a package. */
    staticAnalysisReport = "staticAnalysisReport",
    /** A reference to the software support channel or other support information for a package. */
    support = "support",
    /** A reference to a version control system related to a software artifact. */
    vcs = "vcs",
    /** A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/final). */
    vulnerabilityDisclosureReport = "vulnerabilityDisclosureReport",
    /** A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf). */
    vulnerabilityExploitabilityAssessment = "vulnerabilityExploitabilityAssessment",
};
/**
* A mathematical algorithm that maps data of arbitrary size to a bit string.
*/
export enum HashAlgorithm {
    
    /** Adler-32 checksum is part of the widely used zlib compression library as defined in [RFC 1950](https://datatracker.ietf.org/doc/rfc1950/) Section 2.3. */
    adler32 = "adler32",
    /** BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4. */
    blake2b256 = "blake2b256",
    /** BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4. */
    blake2b384 = "blake2b384",
    /** BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4. */
    blake2b512 = "blake2b512",
    /** [BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf) */
    blake3 = "blake3",
    /** [Dilithium](https://pq-crystals.org/dilithium/) */
    crystalsDilithium = "crystalsDilithium",
    /** [Kyber](https://pq-crystals.org/kyber/) */
    crystalsKyber = "crystalsKyber",
    /** [FALCON](https://falcon-sign.info/falcon.pdf) */
    falcon = "falcon",
    /** MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/). */
    md2 = "md2",
    /** MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/). */
    md4 = "md4",
    /** MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/). */
    md5 = "md5",
    /** [MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf) */
    md6 = "md6",
    /** any hashing algorithm that does not exist in this list of entries */
    other = "other",
    /** SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/). */
    sha1 = "sha1",
    /** SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/). */
    sha224 = "sha224",
    /** SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/). */
    sha256 = "sha256",
    /** SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/). */
    sha384 = "sha384",
    /** SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final). */
    sha3_224 = "sha3_224",
    /** SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final). */
    sha3_256 = "sha3_256",
    /** SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final). */
    sha3_384 = "sha3_384",
    /** SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final). */
    sha3_512 = "sha3_512",
    /** SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/). */
    sha512 = "sha512",
};
/**
* Provide an enumerated set of lifecycle phases that can provide context to relationships.
*/
export enum LifecycleScopeType {
    
    /** A relationship has specific context implications during an element's build phase, during development. */
    build = "build",
    /** A relationship has specific context implications during an element's design. */
    design = "design",
    /** A relationship has specific context implications during development phase of an element. */
    development = "development",
    /** A relationship has other specific context information necessary to capture that the above set of enumerations does not handle. */
    other = "other",
    /** A relationship has specific context implications during the execution phase of an element. */
    runtime = "runtime",
    /** A relationship has specific context implications during an element's testing phase, during development. */
    test = "test",
};
/**
* Categories of presence or absence.
*/
export enum PresenceType {
    
    /** Indicates absence of the field. */
    no = "no",
    /** Makes no assertion about the field. */
    noAssertion = "noAssertion",
    /** Indicates presence of the field. */
    yes = "yes",
};
/**
* Enumeration of the valid profiles.
*/
export enum ProfileIdentifierType {
    
    /** the element follows the AI profile specification */
    ai = "ai",
    /** the element follows the Build profile specification */
    build = "build",
    /** the element follows the Core profile specification */
    core = "core",
    /** the element follows the Dataset profile specification */
    dataset = "dataset",
    /** the element follows the ExpandedLicensing profile specification */
    expandedLicensing = "expandedLicensing",
    /** the element follows the Extension profile specification */
    extension = "extension",
    /** the element follows the Lite profile specification */
    lite = "lite",
    /** the element follows the Security profile specification */
    security = "security",
    /** the element follows the SimpleLicensing profile specification */
    simpleLicensing = "simpleLicensing",
    /** the element follows the Software profile specification */
    software = "software",
};
/**
* Indicates whether a relationship is known to be complete, incomplete, or if no assertion is made with respect to relationship completeness.
*/
export enum RelationshipCompleteness {
    
    /** The relationship is known to be exhaustive. */
    complete = "complete",
    /** The relationship is known not to be exhaustive. */
    incomplete = "incomplete",
    /** No assertion can be made about the completeness of the relationship. */
    noAssertion = "noAssertion",
};
/**
* Information about the relationship between two Elements.
*/
export enum RelationshipType {
    
    /** The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships. */
    affects = "affects",
    /** The `from` Element is amended by each `to` Element. */
    amendedBy = "amendedBy",
    /** The `from` Element is an ancestor of each `to` Element. */
    ancestorOf = "ancestorOf",
    /** The `from` Element is available from the additional supplier described by each `to` Element. */
    availableFrom = "availableFrom",
    /** The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period. */
    configures = "configures",
    /** The `from` Element contains each `to` Element. */
    contains = "contains",
    /** The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent). */
    coordinatedBy = "coordinatedBy",
    /** The `from` Element has been copied to each `to` Element. */
    copiedTo = "copiedTo",
    /** The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`). */
    delegatedTo = "delegatedTo",
    /** The `from` Element depends on each `to` Element, during a LifecycleScopeType period. */
    dependsOn = "dependsOn",
    /** The `from` Element is a descendant of each `to` Element. */
    descendantOf = "descendantOf",
    /** The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used. */
    describes = "describes",
    /** The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships. */
    doesNotAffect = "doesNotAffect",
    /** The `from` archive expands out as an artifact described by each `to` Element. */
    expandsTo = "expandsTo",
    /** The `from` Vulnerability has had an exploit created against it by each `to` Agent. */
    exploitCreatedBy = "exploitCreatedBy",
    /** Designates a `from` Vulnerability has been fixed by the `to` Agent(s). */
    fixedBy = "fixedBy",
    /** A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships. */
    fixedIn = "fixedIn",
    /** Designates a `from` Vulnerability was originally discovered by the `to` Agent(s). */
    foundBy = "foundBy",
    /** The `from` Element generates each `to` Element. */
    generates = "generates",
    /** Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`). */
    hasAddedFile = "hasAddedFile",
    /** Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types. */
    hasAssessmentFor = "hasAssessmentFor",
    /** Used to associate a `from` Artifact with each `to` Vulnerability. */
    hasAssociatedVulnerability = "hasAssociatedVulnerability",
    /** The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license. */
    hasConcludedLicense = "hasConcludedLicense",
    /** The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup file, and more. For AI training dataset, test dataset, test artifact, configuration data, build input data, and build output data, please consider using the more specific relationship types: `trainedOn`, `testedOn`, `hasTest`, `configures`, `hasInput`, and `hasOutput`, respectively. This relationship does not imply dependency. */
    hasDataFile = "hasDataFile",
    /** The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling. */
    hasDeclaredLicense = "hasDeclaredLicense",
    /** Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`). */
    hasDeletedFile = "hasDeletedFile",
    /** The `from` Element has manifest files that contain dependency information in each `to` Element. */
    hasDependencyManifest = "hasDependencyManifest",
    /** The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file). */
    hasDistributionArtifact = "hasDistributionArtifact",
    /** The `from` Element is documented by each `to` Element. */
    hasDocumentation = "hasDocumentation",
    /** The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period. */
    hasDynamicLink = "hasDynamicLink",
    /** Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`). */
    hasEvidence = "hasEvidence",
    /** Every `to` Element is an example for the `from` Element (`from` hasExample `to`). */
    hasExample = "hasExample",
    /** The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on). */
    hasHost = "hasHost",
    /** The `from` Build has each `to` Element as an input, during a LifecycleScopeType period. */
    hasInput = "hasInput",
    /** Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`). */
    hasMetadata = "hasMetadata",
    /** Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`). */
    hasOptionalComponent = "hasOptionalComponent",
    /** The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period. */
    hasOptionalDependency = "hasOptionalDependency",
    /** The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period. */
    hasOutput = "hasOutput",
    /** The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period. */
    hasPrerequisite = "hasPrerequisite",
    /** The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period. */
    hasProvidedDependency = "hasProvidedDependency",
    /** The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period. */
    hasRequirement = "hasRequirement",
    /** Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period. */
    hasSpecification = "hasSpecification",
    /** The `from` Element statically links in each `to` Element, during a LifecycleScopeType period. */
    hasStaticLink = "hasStaticLink",
    /** Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period. */
    hasTest = "hasTest",
    /** Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`). */
    hasTestCase = "hasTestCase",
    /** Every `to` Element is a variant the `from` Element (`from` hasVariant `to`). */
    hasVariant = "hasVariant",
    /** The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step). */
    invokedBy = "invokedBy",
    /** The `from` Element is modified by each `to` Element. */
    modifiedBy = "modifiedBy",
    /** Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless). */
    other = "other",
    /** Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`). */
    packagedBy = "packagedBy",
    /** Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`). */
    patchedBy = "patchedBy",
    /** Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent. */
    publishedBy = "publishedBy",
    /** Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent. */
    reportedBy = "reportedBy",
    /** Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent. */
    republishedBy = "republishedBy",
    /** The `from` SpdxDocument can be found in a serialized form in each `to` Artifact. */
    serializedInArtifact = "serializedInArtifact",
    /** The `from` Element has been tested on the `to` Element(s). */
    testedOn = "testedOn",
    /** The `from` Element has been trained on the `to` Element(s). */
    trainedOn = "trainedOn",
    /** The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships. */
    underInvestigationFor = "underInvestigationFor",
    /** The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period. */
    usesTool = "usesTool",
};
/**
* Indicates the type of support that is associated with an artifact.
*/
export enum SupportType {
    
    /** in addition to being supported by the supplier, the software is known to have been deployed and is in use.  For a software as a service provider, this implies the software is now available as a service. */
    deployed = "deployed",
    /** the artifact is in active development and is not considered ready for formal support from the supplier. */
    development = "development",
    /** there is a defined end of support for the artifact from the supplier.  This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact. */
    endOfSupport = "endOfSupport",
    /** the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support. */
    limitedSupport = "limitedSupport",
    /** no assertion about the type of support is made.   This is considered the default if no other support type is used. */
    noAssertion = "noAssertion",
    /** there is no support for the artifact from the supplier, consumer assumes any support obligations. */
    noSupport = "noSupport",
    /** the artifact has been released, and is supported from the supplier.   There is a validUntilDate that can provide additional information about the duration of support. */
    support = "support",
};
/**
* Categories of confidentiality level.
*/
export enum ConfidentialityLevelType {
    
    /** Data points in the dataset can be shared only with specific organizations and their clients on a need to know basis. */
    amber = "amber",
    /** Dataset may be distributed freely, without restriction. */
    clear = "clear",
    /** Dataset can be shared within a community of peers and partners. */
    green = "green",
    /** Data points in the dataset are highly confidential and can only be shared with named recipients. */
    red = "red",
};
/**
* Availability of dataset.
*/
export enum DatasetAvailabilityType {
    
    /** the dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage. */
    clickthrough = "clickthrough",
    /** the dataset is publicly available and can be downloaded directly. */
    directDownload = "directDownload",
    /** the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset. */
    query = "query",
    /** the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms. */
    registration = "registration",
    /** the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data. */
    scrapingScript = "scrapingScript",
};
/**
* Enumeration of dataset types.
*/
export enum DatasetType {
    
    /** data is audio based, such as a collection of music from the 80s. */
    audio = "audio",
    /** data that is classified into a discrete number of categories, such as the eye color of a population of people. */
    categorical = "categorical",
    /** data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends. */
    graph = "graph",
    /** data is a collection of images such as pictures of animals. */
    image = "image",
    /** data type is not known. */
    noAssertion = "noAssertion",
    /** data consists only of numeric entries. */
    numeric = "numeric",
    /** data is of a type not included in this list. */
    other = "other",
    /** data is recorded from a physical sensor, such as a thermometer reading or biometric device. */
    sensor = "sensor",
    /** data is stored in tabular format or retrieved from a relational database. */
    structured = "structured",
    /** data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing. */
    syntactic = "syntactic",
    /** data consists of unstructured text, such as a book, Wikipedia article (without images), or transcript. */
    text = "text",
    /** data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day. */
    timeseries = "timeseries",
    /** data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends. */
    timestamp = "timestamp",
    /** data is video based, such as a collection of movie clips featuring Tom Hanks. */
    video = "video",
};
/**
* Specifies the CVSS base, temporal, threat, or environmental severity type.
*/
export enum CvssSeverityType {
    
    /** When a CVSS score is between 9.0 - 10.0 */
    critical = "critical",
    /** When a CVSS score is between 7.0 - 8.9 */
    high = "high",
    /** When a CVSS score is between 0.1 - 3.9 */
    low = "low",
    /** When a CVSS score is between 4.0 - 6.9 */
    medium = "medium",
    /** When a CVSS score is 0.0 */
    none = "none",
};
/**
* Specifies the exploit catalog type.
*/
export enum ExploitCatalogType {
    
    /** CISA's Known Exploited Vulnerability (KEV) Catalog */
    kev = "kev",
    /** Other exploit catalogs */
    other = "other",
};
/**
* Specifies the SSVC decision type.
*/
export enum SsvcDecisionType {
    
    /** The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. Typically, internal groups would meet to determine the overall response and then execute agreed upon actions. CISA recommends remediating Act vulnerabilities as soon as possible. */
    act = "act",
    /** The vulnerability requires attention from the organization's internal, supervisory-level individuals. Necessary actions include requesting assistance or information about the vulnerability, and may involve publishing a notification either internally and/or externally. CISA recommends remediating Attend vulnerabilities sooner than standard update timelines. */
    attend = "attend",
    /** The vulnerability does not require action at this time. The organization would continue to track the vulnerability and reassess it if new information becomes available. CISA recommends remediating Track vulnerabilities within standard update timelines. */
    track = "track",
    /** ("Track\*" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track\* vulnerabilities within standard update timelines. */
    trackStar = "trackStar",
};
/**
* Specifies the VEX justification type.
*/
export enum VexJustificationType {
    
    /** The software is not affected because the vulnerable component is not in the product. */
    componentNotPresent = "componentNotPresent",
    /** Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability. */
    inlineMitigationsAlreadyExist = "inlineMitigationsAlreadyExist",
    /** The vulnerable component is present, and the component contains the vulnerable code. However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack. */
    vulnerableCodeCannotBeControlledByAdversary = "vulnerableCodeCannotBeControlledByAdversary",
    /** The affected code is not reachable through the execution of the code, including non-anticipated states of the product. */
    vulnerableCodeNotInExecutePath = "vulnerableCodeNotInExecutePath",
    /** The product is not affected because the code underlying the vulnerability is not present in the product. */
    vulnerableCodeNotPresent = "vulnerableCodeNotPresent",
};
/**
* Specifies the type of a content identifier.
*/
export enum ContentIdentifierType {
    
    /** [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg). */
    gitoid = "gitoid",
    /** SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`. */
    swhid = "swhid",
};
/**
* Enumeration of the different kinds of SPDX file.
*/
export enum FileKindType {
    
    /** The file represents a directory and all content stored in that directory. */
    directory = "directory",
    /** The file represents a single file (default). */
    file = "file",
};
/**
* Provides a set of values to be used to describe the common types of SBOMs that
tools may create.
*/
export enum SbomType {
    
    /** SBOM generated through analysis of artifacts (e.g., executables, packages, containers, and virtual machine images) after its build. Such analysis generally requires a variety of heuristics. In some contexts, this may also be referred to as a "3rd party" SBOM. */
    analyzed = "analyzed",
    /** SBOM generated as part of the process of building the software to create a releasable artifact (e.g., executable or package) from data such as source files, dependencies, built components, build process ephemeral data, and other SBOMs. */
    build = "build",
    /** SBOM provides an inventory of software that is present on a system. This may be an assembly of other SBOMs that combines analysis of configuration options, and examination of execution behavior in a (potentially simulated) deployment environment. */
    deployed = "deployed",
    /** SBOM of intended, planned software project or product with included components (some of which may not yet exist) for a new software artifact. */
    design = "design",
    /** SBOM generated through instrumenting the system running the software, to capture only components present in the system, as well as external call-outs or dynamically loaded components. In some contexts, this may also be referred to as an "Instrumented" or "Dynamic" SBOM. */
    runtime = "runtime",
    /** SBOM created directly from the development environment, source files, and included dependencies used to build an product artifact. */
    source = "source",
};
/**
* Provides information about the primary purpose of an Element.
*/
export enum SoftwarePurpose {
    
    /** The Element is a software application. */
    application = "application",
    /** The Element is an archived collection of one or more files (.tar, .zip, etc.). */
    archive = "archive",
    /** The Element is a bill of materials. */
    bom = "bom",
    /** The Element is configuration data. */
    configuration = "configuration",
    /** The Element is a container image which can be used by a container runtime application. */
    container = "container",
    /** The Element is data. */
    data = "data",
    /** The Element refers to a chipset, processor, or electronic board. */
    device = "device",
    /** The Element represents software that controls hardware devices. */
    deviceDriver = "deviceDriver",
    /** The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc. */
    diskImage = "diskImage",
    /** The Element is documentation. */
    documentation = "documentation",
    /** The Element is the evidence that a specification or requirement has been fulfilled. */
    evidence = "evidence",
    /** The Element is an Artifact that can be run on a computer. */
    executable = "executable",
    /** The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.). */
    file = "file",
    /** The Element is a file system image that can be written to a disk (or virtual) partition. */
    filesystemImage = "filesystemImage",
    /** The Element provides low level control over a device's hardware. */
    firmware = "firmware",
    /** The Element is a software framework. */
    framework = "framework",
    /** The Element is used to install software on disk. */
    install = "install",
    /** The Element is a software library. */
    library = "library",
    /** The Element is a software manifest. */
    manifest = "manifest",
    /** The Element is a machine learning or artificial intelligence model. */
    model = "model",
    /** The Element is a module of a piece of software. */
    module = "module",
    /** The Element is an operating system. */
    operatingSystem = "operatingSystem",
    /** The Element doesn't fit into any of the other categories. */
    other = "other",
    /** The Element contains a set of changes to update, fix, or improve another Element. */
    patch = "patch",
    /** The Element represents a runtime environment. */
    platform = "platform",
    /** The Element provides a requirement needed as input for another Element. */
    requirement = "requirement",
    /** The Element is a single or a collection of source files. */
    source = "source",
    /** The Element is a plan, guideline or strategy how to create, perform or analyze an application. */
    specification = "specification",
    /** The Element is a test used to verify functionality on an software element. */
    test = "test",
};


/**
 * Specifies an AI package and its associated information.
 */
export interface AIPackage extends Package {
    /** Describes relevant information about different steps of the training process. */
    informationAboutTraining?: string,
    /** Describes all the preprocessing steps applied to the training data before the
model training. */
    modelDataPreprocessing?: string[],
    /** Records the type of the model used in the AI software. */
    typeOfModel?: string[],
    /** Records the results of general safety risk assessment of the AI system. */
    safetyRiskAssessment?: string,
    /** Captures the threshold that was used for computation of a metric described in
the metric field. */
    metricDecisionThreshold?: DictionaryEntry[],
    /** Records if sensitive personal information is used during model training or
could be used during the inference. */
    useSensitivePersonalInformation?: string,
    /** Indicates the amount of energy consumption incurred by an AI model. */
    energyConsumption?: EnergyConsumption,
    /** Captures a limitation of the AI software. */
    limitation?: string,
    /** Records a hyperparameter used to build the AI model contained in the AI
package. */
    hyperparameter?: DictionaryEntry[],
    /** Indicates whether the system can perform a decision or action without human
involvement or guidance. */
    autonomyType?: string,
    /** Captures the domain in which the AI package can be used. */
    domain?: string[],
    /** Describes methods that can be used to explain the results from the AI model. */
    modelExplainability?: string[],
    /** Provides relevant information about the AI software, not including the model
description. */
    informationAboutApplication?: string,
    /** Records the measurement of prediction quality of the AI model. */
    metric?: DictionaryEntry[],
    /** Captures a standard that is being complied with. */
    standardCompliance?: string[],
}


/**
 * A class for describing the energy consumption incurred by an AI model in
different stages of its lifecycle.
 */
export interface EnergyConsumption {
    /** Specifies the amount of energy consumed when finetuning the AI model that is
being used in the AI system. */
    finetuningEnergyConsumption?: EnergyConsumptionDescription[],
    /** Specifies the amount of energy consumed during inference time by an AI model
that is being used in the AI system. */
    inferenceEnergyConsumption?: EnergyConsumptionDescription[],
    /** Specifies the amount of energy consumed when training the AI model that is
being used in the AI system. */
    trainingEnergyConsumption?: EnergyConsumptionDescription[],
}


/**
 * The class that helps note down the quantity of energy consumption and the unit
used for measurement.
 */
export interface EnergyConsumptionDescription {
    /** Represents the energy quantity. */
    energyQuantity: string,
    /** Specifies the unit in which energy is measured. */
    energyUnit: string,
}


/**
 * Class that describes a build instance of software/artifacts.
 */
export interface Build extends Element {
    /** A buildType is a hint that is used to indicate the toolchain, platform, or
infrastructure that the build was invoked on. */
    buildType: string,
    /** Property that describes the time at which a build stops. */
    buildEndTime?: string,
    /** A buildId is a locally unique identifier used by a builder to identify a unique
instance of a build produced by it. */
    buildId?: string,
    /** Property that describes the digest of the build configuration file used to
invoke a build. */
    configSourceDigest?: Hash[],
    /** Property describing the start time of a build. */
    buildStartTime?: string,
    /** Property that describes the URI of the build configuration source file. */
    configSourceUri?: string[],
    /** Property describing a parameter used in an instance of a build. */
    parameter?: DictionaryEntry[],
    /** Property describes the invocation entrypoint of a build. */
    configSourceEntrypoint?: string[],
    /** Property describing the session in which a build is invoked. */
    environment?: DictionaryEntry[],
}


/**
 * Agent represents anything with the potential to act on a system.
 */
export interface Agent extends Element {
}


/**
 * An assertion made in relation to one or more elements.
 */
export interface Annotation extends Element {
    /** Provides information about the content type of an Element or a Property. */
    contentType?: string,
    /** Commentary on an assertion that an annotator has made. */
    statement?: string,
    /** An Element an annotator has made an assertion about. */
    subject: Element,
    /** Describes the type of annotation. */
    annotationType: string,
}


/**
 * A distinct article or unit within the digital domain.
 */
export interface Artifact extends Element {
    /** The name of a relevant standard that may apply to an artifact. */
    standardName?: string[],
    /** Specifies the time an artifact was built. */
    builtTime?: string,
    /** Specifies until when the artifact can be used before its usage needs to be
reassessed. */
    validUntilTime?: string,
    /** Specifies the level of support associated with an artifact. */
    supportLevel?: string,
    /** Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element. */
    suppliedBy?: Agent,
    /** Identifies from where or whom the Element originally came. */
    originatedBy?: Agent[],
    /** Specifies the time an artifact was released. */
    releaseTime?: string,
}


/**
 * A container for a grouping of SPDX-3.0 content characterizing details
(provenence, composition, licensing, etc.) about a product.
 */
export interface Bom extends Bundle {
}


/**
 * A collection of Elements that have a shared context.
 */
export interface Bundle extends ElementCollection {
    /** Gives information about the circumstances or unifying properties
that Elements of the bundle have been assembled under. */
    context?: string,
}


/**
 * Provides information about the creation of the Element.
 */
export interface CreationInfo {
    /** Identifies who or what created the Element. */
    createdBy: Agent[],
    /** Identifies the tooling that was used during the creation of the Element. */
    createdUsing?: Tool[],
    /** Identifies when the Element was originally created. */
    created: string,
    /** Provides a reference number that can be used to understand how to parse and
interpret an Element. */
    specVersion: string,
    /** Provide consumers with comments by the creator of the Element about the
Element. */
    comment?: string,
}


/**
 * A key with an associated value.
 */
export interface DictionaryEntry {
    /** A value used in a generic key-value pair. */
    value?: string,
    /** A key used in a generic key-value pair. */
    key: string,
}


/**
 * Base domain class from which all other SPDX-3.0 domain classes derive.
 */
export interface Element {
    /** Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element. */
    externalIdentifier?: ExternalIdentifier[],
    /** Specifies an Extension characterization of some aspect of an Element. */
    extension?: Extension[],
    /** A short description of an Element. */
    summary?: string,
    /** Provides a detailed description of the Element. */
    description?: string,
    /** Provide consumers with comments by the creator of the Element about the
Element. */
    comment?: string,
    /** Provides an IntegrityMethod with which the integrity of an Element can be
asserted. */
    verifiedUsing?: IntegrityMethod[],
    /** Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element. */
    externalRef?: ExternalRef[],
    /** Identifies the name of an Element as designated by the creator. */
    name?: string,
    /** Provides information about the creation of the Element. */
    creationInfo: CreationInfo,
}


/**
 * A collection of Elements, not necessarily with unifying context.
 */
export interface ElementCollection extends Element {
    /** Refers to one or more Elements that are part of an ElementCollection. */
    element?: Element[],
    /** Describes one a profile which the creator of this ElementCollection intends to
conform to. */
    profileConformance?: string,
    /** This property is used to denote the root Element(s) of a tree of elements contained in a BOM. */
    rootElement?: Element[],
}


/**
 * A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
 */
export interface ExternalIdentifier {
    /** Provides the location for more information regarding an external identifier. */
    identifierLocator?: string[],
    /** Specifies the type of the external identifier. */
    externalIdentifierType: string,
    /** An entity that is authorized to issue identification credentials. */
    issuingAuthority?: string,
    /** Uniquely identifies an external element. */
    identifier: string,
    /** Provide consumers with comments by the creator of the Element about the
Element. */
    comment?: string,
}


/**
 * A map of Element identifiers that are used within an SpdxDocument but defined
external to that SpdxDocument.
 */
export interface ExternalMap {
    /** Artifact representing a serialization instance of SPDX data containing the
definition of a particular Element. */
    definingArtifact?: Artifact,
    /** Provides an indication of where to retrieve an external Element. */
    locationHint?: string,
    /** Identifies an external Element used within an SpdxDocument but defined
external to that SpdxDocument. */
    externalSpdxId: string,
    /** Provides an IntegrityMethod with which the integrity of an Element can be
asserted. */
    verifiedUsing?: IntegrityMethod[],
}


/**
 * A reference to a resource outside the scope of SPDX-3.0 content related to an Element.
 */
export interface ExternalRef {
    /** Provides the location of an external reference. */
    core_locator?: string[],
    /** Specifies the type of the external reference. */
    externalRefType?: string,
    /** Provide consumers with comments by the creator of the Element about the
Element. */
    comment?: string,
    /** Provides information about the content type of an Element or a Property. */
    contentType?: string,
}


/**
 * A mathematically calculated representation of a grouping of data.
 */
export interface Hash extends IntegrityMethod {
    /** Specifies the algorithm used for calculating the hash value. */
    algorithm: string,
    /** The result of applying a hash algorithm to an Element. */
    hashValue: string,
}


/**
 * A concrete subclass of Element used by Individuals in the
Core profile.
 */
export interface IndividualElement extends Element {
}


/**
 * Provides an independently reproducible mechanism that permits verification of a specific Element.
 */
export interface IntegrityMethod {
    /** Provide consumers with comments by the creator of the Element about the
Element. */
    comment?: string,
}


/**
 * Provide context for a relationship that occurs in the lifecycle.
 */
export interface LifecycleScopedRelationship extends Relationship {
    /** Capture the scope of information about a specific relationship between elements. */
    scope?: string,
}


/**
 * A mapping between prefixes and namespace partial URIs.
 */
export interface NamespaceMap {
    /** A substitute for a URI. */
    prefix: string,
    /** Provides an unambiguous mechanism for conveying a URI fragment portion of an
Element ID. */
    namespace: string,
}


/**
 * A group of people who work together in an organized way for a shared purpose.
 */
export interface Organization extends Agent {
}


/**
 * An SPDX version 2.X compatible verification method for software packages.
 */
export interface PackageVerificationCode extends IntegrityMethod {
    /** The relative file name of a file to be excluded from the
`PackageVerificationCode`. */
    packageVerificationCodeExcludedFile?: string[],
    /** The result of applying a hash algorithm to an Element. */
    hashValue: string,
    /** Specifies the algorithm used for calculating the hash value. */
    algorithm: string,
}


/**
 * An individual human being.
 */
export interface Person extends Agent {
}


/**
 * A tuple of two positive integers that define a range.
 */
export interface PositiveIntegerRange {
    /** Defines the end of a range. */
    endIntegerRange: number,
    /** Defines the beginning of a range. */
    beginIntegerRange: number,
}


/**
 * Describes a relationship between one or more elements.
 */
export interface Relationship extends Element {
    /** References an Element on the right-hand side of a relationship. */
    to: Element[],
    /** Provides information about the completeness of relationships. */
    completeness?: string,
    /** Specifies the time from which an element is applicable / valid. */
    startTime?: string,
    /** Information about the relationship between two Elements. */
    relationshipType: string,
    /** References the Element on the left-hand side of a relationship. */
    from: Element,
    /** Specifies the time from which an element is no longer applicable / valid. */
    endTime?: string,
}


/**
 * A software agent.
 */
export interface SoftwareAgent extends Agent {
}


/**
 * A collection of SPDX Elements that could potentially be serialized.
 */
export interface SpdxDocument extends ElementCollection {
    /** Provides a NamespaceMap of prefixes and associated namespace partial URIs applicable to an SpdxDocument and independent of any specific serialization format or instance. */
    namespaceMap?: NamespaceMap[],
    /** Provides the license under which the SPDX documentation of the Element can be
used. */
    dataLicense?: AnyLicenseInfo,
    /** Provides an ExternalMap of Element identifiers. */
    import?: ExternalMap[],
}


/**
 * An element of hardware and/or software utilized to carry out a particular function.
 */
export interface Tool extends Element {
}


/**
 * Specifies a data package and its associated information.
 */
export interface DatasetPackage extends Package {
    /** Captures the size of the dataset. */
    datasetSize?: number,
    /** Describes the type of the given dataset. */
    datasetType: string[],
    /** Describes the anonymization methods used. */
    anonymizationMethodUsed?: string[],
    /** Describes a mechanism to update the dataset. */
    datasetUpdateMechanism?: string,
    /** Describes how the dataset was collected. */
    dataCollectionProcess?: string,
    /** Records the biases that the dataset is known to encompass. */
    knownBias?: string[],
    /** Describes a sensor used for collecting the data. */
    sensor?: DictionaryEntry[],
    /** Describes the preprocessing steps that were applied to the raw data to create the given dataset. */
    dataPreprocessing?: string[],
    /** Describes what the given dataset should be used for. */
    intendedUse?: string,
    /** Describes the confidentiality level of the data points contained in the dataset. */
    confidentialityLevel?: string,
    /** The field describes the availability of a dataset. */
    datasetAvailability?: string,
    /** Describes if any sensitive personal information is present in the dataset. */
    hasSensitivePersonalInformation?: string,
    /** Describes potentially noisy elements of the dataset. */
    datasetNoise?: string,
}


/**
 * Portion of an AnyLicenseInfo representing a set of licensing information
where all elements apply.
 */
export interface ConjunctiveLicenseSet extends AnyLicenseInfo {
    /** A license expression participating in a license set. */
    member: AnyLicenseInfo[],
}


/**
 * A license that is not listed on the SPDX License List.
 */
export interface CustomLicense extends License {
}


/**
 * A license addition that is not listed on the SPDX Exceptions List.
 */
export interface CustomLicenseAddition extends LicenseAddition {
}


/**
 * Portion of an AnyLicenseInfo representing a set of licensing information where
only one of the elements applies.
 */
export interface DisjunctiveLicenseSet extends AnyLicenseInfo {
    /** A license expression participating in a license set. */
    member: AnyLicenseInfo[],
}


/**
 * Abstract class representing a License or an OrLaterOperator.
 */
export interface ExtendableLicense extends AnyLicenseInfo {
}


/**
 * A concrete subclass of AnyLicenseInfo used by Individuals in the
ExpandedLicensing profile.
 */
export interface IndividualLicensingInfo extends AnyLicenseInfo {
}


/**
 * Abstract class for the portion of an AnyLicenseInfo representing a license.
 */
export interface License extends ExtendableLicense {
    /** Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition. */
    obsoletedBy?: string,
    /** Provides a License author's preferred text to indicate that a file is covered
by the License. */
    standardLicenseHeader?: string,
    /** Contains a URL where the License or LicenseAddition can be found in use. */
    seeAlso?: string[],
    /** Specifies whether the License is listed as free by the
Free Software Foundation (FSF). */
    isFsfLibre?: boolean,
    /** Specifies whether a license or additional text identifier has been marked as
deprecated. */
    isDeprecatedLicenseId?: boolean,
    /** Specifies whether the License is listed as approved by the
Open Source Initiative (OSI). */
    isOsiApproved?: boolean,
    /** Identifies all the text and metadata associated with a license in the license
XML format. */
    licenseXml?: string,
    /** Identifies the full text of a License or Addition. */
    licenseText: string,
    /** Identifies the full text of a License, in SPDX templating format. */
    standardLicenseTemplate?: string,
}


/**
 * Abstract class for additional text intended to be added to a License, but
which is not itself a standalone License.
 */
export interface LicenseAddition extends Element {
    /** Identifies the full text of a LicenseAddition, in SPDX templating format. */
    standardAdditionTemplate?: string,
    /** Contains a URL where the License or LicenseAddition can be found in use. */
    seeAlso?: string[],
    /** Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition. */
    obsoletedBy?: string,
    /** Identifies all the text and metadata associated with a license in the license
XML format. */
    licenseXml?: string,
    /** Specifies whether an additional text identifier has been marked as deprecated. */
    isDeprecatedAdditionId?: boolean,
    /** Identifies the full text of a LicenseAddition. */
    additionText: string,
}


/**
 * A license that is listed on the SPDX License List.
 */
export interface ListedLicense extends License {
    /** Specifies the SPDX License List version in which this license or exception
identifier was deprecated. */
    deprecatedVersion?: string,
    /** Specifies the SPDX License List version in which this ListedLicense or
ListedLicenseException identifier was first added. */
    listVersionAdded?: string,
}


/**
 * A license exception that is listed on the SPDX Exceptions list.
 */
export interface ListedLicenseException extends LicenseAddition {
    /** Specifies the SPDX License List version in which this ListedLicense or
ListedLicenseException identifier was first added. */
    listVersionAdded?: string,
    /** Specifies the SPDX License List version in which this license or exception
identifier was deprecated. */
    deprecatedVersion?: string,
}


/**
 * Portion of an AnyLicenseInfo representing this version, or any later version,
of the indicated License.
 */
export interface OrLaterOperator extends ExtendableLicense {
    /** A License participating in an 'or later' model. */
    subjectLicense: License,
}


/**
 * Portion of an AnyLicenseInfo representing a License which has additional
text applied to it.
 */
export interface WithAdditionOperator extends AnyLicenseInfo {
    /** A License participating in a 'with addition' model. */
    subjectExtendableLicense: ExtendableLicense,
    /** A LicenseAddition participating in a 'with addition' model. */
    subjectAddition: LicenseAddition,
}


/**
 * A type of extension consisting of a list of name value pairs.
 */
export interface CdxPropertiesExtension extends Extension {
    /** Provides a map of a property names to a values. */
    cdxProperty: CdxPropertyEntry[],
}


/**
 * A property name with an associated value.
 */
export interface CdxPropertyEntry {
    /** A value used in a CdxPropertyEntry name-value pair. */
    cdxPropValue?: string,
    /** A name used in a CdxPropertyEntry name-value pair. */
    cdxPropName: string,
}


/**
 * A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
 */
export interface Extension {
}


/**
 * Provides a CVSS version 2.0 assessment for a vulnerability.
 */
export interface CvssV2VulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** Specifies the CVSS vector string for a vulnerability. */
    vectorString: string,
    /** Provides a numerical (0-10) representation of the severity of a vulnerability. */
    score: string,
}


/**
 * Provides a CVSS version 3 assessment for a vulnerability.
 */
export interface CvssV3VulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software. */
    severity: string,
    /** Specifies the CVSS vector string for a vulnerability. */
    vectorString: string,
    /** Provides a numerical (0-10) representation of the severity of a vulnerability. */
    score: string,
}


/**
 * Provides a CVSS version 4 assessment for a vulnerability.
 */
export interface CvssV4VulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software. */
    severity: string,
    /** Specifies the CVSS vector string for a vulnerability. */
    vectorString: string,
    /** Provides a numerical (0-10) representation of the severity of a vulnerability. */
    score: string,
}


/**
 * Provides an EPSS assessment for a vulnerability.
 */
export interface EpssVulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** The percentile of the current probability score. */
    percentile: string,
    /** A probability score between 0 and 1 of a vulnerability being exploited. */
    probability: string,
}


/**
 * Provides an exploit assessment of a vulnerability.
 */
export interface ExploitCatalogVulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** Describe that a CVE is known to have an exploit because it's been listed in an exploit catalog. */
    exploited: boolean,
    /** Provides the location of an exploit catalog. */
    security_locator: string,
    /** Specifies the exploit catalog type. */
    catalogType: string,
}


/**
 * Provides an SSVC assessment for a vulnerability.
 */
export interface SsvcVulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** Provide the enumeration of possible decisions in the
[Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc). */
    decisionType: string,
}


/**
 * Connects a vulnerability and an element designating the element as a product
affected by the vulnerability.
 */
export interface VexAffectedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {
    /** Provides advise on how to mitigate or remediate a vulnerability when a VEX product
is affected by it. */
    actionStatement: string,
    /** Records the time when a recommended action was communicated in a VEX statement
to mitigate a vulnerability. */
    actionStatementTime?: string,
}


/**
 * Links a vulnerability and elements representing products (in the VEX sense) where
a fix has been applied and are no longer affected.
 */
export interface VexFixedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {
}


/**
 * Links a vulnerability and one or more elements designating the latter as products
not affected by the vulnerability.
 */
export interface VexNotAffectedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {
    /** Timestamp of impact statement. */
    impactStatementTime?: string,
    /** Impact justification label to be used when linking a vulnerability to an element
representing a VEX product with a VexNotAffectedVulnAssessmentRelationship
relationship. */
    justificationType?: string,
    /** Explains why a VEX product is not affected by a vulnerability. It is an
alternative in VexNotAffectedVulnAssessmentRelationship to the machine-readable
justification label. */
    impactStatement?: string,
}


/**
 * Designates elements as products where the impact of a vulnerability is being
investigated.
 */
export interface VexUnderInvestigationVulnAssessmentRelationship extends VexVulnAssessmentRelationship {
}


/**
 * Abstract ancestor class for all VEX relationships
 */
export interface VexVulnAssessmentRelationship extends VulnAssessmentRelationship {
    /** Specifies the version of a VEX statement. */
    vexVersion?: string,
    /** Conveys information about how VEX status was determined. */
    statusNotes?: string,
}


/**
 * Abstract ancestor class for all vulnerability assessments
 */
export interface VulnAssessmentRelationship extends Relationship {
    /** Specified the time and date when a vulnerability was withdrawn. */
    withdrawnTime?: string,
    /** Specifies the time when a vulnerability was published. */
    publishedTime?: string,
    /** Specifies an Element contained in a piece of software where a vulnerability was
found. */
    assessedElement?: SoftwareArtifact,
    /** Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element. */
    suppliedBy?: Agent,
    /** Specifies a time when a vulnerability assessment was modified */
    modifiedTime?: string,
}


/**
 * Specifies a vulnerability and its associated information.
 */
export interface Vulnerability extends Artifact {
    /** Specified the time and date when a vulnerability was withdrawn. */
    withdrawnTime?: string,
    /** Specifies a time when a vulnerability assessment was modified */
    modifiedTime?: string,
    /** Specifies the time when a vulnerability was published. */
    publishedTime?: string,
}


/**
 * Abstract class representing a license combination consisting of one or more licenses.
 */
export interface AnyLicenseInfo extends Element {
}


/**
 * An SPDX Element containing an SPDX license expression string.
 */
export interface LicenseExpression extends AnyLicenseInfo {
    /** Maps a LicenseRef or AdditionRef string for a Custom License or a Custom
License Addition to its URI ID. */
    customIdToUri?: DictionaryEntry[],
    /** A string in the license expression format. */
    licenseExpression: string,
    /** The version of the SPDX License List used in the license expression. */
    licenseListVersion?: string,
}


/**
 * A license or addition that is not listed on the SPDX License List.
 */
export interface SimpleLicensingText extends Element {
    /** Identifies the full text of a License or Addition. */
    licenseText: string,
}


/**
 * A canonical, unique, immutable identifier
 */
export interface ContentIdentifier extends IntegrityMethod {
    /** Specifies the value of the content identifier. */
    contentIdentifierValue: string,
    /** Specifies the type of the content identifier. */
    contentIdentifierType: string,
}


/**
 * Refers to any object that stores content on a computer.
 */
export interface File extends SoftwareArtifact {
    /** Describes if a given file is a directory or non-directory kind of file. */
    fileKind?: string,
    /** Provides information about the content type of an Element or a Property. */
    contentType?: string,
}


/**
 * Refers to any unit of content that can be associated with a distribution of
software.
 */
export interface Package extends SoftwareArtifact {
    /** Records any relevant background information or additional comments
about the origin of the package. */
    sourceInfo?: string,
    /** A place for the SPDX document creator to record a website that serves as the
package's home page. */
    homePage?: string,
    /** Identifies the download Uniform Resource Identifier for the package at the time
that the document was created. */
    downloadLocation?: string,
    /** Identify the version of a package. */
    packageVersion?: string,
    /** Provides a place for the SPDX data creator to record the package URL string
(in accordance with the Package URL specification) for a software Package. */
    packageUrl?: string,
}


/**
 * A collection of SPDX Elements describing a single package.
 */
export interface Sbom extends Bom {
    /** Provides information about the type of an SBOM. */
    sbomType?: string,
}


/**
 * Describes a certain part of a file.
 */
export interface Snippet extends SoftwareArtifact {
    /** Defines the line range in the original host file that the snippet information
applies to. */
    lineRange?: PositiveIntegerRange,
    /** Defines the original host file that the snippet information applies to. */
    snippetFromFile: File,
    /** Defines the byte range in the original host file that the snippet information
applies to. */
    byteRange?: PositiveIntegerRange,
}


/**
 * A distinct article or unit related to Software.
 */
export interface SoftwareArtifact extends Artifact {
    /** Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet. */
    attributionText?: string[],
    /** Provides information about the primary purpose of the software artifact. */
    primaryPurpose?: string,
    /** Provides additional purpose information of the software artifact. */
    additionalPurpose?: string[],
    /** A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity. */
    contentIdentifier?: ContentIdentifier[],
    /** Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any. */
    copyrightText?: string,
}



