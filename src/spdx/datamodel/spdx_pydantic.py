from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "3.0.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'comments': ['This ontology defines the terms and relationships used in the '
                  'SPDX specification to describe system packages'],
     'default_prefix': 'spdx',
     'default_range': 'string',
     'description': 'System Package Data Exchange (SPDX), LinkML schema',
     'id': 'https://w3id.org/lmodel/spdx',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'spdx',
     'prefixes': {'ai': {'prefix_prefix': 'ai',
                         'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/AI/'},
                  'build': {'prefix_prefix': 'build',
                            'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Build/'},
                  'core': {'prefix_prefix': 'core',
                           'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Core/'},
                  'dataset': {'prefix_prefix': 'dataset',
                              'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Dataset/'},
                  'expandedlicensing': {'prefix_prefix': 'expandedlicensing',
                                        'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/'},
                  'extension': {'prefix_prefix': 'extension',
                                'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Extension/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'security': {'prefix_prefix': 'security',
                               'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Security/'},
                  'simplelicensing': {'prefix_prefix': 'simplelicensing',
                                      'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/'},
                  'software': {'prefix_prefix': 'software',
                               'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Software/'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/spdx',
                  'https://spdx.dev/specifications/'],
     'source': 'https://spdx.github.io/spdx-spec/v3.0/rdf/spdx-model.ttl',
     'source_file': 'src/spdx/schema/spdx.yaml',
     'title': 'spdx'} )

class EnergyUnitType(str, Enum):
    """
    Specifies the unit of energy consumption.
    """
    kilowattHour = "kilowattHour"
    """
    Kilowatt-hour.
    """
    megajoule = "megajoule"
    """
    Megajoule.
    """
    other = "other"
    """
    Any other units of energy measurement.
    """


class SafetyRiskAssessmentType(str, Enum):
    """
    Specifies the safety risk level.
    """
    high = "high"
    """
    The second-highest level of risk posed by an AI system.
    """
    low = "low"
    """
    Low/no risk is posed by an AI system.
    """
    medium = "medium"
    """
    The third-highest level of risk posed by an AI system.
    """
    serious = "serious"
    """
    The highest level of risk posed by an AI system.
    """


class AnnotationType(str, Enum):
    """
    Specifies the type of an annotation.
    """
    other = "other"
    """
    Used to store extra information about an Element which is not part of a review (e.g. extra information provided during the creation of the Element).
    """
    review = "review"
    """
    Used when someone reviews the Element.
    """


class ExternalIdentifierType(str, Enum):
    """
    Specifies the type of an external identifier.
    """
    cpe22 = "cpe22"
    """
    [Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)
    """
    cpe23 = "cpe23"
    """
    [Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)
    """
    cve = "cve"
    """
    Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).
    """
    email = "email"
    """
    Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3986/) Section 3.
    """
    gitoid = "gitoid"
    """
    [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).
    """
    other = "other"
    """
    Used when the type does not match any of the other options.
    """
    packageUrl = "packageUrl"
    """
    Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this specification.
    """
    securityOther = "securityOther"
    """
    Used when there is a security related identifier of unspecified type.
    """
    swhid = "swhid"
    """
    SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
    """
    swid = "swid"
    """
    Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.
    """
    urlScheme = "urlScheme"
    """
    [Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.
    """


class ExternalRefType(str, Enum):
    """
    Specifies the type of an external reference.
    """
    altDownloadLocation = "altDownloadLocation"
    """
    A reference to an alternative download location.
    """
    altWebPage = "altWebPage"
    """
    A reference to an alternative web page.
    """
    binaryArtifact = "binaryArtifact"
    """
    A reference to binary artifacts related to a package.
    """
    bower = "bower"
    """
    A reference to a Bower package. The package locator format, looks like `package#version`, is defined in the "install" section of [Bower API documentation](https://bower.io/docs/api/#install).
    """
    buildMeta = "buildMeta"
    """
    A reference build metadata related to a published package.
    """
    buildSystem = "buildSystem"
    """
    A reference build system used to create or publish the package.
    """
    certificationReport = "certificationReport"
    """
    A reference to a certification report for a package from an accredited/independent body.
    """
    chat = "chat"
    """
    A reference to the instant messaging system used by the maintainer for a package.
    """
    componentAnalysisReport = "componentAnalysisReport"
    """
    A reference to a Software Composition Analysis (SCA) report.
    """
    cwe = "cwe"
    """
    [Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/).
    """
    documentation = "documentation"
    """
    A reference to the documentation for a package.
    """
    dynamicAnalysisReport = "dynamicAnalysisReport"
    """
    A reference to a dynamic analysis report for a package.
    """
    eolNotice = "eolNotice"
    """
    A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package.
    """
    exportControlAssessment = "exportControlAssessment"
    """
    A reference to a export control assessment for a package.
    """
    funding = "funding"
    """
    A reference to funding information related to a package.
    """
    issueTracker = "issueTracker"
    """
    A reference to the issue tracker for a package.
    """
    license = "license"
    """
    A reference to additional license information related to an artifact.
    """
    mailingList = "mailingList"
    """
    A reference to the mailing list used by the maintainer for a package.
    """
    mavenCentral = "mavenCentral"
    """
    A reference to a Maven repository artifact. The artifact locator format is defined in the [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html) and looks like `groupId:artifactId[:version]`.
    """
    metrics = "metrics"
    """
    A reference to metrics related to package such as OpenSSF scorecards.
    """
    npm = "npm"
    """
    A reference to an npm package. The package locator format is defined in the [npm documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and looks like `package@version`.
    """
    nuget = "nuget"
    """
    A reference to a NuGet package. The package locator format is defined in the [NuGet documentation](https://docs.nuget.org) and looks like `package/version`.
    """
    other = "other"
    """
    Used when the type does not match any of the other options.
    """
    privacyAssessment = "privacyAssessment"
    """
    A reference to a privacy assessment for a package.
    """
    productMetadata = "productMetadata"
    """
    A reference to additional product metadata such as reference within organization's product catalog.
    """
    purchaseOrder = "purchaseOrder"
    """
    A reference to a purchase order for a package.
    """
    qualityAssessmentReport = "qualityAssessmentReport"
    """
    A reference to a quality assessment for a package.
    """
    releaseHistory = "releaseHistory"
    """
    A reference to a published list of releases for a package.
    """
    releaseNotes = "releaseNotes"
    """
    A reference to the release notes for a package.
    """
    riskAssessment = "riskAssessment"
    """
    A reference to a risk assessment for a package.
    """
    runtimeAnalysisReport = "runtimeAnalysisReport"
    """
    A reference to a runtime analysis report for a package.
    """
    secureSoftwareAttestation = "secureSoftwareAttestation"
    """
    A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form).
    """
    securityAdversaryModel = "securityAdversaryModel"
    """
    A reference to the security adversary model for a package.
    """
    securityAdvisory = "securityAdvisory"
    """
    A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries.
    """
    securityFix = "securityFix"
    """
    A reference to the patch or source code that fixes a vulnerability.
    """
    securityOther = "securityOther"
    """
    A reference to related security information of unspecified type.
    """
    securityPenTestReport = "securityPenTestReport"
    """
    A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package.
    """
    securityPolicy = "securityPolicy"
    """
    A reference to instructions for reporting newly discovered security vulnerabilities for a package.
    """
    securityThreatModel = "securityThreatModel"
    """
    A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package.
    """
    socialMedia = "socialMedia"
    """
    A reference to a social media channel for a package.
    """
    sourceArtifact = "sourceArtifact"
    """
    A reference to an artifact containing the sources for a package.
    """
    staticAnalysisReport = "staticAnalysisReport"
    """
    A reference to a static analysis report for a package.
    """
    support = "support"
    """
    A reference to the software support channel or other support information for a package.
    """
    vcs = "vcs"
    """
    A reference to a version control system related to a software artifact.
    """
    vulnerabilityDisclosureReport = "vulnerabilityDisclosureReport"
    """
    A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/final).
    """
    vulnerabilityExploitabilityAssessment = "vulnerabilityExploitabilityAssessment"
    """
    A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf).
    """


class HashAlgorithm(str, Enum):
    """
    A mathematical algorithm that maps data of arbitrary size to a bit string.
    """
    adler32 = "adler32"
    """
    Adler-32 checksum is part of the widely used zlib compression library as defined in [RFC 1950](https://datatracker.ietf.org/doc/rfc1950/) Section 2.3.
    """
    blake2b256 = "blake2b256"
    """
    BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.
    """
    blake2b384 = "blake2b384"
    """
    BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.
    """
    blake2b512 = "blake2b512"
    """
    BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.
    """
    blake3 = "blake3"
    """
    [BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)
    """
    crystalsDilithium = "crystalsDilithium"
    """
    [Dilithium](https://pq-crystals.org/dilithium/)
    """
    crystalsKyber = "crystalsKyber"
    """
    [Kyber](https://pq-crystals.org/kyber/)
    """
    falcon = "falcon"
    """
    [FALCON](https://falcon-sign.info/falcon.pdf)
    """
    md2 = "md2"
    """
    MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/).
    """
    md4 = "md4"
    """
    MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/).
    """
    md5 = "md5"
    """
    MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/).
    """
    md6 = "md6"
    """
    [MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)
    """
    other = "other"
    """
    any hashing algorithm that does not exist in this list of entries
    """
    sha1 = "sha1"
    """
    SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/).
    """
    sha224 = "sha224"
    """
    SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/).
    """
    sha256 = "sha256"
    """
    SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).
    """
    sha384 = "sha384"
    """
    SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).
    """
    sha3_224 = "sha3_224"
    """
    SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
    """
    sha3_256 = "sha3_256"
    """
    SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
    """
    sha3_384 = "sha3_384"
    """
    SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
    """
    sha3_512 = "sha3_512"
    """
    SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
    """
    sha512 = "sha512"
    """
    SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).
    """


class LifecycleScopeType(str, Enum):
    """
    Provide an enumerated set of lifecycle phases that can provide context to relationships.
    """
    build = "build"
    """
    A relationship has specific context implications during an element's build phase, during development.
    """
    design = "design"
    """
    A relationship has specific context implications during an element's design.
    """
    development = "development"
    """
    A relationship has specific context implications during development phase of an element.
    """
    other = "other"
    """
    A relationship has other specific context information necessary to capture that the above set of enumerations does not handle.
    """
    runtime = "runtime"
    """
    A relationship has specific context implications during the execution phase of an element.
    """
    test = "test"
    """
    A relationship has specific context implications during an element's testing phase, during development.
    """


class PresenceType(str, Enum):
    """
    Categories of presence or absence.
    """
    no = "no"
    """
    Indicates absence of the field.
    """
    noAssertion = "noAssertion"
    """
    Makes no assertion about the field.
    """
    yes = "yes"
    """
    Indicates presence of the field.
    """


class ProfileIdentifierType(str, Enum):
    """
    Enumeration of the valid profiles.
    """
    ai = "ai"
    """
    the element follows the AI profile specification
    """
    build = "build"
    """
    the element follows the Build profile specification
    """
    core = "core"
    """
    the element follows the Core profile specification
    """
    dataset = "dataset"
    """
    the element follows the Dataset profile specification
    """
    expandedLicensing = "expandedLicensing"
    """
    the element follows the ExpandedLicensing profile specification
    """
    extension = "extension"
    """
    the element follows the Extension profile specification
    """
    lite = "lite"
    """
    the element follows the Lite profile specification
    """
    security = "security"
    """
    the element follows the Security profile specification
    """
    simpleLicensing = "simpleLicensing"
    """
    the element follows the SimpleLicensing profile specification
    """
    software = "software"
    """
    the element follows the Software profile specification
    """


class RelationshipCompleteness(str, Enum):
    """
    Indicates whether a relationship is known to be complete, incomplete, or if no assertion is made with respect to relationship completeness.
    """
    complete = "complete"
    """
    The relationship is known to be exhaustive.
    """
    incomplete = "incomplete"
    """
    The relationship is known not to be exhaustive.
    """
    noAssertion = "noAssertion"
    """
    No assertion can be made about the completeness of the relationship.
    """


class RelationshipType(str, Enum):
    """
    Information about the relationship between two Elements.
    """
    affects = "affects"
    """
    The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships.
    """
    amendedBy = "amendedBy"
    """
    The `from` Element is amended by each `to` Element.
    """
    ancestorOf = "ancestorOf"
    """
    The `from` Element is an ancestor of each `to` Element.
    """
    availableFrom = "availableFrom"
    """
    The `from` Element is available from the additional supplier described by each `to` Element.
    """
    configures = "configures"
    """
    The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.
    """
    contains = "contains"
    """
    The `from` Element contains each `to` Element.
    """
    coordinatedBy = "coordinatedBy"
    """
    The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).
    """
    copiedTo = "copiedTo"
    """
    The `from` Element has been copied to each `to` Element.
    """
    delegatedTo = "delegatedTo"
    """
    The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).
    """
    dependsOn = "dependsOn"
    """
    The `from` Element depends on each `to` Element, during a LifecycleScopeType period.
    """
    descendantOf = "descendantOf"
    """
    The `from` Element is a descendant of each `to` Element.
    """
    describes = "describes"
    """
    The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used.
    """
    doesNotAffect = "doesNotAffect"
    """
    The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.
    """
    expandsTo = "expandsTo"
    """
    The `from` archive expands out as an artifact described by each `to` Element.
    """
    exploitCreatedBy = "exploitCreatedBy"
    """
    The `from` Vulnerability has had an exploit created against it by each `to` Agent.
    """
    fixedBy = "fixedBy"
    """
    Designates a `from` Vulnerability has been fixed by the `to` Agent(s).
    """
    fixedIn = "fixedIn"
    """
    A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.
    """
    foundBy = "foundBy"
    """
    Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).
    """
    generates = "generates"
    """
    The `from` Element generates each `to` Element.
    """
    hasAddedFile = "hasAddedFile"
    """
    Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).
    """
    hasAssessmentFor = "hasAssessmentFor"
    """
    Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types.
    """
    hasAssociatedVulnerability = "hasAssociatedVulnerability"
    """
    Used to associate a `from` Artifact with each `to` Vulnerability.
    """
    hasConcludedLicense = "hasConcludedLicense"
    """
    The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license.
    """
    hasDataFile = "hasDataFile"
    """
    The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup file, and more. For AI training dataset, test dataset, test artifact, configuration data, build input data, and build output data, please consider using the more specific relationship types: `trainedOn`, `testedOn`, `hasTest`, `configures`, `hasInput`, and `hasOutput`, respectively. This relationship does not imply dependency.
    """
    hasDeclaredLicense = "hasDeclaredLicense"
    """
    The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.
    """
    hasDeletedFile = "hasDeletedFile"
    """
    Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).
    """
    hasDependencyManifest = "hasDependencyManifest"
    """
    The `from` Element has manifest files that contain dependency information in each `to` Element.
    """
    hasDistributionArtifact = "hasDistributionArtifact"
    """
    The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).
    """
    hasDocumentation = "hasDocumentation"
    """
    The `from` Element is documented by each `to` Element.
    """
    hasDynamicLink = "hasDynamicLink"
    """
    The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.
    """
    hasEvidence = "hasEvidence"
    """
    Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).
    """
    hasExample = "hasExample"
    """
    Every `to` Element is an example for the `from` Element (`from` hasExample `to`).
    """
    hasHost = "hasHost"
    """
    The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).
    """
    hasInput = "hasInput"
    """
    The `from` Build has each `to` Element as an input, during a LifecycleScopeType period.
    """
    hasMetadata = "hasMetadata"
    """
    Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).
    """
    hasOptionalComponent = "hasOptionalComponent"
    """
    Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).
    """
    hasOptionalDependency = "hasOptionalDependency"
    """
    The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.
    """
    hasOutput = "hasOutput"
    """
    The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.
    """
    hasPrerequisite = "hasPrerequisite"
    """
    The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.
    """
    hasProvidedDependency = "hasProvidedDependency"
    """
    The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.
    """
    hasRequirement = "hasRequirement"
    """
    The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.
    """
    hasSpecification = "hasSpecification"
    """
    Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.
    """
    hasStaticLink = "hasStaticLink"
    """
    The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.
    """
    hasTest = "hasTest"
    """
    Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.
    """
    hasTestCase = "hasTestCase"
    """
    Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).
    """
    hasVariant = "hasVariant"
    """
    Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).
    """
    invokedBy = "invokedBy"
    """
    The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).
    """
    modifiedBy = "modifiedBy"
    """
    The `from` Element is modified by each `to` Element.
    """
    other = "other"
    """
    Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).
    """
    packagedBy = "packagedBy"
    """
    Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).
    """
    patchedBy = "patchedBy"
    """
    Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).
    """
    publishedBy = "publishedBy"
    """
    Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.
    """
    reportedBy = "reportedBy"
    """
    Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.
    """
    republishedBy = "republishedBy"
    """
    Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.
    """
    serializedInArtifact = "serializedInArtifact"
    """
    The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.
    """
    testedOn = "testedOn"
    """
    The `from` Element has been tested on the `to` Element(s).
    """
    trainedOn = "trainedOn"
    """
    The `from` Element has been trained on the `to` Element(s).
    """
    underInvestigationFor = "underInvestigationFor"
    """
    The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.
    """
    usesTool = "usesTool"
    """
    The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.
    """


class SupportType(str, Enum):
    """
    Indicates the type of support that is associated with an artifact.
    """
    deployed = "deployed"
    """
    in addition to being supported by the supplier, the software is known to have been deployed and is in use.  For a software as a service provider, this implies the software is now available as a service.
    """
    development = "development"
    """
    the artifact is in active development and is not considered ready for formal support from the supplier.
    """
    endOfSupport = "endOfSupport"
    """
    there is a defined end of support for the artifact from the supplier.  This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact.
    """
    limitedSupport = "limitedSupport"
    """
    the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.
    """
    noAssertion = "noAssertion"
    """
    no assertion about the type of support is made.   This is considered the default if no other support type is used.
    """
    noSupport = "noSupport"
    """
    there is no support for the artifact from the supplier, consumer assumes any support obligations.
    """
    support = "support"
    """
    the artifact has been released, and is supported from the supplier.   There is a validUntilDate that can provide additional information about the duration of support.
    """


class ConfidentialityLevelType(str, Enum):
    """
    Categories of confidentiality level.
    """
    amber = "amber"
    """
    Data points in the dataset can be shared only with specific organizations and their clients on a need to know basis.
    """
    clear = "clear"
    """
    Dataset may be distributed freely, without restriction.
    """
    green = "green"
    """
    Dataset can be shared within a community of peers and partners.
    """
    red = "red"
    """
    Data points in the dataset are highly confidential and can only be shared with named recipients.
    """


class DatasetAvailabilityType(str, Enum):
    """
    Availability of dataset.
    """
    clickthrough = "clickthrough"
    """
    the dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage.
    """
    directDownload = "directDownload"
    """
    the dataset is publicly available and can be downloaded directly.
    """
    query = "query"
    """
    the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.
    """
    registration = "registration"
    """
    the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.
    """
    scrapingScript = "scrapingScript"
    """
    the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data.
    """


class DatasetType(str, Enum):
    """
    Enumeration of dataset types.
    """
    audio = "audio"
    """
    data is audio based, such as a collection of music from the 80s.
    """
    categorical = "categorical"
    """
    data that is classified into a discrete number of categories, such as the eye color of a population of people.
    """
    graph = "graph"
    """
    data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends.
    """
    image = "image"
    """
    data is a collection of images such as pictures of animals.
    """
    noAssertion = "noAssertion"
    """
    data type is not known.
    """
    numeric = "numeric"
    """
    data consists only of numeric entries.
    """
    other = "other"
    """
    data is of a type not included in this list.
    """
    sensor = "sensor"
    """
    data is recorded from a physical sensor, such as a thermometer reading or biometric device.
    """
    structured = "structured"
    """
    data is stored in tabular format or retrieved from a relational database.
    """
    syntactic = "syntactic"
    """
    data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing.
    """
    text = "text"
    """
    data consists of unstructured text, such as a book, Wikipedia article (without images), or transcript.
    """
    timeseries = "timeseries"
    """
    data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day.
    """
    timestamp = "timestamp"
    """
    data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends.
    """
    video = "video"
    """
    data is video based, such as a collection of movie clips featuring Tom Hanks.
    """


class CvssSeverityType(str, Enum):
    """
    Specifies the CVSS base, temporal, threat, or environmental severity type.
    """
    critical = "critical"
    """
    When a CVSS score is between 9.0 - 10.0
    """
    high = "high"
    """
    When a CVSS score is between 7.0 - 8.9
    """
    low = "low"
    """
    When a CVSS score is between 0.1 - 3.9
    """
    medium = "medium"
    """
    When a CVSS score is between 4.0 - 6.9
    """
    none = "none"
    """
    When a CVSS score is 0.0
    """


class ExploitCatalogType(str, Enum):
    """
    Specifies the exploit catalog type.
    """
    kev = "kev"
    """
    CISA's Known Exploited Vulnerability (KEV) Catalog
    """
    other = "other"
    """
    Other exploit catalogs
    """


class SsvcDecisionType(str, Enum):
    """
    Specifies the SSVC decision type.
    """
    act = "act"
    """
    The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. Typically, internal groups would meet to determine the overall response and then execute agreed upon actions. CISA recommends remediating Act vulnerabilities as soon as possible.
    """
    attend = "attend"
    """
    The vulnerability requires attention from the organization's internal, supervisory-level individuals. Necessary actions include requesting assistance or information about the vulnerability, and may involve publishing a notification either internally and/or externally. CISA recommends remediating Attend vulnerabilities sooner than standard update timelines.
    """
    track = "track"
    """
    The vulnerability does not require action at this time. The organization would continue to track the vulnerability and reassess it if new information becomes available. CISA recommends remediating Track vulnerabilities within standard update timelines.
    """
    trackStar = "trackStar"
    """
    ("Track\*" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track\* vulnerabilities within standard update timelines.
    """


class VexJustificationType(str, Enum):
    """
    Specifies the VEX justification type.
    """
    componentNotPresent = "componentNotPresent"
    """
    The software is not affected because the vulnerable component is not in the product.
    """
    inlineMitigationsAlreadyExist = "inlineMitigationsAlreadyExist"
    """
    Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.
    """
    vulnerableCodeCannotBeControlledByAdversary = "vulnerableCodeCannotBeControlledByAdversary"
    """
    The vulnerable component is present, and the component contains the vulnerable code. However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.
    """
    vulnerableCodeNotInExecutePath = "vulnerableCodeNotInExecutePath"
    """
    The affected code is not reachable through the execution of the code, including non-anticipated states of the product.
    """
    vulnerableCodeNotPresent = "vulnerableCodeNotPresent"
    """
    The product is not affected because the code underlying the vulnerability is not present in the product.
    """


class ContentIdentifierType(str, Enum):
    """
    Specifies the type of a content identifier.
    """
    gitoid = "gitoid"
    """
    [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).
    """
    swhid = "swhid"
    """
    SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
    """


class FileKindType(str, Enum):
    """
    Enumeration of the different kinds of SPDX file.
    """
    directory = "directory"
    """
    The file represents a directory and all content stored in that directory.
    """
    file = "file"
    """
    The file represents a single file (default).
    """


class SbomType(str, Enum):
    """
    Provides a set of values to be used to describe the common types of SBOMs that
tools may create.
    """
    analyzed = "analyzed"
    """
    SBOM generated through analysis of artifacts (e.g., executables, packages, containers, and virtual machine images) after its build. Such analysis generally requires a variety of heuristics. In some contexts, this may also be referred to as a "3rd party" SBOM.
    """
    build = "build"
    """
    SBOM generated as part of the process of building the software to create a releasable artifact (e.g., executable or package) from data such as source files, dependencies, built components, build process ephemeral data, and other SBOMs.
    """
    deployed = "deployed"
    """
    SBOM provides an inventory of software that is present on a system. This may be an assembly of other SBOMs that combines analysis of configuration options, and examination of execution behavior in a (potentially simulated) deployment environment.
    """
    design = "design"
    """
    SBOM of intended, planned software project or product with included components (some of which may not yet exist) for a new software artifact.
    """
    runtime = "runtime"
    """
    SBOM generated through instrumenting the system running the software, to capture only components present in the system, as well as external call-outs or dynamically loaded components. In some contexts, this may also be referred to as an "Instrumented" or "Dynamic" SBOM.
    """
    source = "source"
    """
    SBOM created directly from the development environment, source files, and included dependencies used to build an product artifact.
    """


class SoftwarePurpose(str, Enum):
    """
    Provides information about the primary purpose of an Element.
    """
    application = "application"
    """
    The Element is a software application.
    """
    archive = "archive"
    """
    The Element is an archived collection of one or more files (.tar, .zip, etc.).
    """
    bom = "bom"
    """
    The Element is a bill of materials.
    """
    configuration = "configuration"
    """
    The Element is configuration data.
    """
    container = "container"
    """
    The Element is a container image which can be used by a container runtime application.
    """
    data = "data"
    """
    The Element is data.
    """
    device = "device"
    """
    The Element refers to a chipset, processor, or electronic board.
    """
    deviceDriver = "deviceDriver"
    """
    The Element represents software that controls hardware devices.
    """
    diskImage = "diskImage"
    """
    The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.
    """
    documentation = "documentation"
    """
    The Element is documentation.
    """
    evidence = "evidence"
    """
    The Element is the evidence that a specification or requirement has been fulfilled.
    """
    executable = "executable"
    """
    The Element is an Artifact that can be run on a computer.
    """
    file = "file"
    """
    The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.).
    """
    filesystemImage = "filesystemImage"
    """
    The Element is a file system image that can be written to a disk (or virtual) partition.
    """
    firmware = "firmware"
    """
    The Element provides low level control over a device's hardware.
    """
    framework = "framework"
    """
    The Element is a software framework.
    """
    install = "install"
    """
    The Element is used to install software on disk.
    """
    library = "library"
    """
    The Element is a software library.
    """
    manifest = "manifest"
    """
    The Element is a software manifest.
    """
    model = "model"
    """
    The Element is a machine learning or artificial intelligence model.
    """
    module = "module"
    """
    The Element is a module of a piece of software.
    """
    operatingSystem = "operatingSystem"
    """
    The Element is an operating system.
    """
    other = "other"
    """
    The Element doesn't fit into any of the other categories.
    """
    patch = "patch"
    """
    The Element contains a set of changes to update, fix, or improve another Element.
    """
    platform = "platform"
    """
    The Element represents a runtime environment.
    """
    requirement = "requirement"
    """
    The Element provides a requirement needed as input for another Element.
    """
    source = "source"
    """
    The Element is a single or a collection of source files.
    """
    specification = "specification"
    """
    The Element is a plan, guideline or strategy how to create, perform or analyze an application.
    """
    test = "test"
    """
    The Element is a test used to verify functionality on an software element.
    """



class EnergyConsumption(ConfiguredBaseModel):
    """
    A class for describing the energy consumption incurred by an AI model in
    different stages of its lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'finetuningEnergyConsumption': {'multivalued': True,
                                                        'name': 'finetuningEnergyConsumption',
                                                        'notes': ['SHACL nodeKind: '
                                                                  'sh:BlankNodeOrIRI'],
                                                        'range': 'EnergyConsumptionDescription'},
                        'inferenceEnergyConsumption': {'multivalued': True,
                                                       'name': 'inferenceEnergyConsumption',
                                                       'notes': ['SHACL nodeKind: '
                                                                 'sh:BlankNodeOrIRI'],
                                                       'range': 'EnergyConsumptionDescription'},
                        'trainingEnergyConsumption': {'multivalued': True,
                                                      'name': 'trainingEnergyConsumption',
                                                      'notes': ['SHACL nodeKind: '
                                                                'sh:BlankNodeOrIRI'],
                                                      'range': 'EnergyConsumptionDescription'}}})

    finetuningEnergyConsumption: Optional[list[EnergyConsumptionDescription]] = Field(default=None, description="""Specifies the amount of energy consumed when finetuning the AI model that is
being used in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumption'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/finetuningEnergyConsumption'} })
    inferenceEnergyConsumption: Optional[list[EnergyConsumptionDescription]] = Field(default=None, description="""Specifies the amount of energy consumed during inference time by an AI model
that is being used in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumption'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/inferenceEnergyConsumption'} })
    trainingEnergyConsumption: Optional[list[EnergyConsumptionDescription]] = Field(default=None, description="""Specifies the amount of energy consumed when training the AI model that is
being used in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumption'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/trainingEnergyConsumption'} })


class EnergyConsumptionDescription(ConfiguredBaseModel):
    """
    The class that helps note down the quantity of energy consumption and the unit
    used for measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'energyQuantity': {'multivalued': False,
                                           'name': 'energyQuantity',
                                           'notes': ['SHACL nodeKind: sh:Literal'],
                                           'range': 'decimal',
                                           'required': True},
                        'energyUnit': {'multivalued': False,
                                       'name': 'energyUnit',
                                       'notes': ['SHACL nodeKind: sh:IRI',
                                                 'SHACL in: '
                                                 '[ai:EnergyUnitType/kilowattHour, '
                                                 'ai:EnergyUnitType/megajoule, '
                                                 'ai:EnergyUnitType/other]'],
                                       'required': True}}})

    energyQuantity: Decimal = Field(default=..., description="""Represents the energy quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumptionDescription'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/energyQuantity'} })
    energyUnit: Union[EnergyUnitType, str] = Field(default=..., description="""Specifies the unit in which energy is measured.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnergyUnitType'}, {'range': 'string'}],
         'domain_of': ['EnergyConsumptionDescription'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [ai:EnergyUnitType/kilowattHour, '
                   'ai:EnergyUnitType/megajoule, ai:EnergyUnitType/other]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/energyUnit'} })


class CreationInfo(ConfiguredBaseModel):
    """
    Provides information about the creation of the Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'comment': {'multivalued': False,
                                    'name': 'comment',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'},
                        'created': {'multivalued': False,
                                    'name': 'created',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                    'range': 'datetime',
                                    'required': True},
                        'createdBy': {'multivalued': True,
                                      'name': 'createdBy',
                                      'notes': ['SHACL nodeKind: sh:IRI'],
                                      'range': 'Agent',
                                      'required': True},
                        'createdUsing': {'multivalued': True,
                                         'name': 'createdUsing',
                                         'notes': ['SHACL nodeKind: sh:IRI'],
                                         'range': 'Tool'},
                        'specVersion': {'multivalued': False,
                                        'name': 'specVersion',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'pattern': '^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$',
                                        'range': 'string',
                                        'required': True}}})

    createdBy: list[Agent] = Field(default=..., description="""Identifies who or what created the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/createdBy'} })
    createdUsing: Optional[list[Tool]] = Field(default=None, description="""Identifies the tooling that was used during the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/createdUsing'} })
    created: datetime  = Field(default=..., description="""Identifies when the Element was originally created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/created'} })
    specVersion: str = Field(default=..., description="""Provides a reference number that can be used to understand how to parse and
interpret an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/specVersion'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })

    @field_validator('created')
    def pattern_created(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid created format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid created format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('specVersion')
    def pattern_specVersion(cls, v):
        pattern=re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid specVersion format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid specVersion format: {v}"
            raise ValueError(err_msg)
        return v


class DictionaryEntry(ConfiguredBaseModel):
    """
    A key with an associated value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'key': {'multivalued': False,
                                'name': 'key',
                                'notes': ['SHACL nodeKind: sh:Literal'],
                                'range': 'string',
                                'required': True},
                        'value': {'multivalued': False,
                                  'name': 'value',
                                  'notes': ['SHACL nodeKind: sh:Literal'],
                                  'range': 'string'}}})

    value: Optional[str] = Field(default=None, description="""A value used in a generic key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DictionaryEntry'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/value'} })
    key: str = Field(default=..., description="""A key used in a generic key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DictionaryEntry'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/key'} })


class Element(ConfiguredBaseModel):
    """
    Base domain class from which all other SPDX-3.0 domain classes derive.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Core/Element '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue core:Element }'},
                         'shacl_not_slot_extension': {'tag': 'shacl_not_slot_extension',
                                                      'value': '{ sh:or [{ sh:class '
                                                               'security:SsvcVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:CvssV2VulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:ExploitCatalogVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:CvssV4VulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:VexAffectedVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:VexNotAffectedVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:CvssV3VulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:Vulnerability '
                                                               '}, { sh:class '
                                                               'security:VexUnderInvestigationVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:EpssVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'security:VexFixedVulnAssessmentRelationship '
                                                               '}, { sh:class '
                                                               'core:NamespaceMap }, { '
                                                               'sh:class '
                                                               'core:LifecycleScopedRelationship '
                                                               '}, { sh:class '
                                                               'core:Hash }, { '
                                                               'sh:class core:Agent }, '
                                                               '{ sh:class '
                                                               'core:CreationInfo }, { '
                                                               'sh:class '
                                                               'core:ExternalRef }, { '
                                                               'sh:class core:Bom }, { '
                                                               'sh:class '
                                                               'core:IndividualElement '
                                                               '}, { sh:class '
                                                               'core:Relationship }, { '
                                                               'sh:class '
                                                               'core:PositiveIntegerRange '
                                                               '}, { sh:class '
                                                               'core:DictionaryEntry '
                                                               '}, { sh:class '
                                                               'core:ExternalMap }, { '
                                                               'sh:class '
                                                               'core:Annotation }, { '
                                                               'sh:class '
                                                               'core:SpdxDocument }, { '
                                                               'sh:class core:Person '
                                                               '}, { sh:class '
                                                               'core:Organization }, { '
                                                               'sh:class core:Bundle '
                                                               '}, { sh:class '
                                                               'core:Tool }, { '
                                                               'sh:class '
                                                               'core:ExternalIdentifier '
                                                               '}, { sh:class '
                                                               'core:SoftwareAgent }, '
                                                               '{ sh:class '
                                                               'core:PackageVerificationCode '
                                                               '}, { sh:class '
                                                               'ai:AIPackage }, { '
                                                               'sh:class '
                                                               'ai:EnergyConsumptionDescription '
                                                               '}, { sh:class '
                                                               'ai:EnergyConsumption '
                                                               '}, { sh:class '
                                                               'build:Build }, { '
                                                               'sh:class '
                                                               'dataset:DatasetPackage '
                                                               '}, { sh:class '
                                                               'expandedlicensing:CustomLicense '
                                                               '}, { sh:class '
                                                               'expandedlicensing:OrLaterOperator '
                                                               '}, { sh:class '
                                                               'expandedlicensing:ListedLicense '
                                                               '}, { sh:class '
                                                               'expandedlicensing:DisjunctiveLicenseSet '
                                                               '}, { sh:class '
                                                               'expandedlicensing:ListedLicenseException '
                                                               '}, { sh:class '
                                                               'expandedlicensing:WithAdditionOperator '
                                                               '}, { sh:class '
                                                               'expandedlicensing:IndividualLicensingInfo '
                                                               '}, { sh:class '
                                                               'expandedlicensing:CustomLicenseAddition '
                                                               '}, { sh:class '
                                                               'expandedlicensing:ConjunctiveLicenseSet '
                                                               '}, { sh:class '
                                                               'simplelicensing:LicenseExpression '
                                                               '}, { sh:class '
                                                               'simplelicensing:SimpleLicensingText '
                                                               '}, { sh:class '
                                                               'extension:CdxPropertyEntry '
                                                               '}, { sh:class '
                                                               'software:Package }, { '
                                                               'sh:class software:File '
                                                               '}, { sh:class '
                                                               'software:Sbom }, { '
                                                               'sh:class '
                                                               'software:Snippet }, { '
                                                               'sh:class '
                                                               'software:ContentIdentifier '
                                                               '}] }'},
                         'shacl_not_slot_extension_constraint_type': {'tag': 'shacl_not_slot_extension_constraint_type',
                                                                      'value': 'sh:or'},
                         'shacl_not_slot_extension_item_count': {'tag': 'shacl_not_slot_extension_item_count',
                                                                 'value': '54'},
                         'shacl_not_slot_extension_summary': {'tag': 'shacl_not_slot_extension_summary',
                                                              'value': '54 restricted '
                                                                       'classes'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Element',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'comment': {'multivalued': False,
                                    'name': 'comment',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'},
                        'creationInfo': {'multivalued': False,
                                         'name': 'creationInfo',
                                         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                         'range': 'CreationInfo',
                                         'required': True},
                        'description': {'multivalued': False,
                                        'name': 'description',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string'},
                        'extension': {'comments': ['Class is known to not derive from '
                                                   'Extension and cannot be used'],
                                      'multivalued': True,
                                      'name': 'extension',
                                      'notes': ['SHACL not: (54 restricted classes)',
                                                'SHACL nodeKind: sh:BlankNodeOrIRI'],
                                      'range': 'Extension'},
                        'externalIdentifier': {'multivalued': True,
                                               'name': 'externalIdentifier',
                                               'notes': ['SHACL nodeKind: '
                                                         'sh:BlankNodeOrIRI'],
                                               'range': 'ExternalIdentifier'},
                        'externalRef': {'multivalued': True,
                                        'name': 'externalRef',
                                        'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                        'range': 'ExternalRef'},
                        'name': {'multivalued': False,
                                 'name': 'name',
                                 'notes': ['SHACL nodeKind: sh:Literal'],
                                 'range': 'string'},
                        'summary': {'multivalued': False,
                                    'name': 'summary',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'},
                        'verifiedUsing': {'multivalued': True,
                                          'name': 'verifiedUsing',
                                          'notes': ['SHACL nodeKind: '
                                                    'sh:BlankNodeOrIRI'],
                                          'range': 'IntegrityMethod'}}})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class Build(Element):
    """
    Class that describes a build instance of software/artifacts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/Build',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'buildEndTime': {'multivalued': False,
                                         'name': 'buildEndTime',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                         'range': 'datetime'},
                        'buildId': {'multivalued': False,
                                    'name': 'buildId',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'},
                        'buildStartTime': {'multivalued': False,
                                           'name': 'buildStartTime',
                                           'notes': ['SHACL nodeKind: sh:Literal'],
                                           'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                           'range': 'datetime'},
                        'buildType': {'multivalued': False,
                                      'name': 'buildType',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'uri',
                                      'required': True},
                        'configSourceDigest': {'multivalued': True,
                                               'name': 'configSourceDigest',
                                               'notes': ['SHACL nodeKind: '
                                                         'sh:BlankNodeOrIRI'],
                                               'range': 'Hash'},
                        'configSourceEntrypoint': {'multivalued': True,
                                                   'name': 'configSourceEntrypoint',
                                                   'notes': ['SHACL nodeKind: '
                                                             'sh:Literal'],
                                                   'range': 'string'},
                        'configSourceUri': {'multivalued': True,
                                            'name': 'configSourceUri',
                                            'notes': ['SHACL nodeKind: sh:Literal'],
                                            'range': 'uri'},
                        'environment': {'multivalued': True,
                                        'name': 'environment',
                                        'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                        'range': 'DictionaryEntry'},
                        'parameter': {'multivalued': True,
                                      'name': 'parameter',
                                      'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                      'range': 'DictionaryEntry'}}})

    buildType: str = Field(default=..., description="""A buildType is a hint that is used to indicate the toolchain, platform, or
infrastructure that the build was invoked on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/buildType'} })
    buildEndTime: Optional[datetime ] = Field(default=None, description="""Property that describes the time at which a build stops.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/buildEndTime'} })
    buildId: Optional[str] = Field(default=None, description="""A buildId is a locally unique identifier used by a builder to identify a unique
instance of a build produced by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/buildId'} })
    configSourceDigest: Optional[list[Hash]] = Field(default=None, description="""Property that describes the digest of the build configuration file used to
invoke a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/configSourceDigest'} })
    buildStartTime: Optional[datetime ] = Field(default=None, description="""Property describing the start time of a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/buildStartTime'} })
    configSourceUri: Optional[list[str]] = Field(default=None, description="""Property that describes the URI of the build configuration source file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/configSourceUri'} })
    parameter: Optional[list[DictionaryEntry]] = Field(default=None, description="""Property describing a parameter used in an instance of a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/parameter'} })
    configSourceEntrypoint: Optional[list[str]] = Field(default=None, description="""Property describes the invocation entrypoint of a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/configSourceEntrypoint'} })
    environment: Optional[list[DictionaryEntry]] = Field(default=None, description="""Property describing the session in which a build is invoked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Build/environment'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('buildEndTime')
    def pattern_buildEndTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid buildEndTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid buildEndTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('buildStartTime')
    def pattern_buildStartTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid buildStartTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid buildStartTime format: {v}"
            raise ValueError(err_msg)
        return v


class Agent(Element):
    """
    Agent represents anything with the potential to act on a system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Agent',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class Annotation(Element):
    """
    An assertion made in relation to one or more elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Annotation',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'annotationType': {'multivalued': False,
                                           'name': 'annotationType',
                                           'notes': ['SHACL nodeKind: sh:IRI',
                                                     'SHACL in: '
                                                     '[core:AnnotationType/other, '
                                                     'core:AnnotationType/review]'],
                                           'required': True},
                        'contentType': {'multivalued': False,
                                        'name': 'contentType',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'pattern': '^[^\\/]+\\/[^\\/]+$',
                                        'range': 'string'},
                        'statement': {'multivalued': False,
                                      'name': 'statement',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'string'},
                        'subject': {'multivalued': False,
                                    'name': 'subject',
                                    'notes': ['SHACL nodeKind: sh:IRI'],
                                    'range': 'Element',
                                    'required': True}}})

    contentType: Optional[str] = Field(default=None, description="""Provides information about the content type of an Element or a Property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation', 'ExternalRef', 'File'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/contentType'} })
    statement: Optional[str] = Field(default=None, description="""Commentary on an assertion that an annotator has made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/statement'} })
    subject: Element = Field(default=..., description="""An Element an annotator has made an assertion about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/subject'} })
    annotationType: Union[AnnotationType, str] = Field(default=..., description="""Describes the type of annotation.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'AnnotationType'}, {'range': 'string'}],
         'domain_of': ['Annotation'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:AnnotationType/other, core:AnnotationType/review]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/annotationType'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('contentType')
    def pattern_contentType(cls, v):
        pattern=re.compile(r"^[^\/]+\/[^\/]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid contentType format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid contentType format: {v}"
            raise ValueError(err_msg)
        return v


class Artifact(Element):
    """
    A distinct article or unit within the digital domain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Core/Artifact '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue core:Artifact }'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Artifact',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'builtTime': {'multivalued': False,
                                      'name': 'builtTime',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                      'range': 'datetime'},
                        'originatedBy': {'multivalued': True,
                                         'name': 'originatedBy',
                                         'notes': ['SHACL nodeKind: sh:IRI'],
                                         'range': 'Agent'},
                        'releaseTime': {'multivalued': False,
                                        'name': 'releaseTime',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                        'range': 'datetime'},
                        'standardName': {'multivalued': True,
                                         'name': 'standardName',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string'},
                        'suppliedBy': {'multivalued': False,
                                       'name': 'suppliedBy',
                                       'notes': ['SHACL nodeKind: sh:IRI'],
                                       'range': 'Agent'},
                        'supportLevel': {'multivalued': True,
                                         'name': 'supportLevel',
                                         'notes': ['SHACL nodeKind: sh:IRI',
                                                   'SHACL in: '
                                                   '[core:SupportType/development, '
                                                   'core:SupportType/support, '
                                                   'core:SupportType/deployed, '
                                                   'core:SupportType/limitedSupport, '
                                                   'core:SupportType/endOfSupport, '
                                                   'core:SupportType/noSupport, '
                                                   'core:SupportType/noAssertion]'],
                                         'range': 'SupportType'},
                        'validUntilTime': {'multivalued': False,
                                           'name': 'validUntilTime',
                                           'notes': ['SHACL nodeKind: sh:Literal'],
                                           'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                           'range': 'datetime'}}})

    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class ElementCollection(Element):
    """
    A collection of Elements, not necessarily with unifying context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue core:ElementCollection '
                                                '}'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'element': {'multivalued': True,
                                    'name': 'element',
                                    'notes': ['SHACL nodeKind: sh:IRI'],
                                    'range': 'Element'},
                        'profileConformance': {'multivalued': True,
                                               'name': 'profileConformance',
                                               'notes': ['SHACL nodeKind: sh:IRI',
                                                         'SHACL in: '
                                                         '[core:ProfileIdentifierType/core, '
                                                         'core:ProfileIdentifierType/software, '
                                                         'core:ProfileIdentifierType/simpleLicensing, '
                                                         'core:ProfileIdentifierType/expandedLicensing, '
                                                         'core:ProfileIdentifierType/security, '
                                                         'core:ProfileIdentifierType/build, '
                                                         'core:ProfileIdentifierType/ai, '
                                                         'core:ProfileIdentifierType/dataset, '
                                                         'core:ProfileIdentifierType/extension, '
                                                         'core:ProfileIdentifierType/lite]'],
                                               'range': 'ProfileIdentifierType'},
                        'rootElement': {'multivalued': True,
                                        'name': 'rootElement',
                                        'notes': ['SHACL nodeKind: sh:IRI'],
                                        'range': 'Element'}}})

    element: Optional[list[Element]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to
conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ProfileIdentifierType/core, '
                   'core:ProfileIdentifierType/software, '
                   'core:ProfileIdentifierType/simpleLicensing, '
                   'core:ProfileIdentifierType/expandedLicensing, '
                   'core:ProfileIdentifierType/security, '
                   'core:ProfileIdentifierType/build, core:ProfileIdentifierType/ai, '
                   'core:ProfileIdentifierType/dataset, '
                   'core:ProfileIdentifierType/extension, '
                   'core:ProfileIdentifierType/lite]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance'} })
    rootElement: Optional[list[Element]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/rootElement'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class Bundle(ElementCollection):
    """
    A collection of Elements that have a shared context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Bundle',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'context': {'multivalued': False,
                                    'name': 'context',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'}}})

    context: Optional[str] = Field(default=None, description="""Gives information about the circumstances or unifying properties
that Elements of the bundle have been assembled under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/context'} })
    element: Optional[list[Element]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to
conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ProfileIdentifierType/core, '
                   'core:ProfileIdentifierType/software, '
                   'core:ProfileIdentifierType/simpleLicensing, '
                   'core:ProfileIdentifierType/expandedLicensing, '
                   'core:ProfileIdentifierType/security, '
                   'core:ProfileIdentifierType/build, core:ProfileIdentifierType/ai, '
                   'core:ProfileIdentifierType/dataset, '
                   'core:ProfileIdentifierType/extension, '
                   'core:ProfileIdentifierType/lite]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance'} })
    rootElement: Optional[list[Element]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/rootElement'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class Bom(Bundle):
    """
    A container for a grouping of SPDX-3.0 content characterizing details
    (provenence, composition, licensing, etc.) about a product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Bom',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    context: Optional[str] = Field(default=None, description="""Gives information about the circumstances or unifying properties
that Elements of the bundle have been assembled under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/context'} })
    element: Optional[list[Element]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to
conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ProfileIdentifierType/core, '
                   'core:ProfileIdentifierType/software, '
                   'core:ProfileIdentifierType/simpleLicensing, '
                   'core:ProfileIdentifierType/expandedLicensing, '
                   'core:ProfileIdentifierType/security, '
                   'core:ProfileIdentifierType/build, core:ProfileIdentifierType/ai, '
                   'core:ProfileIdentifierType/dataset, '
                   'core:ProfileIdentifierType/extension, '
                   'core:ProfileIdentifierType/lite]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance'} })
    rootElement: Optional[list[Element]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/rootElement'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class ExternalIdentifier(ConfiguredBaseModel):
    """
    A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'comment': {'multivalued': False,
                                    'name': 'comment',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'},
                        'externalIdentifierType': {'multivalued': False,
                                                   'name': 'externalIdentifierType',
                                                   'notes': ['SHACL nodeKind: sh:IRI',
                                                             'SHACL in: '
                                                             '[core:ExternalIdentifierType/cpe22, '
                                                             'core:ExternalIdentifierType/cpe23, '
                                                             'core:ExternalIdentifierType/cve, '
                                                             'core:ExternalIdentifierType/email, '
                                                             'core:ExternalIdentifierType/gitoid, '
                                                             'core:ExternalIdentifierType/other, '
                                                             'core:ExternalIdentifierType/packageUrl, '
                                                             'core:ExternalIdentifierType/securityOther, '
                                                             'core:ExternalIdentifierType/swhid, '
                                                             'core:ExternalIdentifierType/swid, '
                                                             'core:ExternalIdentifierType/urlScheme]'],
                                                   'required': True},
                        'identifier': {'multivalued': False,
                                       'name': 'identifier',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'string',
                                       'required': True},
                        'identifierLocator': {'multivalued': True,
                                              'name': 'identifierLocator',
                                              'notes': ['SHACL nodeKind: sh:Literal'],
                                              'range': 'uri'},
                        'issuingAuthority': {'multivalued': False,
                                             'name': 'issuingAuthority',
                                             'notes': ['SHACL nodeKind: sh:Literal'],
                                             'range': 'string'}}})

    identifierLocator: Optional[list[str]] = Field(default=None, description="""Provides the location for more information regarding an external identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/identifierLocator'} })
    externalIdentifierType: Union[ExternalIdentifierType, str] = Field(default=..., description="""Specifies the type of the external identifier.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'ExternalIdentifierType'}, {'range': 'string'}],
         'domain_of': ['ExternalIdentifier'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ExternalIdentifierType/cpe22, '
                   'core:ExternalIdentifierType/cpe23, '
                   'core:ExternalIdentifierType/cve, '
                   'core:ExternalIdentifierType/email, '
                   'core:ExternalIdentifierType/gitoid, '
                   'core:ExternalIdentifierType/other, '
                   'core:ExternalIdentifierType/packageUrl, '
                   'core:ExternalIdentifierType/securityOther, '
                   'core:ExternalIdentifierType/swhid, '
                   'core:ExternalIdentifierType/swid, '
                   'core:ExternalIdentifierType/urlScheme]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifierType'} })
    issuingAuthority: Optional[str] = Field(default=None, description="""An entity that is authorized to issue identification credentials.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/issuingAuthority'} })
    identifier: str = Field(default=..., description="""Uniquely identifies an external element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/identifier'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })


class ExternalMap(ConfiguredBaseModel):
    """
    A map of Element identifiers that are used within an SpdxDocument but defined
    external to that SpdxDocument.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'definingArtifact': {'multivalued': False,
                                             'name': 'definingArtifact',
                                             'notes': ['SHACL nodeKind: sh:IRI'],
                                             'range': 'Artifact'},
                        'externalSpdxId': {'multivalued': False,
                                           'name': 'externalSpdxId',
                                           'notes': ['SHACL nodeKind: sh:Literal'],
                                           'range': 'uri',
                                           'required': True},
                        'locationHint': {'multivalued': False,
                                         'name': 'locationHint',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'uri'},
                        'verifiedUsing': {'multivalued': True,
                                          'name': 'verifiedUsing',
                                          'notes': ['SHACL nodeKind: '
                                                    'sh:BlankNodeOrIRI'],
                                          'range': 'IntegrityMethod'}}})

    definingArtifact: Optional[Artifact] = Field(default=None, description="""Artifact representing a serialization instance of SPDX data containing the
definition of a particular Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalMap'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/definingArtifact'} })
    locationHint: Optional[str] = Field(default=None, description="""Provides an indication of where to retrieve an external Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalMap'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/locationHint'} })
    externalSpdxId: str = Field(default=..., description="""Identifies an external Element used within an SpdxDocument but defined
external to that SpdxDocument.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalMap'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalSpdxId'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })


class ExternalRef(ConfiguredBaseModel):
    """
    A reference to a resource outside the scope of SPDX-3.0 content related to an Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'comment': {'multivalued': False,
                                    'name': 'comment',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'},
                        'contentType': {'multivalued': False,
                                        'name': 'contentType',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'pattern': '^[^\\/]+\\/[^\\/]+$',
                                        'range': 'string'},
                        'core_locator': {'multivalued': True,
                                         'name': 'core_locator',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string'},
                        'externalRefType': {'multivalued': False,
                                            'name': 'externalRefType',
                                            'notes': ['SHACL nodeKind: sh:IRI',
                                                      'SHACL in: '
                                                      '[core:ExternalRefType/altDownloadLocation, '
                                                      'core:ExternalRefType/altWebPage, '
                                                      'core:ExternalRefType/binaryArtifact, '
                                                      'core:ExternalRefType/bower, '
                                                      'core:ExternalRefType/buildMeta, '
                                                      'core:ExternalRefType/buildSystem, '
                                                      'core:ExternalRefType/chat, '
                                                      'core:ExternalRefType/certificationReport, '
                                                      'core:ExternalRefType/componentAnalysisReport, '
                                                      'core:ExternalRefType/cwe, '
                                                      'core:ExternalRefType/documentation, '
                                                      'core:ExternalRefType/dynamicAnalysisReport, '
                                                      'core:ExternalRefType/eolNotice, '
                                                      'core:ExternalRefType/exportControlAssessment, '
                                                      'core:ExternalRefType/funding, '
                                                      'core:ExternalRefType/issueTracker, '
                                                      'core:ExternalRefType/mailingList, '
                                                      'core:ExternalRefType/mavenCentral, '
                                                      'core:ExternalRefType/metrics, '
                                                      'core:ExternalRefType/npm, '
                                                      'core:ExternalRefType/nuget, '
                                                      'core:ExternalRefType/license, '
                                                      'core:ExternalRefType/other, '
                                                      'core:ExternalRefType/privacyAssessment, '
                                                      'core:ExternalRefType/productMetadata, '
                                                      'core:ExternalRefType/purchaseOrder, '
                                                      'core:ExternalRefType/qualityAssessmentReport, '
                                                      'core:ExternalRefType/releaseNotes, '
                                                      'core:ExternalRefType/releaseHistory, '
                                                      'core:ExternalRefType/riskAssessment, '
                                                      'core:ExternalRefType/runtimeAnalysisReport, '
                                                      'core:ExternalRefType/secureSoftwareAttestation, '
                                                      'core:ExternalRefType/securityAdvisory, '
                                                      'core:ExternalRefType/securityAdversaryModel, '
                                                      'core:ExternalRefType/securityFix, '
                                                      'core:ExternalRefType/securityOther, '
                                                      'core:ExternalRefType/securityPenTestReport, '
                                                      'core:ExternalRefType/securityPolicy, '
                                                      'core:ExternalRefType/securityThreatModel, '
                                                      'core:ExternalRefType/socialMedia, '
                                                      'core:ExternalRefType/sourceArtifact, '
                                                      'core:ExternalRefType/staticAnalysisReport, '
                                                      'core:ExternalRefType/support, '
                                                      'core:ExternalRefType/vcs, '
                                                      'core:ExternalRefType/vulnerabilityDisclosureReport, '
                                                      'core:ExternalRefType/vulnerabilityExploitabilityAssessment]']}}})

    core_locator: Optional[list[str]] = Field(default=None, description="""Provides the location of an external reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalRef'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/locator'} })
    externalRefType: Optional[Union[ExternalRefType, str]] = Field(default=None, description="""Specifies the type of the external reference.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'ExternalRefType'}, {'range': 'string'}],
         'domain_of': ['ExternalRef'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ExternalRefType/altDownloadLocation, '
                   'core:ExternalRefType/altWebPage, '
                   'core:ExternalRefType/binaryArtifact, core:ExternalRefType/bower, '
                   'core:ExternalRefType/buildMeta, core:ExternalRefType/buildSystem, '
                   'core:ExternalRefType/chat, '
                   'core:ExternalRefType/certificationReport, '
                   'core:ExternalRefType/componentAnalysisReport, '
                   'core:ExternalRefType/cwe, core:ExternalRefType/documentation, '
                   'core:ExternalRefType/dynamicAnalysisReport, '
                   'core:ExternalRefType/eolNotice, '
                   'core:ExternalRefType/exportControlAssessment, '
                   'core:ExternalRefType/funding, core:ExternalRefType/issueTracker, '
                   'core:ExternalRefType/mailingList, '
                   'core:ExternalRefType/mavenCentral, core:ExternalRefType/metrics, '
                   'core:ExternalRefType/npm, core:ExternalRefType/nuget, '
                   'core:ExternalRefType/license, core:ExternalRefType/other, '
                   'core:ExternalRefType/privacyAssessment, '
                   'core:ExternalRefType/productMetadata, '
                   'core:ExternalRefType/purchaseOrder, '
                   'core:ExternalRefType/qualityAssessmentReport, '
                   'core:ExternalRefType/releaseNotes, '
                   'core:ExternalRefType/releaseHistory, '
                   'core:ExternalRefType/riskAssessment, '
                   'core:ExternalRefType/runtimeAnalysisReport, '
                   'core:ExternalRefType/secureSoftwareAttestation, '
                   'core:ExternalRefType/securityAdvisory, '
                   'core:ExternalRefType/securityAdversaryModel, '
                   'core:ExternalRefType/securityFix, '
                   'core:ExternalRefType/securityOther, '
                   'core:ExternalRefType/securityPenTestReport, '
                   'core:ExternalRefType/securityPolicy, '
                   'core:ExternalRefType/securityThreatModel, '
                   'core:ExternalRefType/socialMedia, '
                   'core:ExternalRefType/sourceArtifact, '
                   'core:ExternalRefType/staticAnalysisReport, '
                   'core:ExternalRefType/support, core:ExternalRefType/vcs, '
                   'core:ExternalRefType/vulnerabilityDisclosureReport, '
                   'core:ExternalRefType/vulnerabilityExploitabilityAssessment]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRefType'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    contentType: Optional[str] = Field(default=None, description="""Provides information about the content type of an Element or a Property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation', 'ExternalRef', 'File'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/contentType'} })

    @field_validator('contentType')
    def pattern_contentType(cls, v):
        pattern=re.compile(r"^[^\/]+\/[^\/]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid contentType format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid contentType format: {v}"
            raise ValueError(err_msg)
        return v


class IndividualElement(Element):
    """
    A concrete subclass of Element used by Individuals in the
    Core profile.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class IntegrityMethod(ConfiguredBaseModel):
    """
    Provides an independently reproducible mechanism that permits verification of a specific Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue core:IntegrityMethod '
                                                '}'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'comment': {'multivalued': False,
                                    'name': 'comment',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'string'}}})

    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })


class Hash(IntegrityMethod):
    """
    A mathematically calculated representation of a grouping of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Hash',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'algorithm': {'multivalued': False,
                                      'name': 'algorithm',
                                      'notes': ['SHACL nodeKind: sh:IRI',
                                                'SHACL in: '
                                                '[core:HashAlgorithm/adler32, '
                                                'core:HashAlgorithm/blake2b256, '
                                                'core:HashAlgorithm/blake2b384, '
                                                'core:HashAlgorithm/blake2b512, '
                                                'core:HashAlgorithm/blake3, '
                                                'core:HashAlgorithm/crystalsDilithium, '
                                                'core:HashAlgorithm/crystalsKyber, '
                                                'core:HashAlgorithm/falcon, '
                                                'core:HashAlgorithm/md2, '
                                                'core:HashAlgorithm/md4, '
                                                'core:HashAlgorithm/md5, '
                                                'core:HashAlgorithm/md6, '
                                                'core:HashAlgorithm/other, '
                                                'core:HashAlgorithm/sha1, '
                                                'core:HashAlgorithm/sha224, '
                                                'core:HashAlgorithm/sha256, '
                                                'core:HashAlgorithm/sha384, '
                                                'core:HashAlgorithm/sha512, '
                                                'core:HashAlgorithm/sha3_224, '
                                                'core:HashAlgorithm/sha3_256, '
                                                'core:HashAlgorithm/sha3_384, '
                                                'core:HashAlgorithm/sha3_512]'],
                                      'required': True},
                        'hashValue': {'multivalued': False,
                                      'name': 'hashValue',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'string',
                                      'required': True}}})

    algorithm: Union[HashAlgorithm, str] = Field(default=..., description="""Specifies the algorithm used for calculating the hash value.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'HashAlgorithm'}, {'range': 'string'}],
         'domain_of': ['Hash', 'PackageVerificationCode'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:HashAlgorithm/adler32, '
                   'core:HashAlgorithm/blake2b256, core:HashAlgorithm/blake2b384, '
                   'core:HashAlgorithm/blake2b512, core:HashAlgorithm/blake3, '
                   'core:HashAlgorithm/crystalsDilithium, '
                   'core:HashAlgorithm/crystalsKyber, core:HashAlgorithm/falcon, '
                   'core:HashAlgorithm/md2, core:HashAlgorithm/md4, '
                   'core:HashAlgorithm/md5, core:HashAlgorithm/md6, '
                   'core:HashAlgorithm/other, core:HashAlgorithm/sha1, '
                   'core:HashAlgorithm/sha224, core:HashAlgorithm/sha256, '
                   'core:HashAlgorithm/sha384, core:HashAlgorithm/sha512, '
                   'core:HashAlgorithm/sha3_224, core:HashAlgorithm/sha3_256, '
                   'core:HashAlgorithm/sha3_384, core:HashAlgorithm/sha3_512]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/algorithm'} })
    hashValue: str = Field(default=..., description="""The result of applying a hash algorithm to an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'PackageVerificationCode'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/hashValue'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })


class NamespaceMap(ConfiguredBaseModel):
    """
    A mapping between prefixes and namespace partial URIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'namespace': {'multivalued': False,
                                      'name': 'namespace',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'uri',
                                      'required': True},
                        'prefix': {'multivalued': False,
                                   'name': 'prefix',
                                   'notes': ['SHACL nodeKind: sh:Literal'],
                                   'range': 'string',
                                   'required': True}}})

    prefix: str = Field(default=..., description="""A substitute for a URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamespaceMap'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/prefix'} })
    namespace: str = Field(default=..., description="""Provides an unambiguous mechanism for conveying a URI fragment portion of an
Element ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamespaceMap'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/namespace'} })


class Organization(Agent):
    """
    A group of people who work together in an organized way for a shared purpose.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Organization',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class PackageVerificationCode(IntegrityMethod):
    """
    An SPDX version 2.X compatible verification method for software packages.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'algorithm': {'multivalued': False,
                                      'name': 'algorithm',
                                      'notes': ['SHACL nodeKind: sh:IRI',
                                                'SHACL in: '
                                                '[core:HashAlgorithm/adler32, '
                                                'core:HashAlgorithm/blake2b256, '
                                                'core:HashAlgorithm/blake2b384, '
                                                'core:HashAlgorithm/blake2b512, '
                                                'core:HashAlgorithm/blake3, '
                                                'core:HashAlgorithm/crystalsDilithium, '
                                                'core:HashAlgorithm/crystalsKyber, '
                                                'core:HashAlgorithm/falcon, '
                                                'core:HashAlgorithm/md2, '
                                                'core:HashAlgorithm/md4, '
                                                'core:HashAlgorithm/md5, '
                                                'core:HashAlgorithm/md6, '
                                                'core:HashAlgorithm/other, '
                                                'core:HashAlgorithm/sha1, '
                                                'core:HashAlgorithm/sha224, '
                                                'core:HashAlgorithm/sha256, '
                                                'core:HashAlgorithm/sha384, '
                                                'core:HashAlgorithm/sha512, '
                                                'core:HashAlgorithm/sha3_224, '
                                                'core:HashAlgorithm/sha3_256, '
                                                'core:HashAlgorithm/sha3_384, '
                                                'core:HashAlgorithm/sha3_512]'],
                                      'required': True},
                        'hashValue': {'multivalued': False,
                                      'name': 'hashValue',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'string',
                                      'required': True},
                        'packageVerificationCodeExcludedFile': {'multivalued': True,
                                                                'name': 'packageVerificationCodeExcludedFile',
                                                                'notes': ['SHACL '
                                                                          'nodeKind: '
                                                                          'sh:Literal'],
                                                                'range': 'string'}}})

    packageVerificationCodeExcludedFile: Optional[list[str]] = Field(default=None, description="""The relative file name of a file to be excluded from the
`PackageVerificationCode`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PackageVerificationCode'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/packageVerificationCodeExcludedFile'} })
    hashValue: str = Field(default=..., description="""The result of applying a hash algorithm to an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'PackageVerificationCode'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/hashValue'} })
    algorithm: Union[HashAlgorithm, str] = Field(default=..., description="""Specifies the algorithm used for calculating the hash value.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'HashAlgorithm'}, {'range': 'string'}],
         'domain_of': ['Hash', 'PackageVerificationCode'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:HashAlgorithm/adler32, '
                   'core:HashAlgorithm/blake2b256, core:HashAlgorithm/blake2b384, '
                   'core:HashAlgorithm/blake2b512, core:HashAlgorithm/blake3, '
                   'core:HashAlgorithm/crystalsDilithium, '
                   'core:HashAlgorithm/crystalsKyber, core:HashAlgorithm/falcon, '
                   'core:HashAlgorithm/md2, core:HashAlgorithm/md4, '
                   'core:HashAlgorithm/md5, core:HashAlgorithm/md6, '
                   'core:HashAlgorithm/other, core:HashAlgorithm/sha1, '
                   'core:HashAlgorithm/sha224, core:HashAlgorithm/sha256, '
                   'core:HashAlgorithm/sha384, core:HashAlgorithm/sha512, '
                   'core:HashAlgorithm/sha3_224, core:HashAlgorithm/sha3_256, '
                   'core:HashAlgorithm/sha3_384, core:HashAlgorithm/sha3_512]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/algorithm'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })


class Person(Agent):
    """
    An individual human being.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Person',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class PositiveIntegerRange(ConfiguredBaseModel):
    """
    A tuple of two positive integers that define a range.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'beginIntegerRange': {'minimum_value': 1,
                                              'multivalued': False,
                                              'name': 'beginIntegerRange',
                                              'notes': ['SHACL nodeKind: sh:Literal'],
                                              'range': 'integer',
                                              'required': True},
                        'endIntegerRange': {'minimum_value': 1,
                                            'multivalued': False,
                                            'name': 'endIntegerRange',
                                            'notes': ['SHACL nodeKind: sh:Literal'],
                                            'range': 'integer',
                                            'required': True}}})

    endIntegerRange: int = Field(default=..., description="""Defines the end of a range.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['PositiveIntegerRange'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endIntegerRange'} })
    beginIntegerRange: int = Field(default=..., description="""Defines the beginning of a range.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['PositiveIntegerRange'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/beginIntegerRange'} })


class Relationship(Element):
    """
    Describes a relationship between one or more elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Relationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'completeness': {'multivalued': False,
                                         'name': 'completeness',
                                         'notes': ['SHACL nodeKind: sh:IRI',
                                                   'SHACL in: '
                                                   '[core:RelationshipCompleteness/incomplete, '
                                                   'core:RelationshipCompleteness/complete, '
                                                   'core:RelationshipCompleteness/noAssertion]'],
                                         'range': 'RelationshipCompleteness'},
                        'endTime': {'multivalued': False,
                                    'name': 'endTime',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                    'range': 'datetime'},
                        'from': {'multivalued': False,
                                 'name': 'from',
                                 'notes': ['SHACL nodeKind: sh:IRI'],
                                 'range': 'Element',
                                 'required': True},
                        'relationshipType': {'multivalued': False,
                                             'name': 'relationshipType',
                                             'notes': ['SHACL nodeKind: sh:IRI',
                                                       'SHACL in: '
                                                       '[core:RelationshipType/affects, '
                                                       'core:RelationshipType/amendedBy, '
                                                       'core:RelationshipType/ancestorOf, '
                                                       'core:RelationshipType/availableFrom, '
                                                       'core:RelationshipType/configures, '
                                                       'core:RelationshipType/contains, '
                                                       'core:RelationshipType/coordinatedBy, '
                                                       'core:RelationshipType/copiedTo, '
                                                       'core:RelationshipType/delegatedTo, '
                                                       'core:RelationshipType/dependsOn, '
                                                       'core:RelationshipType/descendantOf, '
                                                       'core:RelationshipType/describes, '
                                                       'core:RelationshipType/doesNotAffect, '
                                                       'core:RelationshipType/expandsTo, '
                                                       'core:RelationshipType/exploitCreatedBy, '
                                                       'core:RelationshipType/fixedBy, '
                                                       'core:RelationshipType/fixedIn, '
                                                       'core:RelationshipType/foundBy, '
                                                       'core:RelationshipType/generates, '
                                                       'core:RelationshipType/hasAddedFile, '
                                                       'core:RelationshipType/hasAssessmentFor, '
                                                       'core:RelationshipType/hasAssociatedVulnerability, '
                                                       'core:RelationshipType/hasConcludedLicense, '
                                                       'core:RelationshipType/hasDataFile, '
                                                       'core:RelationshipType/hasDeclaredLicense, '
                                                       'core:RelationshipType/hasDeletedFile, '
                                                       'core:RelationshipType/hasDependencyManifest, '
                                                       'core:RelationshipType/hasDistributionArtifact, '
                                                       'core:RelationshipType/hasDocumentation, '
                                                       'core:RelationshipType/hasDynamicLink, '
                                                       'core:RelationshipType/hasEvidence, '
                                                       'core:RelationshipType/hasExample, '
                                                       'core:RelationshipType/hasHost, '
                                                       'core:RelationshipType/hasInput, '
                                                       'core:RelationshipType/hasMetadata, '
                                                       'core:RelationshipType/hasOptionalComponent, '
                                                       'core:RelationshipType/hasOptionalDependency, '
                                                       'core:RelationshipType/hasOutput, '
                                                       'core:RelationshipType/hasPrerequisite, '
                                                       'core:RelationshipType/hasProvidedDependency, '
                                                       'core:RelationshipType/hasRequirement, '
                                                       'core:RelationshipType/hasSpecification, '
                                                       'core:RelationshipType/hasStaticLink, '
                                                       'core:RelationshipType/hasTest, '
                                                       'core:RelationshipType/hasTestCase, '
                                                       'core:RelationshipType/hasVariant, '
                                                       'core:RelationshipType/invokedBy, '
                                                       'core:RelationshipType/modifiedBy, '
                                                       'core:RelationshipType/other, '
                                                       'core:RelationshipType/packagedBy, '
                                                       'core:RelationshipType/patchedBy, '
                                                       'core:RelationshipType/publishedBy, '
                                                       'core:RelationshipType/reportedBy, '
                                                       'core:RelationshipType/republishedBy, '
                                                       'core:RelationshipType/serializedInArtifact, '
                                                       'core:RelationshipType/testedOn, '
                                                       'core:RelationshipType/trainedOn, '
                                                       'core:RelationshipType/underInvestigationFor, '
                                                       'core:RelationshipType/usesTool]'],
                                             'required': True},
                        'startTime': {'multivalued': False,
                                      'name': 'startTime',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                      'range': 'datetime'},
                        'to': {'multivalued': True,
                               'name': 'to',
                               'notes': ['SHACL nodeKind: sh:IRI'],
                               'range': 'Element',
                               'required': True}}})

    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class LifecycleScopedRelationship(Relationship):
    """
    Provide context for a relationship that occurs in the lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'scope': {'multivalued': False,
                                  'name': 'scope',
                                  'notes': ['SHACL nodeKind: sh:IRI',
                                            'SHACL in: '
                                            '[core:LifecycleScopeType/design, '
                                            'core:LifecycleScopeType/development, '
                                            'core:LifecycleScopeType/build, '
                                            'core:LifecycleScopeType/test, '
                                            'core:LifecycleScopeType/runtime, '
                                            'core:LifecycleScopeType/other]']}}})

    scope: Optional[Union[LifecycleScopeType, str]] = Field(default=None, description="""Capture the scope of information about a specific relationship between elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'LifecycleScopeType'}, {'range': 'string'}],
         'domain_of': ['LifecycleScopedRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:LifecycleScopeType/design, '
                   'core:LifecycleScopeType/development, '
                   'core:LifecycleScopeType/build, core:LifecycleScopeType/test, '
                   'core:LifecycleScopeType/runtime, core:LifecycleScopeType/other]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/scope'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class SoftwareAgent(Agent):
    """
    A software agent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class SpdxDocument(ElementCollection):
    """
    A collection of SPDX Elements that could potentially be serialized.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'dataLicense': {'multivalued': False,
                                        'name': 'dataLicense',
                                        'notes': ['SHACL nodeKind: sh:IRI'],
                                        'range': 'AnyLicenseInfo'},
                        'import': {'multivalued': True,
                                   'name': 'import',
                                   'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                   'range': 'ExternalMap'},
                        'namespaceMap': {'multivalued': True,
                                         'name': 'namespaceMap',
                                         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                         'range': 'NamespaceMap'}}})

    namespaceMap: Optional[list[NamespaceMap]] = Field(default=None, description="""Provides a NamespaceMap of prefixes and associated namespace partial URIs applicable to an SpdxDocument and independent of any specific serialization format or instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpdxDocument'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/namespaceMap'} })
    dataLicense: Optional[AnyLicenseInfo] = Field(default=None, description="""Provides the license under which the SPDX documentation of the Element can be
used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpdxDocument'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/dataLicense'} })
    import_: Optional[list[ExternalMap]] = Field(default=None, alias="import", description="""Provides an ExternalMap of Element identifiers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpdxDocument'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/import'} })
    element: Optional[list[Element]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to
conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ProfileIdentifierType/core, '
                   'core:ProfileIdentifierType/software, '
                   'core:ProfileIdentifierType/simpleLicensing, '
                   'core:ProfileIdentifierType/expandedLicensing, '
                   'core:ProfileIdentifierType/security, '
                   'core:ProfileIdentifierType/build, core:ProfileIdentifierType/ai, '
                   'core:ProfileIdentifierType/dataset, '
                   'core:ProfileIdentifierType/extension, '
                   'core:ProfileIdentifierType/lite]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance'} })
    rootElement: Optional[list[Element]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/rootElement'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class Tool(Element):
    """
    An element of hardware and/or software utilized to carry out a particular function.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/Tool',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class LicenseAddition(Element):
    """
    Abstract class for additional text intended to be added to a License, but
    which is not itself a standalone License.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue '
                                                'expandedlicensing:LicenseAddition }'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'additionText': {'multivalued': False,
                                         'name': 'additionText',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string',
                                         'required': True},
                        'isDeprecatedAdditionId': {'multivalued': False,
                                                   'name': 'isDeprecatedAdditionId',
                                                   'notes': ['SHACL nodeKind: '
                                                             'sh:Literal'],
                                                   'range': 'boolean'},
                        'licenseXml': {'multivalued': False,
                                       'name': 'licenseXml',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'string'},
                        'obsoletedBy': {'multivalued': False,
                                        'name': 'obsoletedBy',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string'},
                        'seeAlso': {'multivalued': True,
                                    'name': 'seeAlso',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'uri'},
                        'standardAdditionTemplate': {'multivalued': False,
                                                     'name': 'standardAdditionTemplate',
                                                     'notes': ['SHACL nodeKind: '
                                                               'sh:Literal'],
                                                     'range': 'string'}}})

    standardAdditionTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a LicenseAddition, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardAdditionTemplate'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license
XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'} })
    isDeprecatedAdditionId: Optional[bool] = Field(default=None, description="""Specifies whether an additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedAdditionId'} })
    additionText: str = Field(default=..., description="""Identifies the full text of a LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/additionText'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class CustomLicenseAddition(LicenseAddition):
    """
    A license addition that is not listed on the SPDX Exceptions List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    standardAdditionTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a LicenseAddition, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardAdditionTemplate'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license
XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'} })
    isDeprecatedAdditionId: Optional[bool] = Field(default=None, description="""Specifies whether an additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedAdditionId'} })
    additionText: str = Field(default=..., description="""Identifies the full text of a LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/additionText'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class ListedLicenseException(LicenseAddition):
    """
    A license exception that is listed on the SPDX Exceptions list.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'deprecatedVersion': {'multivalued': False,
                                              'name': 'deprecatedVersion',
                                              'notes': ['SHACL nodeKind: sh:Literal'],
                                              'range': 'string'},
                        'listVersionAdded': {'multivalued': False,
                                             'name': 'listVersionAdded',
                                             'notes': ['SHACL nodeKind: sh:Literal'],
                                             'range': 'string'}}})

    listVersionAdded: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this ListedLicense or
ListedLicenseException identifier was first added.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/listVersionAdded'} })
    deprecatedVersion: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this license or exception
identifier was deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/deprecatedVersion'} })
    standardAdditionTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a LicenseAddition, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardAdditionTemplate'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license
XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'} })
    isDeprecatedAdditionId: Optional[bool] = Field(default=None, description="""Specifies whether an additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedAdditionId'} })
    additionText: str = Field(default=..., description="""Identifies the full text of a LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/additionText'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class CdxPropertyEntry(ConfiguredBaseModel):
    """
    A property name with an associated value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'cdxPropName': {'multivalued': False,
                                        'name': 'cdxPropName',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string',
                                        'required': True},
                        'cdxPropValue': {'multivalued': False,
                                         'name': 'cdxPropValue',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string'}}})

    cdxPropValue: Optional[str] = Field(default=None, description="""A value used in a CdxPropertyEntry name-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CdxPropertyEntry'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Extension/cdxPropValue'} })
    cdxPropName: str = Field(default=..., description="""A name used in a CdxPropertyEntry name-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CdxPropertyEntry'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Extension/cdxPropName'} })


class Extension(ConfiguredBaseModel):
    """
    A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Extension/Extension',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    pass


class CdxPropertiesExtension(Extension):
    """
    A type of extension consisting of a list of name value pairs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'cdxProperty': {'multivalued': True,
                                        'name': 'cdxProperty',
                                        'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                        'range': 'CdxPropertyEntry',
                                        'required': True}}})

    cdxProperty: list[CdxPropertyEntry] = Field(default=..., description="""Provides a map of a property names to a values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CdxPropertiesExtension'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Extension/cdxProperty'} })


class VulnAssessmentRelationship(Relationship):
    """
    Abstract ancestor class for all vulnerability assessments
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue '
                                                'security:VulnAssessmentRelationship '
                                                '}'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'assessedElement': {'multivalued': False,
                                            'name': 'assessedElement',
                                            'notes': ['SHACL nodeKind: sh:IRI'],
                                            'range': 'SoftwareArtifact'},
                        'modifiedTime': {'multivalued': False,
                                         'name': 'modifiedTime',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                         'range': 'datetime'},
                        'publishedTime': {'multivalued': False,
                                          'name': 'publishedTime',
                                          'notes': ['SHACL nodeKind: sh:Literal'],
                                          'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                          'range': 'datetime'},
                        'suppliedBy': {'multivalued': False,
                                       'name': 'suppliedBy',
                                       'notes': ['SHACL nodeKind: sh:IRI'],
                                       'range': 'Agent'},
                        'withdrawnTime': {'multivalued': False,
                                          'name': 'withdrawnTime',
                                          'notes': ['SHACL nodeKind: sh:Literal'],
                                          'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                          'range': 'datetime'}}})

    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV2VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 2.0 assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'score': {'multivalued': False,
                                  'name': 'score',
                                  'notes': ['SHACL nodeKind: sh:Literal'],
                                  'range': 'decimal',
                                  'required': True},
                        'vectorString': {'multivalued': False,
                                         'name': 'vectorString',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string',
                                         'required': True}}})

    vectorString: str = Field(default=..., description="""Specifies the CVSS vector string for a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vectorString'} })
    score: Decimal = Field(default=..., description="""Provides a numerical (0-10) representation of the severity of a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/score'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV3VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 3 assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'score': {'multivalued': False,
                                  'name': 'score',
                                  'notes': ['SHACL nodeKind: sh:Literal'],
                                  'range': 'decimal',
                                  'required': True},
                        'severity': {'multivalued': False,
                                     'name': 'severity',
                                     'notes': ['SHACL nodeKind: sh:IRI',
                                               'SHACL in: '
                                               '[security:CvssSeverityType/critical, '
                                               'security:CvssSeverityType/high, '
                                               'security:CvssSeverityType/medium, '
                                               'security:CvssSeverityType/low, '
                                               'security:CvssSeverityType/none]'],
                                     'range': 'CvssSeverityType',
                                     'required': True},
                        'vectorString': {'multivalued': False,
                                         'name': 'vectorString',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string',
                                         'required': True}}})

    severity: CvssSeverityType = Field(default=..., description="""Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [security:CvssSeverityType/critical, '
                   'security:CvssSeverityType/high, security:CvssSeverityType/medium, '
                   'security:CvssSeverityType/low, security:CvssSeverityType/none]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/severity'} })
    vectorString: str = Field(default=..., description="""Specifies the CVSS vector string for a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vectorString'} })
    score: Decimal = Field(default=..., description="""Provides a numerical (0-10) representation of the severity of a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/score'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV4VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 4 assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'score': {'multivalued': False,
                                  'name': 'score',
                                  'notes': ['SHACL nodeKind: sh:Literal'],
                                  'range': 'decimal',
                                  'required': True},
                        'severity': {'multivalued': False,
                                     'name': 'severity',
                                     'notes': ['SHACL nodeKind: sh:IRI',
                                               'SHACL in: '
                                               '[security:CvssSeverityType/critical, '
                                               'security:CvssSeverityType/high, '
                                               'security:CvssSeverityType/medium, '
                                               'security:CvssSeverityType/low, '
                                               'security:CvssSeverityType/none]'],
                                     'range': 'CvssSeverityType',
                                     'required': True},
                        'vectorString': {'multivalued': False,
                                         'name': 'vectorString',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string',
                                         'required': True}}})

    severity: CvssSeverityType = Field(default=..., description="""Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [security:CvssSeverityType/critical, '
                   'security:CvssSeverityType/high, security:CvssSeverityType/medium, '
                   'security:CvssSeverityType/low, security:CvssSeverityType/none]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/severity'} })
    vectorString: str = Field(default=..., description="""Specifies the CVSS vector string for a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vectorString'} })
    score: Decimal = Field(default=..., description="""Provides a numerical (0-10) representation of the severity of a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/score'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class EpssVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an EPSS assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'percentile': {'multivalued': False,
                                       'name': 'percentile',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'decimal',
                                       'required': True},
                        'probability': {'multivalued': False,
                                        'name': 'probability',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'decimal',
                                        'required': True}}})

    percentile: Decimal = Field(default=..., description="""The percentile of the current probability score.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EpssVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/percentile'} })
    probability: Decimal = Field(default=..., description="""A probability score between 0 and 1 of a vulnerability being exploited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EpssVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/probability'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class ExploitCatalogVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an exploit assessment of a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'catalogType': {'multivalued': False,
                                        'name': 'catalogType',
                                        'notes': ['SHACL nodeKind: sh:IRI',
                                                  'SHACL in: '
                                                  '[security:ExploitCatalogType/kev, '
                                                  'security:ExploitCatalogType/other]'],
                                        'required': True},
                        'exploited': {'multivalued': False,
                                      'name': 'exploited',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'boolean',
                                      'required': True},
                        'security_locator': {'multivalued': False,
                                             'name': 'security_locator',
                                             'notes': ['SHACL nodeKind: sh:Literal'],
                                             'range': 'uri',
                                             'required': True}}})

    exploited: bool = Field(default=..., description="""Describe that a CVE is known to have an exploit because it's been listed in an exploit catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExploitCatalogVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/exploited'} })
    security_locator: str = Field(default=..., description="""Provides the location of an exploit catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExploitCatalogVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/locator'} })
    catalogType: Union[ExploitCatalogType, str] = Field(default=..., description="""Specifies the exploit catalog type.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'ExploitCatalogType'}, {'range': 'string'}],
         'domain_of': ['ExploitCatalogVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [security:ExploitCatalogType/kev, '
                   'security:ExploitCatalogType/other]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/catalogType'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class SsvcVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an SSVC assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'decisionType': {'multivalued': False,
                                         'name': 'decisionType',
                                         'notes': ['SHACL nodeKind: sh:IRI',
                                                   'SHACL in: '
                                                   '[security:SsvcDecisionType/act, '
                                                   'security:SsvcDecisionType/attend, '
                                                   'security:SsvcDecisionType/track, '
                                                   'security:SsvcDecisionType/trackStar]'],
                                         'range': 'SsvcDecisionType',
                                         'required': True}}})

    decisionType: SsvcDecisionType = Field(default=..., description="""Provide the enumeration of possible decisions in the
[Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsvcVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [security:SsvcDecisionType/act, '
                   'security:SsvcDecisionType/attend, security:SsvcDecisionType/track, '
                   'security:SsvcDecisionType/trackStar]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/decisionType'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class VexVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Abstract ancestor class for all VEX relationships
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue '
                                                'security:VexVulnAssessmentRelationship '
                                                '}'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'statusNotes': {'multivalued': False,
                                        'name': 'statusNotes',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string'},
                        'vexVersion': {'multivalued': False,
                                       'name': 'vexVersion',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'string'}}})

    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class VexAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Connects a vulnerability and an element designating the element as a product
    affected by the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'actionStatement': {'multivalued': False,
                                            'name': 'actionStatement',
                                            'notes': ['SHACL nodeKind: sh:Literal'],
                                            'range': 'string',
                                            'required': True},
                        'actionStatementTime': {'multivalued': False,
                                                'name': 'actionStatementTime',
                                                'notes': ['SHACL nodeKind: sh:Literal'],
                                                'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                                'range': 'datetime'}}})

    actionStatement: str = Field(default=..., description="""Provides advise on how to mitigate or remediate a vulnerability when a VEX product
is affected by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexAffectedVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/actionStatement'} })
    actionStatementTime: Optional[datetime ] = Field(default=None, description="""Records the time when a recommended action was communicated in a VEX statement
to mitigate a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexAffectedVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/actionStatementTime'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('actionStatementTime')
    def pattern_actionStatementTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid actionStatementTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid actionStatementTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class VexFixedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and elements representing products (in the VEX sense) where
    a fix has been applied and are no longer affected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class VexNotAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and one or more elements designating the latter as products
    not affected by the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'impactStatement': {'multivalued': False,
                                            'name': 'impactStatement',
                                            'notes': ['SHACL nodeKind: sh:Literal'],
                                            'range': 'string'},
                        'impactStatementTime': {'multivalued': False,
                                                'name': 'impactStatementTime',
                                                'notes': ['SHACL nodeKind: sh:Literal'],
                                                'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                                'range': 'datetime'},
                        'justificationType': {'multivalued': False,
                                              'name': 'justificationType',
                                              'notes': ['SHACL nodeKind: sh:IRI',
                                                        'SHACL in: '
                                                        '[security:VexJustificationType/componentNotPresent, '
                                                        'security:VexJustificationType/vulnerableCodeNotPresent, '
                                                        'security:VexJustificationType/vulnerableCodeCannotBeControlledByAdversary, '
                                                        'security:VexJustificationType/vulnerableCodeNotInExecutePath, '
                                                        'security:VexJustificationType/inlineMitigationsAlreadyExist]'],
                                              'range': 'VexJustificationType'}}})

    impactStatementTime: Optional[datetime ] = Field(default=None, description="""Timestamp of impact statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexNotAffectedVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/impactStatementTime'} })
    justificationType: Optional[VexJustificationType] = Field(default=None, description="""Impact justification label to be used when linking a vulnerability to an element
representing a VEX product with a VexNotAffectedVulnAssessmentRelationship
relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexNotAffectedVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [security:VexJustificationType/componentNotPresent, '
                   'security:VexJustificationType/vulnerableCodeNotPresent, '
                   'security:VexJustificationType/vulnerableCodeCannotBeControlledByAdversary, '
                   'security:VexJustificationType/vulnerableCodeNotInExecutePath, '
                   'security:VexJustificationType/inlineMitigationsAlreadyExist]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/justificationType'} })
    impactStatement: Optional[str] = Field(default=None, description="""Explains why a VEX product is not affected by a vulnerability. It is an
alternative in VexNotAffectedVulnAssessmentRelationship to the machine-readable
justification label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexNotAffectedVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/impactStatement'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('impactStatementTime')
    def pattern_impactStatementTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid impactStatementTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid impactStatementTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class VexUnderInvestigationVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Designates elements as products where the impact of a vulnerability is being
    investigated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes'} })
    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    assessedElement: Optional[SoftwareArtifact] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was
found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    to: list[Element] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/to'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipCompleteness/incomplete, '
                   'core:RelationshipCompleteness/complete, '
                   'core:RelationshipCompleteness/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'} })
    startTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'} })
    relationshipType: Union[RelationshipType, str] = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RelationshipType'}, {'range': 'string'}],
         'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:RelationshipType/affects, '
                   'core:RelationshipType/amendedBy, core:RelationshipType/ancestorOf, '
                   'core:RelationshipType/availableFrom, '
                   'core:RelationshipType/configures, core:RelationshipType/contains, '
                   'core:RelationshipType/coordinatedBy, '
                   'core:RelationshipType/copiedTo, core:RelationshipType/delegatedTo, '
                   'core:RelationshipType/dependsOn, '
                   'core:RelationshipType/descendantOf, '
                   'core:RelationshipType/describes, '
                   'core:RelationshipType/doesNotAffect, '
                   'core:RelationshipType/expandsTo, '
                   'core:RelationshipType/exploitCreatedBy, '
                   'core:RelationshipType/fixedBy, core:RelationshipType/fixedIn, '
                   'core:RelationshipType/foundBy, core:RelationshipType/generates, '
                   'core:RelationshipType/hasAddedFile, '
                   'core:RelationshipType/hasAssessmentFor, '
                   'core:RelationshipType/hasAssociatedVulnerability, '
                   'core:RelationshipType/hasConcludedLicense, '
                   'core:RelationshipType/hasDataFile, '
                   'core:RelationshipType/hasDeclaredLicense, '
                   'core:RelationshipType/hasDeletedFile, '
                   'core:RelationshipType/hasDependencyManifest, '
                   'core:RelationshipType/hasDistributionArtifact, '
                   'core:RelationshipType/hasDocumentation, '
                   'core:RelationshipType/hasDynamicLink, '
                   'core:RelationshipType/hasEvidence, '
                   'core:RelationshipType/hasExample, core:RelationshipType/hasHost, '
                   'core:RelationshipType/hasInput, core:RelationshipType/hasMetadata, '
                   'core:RelationshipType/hasOptionalComponent, '
                   'core:RelationshipType/hasOptionalDependency, '
                   'core:RelationshipType/hasOutput, '
                   'core:RelationshipType/hasPrerequisite, '
                   'core:RelationshipType/hasProvidedDependency, '
                   'core:RelationshipType/hasRequirement, '
                   'core:RelationshipType/hasSpecification, '
                   'core:RelationshipType/hasStaticLink, '
                   'core:RelationshipType/hasTest, core:RelationshipType/hasTestCase, '
                   'core:RelationshipType/hasVariant, core:RelationshipType/invokedBy, '
                   'core:RelationshipType/modifiedBy, core:RelationshipType/other, '
                   'core:RelationshipType/packagedBy, core:RelationshipType/patchedBy, '
                   'core:RelationshipType/publishedBy, '
                   'core:RelationshipType/reportedBy, '
                   'core:RelationshipType/republishedBy, '
                   'core:RelationshipType/serializedInArtifact, '
                   'core:RelationshipType/testedOn, core:RelationshipType/trainedOn, '
                   'core:RelationshipType/underInvestigationFor, '
                   'core:RelationshipType/usesTool]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'} })
    from_: Element = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/from'} })
    endTime: Optional[datetime ] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('startTime')
    def pattern_startTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid startTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid startTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('endTime')
    def pattern_endTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid endTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid endTime format: {v}"
            raise ValueError(err_msg)
        return v


class Vulnerability(Artifact):
    """
    Specifies a vulnerability and its associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'modifiedTime': {'multivalued': False,
                                         'name': 'modifiedTime',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                         'range': 'datetime'},
                        'publishedTime': {'multivalued': False,
                                          'name': 'publishedTime',
                                          'notes': ['SHACL nodeKind: sh:Literal'],
                                          'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                          'range': 'datetime'},
                        'withdrawnTime': {'multivalued': False,
                                          'name': 'withdrawnTime',
                                          'notes': ['SHACL nodeKind: sh:Literal'],
                                          'pattern': '^\\d\\d\\d\\d-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$',
                                          'range': 'datetime'}}})

    withdrawnTime: Optional[datetime ] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'} })
    modifiedTime: Optional[datetime ] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'} })
    publishedTime: Optional[datetime ] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('withdrawnTime')
    def pattern_withdrawnTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid withdrawnTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid withdrawnTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modifiedTime')
    def pattern_modifiedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid modifiedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid modifiedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publishedTime')
    def pattern_publishedTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publishedTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publishedTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class AnyLicenseInfo(Element):
    """
    Abstract class representing a license combination consisting of one or more licenses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class ConjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information
    where all elements apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'member': {'multivalued': True,
                                   'name': 'member',
                                   'notes': ['SHACL nodeKind: sh:IRI'],
                                   'range': 'AnyLicenseInfo',
                                   'required': True}}})

    member: list[AnyLicenseInfo] = Field(default=..., description="""A license expression participating in a license set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConjunctiveLicenseSet', 'DisjunctiveLicenseSet'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/member'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class DisjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information where
    only one of the elements applies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'member': {'multivalued': True,
                                   'name': 'member',
                                   'notes': ['SHACL nodeKind: sh:IRI'],
                                   'range': 'AnyLicenseInfo',
                                   'required': True}}})

    member: list[AnyLicenseInfo] = Field(default=..., description="""A license expression participating in a license set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConjunctiveLicenseSet', 'DisjunctiveLicenseSet'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/member'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class ExtendableLicense(AnyLicenseInfo):
    """
    Abstract class representing a License or an OrLaterOperator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class IndividualLicensingInfo(AnyLicenseInfo):
    """
    A concrete subclass of AnyLicenseInfo used by Individuals in the
    ExpandedLicensing profile.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class License(ExtendableLicense):
    """
    Abstract class for the portion of an AnyLicenseInfo representing a license.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue '
                                                'expandedlicensing:License }'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'isDeprecatedLicenseId': {'multivalued': False,
                                                  'name': 'isDeprecatedLicenseId',
                                                  'notes': ['SHACL nodeKind: '
                                                            'sh:Literal'],
                                                  'range': 'boolean'},
                        'isFsfLibre': {'multivalued': False,
                                       'name': 'isFsfLibre',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'boolean'},
                        'isOsiApproved': {'multivalued': False,
                                          'name': 'isOsiApproved',
                                          'notes': ['SHACL nodeKind: sh:Literal'],
                                          'range': 'boolean'},
                        'licenseText': {'multivalued': False,
                                        'name': 'licenseText',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string',
                                        'required': True},
                        'licenseXml': {'multivalued': False,
                                       'name': 'licenseXml',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'string'},
                        'obsoletedBy': {'multivalued': False,
                                        'name': 'obsoletedBy',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string'},
                        'seeAlso': {'multivalued': True,
                                    'name': 'seeAlso',
                                    'notes': ['SHACL nodeKind: sh:Literal'],
                                    'range': 'uri'},
                        'standardLicenseHeader': {'multivalued': False,
                                                  'name': 'standardLicenseHeader',
                                                  'notes': ['SHACL nodeKind: '
                                                            'sh:Literal'],
                                                  'range': 'string'},
                        'standardLicenseTemplate': {'multivalued': False,
                                                    'name': 'standardLicenseTemplate',
                                                    'notes': ['SHACL nodeKind: '
                                                              'sh:Literal'],
                                                    'range': 'string'}}})

    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'} })
    standardLicenseHeader: Optional[str] = Field(default=None, description="""Provides a License author's preferred text to indicate that a file is covered
by the License.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseHeader'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'} })
    isFsfLibre: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as free by the
Free Software Foundation (FSF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isFsfLibre'} })
    isDeprecatedLicenseId: Optional[bool] = Field(default=None, description="""Specifies whether a license or additional text identifier has been marked as
deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedLicenseId'} })
    isOsiApproved: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as approved by the
Open Source Initiative (OSI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isOsiApproved'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license
XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'} })
    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'SimpleLicensingText'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText'} })
    standardLicenseTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a License, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseTemplate'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class CustomLicense(License):
    """
    A license that is not listed on the SPDX License List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense',
         'from_schema': 'https://w3id.org/lmodel/spdx'})

    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'} })
    standardLicenseHeader: Optional[str] = Field(default=None, description="""Provides a License author's preferred text to indicate that a file is covered
by the License.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseHeader'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'} })
    isFsfLibre: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as free by the
Free Software Foundation (FSF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isFsfLibre'} })
    isDeprecatedLicenseId: Optional[bool] = Field(default=None, description="""Specifies whether a license or additional text identifier has been marked as
deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedLicenseId'} })
    isOsiApproved: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as approved by the
Open Source Initiative (OSI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isOsiApproved'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license
XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'} })
    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'SimpleLicensingText'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText'} })
    standardLicenseTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a License, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseTemplate'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class ListedLicense(License):
    """
    A license that is listed on the SPDX License List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'deprecatedVersion': {'multivalued': False,
                                              'name': 'deprecatedVersion',
                                              'notes': ['SHACL nodeKind: sh:Literal'],
                                              'range': 'string'},
                        'listVersionAdded': {'multivalued': False,
                                             'name': 'listVersionAdded',
                                             'notes': ['SHACL nodeKind: sh:Literal'],
                                             'range': 'string'}}})

    deprecatedVersion: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this license or exception
identifier was deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/deprecatedVersion'} })
    listVersionAdded: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this ListedLicense or
ListedLicenseException identifier was first added.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/listVersionAdded'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated
License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'} })
    standardLicenseHeader: Optional[str] = Field(default=None, description="""Provides a License author's preferred text to indicate that a file is covered
by the License.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseHeader'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'} })
    isFsfLibre: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as free by the
Free Software Foundation (FSF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isFsfLibre'} })
    isDeprecatedLicenseId: Optional[bool] = Field(default=None, description="""Specifies whether a license or additional text identifier has been marked as
deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedLicenseId'} })
    isOsiApproved: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as approved by the
Open Source Initiative (OSI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isOsiApproved'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license
XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'} })
    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'SimpleLicensingText'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText'} })
    standardLicenseTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a License, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseTemplate'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class OrLaterOperator(ExtendableLicense):
    """
    Portion of an AnyLicenseInfo representing this version, or any later version,
    of the indicated License.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'subjectLicense': {'multivalued': False,
                                           'name': 'subjectLicense',
                                           'notes': ['SHACL nodeKind: sh:IRI'],
                                           'range': 'License',
                                           'required': True}}})

    subjectLicense: License = Field(default=..., description="""A License participating in an 'or later' model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OrLaterOperator'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectLicense'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class WithAdditionOperator(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a License which has additional
    text applied to it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'subjectAddition': {'multivalued': False,
                                            'name': 'subjectAddition',
                                            'notes': ['SHACL nodeKind: sh:IRI'],
                                            'range': 'LicenseAddition',
                                            'required': True},
                        'subjectExtendableLicense': {'multivalued': False,
                                                     'name': 'subjectExtendableLicense',
                                                     'notes': ['SHACL nodeKind: '
                                                               'sh:IRI'],
                                                     'range': 'ExtendableLicense',
                                                     'required': True}}})

    subjectExtendableLicense: ExtendableLicense = Field(default=..., description="""A License participating in a 'with addition' model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithAdditionOperator'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectExtendableLicense'} })
    subjectAddition: LicenseAddition = Field(default=..., description="""A LicenseAddition participating in a 'with addition' model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithAdditionOperator'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectAddition'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class LicenseExpression(AnyLicenseInfo):
    """
    An SPDX Element containing an SPDX license expression string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'customIdToUri': {'multivalued': True,
                                          'name': 'customIdToUri',
                                          'notes': ['SHACL nodeKind: '
                                                    'sh:BlankNodeOrIRI'],
                                          'range': 'DictionaryEntry'},
                        'licenseExpression': {'multivalued': False,
                                              'name': 'licenseExpression',
                                              'notes': ['SHACL nodeKind: sh:Literal'],
                                              'range': 'string',
                                              'required': True},
                        'licenseListVersion': {'multivalued': False,
                                               'name': 'licenseListVersion',
                                               'notes': ['SHACL nodeKind: sh:Literal'],
                                               'pattern': '^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$',
                                               'range': 'string'}}})

    customIdToUri: Optional[list[DictionaryEntry]] = Field(default=None, description="""Maps a LicenseRef or AdditionRef string for a Custom License or a Custom
License Addition to its URI ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseExpression'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/customIdToUri'} })
    licenseExpression: str = Field(default=..., description="""A string in the license expression format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseExpression'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseExpression'} })
    licenseListVersion: Optional[str] = Field(default=None, description="""The version of the SPDX License List used in the license expression.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseExpression'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseListVersion'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('licenseListVersion')
    def pattern_licenseListVersion(cls, v):
        pattern=re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid licenseListVersion format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid licenseListVersion format: {v}"
            raise ValueError(err_msg)
        return v


class SimpleLicensingText(Element):
    """
    A license or addition that is not listed on the SPDX License List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'licenseText': {'multivalued': False,
                                        'name': 'licenseText',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string',
                                        'required': True}}})

    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'SimpleLicensingText'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class ContentIdentifier(IntegrityMethod):
    """
    A canonical, unique, immutable identifier
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:BlankNodeOrIRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'contentIdentifierType': {'multivalued': False,
                                                  'name': 'contentIdentifierType',
                                                  'notes': ['SHACL nodeKind: sh:IRI',
                                                            'SHACL in: '
                                                            '[software:ContentIdentifierType/gitoid, '
                                                            'software:ContentIdentifierType/swhid]'],
                                                  'range': 'ContentIdentifierType',
                                                  'required': True},
                        'contentIdentifierValue': {'multivalued': False,
                                                   'name': 'contentIdentifierValue',
                                                   'notes': ['SHACL nodeKind: '
                                                             'sh:Literal'],
                                                   'range': 'uri',
                                                   'required': True}}})

    contentIdentifierValue: str = Field(default=..., description="""Specifies the value of the content identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentIdentifier'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifierValue'} })
    contentIdentifierType: ContentIdentifierType = Field(default=..., description="""Specifies the type of the content identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentIdentifier'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:ContentIdentifierType/gitoid, '
                   'software:ContentIdentifierType/swhid]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifierType'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })


class Sbom(Bom):
    """
    A collection of SPDX Elements describing a single package.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/Sbom',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'sbomType': {'multivalued': True,
                                     'name': 'sbomType',
                                     'notes': ['SHACL nodeKind: sh:IRI',
                                               'SHACL in: [software:SbomType/design, '
                                               'software:SbomType/source, '
                                               'software:SbomType/build, '
                                               'software:SbomType/deployed, '
                                               'software:SbomType/runtime, '
                                               'software:SbomType/analyzed]'],
                                     'range': 'SbomType'}}})

    sbomType: Optional[list[SbomType]] = Field(default=None, description="""Provides information about the type of an SBOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sbom'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SbomType/design, software:SbomType/source, '
                   'software:SbomType/build, software:SbomType/deployed, '
                   'software:SbomType/runtime, software:SbomType/analyzed]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/sbomType'} })
    context: Optional[str] = Field(default=None, description="""Gives information about the circumstances or unifying properties
that Elements of the bundle have been assembled under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/context'} })
    element: Optional[list[Element]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to
conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:ProfileIdentifierType/core, '
                   'core:ProfileIdentifierType/software, '
                   'core:ProfileIdentifierType/simpleLicensing, '
                   'core:ProfileIdentifierType/expandedLicensing, '
                   'core:ProfileIdentifierType/security, '
                   'core:ProfileIdentifierType/build, core:ProfileIdentifierType/ai, '
                   'core:ProfileIdentifierType/dataset, '
                   'core:ProfileIdentifierType/extension, '
                   'core:ProfileIdentifierType/lite]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance'} })
    rootElement: Optional[list[Element]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/rootElement'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })


class SoftwareArtifact(Artifact):
    """
    A distinct article or unit related to Software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'shacl_message': {'tag': 'shacl_message',
                                           'value': 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact '
                                                    'is an abstract class and should '
                                                    'not be instantiated directly. '
                                                    'Instantiate a subclass instead.'},
                         'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'},
                         'shacl_not': {'tag': 'shacl_not',
                                       'value': '{ sh:hasValue '
                                                'software:SoftwareArtifact }'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'additionalPurpose': {'multivalued': True,
                                              'name': 'additionalPurpose',
                                              'notes': ['SHACL nodeKind: sh:IRI',
                                                        'SHACL in: '
                                                        '[software:SoftwarePurpose/application, '
                                                        'software:SoftwarePurpose/archive, '
                                                        'software:SoftwarePurpose/bom, '
                                                        'software:SoftwarePurpose/configuration, '
                                                        'software:SoftwarePurpose/container, '
                                                        'software:SoftwarePurpose/data, '
                                                        'software:SoftwarePurpose/device, '
                                                        'software:SoftwarePurpose/diskImage, '
                                                        'software:SoftwarePurpose/deviceDriver, '
                                                        'software:SoftwarePurpose/documentation, '
                                                        'software:SoftwarePurpose/evidence, '
                                                        'software:SoftwarePurpose/executable, '
                                                        'software:SoftwarePurpose/file, '
                                                        'software:SoftwarePurpose/filesystemImage, '
                                                        'software:SoftwarePurpose/firmware, '
                                                        'software:SoftwarePurpose/framework, '
                                                        'software:SoftwarePurpose/install, '
                                                        'software:SoftwarePurpose/library, '
                                                        'software:SoftwarePurpose/manifest, '
                                                        'software:SoftwarePurpose/model, '
                                                        'software:SoftwarePurpose/module, '
                                                        'software:SoftwarePurpose/operatingSystem, '
                                                        'software:SoftwarePurpose/other, '
                                                        'software:SoftwarePurpose/patch, '
                                                        'software:SoftwarePurpose/platform, '
                                                        'software:SoftwarePurpose/requirement, '
                                                        'software:SoftwarePurpose/source, '
                                                        'software:SoftwarePurpose/specification, '
                                                        'software:SoftwarePurpose/test]']},
                        'attributionText': {'multivalued': True,
                                            'name': 'attributionText',
                                            'notes': ['SHACL nodeKind: sh:Literal'],
                                            'range': 'string'},
                        'contentIdentifier': {'multivalued': True,
                                              'name': 'contentIdentifier',
                                              'notes': ['SHACL nodeKind: '
                                                        'sh:BlankNodeOrIRI'],
                                              'range': 'ContentIdentifier'},
                        'copyrightText': {'multivalued': False,
                                          'name': 'copyrightText',
                                          'notes': ['SHACL nodeKind: sh:Literal'],
                                          'range': 'string'},
                        'primaryPurpose': {'multivalued': False,
                                           'name': 'primaryPurpose',
                                           'notes': ['SHACL nodeKind: sh:IRI',
                                                     'SHACL in: '
                                                     '[software:SoftwarePurpose/application, '
                                                     'software:SoftwarePurpose/archive, '
                                                     'software:SoftwarePurpose/bom, '
                                                     'software:SoftwarePurpose/configuration, '
                                                     'software:SoftwarePurpose/container, '
                                                     'software:SoftwarePurpose/data, '
                                                     'software:SoftwarePurpose/device, '
                                                     'software:SoftwarePurpose/diskImage, '
                                                     'software:SoftwarePurpose/deviceDriver, '
                                                     'software:SoftwarePurpose/documentation, '
                                                     'software:SoftwarePurpose/evidence, '
                                                     'software:SoftwarePurpose/executable, '
                                                     'software:SoftwarePurpose/file, '
                                                     'software:SoftwarePurpose/filesystemImage, '
                                                     'software:SoftwarePurpose/firmware, '
                                                     'software:SoftwarePurpose/framework, '
                                                     'software:SoftwarePurpose/install, '
                                                     'software:SoftwarePurpose/library, '
                                                     'software:SoftwarePurpose/manifest, '
                                                     'software:SoftwarePurpose/model, '
                                                     'software:SoftwarePurpose/module, '
                                                     'software:SoftwarePurpose/operatingSystem, '
                                                     'software:SoftwarePurpose/other, '
                                                     'software:SoftwarePurpose/patch, '
                                                     'software:SoftwarePurpose/platform, '
                                                     'software:SoftwarePurpose/requirement, '
                                                     'software:SoftwarePurpose/source, '
                                                     'software:SoftwarePurpose/specification, '
                                                     'software:SoftwarePurpose/test]']}}})

    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'} })
    primaryPurpose: Optional[Union[SoftwarePurpose, str]] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'} })
    additionalPurpose: Optional[list[Union[SoftwarePurpose, str]]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class File(SoftwareArtifact):
    """
    Refers to any object that stores content on a computer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/File',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'contentType': {'multivalued': False,
                                        'name': 'contentType',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'pattern': '^[^\\/]+\\/[^\\/]+$',
                                        'range': 'string'},
                        'fileKind': {'multivalued': False,
                                     'name': 'fileKind',
                                     'notes': ['SHACL nodeKind: sh:IRI',
                                               'SHACL in: [software:FileKindType/file, '
                                               'software:FileKindType/directory]'],
                                     'range': 'FileKindType'}}})

    fileKind: Optional[FileKindType] = Field(default=None, description="""Describes if a given file is a directory or non-directory kind of file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:FileKindType/file, '
                   'software:FileKindType/directory]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/fileKind'} })
    contentType: Optional[str] = Field(default=None, description="""Provides information about the content type of an Element or a Property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation', 'ExternalRef', 'File'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/contentType'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'} })
    primaryPurpose: Optional[Union[SoftwarePurpose, str]] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'} })
    additionalPurpose: Optional[list[Union[SoftwarePurpose, str]]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('contentType')
    def pattern_contentType(cls, v):
        pattern=re.compile(r"^[^\/]+\/[^\/]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid contentType format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid contentType format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class Package(SoftwareArtifact):
    """
    Refers to any unit of content that can be associated with a distribution of
    software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/Package',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'downloadLocation': {'multivalued': False,
                                             'name': 'downloadLocation',
                                             'notes': ['SHACL nodeKind: sh:Literal'],
                                             'range': 'uri'},
                        'homePage': {'multivalued': False,
                                     'name': 'homePage',
                                     'notes': ['SHACL nodeKind: sh:Literal'],
                                     'range': 'uri'},
                        'packageUrl': {'multivalued': False,
                                       'name': 'packageUrl',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'uri'},
                        'packageVersion': {'multivalued': False,
                                           'name': 'packageVersion',
                                           'notes': ['SHACL nodeKind: sh:Literal'],
                                           'range': 'string'},
                        'sourceInfo': {'multivalued': False,
                                       'name': 'sourceInfo',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'string'}}})

    sourceInfo: Optional[str] = Field(default=None, description="""Records any relevant background information or additional comments
about the origin of the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/sourceInfo'} })
    homePage: Optional[str] = Field(default=None, description="""A place for the SPDX document creator to record a website that serves as the
package's home page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/homePage'} })
    downloadLocation: Optional[str] = Field(default=None, description="""Identifies the download Uniform Resource Identifier for the package at the time
that the document was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/downloadLocation'} })
    packageVersion: Optional[str] = Field(default=None, description="""Identify the version of a package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/packageVersion'} })
    packageUrl: Optional[str] = Field(default=None, description="""Provides a place for the SPDX data creator to record the package URL string
(in accordance with the Package URL specification) for a software Package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/packageUrl'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'} })
    primaryPurpose: Optional[Union[SoftwarePurpose, str]] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'} })
    additionalPurpose: Optional[list[Union[SoftwarePurpose, str]]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class AIPackage(Package):
    """
    Specifies an AI package and its associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/AIPackage',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'autonomyType': {'multivalued': False,
                                         'name': 'autonomyType',
                                         'notes': ['SHACL nodeKind: sh:IRI',
                                                   'SHACL in: [core:PresenceType/yes, '
                                                   'core:PresenceType/no, '
                                                   'core:PresenceType/noAssertion]'],
                                         'range': 'PresenceType'},
                        'domain': {'multivalued': True,
                                   'name': 'domain',
                                   'notes': ['SHACL nodeKind: sh:Literal'],
                                   'range': 'string'},
                        'energyConsumption': {'multivalued': False,
                                              'name': 'energyConsumption',
                                              'notes': ['SHACL nodeKind: '
                                                        'sh:BlankNodeOrIRI'],
                                              'range': 'EnergyConsumption'},
                        'hyperparameter': {'multivalued': True,
                                           'name': 'hyperparameter',
                                           'notes': ['SHACL nodeKind: '
                                                     'sh:BlankNodeOrIRI'],
                                           'range': 'DictionaryEntry'},
                        'informationAboutApplication': {'multivalued': False,
                                                        'name': 'informationAboutApplication',
                                                        'notes': ['SHACL nodeKind: '
                                                                  'sh:Literal'],
                                                        'range': 'string'},
                        'informationAboutTraining': {'multivalued': False,
                                                     'name': 'informationAboutTraining',
                                                     'notes': ['SHACL nodeKind: '
                                                               'sh:Literal'],
                                                     'range': 'string'},
                        'limitation': {'multivalued': False,
                                       'name': 'limitation',
                                       'notes': ['SHACL nodeKind: sh:Literal'],
                                       'range': 'string'},
                        'metric': {'multivalued': True,
                                   'name': 'metric',
                                   'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                   'range': 'DictionaryEntry'},
                        'metricDecisionThreshold': {'multivalued': True,
                                                    'name': 'metricDecisionThreshold',
                                                    'notes': ['SHACL nodeKind: '
                                                              'sh:BlankNodeOrIRI'],
                                                    'range': 'DictionaryEntry'},
                        'modelDataPreprocessing': {'multivalued': True,
                                                   'name': 'modelDataPreprocessing',
                                                   'notes': ['SHACL nodeKind: '
                                                             'sh:Literal'],
                                                   'range': 'string'},
                        'modelExplainability': {'multivalued': True,
                                                'name': 'modelExplainability',
                                                'notes': ['SHACL nodeKind: sh:Literal'],
                                                'range': 'string'},
                        'safetyRiskAssessment': {'multivalued': False,
                                                 'name': 'safetyRiskAssessment',
                                                 'notes': ['SHACL nodeKind: sh:IRI',
                                                           'SHACL in: '
                                                           '[ai:SafetyRiskAssessmentType/serious, '
                                                           'ai:SafetyRiskAssessmentType/high, '
                                                           'ai:SafetyRiskAssessmentType/medium, '
                                                           'ai:SafetyRiskAssessmentType/low]'],
                                                 'range': 'SafetyRiskAssessmentType'},
                        'standardCompliance': {'multivalued': True,
                                               'name': 'standardCompliance',
                                               'notes': ['SHACL nodeKind: sh:Literal'],
                                               'range': 'string'},
                        'typeOfModel': {'multivalued': True,
                                        'name': 'typeOfModel',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string'},
                        'useSensitivePersonalInformation': {'multivalued': False,
                                                            'name': 'useSensitivePersonalInformation',
                                                            'notes': ['SHACL nodeKind: '
                                                                      'sh:IRI',
                                                                      'SHACL in: '
                                                                      '[core:PresenceType/yes, '
                                                                      'core:PresenceType/no, '
                                                                      'core:PresenceType/noAssertion]'],
                                                            'range': 'PresenceType'}}})

    informationAboutTraining: Optional[str] = Field(default=None, description="""Describes relevant information about different steps of the training process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/informationAboutTraining'} })
    modelDataPreprocessing: Optional[list[str]] = Field(default=None, description="""Describes all the preprocessing steps applied to the training data before the
model training.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/modelDataPreprocessing'} })
    typeOfModel: Optional[list[str]] = Field(default=None, description="""Records the type of the model used in the AI software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/typeOfModel'} })
    safetyRiskAssessment: Optional[SafetyRiskAssessmentType] = Field(default=None, description="""Records the results of general safety risk assessment of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [ai:SafetyRiskAssessmentType/serious, '
                   'ai:SafetyRiskAssessmentType/high, '
                   'ai:SafetyRiskAssessmentType/medium, '
                   'ai:SafetyRiskAssessmentType/low]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/safetyRiskAssessment'} })
    metricDecisionThreshold: Optional[list[DictionaryEntry]] = Field(default=None, description="""Captures the threshold that was used for computation of a metric described in
the metric field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/metricDecisionThreshold'} })
    useSensitivePersonalInformation: Optional[PresenceType] = Field(default=None, description="""Records if sensitive personal information is used during model training or
could be used during the inference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:PresenceType/yes, core:PresenceType/no, '
                   'core:PresenceType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/useSensitivePersonalInformation'} })
    energyConsumption: Optional[EnergyConsumption] = Field(default=None, description="""Indicates the amount of energy consumption incurred by an AI model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/energyConsumption'} })
    limitation: Optional[str] = Field(default=None, description="""Captures a limitation of the AI software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/limitation'} })
    hyperparameter: Optional[list[DictionaryEntry]] = Field(default=None, description="""Records a hyperparameter used to build the AI model contained in the AI
package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/hyperparameter'} })
    autonomyType: Optional[PresenceType] = Field(default=None, description="""Indicates whether the system can perform a decision or action without human
involvement or guidance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:PresenceType/yes, core:PresenceType/no, '
                   'core:PresenceType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/autonomyType'} })
    domain: Optional[list[str]] = Field(default=None, description="""Captures the domain in which the AI package can be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/domain'} })
    modelExplainability: Optional[list[str]] = Field(default=None, description="""Describes methods that can be used to explain the results from the AI model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/modelExplainability'} })
    informationAboutApplication: Optional[str] = Field(default=None, description="""Provides relevant information about the AI software, not including the model
description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/informationAboutApplication'} })
    metric: Optional[list[DictionaryEntry]] = Field(default=None, description="""Records the measurement of prediction quality of the AI model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/metric'} })
    standardCompliance: Optional[list[str]] = Field(default=None, description="""Captures a standard that is being complied with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/AI/standardCompliance'} })
    sourceInfo: Optional[str] = Field(default=None, description="""Records any relevant background information or additional comments
about the origin of the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/sourceInfo'} })
    homePage: Optional[str] = Field(default=None, description="""A place for the SPDX document creator to record a website that serves as the
package's home page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/homePage'} })
    downloadLocation: Optional[str] = Field(default=None, description="""Identifies the download Uniform Resource Identifier for the package at the time
that the document was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/downloadLocation'} })
    packageVersion: Optional[str] = Field(default=None, description="""Identify the version of a package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/packageVersion'} })
    packageUrl: Optional[str] = Field(default=None, description="""Provides a place for the SPDX data creator to record the package URL string
(in accordance with the Package URL specification) for a software Package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/packageUrl'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'} })
    primaryPurpose: Optional[Union[SoftwarePurpose, str]] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'} })
    additionalPurpose: Optional[list[Union[SoftwarePurpose, str]]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class DatasetPackage(Package):
    """
    Specifies a data package and its associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'anonymizationMethodUsed': {'multivalued': True,
                                                    'name': 'anonymizationMethodUsed',
                                                    'notes': ['SHACL nodeKind: '
                                                              'sh:Literal'],
                                                    'range': 'string'},
                        'confidentialityLevel': {'multivalued': False,
                                                 'name': 'confidentialityLevel',
                                                 'notes': ['SHACL nodeKind: sh:IRI',
                                                           'SHACL in: '
                                                           '[dataset:ConfidentialityLevelType/red, '
                                                           'dataset:ConfidentialityLevelType/amber, '
                                                           'dataset:ConfidentialityLevelType/green, '
                                                           'dataset:ConfidentialityLevelType/clear]'],
                                                 'range': 'ConfidentialityLevelType'},
                        'dataCollectionProcess': {'multivalued': False,
                                                  'name': 'dataCollectionProcess',
                                                  'notes': ['SHACL nodeKind: '
                                                            'sh:Literal'],
                                                  'range': 'string'},
                        'dataPreprocessing': {'multivalued': True,
                                              'name': 'dataPreprocessing',
                                              'notes': ['SHACL nodeKind: sh:Literal'],
                                              'range': 'string'},
                        'datasetAvailability': {'multivalued': False,
                                                'name': 'datasetAvailability',
                                                'notes': ['SHACL nodeKind: sh:IRI',
                                                          'SHACL in: '
                                                          '[dataset:DatasetAvailabilityType/clickthrough, '
                                                          'dataset:DatasetAvailabilityType/directDownload, '
                                                          'dataset:DatasetAvailabilityType/query, '
                                                          'dataset:DatasetAvailabilityType/registration, '
                                                          'dataset:DatasetAvailabilityType/scrapingScript]'],
                                                'range': 'DatasetAvailabilityType'},
                        'datasetNoise': {'multivalued': False,
                                         'name': 'datasetNoise',
                                         'notes': ['SHACL nodeKind: sh:Literal'],
                                         'range': 'string'},
                        'datasetSize': {'minimum_value': 0,
                                        'multivalued': False,
                                        'name': 'datasetSize',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'integer'},
                        'datasetType': {'multivalued': True,
                                        'name': 'datasetType',
                                        'notes': ['SHACL nodeKind: sh:IRI',
                                                  'SHACL in: '
                                                  '[dataset:DatasetType/audio, '
                                                  'dataset:DatasetType/categorical, '
                                                  'dataset:DatasetType/graph, '
                                                  'dataset:DatasetType/image, '
                                                  'dataset:DatasetType/noAssertion, '
                                                  'dataset:DatasetType/numeric, '
                                                  'dataset:DatasetType/other, '
                                                  'dataset:DatasetType/sensor, '
                                                  'dataset:DatasetType/structured, '
                                                  'dataset:DatasetType/syntactic, '
                                                  'dataset:DatasetType/text, '
                                                  'dataset:DatasetType/timeseries, '
                                                  'dataset:DatasetType/timestamp, '
                                                  'dataset:DatasetType/video]'],
                                        'required': True},
                        'datasetUpdateMechanism': {'multivalued': False,
                                                   'name': 'datasetUpdateMechanism',
                                                   'notes': ['SHACL nodeKind: '
                                                             'sh:Literal'],
                                                   'range': 'string'},
                        'hasSensitivePersonalInformation': {'multivalued': False,
                                                            'name': 'hasSensitivePersonalInformation',
                                                            'notes': ['SHACL nodeKind: '
                                                                      'sh:IRI',
                                                                      'SHACL in: '
                                                                      '[core:PresenceType/yes, '
                                                                      'core:PresenceType/no, '
                                                                      'core:PresenceType/noAssertion]'],
                                                            'range': 'PresenceType'},
                        'intendedUse': {'multivalued': False,
                                        'name': 'intendedUse',
                                        'notes': ['SHACL nodeKind: sh:Literal'],
                                        'range': 'string'},
                        'knownBias': {'multivalued': True,
                                      'name': 'knownBias',
                                      'notes': ['SHACL nodeKind: sh:Literal'],
                                      'range': 'string'},
                        'sensor': {'multivalued': True,
                                   'name': 'sensor',
                                   'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                   'range': 'DictionaryEntry'}}})

    datasetSize: Optional[int] = Field(default=None, description="""Captures the size of the dataset.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/datasetSize'} })
    datasetType: list[Union[DatasetType, str]] = Field(default=..., description="""Describes the type of the given dataset.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'DatasetType'}, {'range': 'string'}],
         'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [dataset:DatasetType/audio, '
                   'dataset:DatasetType/categorical, dataset:DatasetType/graph, '
                   'dataset:DatasetType/image, dataset:DatasetType/noAssertion, '
                   'dataset:DatasetType/numeric, dataset:DatasetType/other, '
                   'dataset:DatasetType/sensor, dataset:DatasetType/structured, '
                   'dataset:DatasetType/syntactic, dataset:DatasetType/text, '
                   'dataset:DatasetType/timeseries, dataset:DatasetType/timestamp, '
                   'dataset:DatasetType/video]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/datasetType'} })
    anonymizationMethodUsed: Optional[list[str]] = Field(default=None, description="""Describes the anonymization methods used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/anonymizationMethodUsed'} })
    datasetUpdateMechanism: Optional[str] = Field(default=None, description="""Describes a mechanism to update the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/datasetUpdateMechanism'} })
    dataCollectionProcess: Optional[str] = Field(default=None, description="""Describes how the dataset was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/dataCollectionProcess'} })
    knownBias: Optional[list[str]] = Field(default=None, description="""Records the biases that the dataset is known to encompass.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/knownBias'} })
    sensor: Optional[list[DictionaryEntry]] = Field(default=None, description="""Describes a sensor used for collecting the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/sensor'} })
    dataPreprocessing: Optional[list[str]] = Field(default=None, description="""Describes the preprocessing steps that were applied to the raw data to create the given dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/dataPreprocessing'} })
    intendedUse: Optional[str] = Field(default=None, description="""Describes what the given dataset should be used for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/intendedUse'} })
    confidentialityLevel: Optional[ConfidentialityLevelType] = Field(default=None, description="""Describes the confidentiality level of the data points contained in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [dataset:ConfidentialityLevelType/red, '
                   'dataset:ConfidentialityLevelType/amber, '
                   'dataset:ConfidentialityLevelType/green, '
                   'dataset:ConfidentialityLevelType/clear]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/confidentialityLevel'} })
    datasetAvailability: Optional[DatasetAvailabilityType] = Field(default=None, description="""The field describes the availability of a dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [dataset:DatasetAvailabilityType/clickthrough, '
                   'dataset:DatasetAvailabilityType/directDownload, '
                   'dataset:DatasetAvailabilityType/query, '
                   'dataset:DatasetAvailabilityType/registration, '
                   'dataset:DatasetAvailabilityType/scrapingScript]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/datasetAvailability'} })
    hasSensitivePersonalInformation: Optional[PresenceType] = Field(default=None, description="""Describes if any sensitive personal information is present in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:PresenceType/yes, core:PresenceType/no, '
                   'core:PresenceType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/hasSensitivePersonalInformation'} })
    datasetNoise: Optional[str] = Field(default=None, description="""Describes potentially noisy elements of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Dataset/datasetNoise'} })
    sourceInfo: Optional[str] = Field(default=None, description="""Records any relevant background information or additional comments
about the origin of the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/sourceInfo'} })
    homePage: Optional[str] = Field(default=None, description="""A place for the SPDX document creator to record a website that serves as the
package's home page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/homePage'} })
    downloadLocation: Optional[str] = Field(default=None, description="""Identifies the download Uniform Resource Identifier for the package at the time
that the document was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/downloadLocation'} })
    packageVersion: Optional[str] = Field(default=None, description="""Identify the version of a package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/packageVersion'} })
    packageUrl: Optional[str] = Field(default=None, description="""Provides a place for the SPDX data creator to record the package URL string
(in accordance with the Package URL specification) for a software Package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/packageUrl'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'} })
    primaryPurpose: Optional[Union[SoftwarePurpose, str]] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'} })
    additionalPurpose: Optional[list[Union[SoftwarePurpose, str]]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


class Snippet(SoftwareArtifact):
    """
    Describes a certain part of a file.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'shacl_node_kind': {'tag': 'shacl_node_kind',
                                             'value': 'sh:IRI'}},
         'class_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/Snippet',
         'from_schema': 'https://w3id.org/lmodel/spdx',
         'slot_usage': {'byteRange': {'multivalued': False,
                                      'name': 'byteRange',
                                      'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                      'range': 'PositiveIntegerRange'},
                        'lineRange': {'multivalued': False,
                                      'name': 'lineRange',
                                      'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
                                      'range': 'PositiveIntegerRange'},
                        'snippetFromFile': {'multivalued': False,
                                            'name': 'snippetFromFile',
                                            'notes': ['SHACL nodeKind: sh:IRI'],
                                            'range': 'File',
                                            'required': True}}})

    lineRange: Optional[PositiveIntegerRange] = Field(default=None, description="""Defines the line range in the original host file that the snippet information
applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Snippet'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/lineRange'} })
    snippetFromFile: File = Field(default=..., description="""Defines the original host file that the snippet information applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Snippet'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/snippetFromFile'} })
    byteRange: Optional[PositiveIntegerRange] = Field(default=None, description="""Defines the byte range in the original host file that the snippet information
applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Snippet'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/byteRange'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for
a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'} })
    primaryPurpose: Optional[Union[SoftwarePurpose, str]] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'} })
    additionalPurpose: Optional[list[Union[SoftwarePurpose, str]]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'SoftwarePurpose'}, {'range': 'string'}],
         'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [software:SoftwarePurpose/application, '
                   'software:SoftwarePurpose/archive, software:SoftwarePurpose/bom, '
                   'software:SoftwarePurpose/configuration, '
                   'software:SoftwarePurpose/container, software:SoftwarePurpose/data, '
                   'software:SoftwarePurpose/device, '
                   'software:SoftwarePurpose/diskImage, '
                   'software:SoftwarePurpose/deviceDriver, '
                   'software:SoftwarePurpose/documentation, '
                   'software:SoftwarePurpose/evidence, '
                   'software:SoftwarePurpose/executable, '
                   'software:SoftwarePurpose/file, '
                   'software:SoftwarePurpose/filesystemImage, '
                   'software:SoftwarePurpose/firmware, '
                   'software:SoftwarePurpose/framework, '
                   'software:SoftwarePurpose/install, '
                   'software:SoftwarePurpose/library, '
                   'software:SoftwarePurpose/manifest, software:SoftwarePurpose/model, '
                   'software:SoftwarePurpose/module, '
                   'software:SoftwarePurpose/operatingSystem, '
                   'software:SoftwarePurpose/other, software:SoftwarePurpose/patch, '
                   'software:SoftwarePurpose/platform, '
                   'software:SoftwarePurpose/requirement, '
                   'software:SoftwarePurpose/source, '
                   'software:SoftwarePurpose/specification, '
                   'software:SoftwarePurpose/test]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be
used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'} })
    builtTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'} })
    validUntilTime: Optional[datetime ] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be
reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI',
                   'SHACL in: [core:SupportType/development, core:SupportType/support, '
                   'core:SupportType/deployed, core:SupportType/limitedSupport, '
                   'core:SupportType/endOfSupport, core:SupportType/noSupport, '
                   'core:SupportType/noAssertion]'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'} })
    suppliedBy: Optional[Agent] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'} })
    originatedBy: Optional[list[Agent]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:IRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'} })
    releaseTime: Optional[datetime ] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content
that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'} })
    extension: Optional[list[Extension]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'comments': ['Class is known to not derive from Extension and cannot be used'],
         'domain_of': ['Element'],
         'notes': ['SHACL not: (54 restricted classes)',
                   'SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/extension'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/summary'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/description'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the
Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/comment'} })
    verifiedUsing: Optional[list[IntegrityMethod]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be
asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content
that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:Literal'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/name'} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'notes': ['SHACL nodeKind: sh:BlankNodeOrIRI'],
         'slot_uri': 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'} })

    @field_validator('builtTime')
    def pattern_builtTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid builtTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid builtTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('validUntilTime')
    def pattern_validUntilTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid validUntilTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid validUntilTime format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('releaseTime')
    def pattern_releaseTime(cls, v):
        pattern=re.compile(r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid releaseTime format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid releaseTime format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
EnergyConsumption.model_rebuild()
EnergyConsumptionDescription.model_rebuild()
CreationInfo.model_rebuild()
DictionaryEntry.model_rebuild()
Element.model_rebuild()
Build.model_rebuild()
Agent.model_rebuild()
Annotation.model_rebuild()
Artifact.model_rebuild()
ElementCollection.model_rebuild()
Bundle.model_rebuild()
Bom.model_rebuild()
ExternalIdentifier.model_rebuild()
ExternalMap.model_rebuild()
ExternalRef.model_rebuild()
IndividualElement.model_rebuild()
IntegrityMethod.model_rebuild()
Hash.model_rebuild()
NamespaceMap.model_rebuild()
Organization.model_rebuild()
PackageVerificationCode.model_rebuild()
Person.model_rebuild()
PositiveIntegerRange.model_rebuild()
Relationship.model_rebuild()
LifecycleScopedRelationship.model_rebuild()
SoftwareAgent.model_rebuild()
SpdxDocument.model_rebuild()
Tool.model_rebuild()
LicenseAddition.model_rebuild()
CustomLicenseAddition.model_rebuild()
ListedLicenseException.model_rebuild()
CdxPropertyEntry.model_rebuild()
Extension.model_rebuild()
CdxPropertiesExtension.model_rebuild()
VulnAssessmentRelationship.model_rebuild()
CvssV2VulnAssessmentRelationship.model_rebuild()
CvssV3VulnAssessmentRelationship.model_rebuild()
CvssV4VulnAssessmentRelationship.model_rebuild()
EpssVulnAssessmentRelationship.model_rebuild()
ExploitCatalogVulnAssessmentRelationship.model_rebuild()
SsvcVulnAssessmentRelationship.model_rebuild()
VexVulnAssessmentRelationship.model_rebuild()
VexAffectedVulnAssessmentRelationship.model_rebuild()
VexFixedVulnAssessmentRelationship.model_rebuild()
VexNotAffectedVulnAssessmentRelationship.model_rebuild()
VexUnderInvestigationVulnAssessmentRelationship.model_rebuild()
Vulnerability.model_rebuild()
AnyLicenseInfo.model_rebuild()
ConjunctiveLicenseSet.model_rebuild()
DisjunctiveLicenseSet.model_rebuild()
ExtendableLicense.model_rebuild()
IndividualLicensingInfo.model_rebuild()
License.model_rebuild()
CustomLicense.model_rebuild()
ListedLicense.model_rebuild()
OrLaterOperator.model_rebuild()
WithAdditionOperator.model_rebuild()
LicenseExpression.model_rebuild()
SimpleLicensingText.model_rebuild()
ContentIdentifier.model_rebuild()
Sbom.model_rebuild()
SoftwareArtifact.model_rebuild()
File.model_rebuild()
Package.model_rebuild()
AIPackage.model_rebuild()
DatasetPackage.model_rebuild()
Snippet.model_rebuild()
