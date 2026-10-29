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


metamodel_version = "1.12.0"
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


linkml_meta = LinkMLMeta({'comments': ['scripts/spdx_to_linkml.py writes every YAML file in this folder '
                  'from the vendored model, upstream/spdx-model.ttl. Change the '
                  'script or the model, never the files.',
                  'spdx_core imports only the LinkML types, each profile module '
                  'imports the modules it references, and this file adds nothing '
                  'of its own, so an importer can take one profile.',
                  "The element descriptions are the model's own rdfs:comment "
                  'texts, which the SPDX Project publishes under the Community '
                  'Specification License 1.0.',
                  "The model's individuals (NoAssertionElement, NoneElement, "
                  'NoAssertionLicense, NoneLicense and SpdxOrganization) are '
                  'instance data, not schema. A reference to one is an IRI like '
                  'any other Element reference.'],
     'default_prefix': 'spdx_linkml',
     'default_range': 'string',
     'description': 'A LinkML rendering of the SPDX 3.0.1 model: its nine '
                    'profiles, each a module, with every class, property and '
                    'vocabulary keeping its SPDX IRI.',
     'id': 'https://w3id.org/lmodel/spdx',
     'imports': ['linkml:types',
                 './spdx_core',
                 './spdx_build',
                 './spdx_extension',
                 './spdx_simple_licensing',
                 './spdx_software',
                 './spdx_ai',
                 './spdx_dataset',
                 './spdx_expanded_licensing',
                 './spdx_security'],
     'license': 'Apache-2.0',
     'name': 'spdx',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/'},
                  'spdx_ai': {'prefix_prefix': 'spdx_ai',
                              'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/AI/'},
                  'spdx_build': {'prefix_prefix': 'spdx_build',
                                 'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Build/'},
                  'spdx_core': {'prefix_prefix': 'spdx_core',
                                'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Core/'},
                  'spdx_dataset': {'prefix_prefix': 'spdx_dataset',
                                   'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Dataset/'},
                  'spdx_expanded_licensing': {'prefix_prefix': 'spdx_expanded_licensing',
                                              'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/'},
                  'spdx_extension': {'prefix_prefix': 'spdx_extension',
                                     'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Extension/'},
                  'spdx_linkml': {'prefix_prefix': 'spdx_linkml',
                                  'prefix_reference': 'https://w3id.org/lmodel/spdx/'},
                  'spdx_security': {'prefix_prefix': 'spdx_security',
                                    'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Security/'},
                  'spdx_simple_licensing': {'prefix_prefix': 'spdx_simple_licensing',
                                            'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/'},
                  'spdx_software': {'prefix_prefix': 'spdx_software',
                                    'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Software/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/spdx',
                  'https://spdx.github.io/spdx-spec/v3.0.1/',
                  'https://spdx.dev/specifications/'],
     'source': 'https://spdx.org/rdf/3.0.1/spdx-model.ttl',
     'source_file': 'src/spdx/schema/spdx.yaml',
     'title': 'System Package Data Exchange (SPDX)'} )

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
    Package URL, as defined in the corresponding [Annex](https://spdx.github.io/spdx-spec/v3.0.1/annexes/pkg-url-specification/) of this specification.
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
    in addition to being supported by the supplier, the software is known to have been deployed and is in use. For a software as a service provider, this implies the software is now available as a service.
    """
    development = "development"
    """
    the artifact is in active development and is not considered ready for formal support from the supplier.
    """
    endOfSupport = "endOfSupport"
    """
    there is a defined end of support for the artifact from the supplier. This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact.
    """
    limitedSupport = "limitedSupport"
    """
    the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.
    """
    noAssertion = "noAssertion"
    """
    no assertion about the type of support is made. This is considered the default if no other support type is used.
    """
    noSupport = "noSupport"
    """
    there is no support for the artifact from the supplier, consumer assumes any support obligations.
    """
    support = "support"
    """
    the artifact has been released, and is supported from the supplier. There is a validUntilDate that can provide additional information about the duration of support.
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
    Provides a set of values to be used to describe the common types of SBOMs that tools may create.
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
    ("Track*" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track* vulnerabilities within standard update timelines.
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



class CreationInfo(ConfiguredBaseModel):
    """
    Provides information about the creation of the Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:CreationInfo',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/CreationInfo/']})

    type: Literal["https://w3id.org/lmodel/spdx/CreationInfo","https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo","spdx_linkml:CreationInfo","spdx_core:CreationInfo"] = Field(default="spdx_core:CreationInfo", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    created: str = Field(default=..., description="""Identifies when the Element was originally created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/created/'],
         'slot_uri': 'spdx_core:created'} })
    createdBy: list[str] = Field(default=..., description="""Identifies who or what created the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/createdBy/'],
         'slot_uri': 'spdx_core:createdBy'} })
    createdUsing: Optional[list[str]] = Field(default=None, description="""Identifies the tooling that was used during the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/createdUsing/'],
         'slot_uri': 'spdx_core:createdUsing'} })
    specVersion: str = Field(default=..., description="""Provides a reference number that can be used to understand how to parse and interpret an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/specVersion/'],
         'slot_uri': 'spdx_core:specVersion'} })


class DictionaryEntry(ConfiguredBaseModel):
    """
    A key with an associated value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:DictionaryEntry',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/DictionaryEntry/']})

    type: Literal["https://w3id.org/lmodel/spdx/DictionaryEntry","https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry","spdx_linkml:DictionaryEntry","spdx_core:DictionaryEntry"] = Field(default="spdx_core:DictionaryEntry", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    key: str = Field(default=..., description="""A key used in a generic key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DictionaryEntry'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/key/'],
         'slot_uri': 'spdx_core:key'} })
    value: Optional[str] = Field(default=None, description="""A value used in a generic key-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DictionaryEntry'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/value/'],
         'slot_uri': 'spdx_core:value'} })


class Element(ConfiguredBaseModel):
    """
    Base domain class from which all other SPDX-3.0 domain classes derive.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_core:Element',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Element/']})

    type: Literal["https://w3id.org/lmodel/spdx/Element","https://spdx.org/rdf/3.0.1/terms/Core/Element","spdx_linkml:Element","spdx_core:Element"] = Field(default="spdx_core:Element", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Agent(Element):
    """
    Agent represents anything with the potential to act on a system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Agent',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Agent/']})

    type: Literal["https://w3id.org/lmodel/spdx/Agent","https://spdx.org/rdf/3.0.1/terms/Core/Agent","spdx_linkml:Agent","spdx_core:Agent"] = Field(default="spdx_core:Agent", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Annotation(Element):
    """
    An assertion made in relation to one or more elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Annotation',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Annotation/']})

    contentType: Optional[str] = Field(default=None, description="""Provides information about the content type of an Element or a Property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation', 'ExternalRef', 'File'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/contentType/'],
         'slot_uri': 'spdx_core:contentType'} })
    annotationType: AnnotationType = Field(default=..., description="""Describes the type of annotation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/annotationType/'],
         'slot_uri': 'spdx_core:annotationType'} })
    statement: Optional[str] = Field(default=None, description="""Commentary on an assertion that an annotator has made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/statement/'],
         'slot_uri': 'spdx_core:statement'} })
    subject: str = Field(default=..., description="""An Element an annotator has made an assertion about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/subject/'],
         'slot_uri': 'spdx_core:subject'} })
    type: Literal["https://w3id.org/lmodel/spdx/Annotation","https://spdx.org/rdf/3.0.1/terms/Core/Annotation","spdx_linkml:Annotation","spdx_core:Annotation"] = Field(default="spdx_core:Annotation", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class AnyLicenseInfo(Element):
    """
    Abstract class representing a license combination consisting of one or more licenses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_simple_licensing:AnyLicenseInfo',
         'comments': ['Declared in the core module because a Core field ranges over '
                      "it. Its IRI stays in the SimpleLicensing profile's namespace, "
                      'and so does its subset.'],
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Classes/AnyLicenseInfo/']})

    type: Literal["https://w3id.org/lmodel/spdx/AnyLicenseInfo","https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo","spdx_linkml:AnyLicenseInfo","spdx_simple_licensing:AnyLicenseInfo"] = Field(default="spdx_simple_licensing:AnyLicenseInfo", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Artifact(Element):
    """
    A distinct article or unit within the digital domain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_core:Artifact',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Artifact/']})

    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/Artifact","https://spdx.org/rdf/3.0.1/terms/Core/Artifact","spdx_linkml:Artifact","spdx_core:Artifact"] = Field(default="spdx_core:Artifact", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ElementCollection(Element):
    """
    A collection of Elements, not necessarily with unifying context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_core:ElementCollection',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ElementCollection/']})

    element: Optional[list[str]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/element/'],
         'slot_uri': 'spdx_core:element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/profileConformance/'],
         'slot_uri': 'spdx_core:profileConformance'} })
    rootElement: Optional[list[str]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/rootElement/'],
         'slot_uri': 'spdx_core:rootElement'} })
    type: Literal["https://w3id.org/lmodel/spdx/ElementCollection","https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection","spdx_linkml:ElementCollection","spdx_core:ElementCollection"] = Field(default="spdx_core:ElementCollection", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Bundle(ElementCollection):
    """
    A collection of Elements that have a shared context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Bundle',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Bundle/']})

    context: Optional[str] = Field(default=None, description="""Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/context/'],
         'slot_uri': 'spdx_core:context'} })
    element: Optional[list[str]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/element/'],
         'slot_uri': 'spdx_core:element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/profileConformance/'],
         'slot_uri': 'spdx_core:profileConformance'} })
    rootElement: Optional[list[str]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/rootElement/'],
         'slot_uri': 'spdx_core:rootElement'} })
    type: Literal["https://w3id.org/lmodel/spdx/Bundle","https://spdx.org/rdf/3.0.1/terms/Core/Bundle","spdx_linkml:Bundle","spdx_core:Bundle"] = Field(default="spdx_core:Bundle", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Bom(Bundle):
    """
    A container for a grouping of SPDX-3.0 content characterizing details (provenence, composition, licensing, etc.) about a product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Bom',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Bom/']})

    context: Optional[str] = Field(default=None, description="""Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/context/'],
         'slot_uri': 'spdx_core:context'} })
    element: Optional[list[str]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/element/'],
         'slot_uri': 'spdx_core:element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/profileConformance/'],
         'slot_uri': 'spdx_core:profileConformance'} })
    rootElement: Optional[list[str]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/rootElement/'],
         'slot_uri': 'spdx_core:rootElement'} })
    type: Literal["https://w3id.org/lmodel/spdx/Bom","https://spdx.org/rdf/3.0.1/terms/Core/Bom","spdx_linkml:Bom","spdx_core:Bom"] = Field(default="spdx_core:Bom", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Extension(ConfiguredBaseModel):
    """
    A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_extension:Extension',
         'comments': ['Declared in the core module because a Core field ranges over '
                      "it. Its IRI stays in the Extension profile's namespace, and so "
                      'does its subset.'],
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_extension'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Classes/Extension/']})

    type: Literal["https://w3id.org/lmodel/spdx/Extension","https://spdx.org/rdf/3.0.1/terms/Extension/Extension","spdx_linkml:Extension","spdx_extension:Extension"] = Field(default="spdx_extension:Extension", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })


class ExternalIdentifier(ConfiguredBaseModel):
    """
    A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:ExternalIdentifier',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ExternalIdentifier/']})

    type: Literal["https://w3id.org/lmodel/spdx/ExternalIdentifier","https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier","spdx_linkml:ExternalIdentifier","spdx_core:ExternalIdentifier"] = Field(default="spdx_core:ExternalIdentifier", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    externalIdentifierType: ExternalIdentifierType = Field(default=..., description="""Specifies the type of the external identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifierType/'],
         'slot_uri': 'spdx_core:externalIdentifierType'} })
    identifier: str = Field(default=..., description="""Uniquely identifies an external element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/identifier/'],
         'slot_uri': 'spdx_core:identifier'} })
    identifierLocator: Optional[list[str]] = Field(default=None, description="""Provides the location for more information regarding an external identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/identifierLocator/'],
         'slot_uri': 'spdx_core:identifierLocator'} })
    issuingAuthority: Optional[str] = Field(default=None, description="""An entity that is authorized to issue identification credentials.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIdentifier'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/issuingAuthority/'],
         'slot_uri': 'spdx_core:issuingAuthority'} })


class ExternalMap(ConfiguredBaseModel):
    """
    A map of Element identifiers that are used within an SpdxDocument but defined external to that SpdxDocument.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:ExternalMap',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ExternalMap/']})

    type: Literal["https://w3id.org/lmodel/spdx/ExternalMap","https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap","spdx_linkml:ExternalMap","spdx_core:ExternalMap"] = Field(default="spdx_core:ExternalMap", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    definingArtifact: Optional[str] = Field(default=None, description="""Artifact representing a serialization instance of SPDX data containing the definition of a particular Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalMap'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/definingArtifact/'],
         'slot_uri': 'spdx_core:definingArtifact'} })
    externalSpdxId: str = Field(default=..., description="""Identifies an external Element used within an SpdxDocument but defined external to that SpdxDocument.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalMap'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalSpdxId/'],
         'slot_uri': 'spdx_core:externalSpdxId'} })
    locationHint: Optional[str] = Field(default=None, description="""Provides an indication of where to retrieve an external Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalMap'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/locationHint/'],
         'slot_uri': 'spdx_core:locationHint'} })


class ExternalRef(ConfiguredBaseModel):
    """
    A reference to a resource outside the scope of SPDX-3.0 content related to an Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:ExternalRef',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/ExternalRef/']})

    type: Literal["https://w3id.org/lmodel/spdx/ExternalRef","https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef","spdx_linkml:ExternalRef","spdx_core:ExternalRef"] = Field(default="spdx_core:ExternalRef", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    contentType: Optional[str] = Field(default=None, description="""Provides information about the content type of an Element or a Property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation', 'ExternalRef', 'File'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/contentType/'],
         'slot_uri': 'spdx_core:contentType'} })
    externalRefType: Optional[ExternalRefType] = Field(default=None, description="""Specifies the type of the external reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalRef'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRefType/'],
         'slot_uri': 'spdx_core:externalRefType'} })
    locator: Optional[list[str]] = Field(default=None, description="""Provides the location of an external reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalRef'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/locator/'],
         'slot_uri': 'spdx_core:locator'} })


class IndividualElement(Element):
    """
    A concrete subclass of Element used by Individuals in the Core profile.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:IndividualElement',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/IndividualElement/']})

    type: Literal["https://w3id.org/lmodel/spdx/IndividualElement","https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement","spdx_linkml:IndividualElement","spdx_core:IndividualElement"] = Field(default="spdx_core:IndividualElement", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class IntegrityMethod(ConfiguredBaseModel):
    """
    Provides an independently reproducible mechanism that permits verification of a specific Element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_core:IntegrityMethod',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/IntegrityMethod/']})

    type: Literal["https://w3id.org/lmodel/spdx/IntegrityMethod","https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod","spdx_linkml:IntegrityMethod","spdx_core:IntegrityMethod"] = Field(default="spdx_core:IntegrityMethod", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })


class Hash(IntegrityMethod):
    """
    A mathematically calculated representation of a grouping of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Hash',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Hash/']})

    algorithm: HashAlgorithm = Field(default=..., description="""Specifies the algorithm used for calculating the hash value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'PackageVerificationCode'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/algorithm/'],
         'slot_uri': 'spdx_core:algorithm'} })
    hashValue: str = Field(default=..., description="""The result of applying a hash algorithm to an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'PackageVerificationCode'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/hashValue/'],
         'slot_uri': 'spdx_core:hashValue'} })
    type: Literal["https://w3id.org/lmodel/spdx/Hash","https://spdx.org/rdf/3.0.1/terms/Core/Hash","spdx_linkml:Hash","spdx_core:Hash"] = Field(default="spdx_core:Hash", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })


class NamespaceMap(ConfiguredBaseModel):
    """
    A mapping between prefixes and namespace partial URIs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:NamespaceMap',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/NamespaceMap/']})

    type: Literal["https://w3id.org/lmodel/spdx/NamespaceMap","https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap","spdx_linkml:NamespaceMap","spdx_core:NamespaceMap"] = Field(default="spdx_core:NamespaceMap", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    namespace: str = Field(default=..., description="""Provides an unambiguous mechanism for conveying a URI fragment portion of an Element ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamespaceMap'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/namespace/'],
         'slot_uri': 'spdx_core:namespace'} })
    prefix: str = Field(default=..., description="""A substitute for a URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamespaceMap'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/prefix/'],
         'slot_uri': 'spdx_core:prefix'} })


class Organization(Agent):
    """
    A group of people who work together in an organized way for a shared purpose.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Organization',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Organization/']})

    type: Literal["https://w3id.org/lmodel/spdx/Organization","https://spdx.org/rdf/3.0.1/terms/Core/Organization","spdx_linkml:Organization","spdx_core:Organization"] = Field(default="spdx_core:Organization", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class PackageVerificationCode(IntegrityMethod):
    """
    An SPDX version 2.X compatible verification method for software packages.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:PackageVerificationCode',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/PackageVerificationCode/']})

    algorithm: HashAlgorithm = Field(default=..., description="""Specifies the algorithm used for calculating the hash value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'PackageVerificationCode'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/algorithm/'],
         'slot_uri': 'spdx_core:algorithm'} })
    hashValue: str = Field(default=..., description="""The result of applying a hash algorithm to an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'PackageVerificationCode'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/hashValue/'],
         'slot_uri': 'spdx_core:hashValue'} })
    packageVerificationCodeExcludedFile: Optional[list[str]] = Field(default=None, description="""The relative file name of a file to be excluded from the `PackageVerificationCode`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PackageVerificationCode'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/packageVerificationCodeExcludedFile/'],
         'slot_uri': 'spdx_core:packageVerificationCodeExcludedFile'} })
    type: Literal["https://w3id.org/lmodel/spdx/PackageVerificationCode","https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode","spdx_linkml:PackageVerificationCode","spdx_core:PackageVerificationCode"] = Field(default="spdx_core:PackageVerificationCode", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })


class Person(Agent):
    """
    An individual human being.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Person',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Person/']})

    type: Literal["https://w3id.org/lmodel/spdx/Person","https://spdx.org/rdf/3.0.1/terms/Core/Person","spdx_linkml:Person","spdx_core:Person"] = Field(default="spdx_core:Person", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class PositiveIntegerRange(ConfiguredBaseModel):
    """
    A tuple of two positive integers that define a range.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:PositiveIntegerRange',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/PositiveIntegerRange/']})

    type: Literal["https://w3id.org/lmodel/spdx/PositiveIntegerRange","https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange","spdx_linkml:PositiveIntegerRange","spdx_core:PositiveIntegerRange"] = Field(default="spdx_core:PositiveIntegerRange", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    beginIntegerRange: int = Field(default=..., description="""Defines the beginning of a range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PositiveIntegerRange'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/beginIntegerRange/'],
         'slot_uri': 'spdx_core:beginIntegerRange'} })
    endIntegerRange: int = Field(default=..., description="""Defines the end of a range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PositiveIntegerRange'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endIntegerRange/'],
         'slot_uri': 'spdx_core:endIntegerRange'} })


class Relationship(Element):
    """
    Describes a relationship between one or more elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Relationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Relationship/']})

    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/Relationship","https://spdx.org/rdf/3.0.1/terms/Core/Relationship","spdx_linkml:Relationship","spdx_core:Relationship"] = Field(default="spdx_core:Relationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class LifecycleScopedRelationship(Relationship):
    """
    Provide context for a relationship that occurs in the lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:LifecycleScopedRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/LifecycleScopedRelationship/']})

    scope: Optional[LifecycleScopeType] = Field(default=None, description="""Capture the scope of information about a specific relationship between elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LifecycleScopedRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/scope/'],
         'slot_uri': 'spdx_core:scope'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/LifecycleScopedRelationship","https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship","spdx_linkml:LifecycleScopedRelationship","spdx_core:LifecycleScopedRelationship"] = Field(default="spdx_core:LifecycleScopedRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class SoftwareAgent(Agent):
    """
    A software agent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:SoftwareAgent',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/SoftwareAgent/']})

    type: Literal["https://w3id.org/lmodel/spdx/SoftwareAgent","https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent","spdx_linkml:SoftwareAgent","spdx_core:SoftwareAgent"] = Field(default="spdx_core:SoftwareAgent", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class SpdxDocument(ElementCollection):
    """
    A collection of SPDX Elements that could potentially be serialized.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:SpdxDocument',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/SpdxDocument/']})

    dataLicense: Optional[str] = Field(default=None, description="""Provides the license under which the SPDX documentation of the Element can be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpdxDocument'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/dataLicense/'],
         'slot_uri': 'spdx_core:dataLicense'} })
    import_: Optional[list[ExternalMap]] = Field(default=None, alias="import", description="""Provides an ExternalMap of Element identifiers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpdxDocument'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/import/'],
         'slot_uri': 'spdx_core:import'} })
    namespaceMap: Optional[list[NamespaceMap]] = Field(default=None, description="""Provides a NamespaceMap of prefixes and associated namespace partial URIs applicable to an SpdxDocument and independent of any specific serialization format or instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpdxDocument'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/namespaceMap/'],
         'slot_uri': 'spdx_core:namespaceMap'} })
    element: Optional[list[str]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/element/'],
         'slot_uri': 'spdx_core:element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/profileConformance/'],
         'slot_uri': 'spdx_core:profileConformance'} })
    rootElement: Optional[list[str]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/rootElement/'],
         'slot_uri': 'spdx_core:rootElement'} })
    type: Literal["https://w3id.org/lmodel/spdx/SpdxDocument","https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument","spdx_linkml:SpdxDocument","spdx_core:SpdxDocument"] = Field(default="spdx_core:SpdxDocument", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Tool(Element):
    """
    An element of hardware and/or software utilized to carry out a particular function.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_core:Tool',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_core',
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Tool/']})

    type: Literal["https://w3id.org/lmodel/spdx/Tool","https://spdx.org/rdf/3.0.1/terms/Core/Tool","spdx_linkml:Tool","spdx_core:Tool"] = Field(default="spdx_core:Tool", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Build(Element):
    """
    Class that describes a build instance of software/artifacts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_build:Build',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_build',
         'in_subset': ['spdx_build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Classes/Build/']})

    buildEndTime: Optional[str] = Field(default=None, description="""Property that describes the time at which a build stops.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildEndTime/'],
         'slot_uri': 'spdx_build:buildEndTime'} })
    buildId: Optional[str] = Field(default=None, description="""A buildId is a locally unique identifier used by a builder to identify a unique instance of a build produced by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildId/'],
         'slot_uri': 'spdx_build:buildId'} })
    buildStartTime: Optional[str] = Field(default=None, description="""Property describing the start time of a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildStartTime/'],
         'slot_uri': 'spdx_build:buildStartTime'} })
    buildType: str = Field(default=..., description="""A buildType is a hint that is used to indicate the toolchain, platform, or infrastructure that the build was invoked on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/buildType/'],
         'slot_uri': 'spdx_build:buildType'} })
    configSourceDigest: Optional[list[Hash]] = Field(default=None, description="""Property that describes the digest of the build configuration file used to invoke a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/configSourceDigest/'],
         'slot_uri': 'spdx_build:configSourceDigest'} })
    configSourceEntrypoint: Optional[list[str]] = Field(default=None, description="""Property describes the invocation entrypoint of a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/configSourceEntrypoint/'],
         'slot_uri': 'spdx_build:configSourceEntrypoint'} })
    configSourceUri: Optional[list[str]] = Field(default=None, description="""Property that describes the URI of the build configuration source file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/configSourceUri/'],
         'slot_uri': 'spdx_build:configSourceUri'} })
    environment: Optional[list[DictionaryEntry]] = Field(default=None, description="""Property describing the session in which a build is invoked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/environment/'],
         'slot_uri': 'spdx_build:environment'} })
    parameter: Optional[list[DictionaryEntry]] = Field(default=None, description="""Property describing a parameter used in an instance of a build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Build'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Properties/parameter/'],
         'slot_uri': 'spdx_build:parameter'} })
    type: Literal["https://w3id.org/lmodel/spdx/Build","https://spdx.org/rdf/3.0.1/terms/Build/Build","spdx_linkml:Build","spdx_build:Build"] = Field(default="spdx_build:Build", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class CdxPropertiesExtension(Extension):
    """
    A type of extension consisting of a list of name value pairs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_extension:CdxPropertiesExtension',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_extension',
         'in_subset': ['spdx_extension'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Classes/CdxPropertiesExtension/']})

    cdxProperty: list[CdxPropertyEntry] = Field(default=..., description="""Provides a map of a property names to a values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CdxPropertiesExtension'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Properties/cdxProperty/'],
         'slot_uri': 'spdx_extension:cdxProperty'} })
    type: Literal["https://w3id.org/lmodel/spdx/CdxPropertiesExtension","https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension","spdx_linkml:CdxPropertiesExtension","spdx_extension:CdxPropertiesExtension"] = Field(default="spdx_extension:CdxPropertiesExtension", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })


class CdxPropertyEntry(ConfiguredBaseModel):
    """
    A property name with an associated value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_extension:CdxPropertyEntry',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_extension',
         'in_subset': ['spdx_extension'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Classes/CdxPropertyEntry/']})

    type: Literal["https://w3id.org/lmodel/spdx/CdxPropertyEntry","https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry","spdx_linkml:CdxPropertyEntry","spdx_extension:CdxPropertyEntry"] = Field(default="spdx_extension:CdxPropertyEntry", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    cdxPropName: str = Field(default=..., description="""A name used in a CdxPropertyEntry name-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CdxPropertyEntry'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Properties/cdxPropName/'],
         'slot_uri': 'spdx_extension:cdxPropName'} })
    cdxPropValue: Optional[str] = Field(default=None, description="""A value used in a CdxPropertyEntry name-value pair.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CdxPropertyEntry'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Properties/cdxPropValue/'],
         'slot_uri': 'spdx_extension:cdxPropValue'} })


class LicenseExpression(AnyLicenseInfo):
    """
    An SPDX Element containing an SPDX license expression string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_simple_licensing:LicenseExpression',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_simple_licensing',
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Classes/LicenseExpression/']})

    customIdToUri: Optional[list[DictionaryEntry]] = Field(default=None, description="""Maps a LicenseRef or AdditionRef string for a Custom License or a Custom License Addition to its URI ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseExpression'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/customIdToUri/'],
         'slot_uri': 'spdx_simple_licensing:customIdToUri'} })
    licenseExpression: str = Field(default=..., description="""A string in the license expression format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseExpression'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseExpression/'],
         'slot_uri': 'spdx_simple_licensing:licenseExpression'} })
    licenseListVersion: Optional[str] = Field(default=None, description="""The version of the SPDX License List used in the license expression.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseExpression'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseListVersion/'],
         'slot_uri': 'spdx_simple_licensing:licenseListVersion'} })
    type: Literal["https://w3id.org/lmodel/spdx/LicenseExpression","https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression","spdx_linkml:LicenseExpression","spdx_simple_licensing:LicenseExpression"] = Field(default="spdx_simple_licensing:LicenseExpression", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class SimpleLicensingText(Element):
    """
    A license or addition that is not listed on the SPDX License List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_simple_licensing:SimpleLicensingText',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_simple_licensing',
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Classes/SimpleLicensingText/']})

    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SimpleLicensingText', 'License'],
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseText/'],
         'slot_uri': 'spdx_simple_licensing:licenseText'} })
    type: Literal["https://w3id.org/lmodel/spdx/SimpleLicensingText","https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText","spdx_linkml:SimpleLicensingText","spdx_simple_licensing:SimpleLicensingText"] = Field(default="spdx_simple_licensing:SimpleLicensingText", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ContentIdentifier(IntegrityMethod):
    """
    A canonical, unique, immutable identifier
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_software:ContentIdentifier',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_software',
         'in_subset': ['spdx_software'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/ContentIdentifier/']})

    contentIdentifierType: ContentIdentifierType = Field(default=..., description="""Specifies the type of the content identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentIdentifier'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifierType/'],
         'slot_uri': 'spdx_software:contentIdentifierType'} })
    contentIdentifierValue: str = Field(default=..., description="""Specifies the value of the content identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentIdentifier'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifierValue/'],
         'slot_uri': 'spdx_software:contentIdentifierValue'} })
    type: Literal["https://w3id.org/lmodel/spdx/ContentIdentifier","https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier","spdx_linkml:ContentIdentifier","spdx_software:ContentIdentifier"] = Field(default="spdx_software:ContentIdentifier", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })


class Sbom(Bom):
    """
    A collection of SPDX Elements describing a single package.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_software:Sbom',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_software',
         'in_subset': ['spdx_software'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Sbom/']})

    sbomType: Optional[list[SbomType]] = Field(default=None, description="""Provides information about the type of an SBOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sbom'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sbomType/'],
         'slot_uri': 'spdx_software:sbomType'} })
    context: Optional[str] = Field(default=None, description="""Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/context/'],
         'slot_uri': 'spdx_core:context'} })
    element: Optional[list[str]] = Field(default=None, description="""Refers to one or more Elements that are part of an ElementCollection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/element/'],
         'slot_uri': 'spdx_core:element'} })
    profileConformance: Optional[list[ProfileIdentifierType]] = Field(default=None, description="""Describes one a profile which the creator of this ElementCollection intends to conform to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/profileConformance/'],
         'slot_uri': 'spdx_core:profileConformance'} })
    rootElement: Optional[list[str]] = Field(default=None, description="""This property is used to denote the root Element(s) of a tree of elements contained in a BOM.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementCollection'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/rootElement/'],
         'slot_uri': 'spdx_core:rootElement'} })
    type: Literal["https://w3id.org/lmodel/spdx/Sbom","https://spdx.org/rdf/3.0.1/terms/Software/Sbom","spdx_linkml:Sbom","spdx_software:Sbom"] = Field(default="spdx_software:Sbom", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class SoftwareArtifact(Artifact):
    """
    A distinct article or unit related to Software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_software:SoftwareArtifact',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_software',
         'in_subset': ['spdx_software'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/SoftwareArtifact/']})

    additionalPurpose: Optional[list[SoftwarePurpose]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/'],
         'slot_uri': 'spdx_software:additionalPurpose'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/'],
         'slot_uri': 'spdx_software:attributionText'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/'],
         'slot_uri': 'spdx_software:contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/'],
         'slot_uri': 'spdx_software:copyrightText'} })
    primaryPurpose: Optional[SoftwarePurpose] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/'],
         'slot_uri': 'spdx_software:primaryPurpose'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/SoftwareArtifact","https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact","spdx_linkml:SoftwareArtifact","spdx_software:SoftwareArtifact"] = Field(default="spdx_software:SoftwareArtifact", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class File(SoftwareArtifact):
    """
    Refers to any object that stores content on a computer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_software:File',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_software',
         'in_subset': ['spdx_software'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/File/']})

    contentType: Optional[str] = Field(default=None, description="""Provides information about the content type of an Element or a Property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Annotation', 'ExternalRef', 'File'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/contentType/'],
         'slot_uri': 'spdx_core:contentType'} })
    fileKind: Optional[FileKindType] = Field(default=None, description="""Describes if a given file is a directory or non-directory kind of file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/fileKind/'],
         'slot_uri': 'spdx_software:fileKind'} })
    additionalPurpose: Optional[list[SoftwarePurpose]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/'],
         'slot_uri': 'spdx_software:additionalPurpose'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/'],
         'slot_uri': 'spdx_software:attributionText'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/'],
         'slot_uri': 'spdx_software:contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/'],
         'slot_uri': 'spdx_software:copyrightText'} })
    primaryPurpose: Optional[SoftwarePurpose] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/'],
         'slot_uri': 'spdx_software:primaryPurpose'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/File","https://spdx.org/rdf/3.0.1/terms/Software/File","spdx_linkml:File","spdx_software:File"] = Field(default="spdx_software:File", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Package(SoftwareArtifact):
    """
    Refers to any unit of content that can be associated with a distribution of software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_software:Package',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_software',
         'in_subset': ['spdx_software'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Package/']})

    downloadLocation: Optional[str] = Field(default=None, description="""Identifies the download Uniform Resource Identifier for the package at the time that the document was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/downloadLocation/'],
         'slot_uri': 'spdx_software:downloadLocation'} })
    homePage: Optional[str] = Field(default=None, description="""A place for the SPDX document creator to record a website that serves as the package's home page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/homePage/'],
         'slot_uri': 'spdx_software:homePage'} })
    packageUrl: Optional[str] = Field(default=None, description="""Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageUrl/'],
         'slot_uri': 'spdx_software:packageUrl'} })
    packageVersion: Optional[str] = Field(default=None, description="""Identify the version of a package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageVersion/'],
         'slot_uri': 'spdx_software:packageVersion'} })
    sourceInfo: Optional[str] = Field(default=None, description="""Records any relevant background information or additional comments about the origin of the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sourceInfo/'],
         'slot_uri': 'spdx_software:sourceInfo'} })
    additionalPurpose: Optional[list[SoftwarePurpose]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/'],
         'slot_uri': 'spdx_software:additionalPurpose'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/'],
         'slot_uri': 'spdx_software:attributionText'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/'],
         'slot_uri': 'spdx_software:contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/'],
         'slot_uri': 'spdx_software:copyrightText'} })
    primaryPurpose: Optional[SoftwarePurpose] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/'],
         'slot_uri': 'spdx_software:primaryPurpose'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/Package","https://spdx.org/rdf/3.0.1/terms/Software/Package","spdx_linkml:Package","spdx_software:Package"] = Field(default="spdx_software:Package", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Snippet(SoftwareArtifact):
    """
    Describes a certain part of a file.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_software:Snippet',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_software',
         'in_subset': ['spdx_software'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Snippet/']})

    byteRange: Optional[PositiveIntegerRange] = Field(default=None, description="""Defines the byte range in the original host file that the snippet information applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Snippet'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/byteRange/'],
         'slot_uri': 'spdx_software:byteRange'} })
    lineRange: Optional[PositiveIntegerRange] = Field(default=None, description="""Defines the line range in the original host file that the snippet information applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Snippet'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/lineRange/'],
         'slot_uri': 'spdx_software:lineRange'} })
    snippetFromFile: str = Field(default=..., description="""Defines the original host file that the snippet information applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Snippet'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/snippetFromFile/'],
         'slot_uri': 'spdx_software:snippetFromFile'} })
    additionalPurpose: Optional[list[SoftwarePurpose]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/'],
         'slot_uri': 'spdx_software:additionalPurpose'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/'],
         'slot_uri': 'spdx_software:attributionText'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/'],
         'slot_uri': 'spdx_software:contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/'],
         'slot_uri': 'spdx_software:copyrightText'} })
    primaryPurpose: Optional[SoftwarePurpose] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/'],
         'slot_uri': 'spdx_software:primaryPurpose'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/Snippet","https://spdx.org/rdf/3.0.1/terms/Software/Snippet","spdx_linkml:Snippet","spdx_software:Snippet"] = Field(default="spdx_software:Snippet", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class AIPackage(Package):
    """
    Specifies an AI package and its associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_ai:AIPackage',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_ai',
         'in_subset': ['spdx_ai'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/']})

    autonomyType: Optional[PresenceType] = Field(default=None, description="""Indicates whether the system can perform a decision or action without human involvement or guidance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/autonomyType/'],
         'slot_uri': 'spdx_ai:autonomyType'} })
    domain: Optional[list[str]] = Field(default=None, description="""Captures the domain in which the AI package can be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/domain/'],
         'slot_uri': 'spdx_ai:domain'} })
    energyConsumption: Optional[EnergyConsumption] = Field(default=None, description="""Indicates the amount of energy consumption incurred by an AI model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/energyConsumption/'],
         'slot_uri': 'spdx_ai:energyConsumption'} })
    hyperparameter: Optional[list[DictionaryEntry]] = Field(default=None, description="""Records a hyperparameter used to build the AI model contained in the AI package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/hyperparameter/'],
         'slot_uri': 'spdx_ai:hyperparameter'} })
    informationAboutApplication: Optional[str] = Field(default=None, description="""Provides relevant information about the AI software, not including the model description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/informationAboutApplication/'],
         'slot_uri': 'spdx_ai:informationAboutApplication'} })
    informationAboutTraining: Optional[str] = Field(default=None, description="""Describes relevant information about different steps of the training process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/informationAboutTraining/'],
         'slot_uri': 'spdx_ai:informationAboutTraining'} })
    limitation: Optional[str] = Field(default=None, description="""Captures a limitation of the AI software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/limitation/'],
         'slot_uri': 'spdx_ai:limitation'} })
    metric: Optional[list[DictionaryEntry]] = Field(default=None, description="""Records the measurement of prediction quality of the AI model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/metric/'],
         'slot_uri': 'spdx_ai:metric'} })
    metricDecisionThreshold: Optional[list[DictionaryEntry]] = Field(default=None, description="""Captures the threshold that was used for computation of a metric described in the metric field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/metricDecisionThreshold/'],
         'slot_uri': 'spdx_ai:metricDecisionThreshold'} })
    modelDataPreprocessing: Optional[list[str]] = Field(default=None, description="""Describes all the preprocessing steps applied to the training data before the model training.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/modelDataPreprocessing/'],
         'slot_uri': 'spdx_ai:modelDataPreprocessing'} })
    modelExplainability: Optional[list[str]] = Field(default=None, description="""Describes methods that can be used to explain the results from the AI model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/modelExplainability/'],
         'slot_uri': 'spdx_ai:modelExplainability'} })
    safetyRiskAssessment: Optional[SafetyRiskAssessmentType] = Field(default=None, description="""Records the results of general safety risk assessment of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/safetyRiskAssessment/'],
         'slot_uri': 'spdx_ai:safetyRiskAssessment'} })
    standardCompliance: Optional[list[str]] = Field(default=None, description="""Captures a standard that is being complied with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/standardCompliance/'],
         'slot_uri': 'spdx_ai:standardCompliance'} })
    typeOfModel: Optional[list[str]] = Field(default=None, description="""Records the type of the model used in the AI software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/typeOfModel/'],
         'slot_uri': 'spdx_ai:typeOfModel'} })
    useSensitivePersonalInformation: Optional[PresenceType] = Field(default=None, description="""Records if sensitive personal information is used during model training or could be used during the inference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/useSensitivePersonalInformation/'],
         'slot_uri': 'spdx_ai:useSensitivePersonalInformation'} })
    downloadLocation: Optional[str] = Field(default=None, description="""Identifies the download Uniform Resource Identifier for the package at the time that the document was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/downloadLocation/'],
         'slot_uri': 'spdx_software:downloadLocation'} })
    homePage: Optional[str] = Field(default=None, description="""A place for the SPDX document creator to record a website that serves as the package's home page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/homePage/'],
         'slot_uri': 'spdx_software:homePage'} })
    packageUrl: Optional[str] = Field(default=None, description="""Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageUrl/'],
         'slot_uri': 'spdx_software:packageUrl'} })
    packageVersion: Optional[str] = Field(default=None, description="""Identify the version of a package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageVersion/'],
         'slot_uri': 'spdx_software:packageVersion'} })
    sourceInfo: Optional[str] = Field(default=None, description="""Records any relevant background information or additional comments about the origin of the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sourceInfo/'],
         'slot_uri': 'spdx_software:sourceInfo'} })
    additionalPurpose: Optional[list[SoftwarePurpose]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/'],
         'slot_uri': 'spdx_software:additionalPurpose'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/'],
         'slot_uri': 'spdx_software:attributionText'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/'],
         'slot_uri': 'spdx_software:contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/'],
         'slot_uri': 'spdx_software:copyrightText'} })
    primaryPurpose: Optional[SoftwarePurpose] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/'],
         'slot_uri': 'spdx_software:primaryPurpose'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/AIPackage","https://spdx.org/rdf/3.0.1/terms/AI/AIPackage","spdx_linkml:AIPackage","spdx_ai:AIPackage"] = Field(default="spdx_ai:AIPackage", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class EnergyConsumption(ConfiguredBaseModel):
    """
    A class for describing the energy consumption incurred by an AI model in different stages of its lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_ai:EnergyConsumption',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_ai',
         'in_subset': ['spdx_ai'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/EnergyConsumption/']})

    type: Literal["https://w3id.org/lmodel/spdx/EnergyConsumption","https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption","spdx_linkml:EnergyConsumption","spdx_ai:EnergyConsumption"] = Field(default="spdx_ai:EnergyConsumption", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    finetuningEnergyConsumption: Optional[list[EnergyConsumptionDescription]] = Field(default=None, description="""Specifies the amount of energy consumed when finetuning the AI model that is being used in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumption'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/finetuningEnergyConsumption/'],
         'slot_uri': 'spdx_ai:finetuningEnergyConsumption'} })
    inferenceEnergyConsumption: Optional[list[EnergyConsumptionDescription]] = Field(default=None, description="""Specifies the amount of energy consumed during inference time by an AI model that is being used in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumption'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/inferenceEnergyConsumption/'],
         'slot_uri': 'spdx_ai:inferenceEnergyConsumption'} })
    trainingEnergyConsumption: Optional[list[EnergyConsumptionDescription]] = Field(default=None, description="""Specifies the amount of energy consumed when training the AI model that is being used in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumption'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/trainingEnergyConsumption/'],
         'slot_uri': 'spdx_ai:trainingEnergyConsumption'} })


class EnergyConsumptionDescription(ConfiguredBaseModel):
    """
    The class that helps note down the quantity of energy consumption and the unit used for measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_ai:EnergyConsumptionDescription',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_ai',
         'in_subset': ['spdx_ai'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/EnergyConsumptionDescription/']})

    type: Literal["https://w3id.org/lmodel/spdx/EnergyConsumptionDescription","https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription","spdx_linkml:EnergyConsumptionDescription","spdx_ai:EnergyConsumptionDescription"] = Field(default="spdx_ai:EnergyConsumptionDescription", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    energyQuantity: Decimal = Field(default=..., description="""Represents the energy quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumptionDescription'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/energyQuantity/'],
         'slot_uri': 'spdx_ai:energyQuantity'} })
    energyUnit: EnergyUnitType = Field(default=..., description="""Specifies the unit in which energy is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnergyConsumptionDescription'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Properties/energyUnit/'],
         'slot_uri': 'spdx_ai:energyUnit'} })


class DatasetPackage(Package):
    """
    Specifies a data package and its associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_dataset:DatasetPackage',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_dataset',
         'in_subset': ['spdx_dataset'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/']})

    anonymizationMethodUsed: Optional[list[str]] = Field(default=None, description="""Describes the anonymization methods used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/anonymizationMethodUsed/'],
         'slot_uri': 'spdx_dataset:anonymizationMethodUsed'} })
    confidentialityLevel: Optional[ConfidentialityLevelType] = Field(default=None, description="""Describes the confidentiality level of the data points contained in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/confidentialityLevel/'],
         'slot_uri': 'spdx_dataset:confidentialityLevel'} })
    dataCollectionProcess: Optional[str] = Field(default=None, description="""Describes how the dataset was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/dataCollectionProcess/'],
         'slot_uri': 'spdx_dataset:dataCollectionProcess'} })
    dataPreprocessing: Optional[list[str]] = Field(default=None, description="""Describes the preprocessing steps that were applied to the raw data to create the given dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/dataPreprocessing/'],
         'slot_uri': 'spdx_dataset:dataPreprocessing'} })
    datasetAvailability: Optional[DatasetAvailabilityType] = Field(default=None, description="""The field describes the availability of a dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetAvailability/'],
         'slot_uri': 'spdx_dataset:datasetAvailability'} })
    datasetNoise: Optional[str] = Field(default=None, description="""Describes potentially noisy elements of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetNoise/'],
         'slot_uri': 'spdx_dataset:datasetNoise'} })
    datasetSize: Optional[int] = Field(default=None, description="""Captures the size of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetSize/'],
         'slot_uri': 'spdx_dataset:datasetSize'} })
    datasetType: list[DatasetType] = Field(default=..., description="""Describes the type of the given dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetType/'],
         'slot_uri': 'spdx_dataset:datasetType'} })
    datasetUpdateMechanism: Optional[str] = Field(default=None, description="""Describes a mechanism to update the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/datasetUpdateMechanism/'],
         'slot_uri': 'spdx_dataset:datasetUpdateMechanism'} })
    hasSensitivePersonalInformation: Optional[PresenceType] = Field(default=None, description="""Describes if any sensitive personal information is present in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/hasSensitivePersonalInformation/'],
         'slot_uri': 'spdx_dataset:hasSensitivePersonalInformation'} })
    intendedUse: Optional[str] = Field(default=None, description="""Describes what the given dataset should be used for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/intendedUse/'],
         'slot_uri': 'spdx_dataset:intendedUse'} })
    knownBias: Optional[list[str]] = Field(default=None, description="""Records the biases that the dataset is known to encompass.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/knownBias/'],
         'slot_uri': 'spdx_dataset:knownBias'} })
    sensor: Optional[list[DictionaryEntry]] = Field(default=None, description="""Describes a sensor used for collecting the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatasetPackage'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Properties/sensor/'],
         'slot_uri': 'spdx_dataset:sensor'} })
    downloadLocation: Optional[str] = Field(default=None, description="""Identifies the download Uniform Resource Identifier for the package at the time that the document was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/downloadLocation/'],
         'slot_uri': 'spdx_software:downloadLocation'} })
    homePage: Optional[str] = Field(default=None, description="""A place for the SPDX document creator to record a website that serves as the package's home page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/homePage/'],
         'slot_uri': 'spdx_software:homePage'} })
    packageUrl: Optional[str] = Field(default=None, description="""Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageUrl/'],
         'slot_uri': 'spdx_software:packageUrl'} })
    packageVersion: Optional[str] = Field(default=None, description="""Identify the version of a package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/packageVersion/'],
         'slot_uri': 'spdx_software:packageVersion'} })
    sourceInfo: Optional[str] = Field(default=None, description="""Records any relevant background information or additional comments about the origin of the package.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Package'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/sourceInfo/'],
         'slot_uri': 'spdx_software:sourceInfo'} })
    additionalPurpose: Optional[list[SoftwarePurpose]] = Field(default=None, description="""Provides additional purpose information of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/additionalPurpose/'],
         'slot_uri': 'spdx_software:additionalPurpose'} })
    attributionText: Optional[list[str]] = Field(default=None, description="""Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/attributionText/'],
         'slot_uri': 'spdx_software:attributionText'} })
    contentIdentifier: Optional[list[ContentIdentifier]] = Field(default=None, description="""A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/contentIdentifier/'],
         'slot_uri': 'spdx_software:contentIdentifier'} })
    copyrightText: Optional[str] = Field(default=None, description="""Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/copyrightText/'],
         'slot_uri': 'spdx_software:copyrightText'} })
    primaryPurpose: Optional[SoftwarePurpose] = Field(default=None, description="""Provides information about the primary purpose of the software artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftwareArtifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Properties/primaryPurpose/'],
         'slot_uri': 'spdx_software:primaryPurpose'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/DatasetPackage","https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage","spdx_linkml:DatasetPackage","spdx_dataset:DatasetPackage"] = Field(default="spdx_dataset:DatasetPackage", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ConjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information where all elements apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:ConjunctiveLicenseSet',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/ConjunctiveLicenseSet/']})

    member: list[str] = Field(default=..., description="""A license expression participating in a license set.""", min_length=2, json_schema_extra = { "linkml_meta": {'domain_of': ['ConjunctiveLicenseSet', 'DisjunctiveLicenseSet'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/member/'],
         'slot_uri': 'spdx_expanded_licensing:member'} })
    type: Literal["https://w3id.org/lmodel/spdx/ConjunctiveLicenseSet","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet","spdx_linkml:ConjunctiveLicenseSet","spdx_expanded_licensing:ConjunctiveLicenseSet"] = Field(default="spdx_expanded_licensing:ConjunctiveLicenseSet", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class DisjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information where only one of the elements applies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:DisjunctiveLicenseSet',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/DisjunctiveLicenseSet/']})

    member: list[str] = Field(default=..., description="""A license expression participating in a license set.""", min_length=2, json_schema_extra = { "linkml_meta": {'domain_of': ['ConjunctiveLicenseSet', 'DisjunctiveLicenseSet'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/member/'],
         'slot_uri': 'spdx_expanded_licensing:member'} })
    type: Literal["https://w3id.org/lmodel/spdx/DisjunctiveLicenseSet","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet","spdx_linkml:DisjunctiveLicenseSet","spdx_expanded_licensing:DisjunctiveLicenseSet"] = Field(default="spdx_expanded_licensing:DisjunctiveLicenseSet", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ExtendableLicense(AnyLicenseInfo):
    """
    Abstract class representing a License or an OrLaterOperator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_expanded_licensing:ExtendableLicense',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/ExtendableLicense/']})

    type: Literal["https://w3id.org/lmodel/spdx/ExtendableLicense","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense","spdx_linkml:ExtendableLicense","spdx_expanded_licensing:ExtendableLicense"] = Field(default="spdx_expanded_licensing:ExtendableLicense", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class IndividualLicensingInfo(AnyLicenseInfo):
    """
    A concrete subclass of AnyLicenseInfo used by Individuals in the ExpandedLicensing profile.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:IndividualLicensingInfo',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/IndividualLicensingInfo/']})

    type: Literal["https://w3id.org/lmodel/spdx/IndividualLicensingInfo","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo","spdx_linkml:IndividualLicensingInfo","spdx_expanded_licensing:IndividualLicensingInfo"] = Field(default="spdx_expanded_licensing:IndividualLicensingInfo", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class License(ExtendableLicense):
    """
    Abstract class for the portion of an AnyLicenseInfo representing a license.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_expanded_licensing:License',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/License/']})

    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SimpleLicensingText', 'License'],
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseText/'],
         'slot_uri': 'spdx_simple_licensing:licenseText'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/'],
         'slot_uri': 'spdx_expanded_licensing:licenseXml'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/'],
         'slot_uri': 'spdx_expanded_licensing:obsoletedBy'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/'],
         'slot_uri': 'spdx_expanded_licensing:seeAlso'} })
    isDeprecatedLicenseId: Optional[bool] = Field(default=None, description="""Specifies whether a license or additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedLicenseId/'],
         'slot_uri': 'spdx_expanded_licensing:isDeprecatedLicenseId'} })
    isFsfLibre: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as free by the Free Software Foundation (FSF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isFsfLibre/'],
         'slot_uri': 'spdx_expanded_licensing:isFsfLibre'} })
    isOsiApproved: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as approved by the Open Source Initiative (OSI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isOsiApproved/'],
         'slot_uri': 'spdx_expanded_licensing:isOsiApproved'} })
    standardLicenseHeader: Optional[str] = Field(default=None, description="""Provides a License author's preferred text to indicate that a file is covered by the License.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseHeader/'],
         'slot_uri': 'spdx_expanded_licensing:standardLicenseHeader'} })
    standardLicenseTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a License, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseTemplate/'],
         'slot_uri': 'spdx_expanded_licensing:standardLicenseTemplate'} })
    type: Literal["https://w3id.org/lmodel/spdx/License","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License","spdx_linkml:License","spdx_expanded_licensing:License"] = Field(default="spdx_expanded_licensing:License", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class CustomLicense(License):
    """
    A license that is not listed on the SPDX License List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:CustomLicense',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/CustomLicense/']})

    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SimpleLicensingText', 'License'],
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseText/'],
         'slot_uri': 'spdx_simple_licensing:licenseText'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/'],
         'slot_uri': 'spdx_expanded_licensing:licenseXml'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/'],
         'slot_uri': 'spdx_expanded_licensing:obsoletedBy'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/'],
         'slot_uri': 'spdx_expanded_licensing:seeAlso'} })
    isDeprecatedLicenseId: Optional[bool] = Field(default=None, description="""Specifies whether a license or additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedLicenseId/'],
         'slot_uri': 'spdx_expanded_licensing:isDeprecatedLicenseId'} })
    isFsfLibre: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as free by the Free Software Foundation (FSF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isFsfLibre/'],
         'slot_uri': 'spdx_expanded_licensing:isFsfLibre'} })
    isOsiApproved: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as approved by the Open Source Initiative (OSI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isOsiApproved/'],
         'slot_uri': 'spdx_expanded_licensing:isOsiApproved'} })
    standardLicenseHeader: Optional[str] = Field(default=None, description="""Provides a License author's preferred text to indicate that a file is covered by the License.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseHeader/'],
         'slot_uri': 'spdx_expanded_licensing:standardLicenseHeader'} })
    standardLicenseTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a License, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseTemplate/'],
         'slot_uri': 'spdx_expanded_licensing:standardLicenseTemplate'} })
    type: Literal["https://w3id.org/lmodel/spdx/CustomLicense","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense","spdx_linkml:CustomLicense","spdx_expanded_licensing:CustomLicense"] = Field(default="spdx_expanded_licensing:CustomLicense", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class LicenseAddition(Element):
    """
    Abstract class for additional text intended to be added to a License, but which is not itself a standalone License.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_expanded_licensing:LicenseAddition',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/LicenseAddition/']})

    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/'],
         'slot_uri': 'spdx_expanded_licensing:licenseXml'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/'],
         'slot_uri': 'spdx_expanded_licensing:obsoletedBy'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/'],
         'slot_uri': 'spdx_expanded_licensing:seeAlso'} })
    additionText: str = Field(default=..., description="""Identifies the full text of a LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/additionText/'],
         'slot_uri': 'spdx_expanded_licensing:additionText'} })
    isDeprecatedAdditionId: Optional[bool] = Field(default=None, description="""Specifies whether an additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedAdditionId/'],
         'slot_uri': 'spdx_expanded_licensing:isDeprecatedAdditionId'} })
    standardAdditionTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a LicenseAddition, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardAdditionTemplate/'],
         'slot_uri': 'spdx_expanded_licensing:standardAdditionTemplate'} })
    type: Literal["https://w3id.org/lmodel/spdx/LicenseAddition","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition","spdx_linkml:LicenseAddition","spdx_expanded_licensing:LicenseAddition"] = Field(default="spdx_expanded_licensing:LicenseAddition", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class CustomLicenseAddition(LicenseAddition):
    """
    A license addition that is not listed on the SPDX Exceptions List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:CustomLicenseAddition',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/CustomLicenseAddition/']})

    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/'],
         'slot_uri': 'spdx_expanded_licensing:licenseXml'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/'],
         'slot_uri': 'spdx_expanded_licensing:obsoletedBy'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/'],
         'slot_uri': 'spdx_expanded_licensing:seeAlso'} })
    additionText: str = Field(default=..., description="""Identifies the full text of a LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/additionText/'],
         'slot_uri': 'spdx_expanded_licensing:additionText'} })
    isDeprecatedAdditionId: Optional[bool] = Field(default=None, description="""Specifies whether an additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedAdditionId/'],
         'slot_uri': 'spdx_expanded_licensing:isDeprecatedAdditionId'} })
    standardAdditionTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a LicenseAddition, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardAdditionTemplate/'],
         'slot_uri': 'spdx_expanded_licensing:standardAdditionTemplate'} })
    type: Literal["https://w3id.org/lmodel/spdx/CustomLicenseAddition","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition","spdx_linkml:CustomLicenseAddition","spdx_expanded_licensing:CustomLicenseAddition"] = Field(default="spdx_expanded_licensing:CustomLicenseAddition", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ListedLicense(License):
    """
    A license that is listed on the SPDX License List.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:ListedLicense',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/ListedLicense/']})

    deprecatedVersion: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this license or exception identifier was deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/deprecatedVersion/'],
         'slot_uri': 'spdx_expanded_licensing:deprecatedVersion'} })
    listVersionAdded: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this ListedLicense or ListedLicenseException identifier was first added.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/listVersionAdded/'],
         'slot_uri': 'spdx_expanded_licensing:listVersionAdded'} })
    licenseText: str = Field(default=..., description="""Identifies the full text of a License or Addition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SimpleLicensingText', 'License'],
         'in_subset': ['spdx_simple_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/SimpleLicensing/Properties/licenseText/'],
         'slot_uri': 'spdx_simple_licensing:licenseText'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/'],
         'slot_uri': 'spdx_expanded_licensing:licenseXml'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/'],
         'slot_uri': 'spdx_expanded_licensing:obsoletedBy'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/'],
         'slot_uri': 'spdx_expanded_licensing:seeAlso'} })
    isDeprecatedLicenseId: Optional[bool] = Field(default=None, description="""Specifies whether a license or additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedLicenseId/'],
         'slot_uri': 'spdx_expanded_licensing:isDeprecatedLicenseId'} })
    isFsfLibre: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as free by the Free Software Foundation (FSF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isFsfLibre/'],
         'slot_uri': 'spdx_expanded_licensing:isFsfLibre'} })
    isOsiApproved: Optional[bool] = Field(default=None, description="""Specifies whether the License is listed as approved by the Open Source Initiative (OSI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isOsiApproved/'],
         'slot_uri': 'spdx_expanded_licensing:isOsiApproved'} })
    standardLicenseHeader: Optional[str] = Field(default=None, description="""Provides a License author's preferred text to indicate that a file is covered by the License.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseHeader/'],
         'slot_uri': 'spdx_expanded_licensing:standardLicenseHeader'} })
    standardLicenseTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a License, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardLicenseTemplate/'],
         'slot_uri': 'spdx_expanded_licensing:standardLicenseTemplate'} })
    type: Literal["https://w3id.org/lmodel/spdx/ListedLicense","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense","spdx_linkml:ListedLicense","spdx_expanded_licensing:ListedLicense"] = Field(default="spdx_expanded_licensing:ListedLicense", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ListedLicenseException(LicenseAddition):
    """
    A license exception that is listed on the SPDX Exceptions list.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:ListedLicenseException',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/ListedLicenseException/']})

    deprecatedVersion: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this license or exception identifier was deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/deprecatedVersion/'],
         'slot_uri': 'spdx_expanded_licensing:deprecatedVersion'} })
    listVersionAdded: Optional[str] = Field(default=None, description="""Specifies the SPDX License List version in which this ListedLicense or ListedLicenseException identifier was first added.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ListedLicense', 'ListedLicenseException'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/listVersionAdded/'],
         'slot_uri': 'spdx_expanded_licensing:listVersionAdded'} })
    licenseXml: Optional[str] = Field(default=None, description="""Identifies all the text and metadata associated with a license in the license XML format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/licenseXml/'],
         'slot_uri': 'spdx_expanded_licensing:licenseXml'} })
    obsoletedBy: Optional[str] = Field(default=None, description="""Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/obsoletedBy/'],
         'slot_uri': 'spdx_expanded_licensing:obsoletedBy'} })
    seeAlso: Optional[list[str]] = Field(default=None, description="""Contains a URL where the License or LicenseAddition can be found in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'LicenseAddition'],
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/seeAlso/'],
         'slot_uri': 'spdx_expanded_licensing:seeAlso'} })
    additionText: str = Field(default=..., description="""Identifies the full text of a LicenseAddition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/additionText/'],
         'slot_uri': 'spdx_expanded_licensing:additionText'} })
    isDeprecatedAdditionId: Optional[bool] = Field(default=None, description="""Specifies whether an additional text identifier has been marked as deprecated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/isDeprecatedAdditionId/'],
         'slot_uri': 'spdx_expanded_licensing:isDeprecatedAdditionId'} })
    standardAdditionTemplate: Optional[str] = Field(default=None, description="""Identifies the full text of a LicenseAddition, in SPDX templating format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LicenseAddition'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/standardAdditionTemplate/'],
         'slot_uri': 'spdx_expanded_licensing:standardAdditionTemplate'} })
    type: Literal["https://w3id.org/lmodel/spdx/ListedLicenseException","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException","spdx_linkml:ListedLicenseException","spdx_expanded_licensing:ListedLicenseException"] = Field(default="spdx_expanded_licensing:ListedLicenseException", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class OrLaterOperator(ExtendableLicense):
    """
    Portion of an AnyLicenseInfo representing this version, or any later version, of the indicated License.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:OrLaterOperator',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/OrLaterOperator/']})

    subjectLicense: str = Field(default=..., description="""A License participating in an 'or later' model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OrLaterOperator'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/subjectLicense/'],
         'slot_uri': 'spdx_expanded_licensing:subjectLicense'} })
    type: Literal["https://w3id.org/lmodel/spdx/OrLaterOperator","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator","spdx_linkml:OrLaterOperator","spdx_expanded_licensing:OrLaterOperator"] = Field(default="spdx_expanded_licensing:OrLaterOperator", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class WithAdditionOperator(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a License which has additional text applied to it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_expanded_licensing:WithAdditionOperator',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_expanded_licensing',
         'in_subset': ['spdx_expanded_licensing'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Classes/WithAdditionOperator/']})

    subjectAddition: str = Field(default=..., description="""A LicenseAddition participating in a 'with addition' model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithAdditionOperator'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/subjectAddition/'],
         'slot_uri': 'spdx_expanded_licensing:subjectAddition'} })
    subjectExtendableLicense: str = Field(default=..., description="""A License participating in a 'with addition' model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithAdditionOperator'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/ExpandedLicensing/Properties/subjectExtendableLicense/'],
         'slot_uri': 'spdx_expanded_licensing:subjectExtendableLicense'} })
    type: Literal["https://w3id.org/lmodel/spdx/WithAdditionOperator","https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator","spdx_linkml:WithAdditionOperator","spdx_expanded_licensing:WithAdditionOperator"] = Field(default="spdx_expanded_licensing:WithAdditionOperator", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class VulnAssessmentRelationship(Relationship):
    """
    Abstract ancestor class for all vulnerability assessments
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_security:VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/VulnAssessmentRelationship/']})

    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/VulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship","spdx_linkml:VulnAssessmentRelationship","spdx_security:VulnAssessmentRelationship"] = Field(default="spdx_security:VulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class CvssV2VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 2.0 assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:CvssV2VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/CvssV2VulnAssessmentRelationship/']})

    score: Decimal = Field(default=..., description="""Provides a numerical (0-10) representation of the severity of a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/score/'],
         'slot_uri': 'spdx_security:score'} })
    vectorString: str = Field(default=..., description="""Specifies the CVSS vector string for a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vectorString/'],
         'slot_uri': 'spdx_security:vectorString'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/CvssV2VulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship","spdx_linkml:CvssV2VulnAssessmentRelationship","spdx_security:CvssV2VulnAssessmentRelationship"] = Field(default="spdx_security:CvssV2VulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class CvssV3VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 3 assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:CvssV3VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/CvssV3VulnAssessmentRelationship/']})

    score: Decimal = Field(default=..., description="""Provides a numerical (0-10) representation of the severity of a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/score/'],
         'slot_uri': 'spdx_security:score'} })
    severity: CvssSeverityType = Field(default=..., description="""Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/severity/'],
         'slot_uri': 'spdx_security:severity'} })
    vectorString: str = Field(default=..., description="""Specifies the CVSS vector string for a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vectorString/'],
         'slot_uri': 'spdx_security:vectorString'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/CvssV3VulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship","spdx_linkml:CvssV3VulnAssessmentRelationship","spdx_security:CvssV3VulnAssessmentRelationship"] = Field(default="spdx_security:CvssV3VulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class CvssV4VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 4 assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:CvssV4VulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/CvssV4VulnAssessmentRelationship/']})

    score: Decimal = Field(default=..., description="""Provides a numerical (0-10) representation of the severity of a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/score/'],
         'slot_uri': 'spdx_security:score'} })
    severity: CvssSeverityType = Field(default=..., description="""Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/severity/'],
         'slot_uri': 'spdx_security:severity'} })
    vectorString: str = Field(default=..., description="""Specifies the CVSS vector string for a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CvssV2VulnAssessmentRelationship',
                       'CvssV3VulnAssessmentRelationship',
                       'CvssV4VulnAssessmentRelationship'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vectorString/'],
         'slot_uri': 'spdx_security:vectorString'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/CvssV4VulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship","spdx_linkml:CvssV4VulnAssessmentRelationship","spdx_security:CvssV4VulnAssessmentRelationship"] = Field(default="spdx_security:CvssV4VulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class EpssVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an EPSS assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:EpssVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/EpssVulnAssessmentRelationship/']})

    percentile: Decimal = Field(default=..., description="""The percentile of the current probability score.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EpssVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/percentile/'],
         'slot_uri': 'spdx_security:percentile'} })
    probability: Decimal = Field(default=..., description="""A probability score between 0 and 1 of a vulnerability being exploited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EpssVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/probability/'],
         'slot_uri': 'spdx_security:probability'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/EpssVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship","spdx_linkml:EpssVulnAssessmentRelationship","spdx_security:EpssVulnAssessmentRelationship"] = Field(default="spdx_security:EpssVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class ExploitCatalogVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an exploit assessment of a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:ExploitCatalogVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/ExploitCatalogVulnAssessmentRelationship/']})

    catalogType: ExploitCatalogType = Field(default=..., description="""Specifies the exploit catalog type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExploitCatalogVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/catalogType/'],
         'slot_uri': 'spdx_security:catalogType'} })
    exploited: bool = Field(default=..., description="""Describe that a CVE is known to have an exploit because it's been listed in an exploit catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExploitCatalogVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/exploited/'],
         'slot_uri': 'spdx_security:exploited'} })
    security_locator: str = Field(default=..., description="""Provides the location of an exploit catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExploitCatalogVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/locator/'],
         'slot_uri': 'spdx_security:locator'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/ExploitCatalogVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship","spdx_linkml:ExploitCatalogVulnAssessmentRelationship","spdx_security:ExploitCatalogVulnAssessmentRelationship"] = Field(default="spdx_security:ExploitCatalogVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class SsvcVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an SSVC assessment for a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:SsvcVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/SsvcVulnAssessmentRelationship/']})

    decisionType: SsvcDecisionType = Field(default=..., description="""Provide the enumeration of possible decisions in the [Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsvcVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/decisionType/'],
         'slot_uri': 'spdx_security:decisionType'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/SsvcVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship","spdx_linkml:SsvcVulnAssessmentRelationship","spdx_security:SsvcVulnAssessmentRelationship"] = Field(default="spdx_security:SsvcVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class VexVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Abstract ancestor class for all VEX relationships
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'spdx_security:VexVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/VexVulnAssessmentRelationship/']})

    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/statusNotes/'],
         'slot_uri': 'spdx_security:statusNotes'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vexVersion/'],
         'slot_uri': 'spdx_security:vexVersion'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/VexVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship","spdx_linkml:VexVulnAssessmentRelationship","spdx_security:VexVulnAssessmentRelationship"] = Field(default="spdx_security:VexVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class VexAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Connects a vulnerability and an element designating the element as a product affected by the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:VexAffectedVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/VexAffectedVulnAssessmentRelationship/']})

    actionStatement: str = Field(default=..., description="""Provides advise on how to mitigate or remediate a vulnerability when a VEX product is affected by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexAffectedVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/actionStatement/'],
         'slot_uri': 'spdx_security:actionStatement'} })
    actionStatementTime: Optional[str] = Field(default=None, description="""Records the time when a recommended action was communicated in a VEX statement to mitigate a vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexAffectedVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/actionStatementTime/'],
         'slot_uri': 'spdx_security:actionStatementTime'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/statusNotes/'],
         'slot_uri': 'spdx_security:statusNotes'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vexVersion/'],
         'slot_uri': 'spdx_security:vexVersion'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/VexAffectedVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship","spdx_linkml:VexAffectedVulnAssessmentRelationship","spdx_security:VexAffectedVulnAssessmentRelationship"] = Field(default="spdx_security:VexAffectedVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class VexFixedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and elements representing products (in the VEX sense) where a fix has been applied and are no longer affected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:VexFixedVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/VexFixedVulnAssessmentRelationship/']})

    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/statusNotes/'],
         'slot_uri': 'spdx_security:statusNotes'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vexVersion/'],
         'slot_uri': 'spdx_security:vexVersion'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/VexFixedVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship","spdx_linkml:VexFixedVulnAssessmentRelationship","spdx_security:VexFixedVulnAssessmentRelationship"] = Field(default="spdx_security:VexFixedVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class VexNotAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and one or more elements designating the latter as products not affected by the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:VexNotAffectedVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/VexNotAffectedVulnAssessmentRelationship/']})

    impactStatement: Optional[str] = Field(default=None, description="""Explains why a VEX product is not affected by a vulnerability. It is an alternative in VexNotAffectedVulnAssessmentRelationship to the machine-readable justification label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexNotAffectedVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/impactStatement/'],
         'slot_uri': 'spdx_security:impactStatement'} })
    impactStatementTime: Optional[str] = Field(default=None, description="""Timestamp of impact statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexNotAffectedVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/impactStatementTime/'],
         'slot_uri': 'spdx_security:impactStatementTime'} })
    justificationType: Optional[VexJustificationType] = Field(default=None, description="""Impact justification label to be used when linking a vulnerability to an element representing a VEX product with a VexNotAffectedVulnAssessmentRelationship relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexNotAffectedVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/justificationType/'],
         'slot_uri': 'spdx_security:justificationType'} })
    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/statusNotes/'],
         'slot_uri': 'spdx_security:statusNotes'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vexVersion/'],
         'slot_uri': 'spdx_security:vexVersion'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/VexNotAffectedVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship","spdx_linkml:VexNotAffectedVulnAssessmentRelationship","spdx_security:VexNotAffectedVulnAssessmentRelationship"] = Field(default="spdx_security:VexNotAffectedVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class VexUnderInvestigationVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Designates elements as products where the impact of a vulnerability is being investigated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:VexUnderInvestigationVulnAssessmentRelationship',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/VexUnderInvestigationVulnAssessmentRelationship/']})

    statusNotes: Optional[str] = Field(default=None, description="""Conveys information about how VEX status was determined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/statusNotes/'],
         'slot_uri': 'spdx_security:statusNotes'} })
    vexVersion: Optional[str] = Field(default=None, description="""Specifies the version of a VEX statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VexVulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/vexVersion/'],
         'slot_uri': 'spdx_security:vexVersion'} })
    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    assessedElement: Optional[str] = Field(default=None, description="""Specifies an Element contained in a piece of software where a vulnerability was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/assessedElement/'],
         'slot_uri': 'spdx_security:assessedElement'} })
    completeness: Optional[RelationshipCompleteness] = Field(default=None, description="""Provides information about the completeness of relationships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/completeness/'],
         'slot_uri': 'spdx_core:completeness'} })
    endTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is no longer applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/endTime/'],
         'slot_uri': 'spdx_core:endTime'} })
    from_: str = Field(default=..., alias="from", description="""References the Element on the left-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/from/'],
         'slot_uri': 'spdx_core:from'} })
    relationshipType: RelationshipType = Field(default=..., description="""Information about the relationship between two Elements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/relationshipType/'],
         'slot_uri': 'spdx_core:relationshipType'} })
    startTime: Optional[str] = Field(default=None, description="""Specifies the time from which an element is applicable / valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/startTime/'],
         'slot_uri': 'spdx_core:startTime'} })
    to: list[str] = Field(default=..., description="""References an Element on the right-hand side of a relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/to/'],
         'slot_uri': 'spdx_core:to'} })
    type: Literal["https://w3id.org/lmodel/spdx/VexUnderInvestigationVulnAssessmentRelationship","https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship","spdx_linkml:VexUnderInvestigationVulnAssessmentRelationship","spdx_security:VexUnderInvestigationVulnAssessmentRelationship"] = Field(default="spdx_security:VexUnderInvestigationVulnAssessmentRelationship", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


class Vulnerability(Artifact):
    """
    Specifies a vulnerability and its associated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'spdx_security:Vulnerability',
         'from_schema': 'https://w3id.org/lmodel/spdx/spdx_security',
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Classes/Vulnerability/']})

    modifiedTime: Optional[str] = Field(default=None, description="""Specifies a time when a vulnerability assessment was modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/modifiedTime/'],
         'slot_uri': 'spdx_security:modifiedTime'} })
    publishedTime: Optional[str] = Field(default=None, description="""Specifies the time when a vulnerability was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/publishedTime/'],
         'slot_uri': 'spdx_security:publishedTime'} })
    withdrawnTime: Optional[str] = Field(default=None, description="""Specified the time and date when a vulnerability was withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VulnAssessmentRelationship', 'Vulnerability'],
         'in_subset': ['spdx_security'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Security/Properties/withdrawnTime/'],
         'slot_uri': 'spdx_security:withdrawnTime'} })
    suppliedBy: Optional[str] = Field(default=None, description="""Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact', 'VulnAssessmentRelationship'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/suppliedBy/'],
         'slot_uri': 'spdx_core:suppliedBy'} })
    builtTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was built.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/builtTime/'],
         'slot_uri': 'spdx_core:builtTime'} })
    originatedBy: Optional[list[str]] = Field(default=None, description="""Identifies from where or whom the Element originally came.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/originatedBy/'],
         'slot_uri': 'spdx_core:originatedBy'} })
    releaseTime: Optional[str] = Field(default=None, description="""Specifies the time an artifact was released.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/releaseTime/'],
         'slot_uri': 'spdx_core:releaseTime'} })
    standardName: Optional[list[str]] = Field(default=None, description="""The name of a relevant standard that may apply to an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/standardName/'],
         'slot_uri': 'spdx_core:standardName'} })
    supportLevel: Optional[list[SupportType]] = Field(default=None, description="""Specifies the level of support associated with an artifact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/supportLevel/'],
         'slot_uri': 'spdx_core:supportLevel'} })
    validUntilTime: Optional[str] = Field(default=None, description="""Specifies until when the artifact can be used before its usage needs to be reassessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Artifact'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/validUntilTime/'],
         'slot_uri': 'spdx_core:validUntilTime'} })
    type: Literal["https://w3id.org/lmodel/spdx/Vulnerability","https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability","spdx_linkml:Vulnerability","spdx_security:Vulnerability"] = Field(default="spdx_security:Vulnerability", description="""The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.""", json_schema_extra = { "linkml_meta": {'comments': ['SPDX JSON-LD writes the same key with a term of its context, '
                      "software_Package for a Package. This schema takes the class's "
                      'CURIE or its full IRI, so RDF written from the data types each '
                      'object with its SPDX class.'],
         'designates_type': True,
         'domain_of': ['CreationInfo',
                       'DictionaryEntry',
                       'Element',
                       'Extension',
                       'ExternalIdentifier',
                       'ExternalMap',
                       'ExternalRef',
                       'IntegrityMethod',
                       'NamespaceMap',
                       'PositiveIntegerRange',
                       'CdxPropertyEntry',
                       'EnergyConsumption',
                       'EnergyConsumptionDescription'],
         'in_subset': ['spdx_core'],
         'slot_uri': 'rdf:type'} })
    comment: Optional[str] = Field(default=None, description="""Provide consumers with comments by the creator of the Element about the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CreationInfo',
                       'Element',
                       'ExternalIdentifier',
                       'ExternalRef',
                       'IntegrityMethod'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/comment/'],
         'slot_uri': 'spdx_core:comment'} })
    verifiedUsing: Optional[list[Union[Hash,PackageVerificationCode,ContentIdentifier]]] = Field(default=None, description="""Provides an IntegrityMethod with which the integrity of an Element can be asserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element', 'ExternalMap'],
         'in_subset': ['spdx_core'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/verifiedUsing/'],
         'slot_uri': 'spdx_core:verifiedUsing'} })
    spdxId: str = Field(default=..., description="""The IRI that identifies this Element. A reference to an Element from any field is this IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["SPDX JSON-LD writes an Element's IRI as spdxId. The model has "
                      "no property for it, so this key is the schema's own, in its own "
                      'namespace.'],
         'domain_of': ['Element']} })
    creationInfo: CreationInfo = Field(default=..., description="""Provides information about the creation of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/creationInfo/'],
         'slot_uri': 'spdx_core:creationInfo'} })
    description: Optional[str] = Field(default=None, description="""Provides a detailed description of the Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/description/'],
         'slot_uri': 'spdx_core:description'} })
    extension: Optional[list[Union[CdxPropertiesExtension]]] = Field(default=None, description="""Specifies an Extension characterization of some aspect of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/extension/'],
         'slot_uri': 'spdx_core:extension'} })
    externalIdentifier: Optional[list[ExternalIdentifier]] = Field(default=None, description="""Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalIdentifier/'],
         'slot_uri': 'spdx_core:externalIdentifier'} })
    externalRef: Optional[list[ExternalRef]] = Field(default=None, description="""Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/externalRef/'],
         'slot_uri': 'spdx_core:externalRef'} })
    name: Optional[str] = Field(default=None, description="""Identifies the name of an Element as designated by the creator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/name/'],
         'slot_uri': 'spdx_core:name'} })
    summary: Optional[str] = Field(default=None, description="""A short description of an Element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Element'],
         'see_also': ['https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Properties/summary/'],
         'slot_uri': 'spdx_core:summary'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CreationInfo.model_rebuild()
DictionaryEntry.model_rebuild()
Element.model_rebuild()
Agent.model_rebuild()
Annotation.model_rebuild()
AnyLicenseInfo.model_rebuild()
Artifact.model_rebuild()
ElementCollection.model_rebuild()
Bundle.model_rebuild()
Bom.model_rebuild()
Extension.model_rebuild()
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
Build.model_rebuild()
CdxPropertiesExtension.model_rebuild()
CdxPropertyEntry.model_rebuild()
LicenseExpression.model_rebuild()
SimpleLicensingText.model_rebuild()
ContentIdentifier.model_rebuild()
Sbom.model_rebuild()
SoftwareArtifact.model_rebuild()
File.model_rebuild()
Package.model_rebuild()
Snippet.model_rebuild()
AIPackage.model_rebuild()
EnergyConsumption.model_rebuild()
EnergyConsumptionDescription.model_rebuild()
DatasetPackage.model_rebuild()
ConjunctiveLicenseSet.model_rebuild()
DisjunctiveLicenseSet.model_rebuild()
ExtendableLicense.model_rebuild()
IndividualLicensingInfo.model_rebuild()
License.model_rebuild()
CustomLicense.model_rebuild()
LicenseAddition.model_rebuild()
CustomLicenseAddition.model_rebuild()
ListedLicense.model_rebuild()
ListedLicenseException.model_rebuild()
OrLaterOperator.model_rebuild()
WithAdditionOperator.model_rebuild()
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
