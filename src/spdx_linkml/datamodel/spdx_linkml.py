# Auto generated from spdx_linkml.yaml by pythongen.py version: 0.0.1
# Schema: spdx_linkml
#
# id: https://w3id.org/lmodel/spdx
# description: A LinkML rendering of the SPDX 3.0.1 model: its nine profiles, each a module, with every class, property and vocabulary keeping its SPDX IRI.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Decimal, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI, URIorCURIE

metamodel_version = "1.12.0"
version = "3.0.1"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SPDX = CurieNamespace('spdx', 'https://spdx.org/rdf/3.0.1/terms/')
SPDX_AI = CurieNamespace('spdx_ai', 'https://spdx.org/rdf/3.0.1/terms/AI/')
SPDX_BUILD = CurieNamespace('spdx_build', 'https://spdx.org/rdf/3.0.1/terms/Build/')
SPDX_CORE = CurieNamespace('spdx_core', 'https://spdx.org/rdf/3.0.1/terms/Core/')
SPDX_DATASET = CurieNamespace('spdx_dataset', 'https://spdx.org/rdf/3.0.1/terms/Dataset/')
SPDX_EXPANDED_LICENSING = CurieNamespace('spdx_expanded_licensing', 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/')
SPDX_EXTENSION = CurieNamespace('spdx_extension', 'https://spdx.org/rdf/3.0.1/terms/Extension/')
SPDX_LINKML = CurieNamespace('spdx_linkml', 'https://w3id.org/lmodel/spdx/')
SPDX_SECURITY = CurieNamespace('spdx_security', 'https://spdx.org/rdf/3.0.1/terms/Security/')
SPDX_SIMPLE_LICENSING = CurieNamespace('spdx_simple_licensing', 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/')
SPDX_SOFTWARE = CurieNamespace('spdx_software', 'https://spdx.org/rdf/3.0.1/terms/Software/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SPDX_LINKML


# Types
class DateTimeStamp(String):
    """ A UTC timestamp as SPDX writes one: a date, a time to the second and a trailing Z. """
    type_class_uri = XSD["dateTimeStamp"]
    type_class_curie = "xsd:dateTimeStamp"
    type_name = "date_time_stamp"
    type_model_uri = SPDX_LINKML.DateTimeStamp


class MediaType(String):
    """ An IANA media type, such as text/plain. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "media_type"
    type_model_uri = SPDX_LINKML.MediaType


class Semver(String):
    """ A semantic version, such as 3.0.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "semver"
    type_model_uri = SPDX_LINKML.Semver


class PositiveInteger(Integer):
    """ An integer of one or more. """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive_integer"
    type_model_uri = SPDX_LINKML.PositiveInteger


class NonNegativeInteger(Integer):
    """ An integer of zero or more. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non_negative_integer"
    type_model_uri = SPDX_LINKML.NonNegativeInteger


# Class references
class ElementSpdxId(URI):
    pass


class AgentSpdxId(ElementSpdxId):
    pass


class AnnotationSpdxId(ElementSpdxId):
    pass


class AnyLicenseInfoSpdxId(ElementSpdxId):
    pass


class ArtifactSpdxId(ElementSpdxId):
    pass


class ElementCollectionSpdxId(ElementSpdxId):
    pass


class BundleSpdxId(ElementCollectionSpdxId):
    pass


class BomSpdxId(BundleSpdxId):
    pass


class IndividualElementSpdxId(ElementSpdxId):
    pass


class OrganizationSpdxId(AgentSpdxId):
    pass


class PersonSpdxId(AgentSpdxId):
    pass


class RelationshipSpdxId(ElementSpdxId):
    pass


class LifecycleScopedRelationshipSpdxId(RelationshipSpdxId):
    pass


class SoftwareAgentSpdxId(AgentSpdxId):
    pass


class SpdxDocumentSpdxId(ElementCollectionSpdxId):
    pass


class ToolSpdxId(ElementSpdxId):
    pass


class BuildSpdxId(ElementSpdxId):
    pass


class LicenseExpressionSpdxId(AnyLicenseInfoSpdxId):
    pass


class SimpleLicensingTextSpdxId(ElementSpdxId):
    pass


class SbomSpdxId(BomSpdxId):
    pass


class SoftwareArtifactSpdxId(ArtifactSpdxId):
    pass


class FileSpdxId(SoftwareArtifactSpdxId):
    pass


class PackageSpdxId(SoftwareArtifactSpdxId):
    pass


class SnippetSpdxId(SoftwareArtifactSpdxId):
    pass


class AIPackageSpdxId(PackageSpdxId):
    pass


class DatasetPackageSpdxId(PackageSpdxId):
    pass


class ConjunctiveLicenseSetSpdxId(AnyLicenseInfoSpdxId):
    pass


class DisjunctiveLicenseSetSpdxId(AnyLicenseInfoSpdxId):
    pass


class ExtendableLicenseSpdxId(AnyLicenseInfoSpdxId):
    pass


class IndividualLicensingInfoSpdxId(AnyLicenseInfoSpdxId):
    pass


class LicenseSpdxId(ExtendableLicenseSpdxId):
    pass


class CustomLicenseSpdxId(LicenseSpdxId):
    pass


class LicenseAdditionSpdxId(ElementSpdxId):
    pass


class CustomLicenseAdditionSpdxId(LicenseAdditionSpdxId):
    pass


class ListedLicenseSpdxId(LicenseSpdxId):
    pass


class ListedLicenseExceptionSpdxId(LicenseAdditionSpdxId):
    pass


class OrLaterOperatorSpdxId(ExtendableLicenseSpdxId):
    pass


class WithAdditionOperatorSpdxId(AnyLicenseInfoSpdxId):
    pass


class VulnAssessmentRelationshipSpdxId(RelationshipSpdxId):
    pass


class CvssV2VulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class CvssV3VulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class CvssV4VulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class EpssVulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class ExploitCatalogVulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class SsvcVulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class VexVulnAssessmentRelationshipSpdxId(VulnAssessmentRelationshipSpdxId):
    pass


class VexAffectedVulnAssessmentRelationshipSpdxId(VexVulnAssessmentRelationshipSpdxId):
    pass


class VexFixedVulnAssessmentRelationshipSpdxId(VexVulnAssessmentRelationshipSpdxId):
    pass


class VexNotAffectedVulnAssessmentRelationshipSpdxId(VexVulnAssessmentRelationshipSpdxId):
    pass


class VexUnderInvestigationVulnAssessmentRelationshipSpdxId(VexVulnAssessmentRelationshipSpdxId):
    pass


class VulnerabilitySpdxId(ArtifactSpdxId):
    pass


@dataclass(repr=False)
class CreationInfo(YAMLRoot):
    """
    Provides information about the creation of the Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["CreationInfo"]
    class_class_curie: ClassVar[str] = "spdx_core:CreationInfo"
    class_name: ClassVar[str] = "CreationInfo"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CreationInfo

    created: Union[str, DateTimeStamp] = None
    createdBy: Union[Union[str, AgentSpdxId], list[Union[str, AgentSpdxId]]] = None
    specVersion: Union[str, Semver] = None
    type: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[str] = None
    createdUsing: Optional[Union[Union[str, ToolSpdxId], list[Union[str, ToolSpdxId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, DateTimeStamp):
            self.created = DateTimeStamp(self.created)

        if self._is_empty(self.createdBy):
            self.MissingRequiredField("createdBy")
        if not isinstance(self.createdBy, list):
            self.createdBy = [self.createdBy] if self.createdBy is not None else []
        self.createdBy = [v if isinstance(v, AgentSpdxId) else AgentSpdxId(v) for v in self.createdBy]

        if self._is_empty(self.specVersion):
            self.MissingRequiredField("specVersion")
        if not isinstance(self.specVersion, Semver):
            self.specVersion = Semver(self.specVersion)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if not isinstance(self.createdUsing, list):
            self.createdUsing = [self.createdUsing] if self.createdUsing is not None else []
        self.createdUsing = [v if isinstance(v, ToolSpdxId) else ToolSpdxId(v) for v in self.createdUsing]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DictionaryEntry(YAMLRoot):
    """
    A key with an associated value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["DictionaryEntry"]
    class_class_curie: ClassVar[str] = "spdx_core:DictionaryEntry"
    class_name: ClassVar[str] = "DictionaryEntry"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.DictionaryEntry

    key: str = None
    type: Optional[Union[str, URIorCURIE]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Element(YAMLRoot):
    """
    Base domain class from which all other SPDX-3.0 domain classes derive.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Element"]
    class_class_curie: ClassVar[str] = "spdx_core:Element"
    class_name: ClassVar[str] = "Element"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Element

    spdxId: Union[str, ElementSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    type: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[str] = None
    description: Optional[str] = None
    extension: Optional[Union[Union[dict, "Extension"], list[Union[dict, "Extension"]]]] = empty_list()
    externalIdentifier: Optional[Union[Union[dict, "ExternalIdentifier"], list[Union[dict, "ExternalIdentifier"]]]] = empty_list()
    externalRef: Optional[Union[Union[dict, "ExternalRef"], list[Union[dict, "ExternalRef"]]]] = empty_list()
    name: Optional[str] = None
    summary: Optional[str] = None
    verifiedUsing: Optional[Union[Union[dict, "IntegrityMethod"], list[Union[dict, "IntegrityMethod"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.creationInfo):
            self.MissingRequiredField("creationInfo")
        if not isinstance(self.creationInfo, CreationInfo):
            self.creationInfo = CreationInfo(**as_dict(self.creationInfo))

        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, ElementSpdxId):
            self.spdxId = ElementSpdxId(self.spdxId)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.extension, list):
            self.extension = [self.extension] if self.extension is not None else []
        self.extension = [v if isinstance(v, Extension) else Extension(**as_dict(v)) for v in self.extension]

        self._normalize_inlined_as_list(slot_name="externalIdentifier", slot_type=ExternalIdentifier, key_name="externalIdentifierType", keyed=False)

        if not isinstance(self.externalRef, list):
            self.externalRef = [self.externalRef] if self.externalRef is not None else []
        self.externalRef = [v if isinstance(v, ExternalRef) else ExternalRef(**as_dict(v)) for v in self.externalRef]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.verifiedUsing, list):
            self.verifiedUsing = [self.verifiedUsing] if self.verifiedUsing is not None else []
        self.verifiedUsing = [v if isinstance(v, IntegrityMethod) else IntegrityMethod(**as_dict(v)) for v in self.verifiedUsing]

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Agent(Element):
    """
    Agent represents anything with the potential to act on a system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Agent"]
    class_class_curie: ClassVar[str] = "spdx_core:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Agent

    spdxId: Union[str, AgentSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, AgentSpdxId):
            self.spdxId = AgentSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Annotation(Element):
    """
    An assertion made in relation to one or more elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Annotation"]
    class_class_curie: ClassVar[str] = "spdx_core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Annotation

    spdxId: Union[str, AnnotationSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    annotationType: Union[str, "AnnotationType"] = None
    subject: Union[str, ElementSpdxId] = None
    contentType: Optional[Union[str, MediaType]] = None
    statement: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, AnnotationSpdxId):
            self.spdxId = AnnotationSpdxId(self.spdxId)

        if self._is_empty(self.annotationType):
            self.MissingRequiredField("annotationType")
        if not isinstance(self.annotationType, AnnotationType):
            self.annotationType = AnnotationType(self.annotationType)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ElementSpdxId):
            self.subject = ElementSpdxId(self.subject)

        if self.contentType is not None and not isinstance(self.contentType, MediaType):
            self.contentType = MediaType(self.contentType)

        if self.statement is not None and not isinstance(self.statement, str):
            self.statement = str(self.statement)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AnyLicenseInfo(Element):
    """
    Abstract class representing a license combination consisting of one or more licenses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SIMPLE_LICENSING["AnyLicenseInfo"]
    class_class_curie: ClassVar[str] = "spdx_simple_licensing:AnyLicenseInfo"
    class_name: ClassVar[str] = "AnyLicenseInfo"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.AnyLicenseInfo

    spdxId: Union[str, AnyLicenseInfoSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Artifact(Element):
    """
    A distinct article or unit within the digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Artifact"]
    class_class_curie: ClassVar[str] = "spdx_core:Artifact"
    class_name: ClassVar[str] = "Artifact"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Artifact

    spdxId: Union[str, ArtifactSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    builtTime: Optional[Union[str, DateTimeStamp]] = None
    originatedBy: Optional[Union[Union[str, AgentSpdxId], list[Union[str, AgentSpdxId]]]] = empty_list()
    releaseTime: Optional[Union[str, DateTimeStamp]] = None
    standardName: Optional[Union[str, list[str]]] = empty_list()
    suppliedBy: Optional[Union[str, AgentSpdxId]] = None
    supportLevel: Optional[Union[Union[str, "SupportType"], list[Union[str, "SupportType"]]]] = empty_list()
    validUntilTime: Optional[Union[str, DateTimeStamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.builtTime is not None and not isinstance(self.builtTime, DateTimeStamp):
            self.builtTime = DateTimeStamp(self.builtTime)

        if not isinstance(self.originatedBy, list):
            self.originatedBy = [self.originatedBy] if self.originatedBy is not None else []
        self.originatedBy = [v if isinstance(v, AgentSpdxId) else AgentSpdxId(v) for v in self.originatedBy]

        if self.releaseTime is not None and not isinstance(self.releaseTime, DateTimeStamp):
            self.releaseTime = DateTimeStamp(self.releaseTime)

        if not isinstance(self.standardName, list):
            self.standardName = [self.standardName] if self.standardName is not None else []
        self.standardName = [v if isinstance(v, str) else str(v) for v in self.standardName]

        if self.suppliedBy is not None and not isinstance(self.suppliedBy, AgentSpdxId):
            self.suppliedBy = AgentSpdxId(self.suppliedBy)

        if not isinstance(self.supportLevel, list):
            self.supportLevel = [self.supportLevel] if self.supportLevel is not None else []
        self.supportLevel = [v if isinstance(v, SupportType) else SupportType(v) for v in self.supportLevel]

        if self.validUntilTime is not None and not isinstance(self.validUntilTime, DateTimeStamp):
            self.validUntilTime = DateTimeStamp(self.validUntilTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ElementCollection(Element):
    """
    A collection of Elements, not necessarily with unifying context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["ElementCollection"]
    class_class_curie: ClassVar[str] = "spdx_core:ElementCollection"
    class_name: ClassVar[str] = "ElementCollection"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ElementCollection

    spdxId: Union[str, ElementCollectionSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    element: Optional[Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]]] = empty_list()
    profileConformance: Optional[Union[Union[str, "ProfileIdentifierType"], list[Union[str, "ProfileIdentifierType"]]]] = empty_list()
    rootElement: Optional[Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, ElementSpdxId) else ElementSpdxId(v) for v in self.element]

        if not isinstance(self.profileConformance, list):
            self.profileConformance = [self.profileConformance] if self.profileConformance is not None else []
        self.profileConformance = [v if isinstance(v, ProfileIdentifierType) else ProfileIdentifierType(v) for v in self.profileConformance]

        if not isinstance(self.rootElement, list):
            self.rootElement = [self.rootElement] if self.rootElement is not None else []
        self.rootElement = [v if isinstance(v, ElementSpdxId) else ElementSpdxId(v) for v in self.rootElement]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Bundle(ElementCollection):
    """
    A collection of Elements that have a shared context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Bundle"]
    class_class_curie: ClassVar[str] = "spdx_core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Bundle

    spdxId: Union[str, BundleSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, BundleSpdxId):
            self.spdxId = BundleSpdxId(self.spdxId)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Bom(Bundle):
    """
    A container for a grouping of SPDX-3.0 content characterizing details (provenence, composition, licensing, etc.)
    about a product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Bom"]
    class_class_curie: ClassVar[str] = "spdx_core:Bom"
    class_name: ClassVar[str] = "Bom"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Bom

    spdxId: Union[str, BomSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, BomSpdxId):
            self.spdxId = BomSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Extension(YAMLRoot):
    """
    A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXTENSION["Extension"]
    class_class_curie: ClassVar[str] = "spdx_extension:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Extension

    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class ExternalIdentifier(YAMLRoot):
    """
    A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an
    Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["ExternalIdentifier"]
    class_class_curie: ClassVar[str] = "spdx_core:ExternalIdentifier"
    class_name: ClassVar[str] = "ExternalIdentifier"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ExternalIdentifier

    externalIdentifierType: Union[str, "ExternalIdentifierType"] = None
    identifier: str = None
    type: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[str] = None
    identifierLocator: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    issuingAuthority: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.externalIdentifierType):
            self.MissingRequiredField("externalIdentifierType")
        if not isinstance(self.externalIdentifierType, ExternalIdentifierType):
            self.externalIdentifierType = ExternalIdentifierType(self.externalIdentifierType)

        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if not isinstance(self.identifierLocator, list):
            self.identifierLocator = [self.identifierLocator] if self.identifierLocator is not None else []
        self.identifierLocator = [v if isinstance(v, URI) else URI(v) for v in self.identifierLocator]

        if self.issuingAuthority is not None and not isinstance(self.issuingAuthority, str):
            self.issuingAuthority = str(self.issuingAuthority)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalMap(YAMLRoot):
    """
    A map of Element identifiers that are used within an SpdxDocument but defined external to that SpdxDocument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["ExternalMap"]
    class_class_curie: ClassVar[str] = "spdx_core:ExternalMap"
    class_name: ClassVar[str] = "ExternalMap"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ExternalMap

    externalSpdxId: Union[str, URI] = None
    type: Optional[Union[str, URIorCURIE]] = None
    definingArtifact: Optional[Union[str, ArtifactSpdxId]] = None
    locationHint: Optional[Union[str, URI]] = None
    verifiedUsing: Optional[Union[Union[dict, "IntegrityMethod"], list[Union[dict, "IntegrityMethod"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.externalSpdxId):
            self.MissingRequiredField("externalSpdxId")
        if not isinstance(self.externalSpdxId, URI):
            self.externalSpdxId = URI(self.externalSpdxId)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.definingArtifact is not None and not isinstance(self.definingArtifact, ArtifactSpdxId):
            self.definingArtifact = ArtifactSpdxId(self.definingArtifact)

        if self.locationHint is not None and not isinstance(self.locationHint, URI):
            self.locationHint = URI(self.locationHint)

        if not isinstance(self.verifiedUsing, list):
            self.verifiedUsing = [self.verifiedUsing] if self.verifiedUsing is not None else []
        self.verifiedUsing = [v if isinstance(v, IntegrityMethod) else IntegrityMethod(**as_dict(v)) for v in self.verifiedUsing]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalRef(YAMLRoot):
    """
    A reference to a resource outside the scope of SPDX-3.0 content related to an Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["ExternalRef"]
    class_class_curie: ClassVar[str] = "spdx_core:ExternalRef"
    class_name: ClassVar[str] = "ExternalRef"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ExternalRef

    type: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[str] = None
    contentType: Optional[Union[str, MediaType]] = None
    externalRefType: Optional[Union[str, "ExternalRefType"]] = None
    locator: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.contentType is not None and not isinstance(self.contentType, MediaType):
            self.contentType = MediaType(self.contentType)

        if self.externalRefType is not None and not isinstance(self.externalRefType, ExternalRefType):
            self.externalRefType = ExternalRefType(self.externalRefType)

        if not isinstance(self.locator, list):
            self.locator = [self.locator] if self.locator is not None else []
        self.locator = [v if isinstance(v, str) else str(v) for v in self.locator]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IndividualElement(Element):
    """
    A concrete subclass of Element used by Individuals in the Core profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["IndividualElement"]
    class_class_curie: ClassVar[str] = "spdx_core:IndividualElement"
    class_name: ClassVar[str] = "IndividualElement"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.IndividualElement

    spdxId: Union[str, IndividualElementSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, IndividualElementSpdxId):
            self.spdxId = IndividualElementSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IntegrityMethod(YAMLRoot):
    """
    Provides an independently reproducible mechanism that permits verification of a specific Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["IntegrityMethod"]
    class_class_curie: ClassVar[str] = "spdx_core:IntegrityMethod"
    class_name: ClassVar[str] = "IntegrityMethod"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.IntegrityMethod

    type: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Hash(IntegrityMethod):
    """
    A mathematically calculated representation of a grouping of data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Hash"]
    class_class_curie: ClassVar[str] = "spdx_core:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Hash

    algorithm: Union[str, "HashAlgorithm"] = None
    hashValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, HashAlgorithm):
            self.algorithm = HashAlgorithm(self.algorithm)

        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, str):
            self.hashValue = str(self.hashValue)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NamespaceMap(YAMLRoot):
    """
    A mapping between prefixes and namespace partial URIs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["NamespaceMap"]
    class_class_curie: ClassVar[str] = "spdx_core:NamespaceMap"
    class_name: ClassVar[str] = "NamespaceMap"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.NamespaceMap

    namespace: Union[str, URI] = None
    prefix: str = None
    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.namespace):
            self.MissingRequiredField("namespace")
        if not isinstance(self.namespace, URI):
            self.namespace = URI(self.namespace)

        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(Agent):
    """
    A group of people who work together in an organized way for a shared purpose.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Organization"]
    class_class_curie: ClassVar[str] = "spdx_core:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Organization

    spdxId: Union[str, OrganizationSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, OrganizationSpdxId):
            self.spdxId = OrganizationSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PackageVerificationCode(IntegrityMethod):
    """
    An SPDX version 2.X compatible verification method for software packages.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["PackageVerificationCode"]
    class_class_curie: ClassVar[str] = "spdx_core:PackageVerificationCode"
    class_name: ClassVar[str] = "PackageVerificationCode"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.PackageVerificationCode

    algorithm: Union[str, "HashAlgorithm"] = None
    hashValue: str = None
    packageVerificationCodeExcludedFile: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, HashAlgorithm):
            self.algorithm = HashAlgorithm(self.algorithm)

        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, str):
            self.hashValue = str(self.hashValue)

        if not isinstance(self.packageVerificationCodeExcludedFile, list):
            self.packageVerificationCodeExcludedFile = [self.packageVerificationCodeExcludedFile] if self.packageVerificationCodeExcludedFile is not None else []
        self.packageVerificationCodeExcludedFile = [v if isinstance(v, str) else str(v) for v in self.packageVerificationCodeExcludedFile]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Person(Agent):
    """
    An individual human being.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Person"]
    class_class_curie: ClassVar[str] = "spdx_core:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Person

    spdxId: Union[str, PersonSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, PersonSpdxId):
            self.spdxId = PersonSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PositiveIntegerRange(YAMLRoot):
    """
    A tuple of two positive integers that define a range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["PositiveIntegerRange"]
    class_class_curie: ClassVar[str] = "spdx_core:PositiveIntegerRange"
    class_name: ClassVar[str] = "PositiveIntegerRange"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.PositiveIntegerRange

    beginIntegerRange: Union[int, PositiveInteger] = None
    endIntegerRange: Union[int, PositiveInteger] = None
    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.beginIntegerRange):
            self.MissingRequiredField("beginIntegerRange")
        if not isinstance(self.beginIntegerRange, PositiveInteger):
            self.beginIntegerRange = PositiveInteger(self.beginIntegerRange)

        if self._is_empty(self.endIntegerRange):
            self.MissingRequiredField("endIntegerRange")
        if not isinstance(self.endIntegerRange, PositiveInteger):
            self.endIntegerRange = PositiveInteger(self.endIntegerRange)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(Element):
    """
    Describes a relationship between one or more elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Relationship"]
    class_class_curie: ClassVar[str] = "spdx_core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Relationship

    spdxId: Union[str, RelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    completeness: Optional[Union[str, "RelationshipCompleteness"]] = None
    endTime: Optional[Union[str, DateTimeStamp]] = None
    startTime: Optional[Union[str, DateTimeStamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, RelationshipSpdxId):
            self.spdxId = RelationshipSpdxId(self.spdxId)

        if self._is_empty(self.from_):
            self.MissingRequiredField("from_")
        if not isinstance(self.from_, ElementSpdxId):
            self.from_ = ElementSpdxId(self.from_)

        if self._is_empty(self.relationshipType):
            self.MissingRequiredField("relationshipType")
        if not isinstance(self.relationshipType, RelationshipType):
            self.relationshipType = RelationshipType(self.relationshipType)

        if self._is_empty(self.to):
            self.MissingRequiredField("to")
        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ElementSpdxId) else ElementSpdxId(v) for v in self.to]

        if self.completeness is not None and not isinstance(self.completeness, RelationshipCompleteness):
            self.completeness = RelationshipCompleteness(self.completeness)

        if self.endTime is not None and not isinstance(self.endTime, DateTimeStamp):
            self.endTime = DateTimeStamp(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, DateTimeStamp):
            self.startTime = DateTimeStamp(self.startTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LifecycleScopedRelationship(Relationship):
    """
    Provide context for a relationship that occurs in the lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["LifecycleScopedRelationship"]
    class_class_curie: ClassVar[str] = "spdx_core:LifecycleScopedRelationship"
    class_name: ClassVar[str] = "LifecycleScopedRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.LifecycleScopedRelationship

    spdxId: Union[str, LifecycleScopedRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    scope: Optional[Union[str, "LifecycleScopeType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, LifecycleScopedRelationshipSpdxId):
            self.spdxId = LifecycleScopedRelationshipSpdxId(self.spdxId)

        if self.scope is not None and not isinstance(self.scope, LifecycleScopeType):
            self.scope = LifecycleScopeType(self.scope)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SoftwareAgent(Agent):
    """
    A software agent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["SoftwareAgent"]
    class_class_curie: ClassVar[str] = "spdx_core:SoftwareAgent"
    class_name: ClassVar[str] = "SoftwareAgent"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.SoftwareAgent

    spdxId: Union[str, SoftwareAgentSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, SoftwareAgentSpdxId):
            self.spdxId = SoftwareAgentSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SpdxDocument(ElementCollection):
    """
    A collection of SPDX Elements that could potentially be serialized.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["SpdxDocument"]
    class_class_curie: ClassVar[str] = "spdx_core:SpdxDocument"
    class_name: ClassVar[str] = "SpdxDocument"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.SpdxDocument

    spdxId: Union[str, SpdxDocumentSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    dataLicense: Optional[Union[str, AnyLicenseInfoSpdxId]] = None
    import_: Optional[Union[Union[dict, ExternalMap], list[Union[dict, ExternalMap]]]] = empty_list()
    namespaceMap: Optional[Union[Union[dict, NamespaceMap], list[Union[dict, NamespaceMap]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, SpdxDocumentSpdxId):
            self.spdxId = SpdxDocumentSpdxId(self.spdxId)

        if self.dataLicense is not None and not isinstance(self.dataLicense, AnyLicenseInfoSpdxId):
            self.dataLicense = AnyLicenseInfoSpdxId(self.dataLicense)

        self._normalize_inlined_as_list(slot_name="import_", slot_type=ExternalMap, key_name="externalSpdxId", keyed=False)

        self._normalize_inlined_as_list(slot_name="namespaceMap", slot_type=NamespaceMap, key_name="namespace", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Tool(Element):
    """
    An element of hardware and/or software utilized to carry out a particular function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_CORE["Tool"]
    class_class_curie: ClassVar[str] = "spdx_core:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Tool

    spdxId: Union[str, ToolSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, ToolSpdxId):
            self.spdxId = ToolSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Build(Element):
    """
    Class that describes a build instance of software/artifacts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_BUILD["Build"]
    class_class_curie: ClassVar[str] = "spdx_build:Build"
    class_name: ClassVar[str] = "Build"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Build

    spdxId: Union[str, BuildSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    buildType: Union[str, URI] = None
    buildEndTime: Optional[Union[str, DateTimeStamp]] = None
    buildId: Optional[str] = None
    buildStartTime: Optional[Union[str, DateTimeStamp]] = None
    configSourceDigest: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    configSourceEntrypoint: Optional[Union[str, list[str]]] = empty_list()
    configSourceUri: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    environment: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    parameter: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, BuildSpdxId):
            self.spdxId = BuildSpdxId(self.spdxId)

        if self._is_empty(self.buildType):
            self.MissingRequiredField("buildType")
        if not isinstance(self.buildType, URI):
            self.buildType = URI(self.buildType)

        if self.buildEndTime is not None and not isinstance(self.buildEndTime, DateTimeStamp):
            self.buildEndTime = DateTimeStamp(self.buildEndTime)

        if self.buildId is not None and not isinstance(self.buildId, str):
            self.buildId = str(self.buildId)

        if self.buildStartTime is not None and not isinstance(self.buildStartTime, DateTimeStamp):
            self.buildStartTime = DateTimeStamp(self.buildStartTime)

        self._normalize_inlined_as_list(slot_name="configSourceDigest", slot_type=Hash, key_name="algorithm", keyed=False)

        if not isinstance(self.configSourceEntrypoint, list):
            self.configSourceEntrypoint = [self.configSourceEntrypoint] if self.configSourceEntrypoint is not None else []
        self.configSourceEntrypoint = [v if isinstance(v, str) else str(v) for v in self.configSourceEntrypoint]

        if not isinstance(self.configSourceUri, list):
            self.configSourceUri = [self.configSourceUri] if self.configSourceUri is not None else []
        self.configSourceUri = [v if isinstance(v, URI) else URI(v) for v in self.configSourceUri]

        self._normalize_inlined_as_list(slot_name="environment", slot_type=DictionaryEntry, key_name="key", keyed=False)

        self._normalize_inlined_as_list(slot_name="parameter", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CdxPropertiesExtension(Extension):
    """
    A type of extension consisting of a list of name value pairs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXTENSION["CdxPropertiesExtension"]
    class_class_curie: ClassVar[str] = "spdx_extension:CdxPropertiesExtension"
    class_name: ClassVar[str] = "CdxPropertiesExtension"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CdxPropertiesExtension

    cdxProperty: Union[Union[dict, "CdxPropertyEntry"], list[Union[dict, "CdxPropertyEntry"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cdxProperty):
            self.MissingRequiredField("cdxProperty")
        self._normalize_inlined_as_list(slot_name="cdxProperty", slot_type=CdxPropertyEntry, key_name="cdxPropName", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CdxPropertyEntry(YAMLRoot):
    """
    A property name with an associated value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXTENSION["CdxPropertyEntry"]
    class_class_curie: ClassVar[str] = "spdx_extension:CdxPropertyEntry"
    class_name: ClassVar[str] = "CdxPropertyEntry"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CdxPropertyEntry

    cdxPropName: str = None
    type: Optional[Union[str, URIorCURIE]] = None
    cdxPropValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cdxPropName):
            self.MissingRequiredField("cdxPropName")
        if not isinstance(self.cdxPropName, str):
            self.cdxPropName = str(self.cdxPropName)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.cdxPropValue is not None and not isinstance(self.cdxPropValue, str):
            self.cdxPropValue = str(self.cdxPropValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LicenseExpression(AnyLicenseInfo):
    """
    An SPDX Element containing an SPDX license expression string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SIMPLE_LICENSING["LicenseExpression"]
    class_class_curie: ClassVar[str] = "spdx_simple_licensing:LicenseExpression"
    class_name: ClassVar[str] = "LicenseExpression"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.LicenseExpression

    spdxId: Union[str, LicenseExpressionSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    licenseExpression: str = None
    customIdToUri: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    licenseListVersion: Optional[Union[str, Semver]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, LicenseExpressionSpdxId):
            self.spdxId = LicenseExpressionSpdxId(self.spdxId)

        if self._is_empty(self.licenseExpression):
            self.MissingRequiredField("licenseExpression")
        if not isinstance(self.licenseExpression, str):
            self.licenseExpression = str(self.licenseExpression)

        self._normalize_inlined_as_list(slot_name="customIdToUri", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if self.licenseListVersion is not None and not isinstance(self.licenseListVersion, Semver):
            self.licenseListVersion = Semver(self.licenseListVersion)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SimpleLicensingText(Element):
    """
    A license or addition that is not listed on the SPDX License List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SIMPLE_LICENSING["SimpleLicensingText"]
    class_class_curie: ClassVar[str] = "spdx_simple_licensing:SimpleLicensingText"
    class_name: ClassVar[str] = "SimpleLicensingText"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.SimpleLicensingText

    spdxId: Union[str, SimpleLicensingTextSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, SimpleLicensingTextSpdxId):
            self.spdxId = SimpleLicensingTextSpdxId(self.spdxId)

        if self._is_empty(self.licenseText):
            self.MissingRequiredField("licenseText")
        if not isinstance(self.licenseText, str):
            self.licenseText = str(self.licenseText)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContentIdentifier(IntegrityMethod):
    """
    A canonical, unique, immutable identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SOFTWARE["ContentIdentifier"]
    class_class_curie: ClassVar[str] = "spdx_software:ContentIdentifier"
    class_name: ClassVar[str] = "ContentIdentifier"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ContentIdentifier

    contentIdentifierType: Union[str, "ContentIdentifierType"] = None
    contentIdentifierValue: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.contentIdentifierType):
            self.MissingRequiredField("contentIdentifierType")
        if not isinstance(self.contentIdentifierType, ContentIdentifierType):
            self.contentIdentifierType = ContentIdentifierType(self.contentIdentifierType)

        if self._is_empty(self.contentIdentifierValue):
            self.MissingRequiredField("contentIdentifierValue")
        if not isinstance(self.contentIdentifierValue, URI):
            self.contentIdentifierValue = URI(self.contentIdentifierValue)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Sbom(Bom):
    """
    A collection of SPDX Elements describing a single package.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SOFTWARE["Sbom"]
    class_class_curie: ClassVar[str] = "spdx_software:Sbom"
    class_name: ClassVar[str] = "Sbom"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Sbom

    spdxId: Union[str, SbomSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    sbomType: Optional[Union[Union[str, "SbomType"], list[Union[str, "SbomType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, SbomSpdxId):
            self.spdxId = SbomSpdxId(self.spdxId)

        if not isinstance(self.sbomType, list):
            self.sbomType = [self.sbomType] if self.sbomType is not None else []
        self.sbomType = [v if isinstance(v, SbomType) else SbomType(v) for v in self.sbomType]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SoftwareArtifact(Artifact):
    """
    A distinct article or unit related to Software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SOFTWARE["SoftwareArtifact"]
    class_class_curie: ClassVar[str] = "spdx_software:SoftwareArtifact"
    class_name: ClassVar[str] = "SoftwareArtifact"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.SoftwareArtifact

    spdxId: Union[str, SoftwareArtifactSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    additionalPurpose: Optional[Union[Union[str, "SoftwarePurpose"], list[Union[str, "SoftwarePurpose"]]]] = empty_list()
    attributionText: Optional[Union[str, list[str]]] = empty_list()
    contentIdentifier: Optional[Union[Union[dict, ContentIdentifier], list[Union[dict, ContentIdentifier]]]] = empty_list()
    copyrightText: Optional[str] = None
    primaryPurpose: Optional[Union[str, "SoftwarePurpose"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.additionalPurpose, list):
            self.additionalPurpose = [self.additionalPurpose] if self.additionalPurpose is not None else []
        self.additionalPurpose = [v if isinstance(v, SoftwarePurpose) else SoftwarePurpose(v) for v in self.additionalPurpose]

        if not isinstance(self.attributionText, list):
            self.attributionText = [self.attributionText] if self.attributionText is not None else []
        self.attributionText = [v if isinstance(v, str) else str(v) for v in self.attributionText]

        self._normalize_inlined_as_list(slot_name="contentIdentifier", slot_type=ContentIdentifier, key_name="contentIdentifierType", keyed=False)

        if self.copyrightText is not None and not isinstance(self.copyrightText, str):
            self.copyrightText = str(self.copyrightText)

        if self.primaryPurpose is not None and not isinstance(self.primaryPurpose, SoftwarePurpose):
            self.primaryPurpose = SoftwarePurpose(self.primaryPurpose)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class File(SoftwareArtifact):
    """
    Refers to any object that stores content on a computer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SOFTWARE["File"]
    class_class_curie: ClassVar[str] = "spdx_software:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.File

    spdxId: Union[str, FileSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    contentType: Optional[Union[str, MediaType]] = None
    fileKind: Optional[Union[str, "FileKindType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, FileSpdxId):
            self.spdxId = FileSpdxId(self.spdxId)

        if self.contentType is not None and not isinstance(self.contentType, MediaType):
            self.contentType = MediaType(self.contentType)

        if self.fileKind is not None and not isinstance(self.fileKind, FileKindType):
            self.fileKind = FileKindType(self.fileKind)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Package(SoftwareArtifact):
    """
    Refers to any unit of content that can be associated with a distribution of software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SOFTWARE["Package"]
    class_class_curie: ClassVar[str] = "spdx_software:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Package

    spdxId: Union[str, PackageSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    downloadLocation: Optional[Union[str, URI]] = None
    homePage: Optional[Union[str, URI]] = None
    packageUrl: Optional[Union[str, URI]] = None
    packageVersion: Optional[str] = None
    sourceInfo: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, PackageSpdxId):
            self.spdxId = PackageSpdxId(self.spdxId)

        if self.downloadLocation is not None and not isinstance(self.downloadLocation, URI):
            self.downloadLocation = URI(self.downloadLocation)

        if self.homePage is not None and not isinstance(self.homePage, URI):
            self.homePage = URI(self.homePage)

        if self.packageUrl is not None and not isinstance(self.packageUrl, URI):
            self.packageUrl = URI(self.packageUrl)

        if self.packageVersion is not None and not isinstance(self.packageVersion, str):
            self.packageVersion = str(self.packageVersion)

        if self.sourceInfo is not None and not isinstance(self.sourceInfo, str):
            self.sourceInfo = str(self.sourceInfo)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Snippet(SoftwareArtifact):
    """
    Describes a certain part of a file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SOFTWARE["Snippet"]
    class_class_curie: ClassVar[str] = "spdx_software:Snippet"
    class_name: ClassVar[str] = "Snippet"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Snippet

    spdxId: Union[str, SnippetSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    snippetFromFile: Union[str, FileSpdxId] = None
    byteRange: Optional[Union[dict, PositiveIntegerRange]] = None
    lineRange: Optional[Union[dict, PositiveIntegerRange]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, SnippetSpdxId):
            self.spdxId = SnippetSpdxId(self.spdxId)

        if self._is_empty(self.snippetFromFile):
            self.MissingRequiredField("snippetFromFile")
        if not isinstance(self.snippetFromFile, FileSpdxId):
            self.snippetFromFile = FileSpdxId(self.snippetFromFile)

        if self.byteRange is not None and not isinstance(self.byteRange, PositiveIntegerRange):
            self.byteRange = PositiveIntegerRange(**as_dict(self.byteRange))

        if self.lineRange is not None and not isinstance(self.lineRange, PositiveIntegerRange):
            self.lineRange = PositiveIntegerRange(**as_dict(self.lineRange))

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AIPackage(Package):
    """
    Specifies an AI package and its associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_AI["AIPackage"]
    class_class_curie: ClassVar[str] = "spdx_ai:AIPackage"
    class_name: ClassVar[str] = "AIPackage"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.AIPackage

    spdxId: Union[str, AIPackageSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    autonomyType: Optional[Union[str, "PresenceType"]] = None
    domain: Optional[Union[str, list[str]]] = empty_list()
    energyConsumption: Optional[Union[dict, "EnergyConsumption"]] = None
    hyperparameter: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    informationAboutApplication: Optional[str] = None
    informationAboutTraining: Optional[str] = None
    limitation: Optional[str] = None
    metric: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    metricDecisionThreshold: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    modelDataPreprocessing: Optional[Union[str, list[str]]] = empty_list()
    modelExplainability: Optional[Union[str, list[str]]] = empty_list()
    safetyRiskAssessment: Optional[Union[str, "SafetyRiskAssessmentType"]] = None
    standardCompliance: Optional[Union[str, list[str]]] = empty_list()
    typeOfModel: Optional[Union[str, list[str]]] = empty_list()
    useSensitivePersonalInformation: Optional[Union[str, "PresenceType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, AIPackageSpdxId):
            self.spdxId = AIPackageSpdxId(self.spdxId)

        if self.autonomyType is not None and not isinstance(self.autonomyType, PresenceType):
            self.autonomyType = PresenceType(self.autonomyType)

        if not isinstance(self.domain, list):
            self.domain = [self.domain] if self.domain is not None else []
        self.domain = [v if isinstance(v, str) else str(v) for v in self.domain]

        if self.energyConsumption is not None and not isinstance(self.energyConsumption, EnergyConsumption):
            self.energyConsumption = EnergyConsumption(**as_dict(self.energyConsumption))

        self._normalize_inlined_as_list(slot_name="hyperparameter", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if self.informationAboutApplication is not None and not isinstance(self.informationAboutApplication, str):
            self.informationAboutApplication = str(self.informationAboutApplication)

        if self.informationAboutTraining is not None and not isinstance(self.informationAboutTraining, str):
            self.informationAboutTraining = str(self.informationAboutTraining)

        if self.limitation is not None and not isinstance(self.limitation, str):
            self.limitation = str(self.limitation)

        self._normalize_inlined_as_list(slot_name="metric", slot_type=DictionaryEntry, key_name="key", keyed=False)

        self._normalize_inlined_as_list(slot_name="metricDecisionThreshold", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if not isinstance(self.modelDataPreprocessing, list):
            self.modelDataPreprocessing = [self.modelDataPreprocessing] if self.modelDataPreprocessing is not None else []
        self.modelDataPreprocessing = [v if isinstance(v, str) else str(v) for v in self.modelDataPreprocessing]

        if not isinstance(self.modelExplainability, list):
            self.modelExplainability = [self.modelExplainability] if self.modelExplainability is not None else []
        self.modelExplainability = [v if isinstance(v, str) else str(v) for v in self.modelExplainability]

        if self.safetyRiskAssessment is not None and not isinstance(self.safetyRiskAssessment, SafetyRiskAssessmentType):
            self.safetyRiskAssessment = SafetyRiskAssessmentType(self.safetyRiskAssessment)

        if not isinstance(self.standardCompliance, list):
            self.standardCompliance = [self.standardCompliance] if self.standardCompliance is not None else []
        self.standardCompliance = [v if isinstance(v, str) else str(v) for v in self.standardCompliance]

        if not isinstance(self.typeOfModel, list):
            self.typeOfModel = [self.typeOfModel] if self.typeOfModel is not None else []
        self.typeOfModel = [v if isinstance(v, str) else str(v) for v in self.typeOfModel]

        if self.useSensitivePersonalInformation is not None and not isinstance(self.useSensitivePersonalInformation, PresenceType):
            self.useSensitivePersonalInformation = PresenceType(self.useSensitivePersonalInformation)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EnergyConsumption(YAMLRoot):
    """
    A class for describing the energy consumption incurred by an AI model in different stages of its lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_AI["EnergyConsumption"]
    class_class_curie: ClassVar[str] = "spdx_ai:EnergyConsumption"
    class_name: ClassVar[str] = "EnergyConsumption"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.EnergyConsumption

    type: Optional[Union[str, URIorCURIE]] = None
    finetuningEnergyConsumption: Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]] = empty_list()
    inferenceEnergyConsumption: Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]] = empty_list()
    trainingEnergyConsumption: Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        self._normalize_inlined_as_list(slot_name="finetuningEnergyConsumption", slot_type=EnergyConsumptionDescription, key_name="energyQuantity", keyed=False)

        self._normalize_inlined_as_list(slot_name="inferenceEnergyConsumption", slot_type=EnergyConsumptionDescription, key_name="energyQuantity", keyed=False)

        self._normalize_inlined_as_list(slot_name="trainingEnergyConsumption", slot_type=EnergyConsumptionDescription, key_name="energyQuantity", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnergyConsumptionDescription(YAMLRoot):
    """
    The class that helps note down the quantity of energy consumption and the unit used for measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_AI["EnergyConsumptionDescription"]
    class_class_curie: ClassVar[str] = "spdx_ai:EnergyConsumptionDescription"
    class_name: ClassVar[str] = "EnergyConsumptionDescription"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.EnergyConsumptionDescription

    energyQuantity: Decimal = None
    energyUnit: Union[str, "EnergyUnitType"] = None
    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.energyQuantity):
            self.MissingRequiredField("energyQuantity")
        if not isinstance(self.energyQuantity, Decimal):
            self.energyQuantity = Decimal(self.energyQuantity)

        if self._is_empty(self.energyUnit):
            self.MissingRequiredField("energyUnit")
        if not isinstance(self.energyUnit, EnergyUnitType):
            self.energyUnit = EnergyUnitType(self.energyUnit)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetPackage(Package):
    """
    Specifies a data package and its associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_DATASET["DatasetPackage"]
    class_class_curie: ClassVar[str] = "spdx_dataset:DatasetPackage"
    class_name: ClassVar[str] = "DatasetPackage"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.DatasetPackage

    spdxId: Union[str, DatasetPackageSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    datasetType: Union[Union[str, "DatasetType"], list[Union[str, "DatasetType"]]] = None
    anonymizationMethodUsed: Optional[Union[str, list[str]]] = empty_list()
    confidentialityLevel: Optional[Union[str, "ConfidentialityLevelType"]] = None
    dataCollectionProcess: Optional[str] = None
    dataPreprocessing: Optional[Union[str, list[str]]] = empty_list()
    datasetAvailability: Optional[Union[str, "DatasetAvailabilityType"]] = None
    datasetNoise: Optional[str] = None
    datasetSize: Optional[Union[int, NonNegativeInteger]] = None
    datasetUpdateMechanism: Optional[str] = None
    hasSensitivePersonalInformation: Optional[Union[str, "PresenceType"]] = None
    intendedUse: Optional[str] = None
    knownBias: Optional[Union[str, list[str]]] = empty_list()
    sensor: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, DatasetPackageSpdxId):
            self.spdxId = DatasetPackageSpdxId(self.spdxId)

        if self._is_empty(self.datasetType):
            self.MissingRequiredField("datasetType")
        if not isinstance(self.datasetType, list):
            self.datasetType = [self.datasetType] if self.datasetType is not None else []
        self.datasetType = [v if isinstance(v, DatasetType) else DatasetType(v) for v in self.datasetType]

        if not isinstance(self.anonymizationMethodUsed, list):
            self.anonymizationMethodUsed = [self.anonymizationMethodUsed] if self.anonymizationMethodUsed is not None else []
        self.anonymizationMethodUsed = [v if isinstance(v, str) else str(v) for v in self.anonymizationMethodUsed]

        if self.confidentialityLevel is not None and not isinstance(self.confidentialityLevel, ConfidentialityLevelType):
            self.confidentialityLevel = ConfidentialityLevelType(self.confidentialityLevel)

        if self.dataCollectionProcess is not None and not isinstance(self.dataCollectionProcess, str):
            self.dataCollectionProcess = str(self.dataCollectionProcess)

        if not isinstance(self.dataPreprocessing, list):
            self.dataPreprocessing = [self.dataPreprocessing] if self.dataPreprocessing is not None else []
        self.dataPreprocessing = [v if isinstance(v, str) else str(v) for v in self.dataPreprocessing]

        if self.datasetAvailability is not None and not isinstance(self.datasetAvailability, DatasetAvailabilityType):
            self.datasetAvailability = DatasetAvailabilityType(self.datasetAvailability)

        if self.datasetNoise is not None and not isinstance(self.datasetNoise, str):
            self.datasetNoise = str(self.datasetNoise)

        if self.datasetSize is not None and not isinstance(self.datasetSize, NonNegativeInteger):
            self.datasetSize = NonNegativeInteger(self.datasetSize)

        if self.datasetUpdateMechanism is not None and not isinstance(self.datasetUpdateMechanism, str):
            self.datasetUpdateMechanism = str(self.datasetUpdateMechanism)

        if self.hasSensitivePersonalInformation is not None and not isinstance(self.hasSensitivePersonalInformation, PresenceType):
            self.hasSensitivePersonalInformation = PresenceType(self.hasSensitivePersonalInformation)

        if self.intendedUse is not None and not isinstance(self.intendedUse, str):
            self.intendedUse = str(self.intendedUse)

        if not isinstance(self.knownBias, list):
            self.knownBias = [self.knownBias] if self.knownBias is not None else []
        self.knownBias = [v if isinstance(v, str) else str(v) for v in self.knownBias]

        self._normalize_inlined_as_list(slot_name="sensor", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ConjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information where all elements apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["ConjunctiveLicenseSet"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:ConjunctiveLicenseSet"
    class_name: ClassVar[str] = "ConjunctiveLicenseSet"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ConjunctiveLicenseSet

    spdxId: Union[str, ConjunctiveLicenseSetSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    member: Union[Union[str, AnyLicenseInfoSpdxId], list[Union[str, AnyLicenseInfoSpdxId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, ConjunctiveLicenseSetSpdxId):
            self.spdxId = ConjunctiveLicenseSetSpdxId(self.spdxId)

        if self._is_empty(self.member):
            self.MissingRequiredField("member")
        if not isinstance(self.member, list):
            self.member = [self.member] if self.member is not None else []
        self.member = [v if isinstance(v, AnyLicenseInfoSpdxId) else AnyLicenseInfoSpdxId(v) for v in self.member]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DisjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information where only one of the elements applies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["DisjunctiveLicenseSet"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:DisjunctiveLicenseSet"
    class_name: ClassVar[str] = "DisjunctiveLicenseSet"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.DisjunctiveLicenseSet

    spdxId: Union[str, DisjunctiveLicenseSetSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    member: Union[Union[str, AnyLicenseInfoSpdxId], list[Union[str, AnyLicenseInfoSpdxId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, DisjunctiveLicenseSetSpdxId):
            self.spdxId = DisjunctiveLicenseSetSpdxId(self.spdxId)

        if self._is_empty(self.member):
            self.MissingRequiredField("member")
        if not isinstance(self.member, list):
            self.member = [self.member] if self.member is not None else []
        self.member = [v if isinstance(v, AnyLicenseInfoSpdxId) else AnyLicenseInfoSpdxId(v) for v in self.member]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ExtendableLicense(AnyLicenseInfo):
    """
    Abstract class representing a License or an OrLaterOperator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["ExtendableLicense"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:ExtendableLicense"
    class_name: ClassVar[str] = "ExtendableLicense"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ExtendableLicense

    spdxId: Union[str, ExtendableLicenseSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IndividualLicensingInfo(AnyLicenseInfo):
    """
    A concrete subclass of AnyLicenseInfo used by Individuals in the ExpandedLicensing profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["IndividualLicensingInfo"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:IndividualLicensingInfo"
    class_name: ClassVar[str] = "IndividualLicensingInfo"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.IndividualLicensingInfo

    spdxId: Union[str, IndividualLicensingInfoSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, IndividualLicensingInfoSpdxId):
            self.spdxId = IndividualLicensingInfoSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class License(ExtendableLicense):
    """
    Abstract class for the portion of an AnyLicenseInfo representing a license.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["License"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.License

    spdxId: Union[str, LicenseSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None
    isDeprecatedLicenseId: Optional[Union[bool, Bool]] = None
    isFsfLibre: Optional[Union[bool, Bool]] = None
    isOsiApproved: Optional[Union[bool, Bool]] = None
    licenseXml: Optional[str] = None
    obsoletedBy: Optional[str] = None
    seeAlso: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    standardLicenseHeader: Optional[str] = None
    standardLicenseTemplate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.licenseText):
            self.MissingRequiredField("licenseText")
        if not isinstance(self.licenseText, str):
            self.licenseText = str(self.licenseText)

        if self.isDeprecatedLicenseId is not None and not isinstance(self.isDeprecatedLicenseId, Bool):
            self.isDeprecatedLicenseId = Bool(self.isDeprecatedLicenseId)

        if self.isFsfLibre is not None and not isinstance(self.isFsfLibre, Bool):
            self.isFsfLibre = Bool(self.isFsfLibre)

        if self.isOsiApproved is not None and not isinstance(self.isOsiApproved, Bool):
            self.isOsiApproved = Bool(self.isOsiApproved)

        if self.licenseXml is not None and not isinstance(self.licenseXml, str):
            self.licenseXml = str(self.licenseXml)

        if self.obsoletedBy is not None and not isinstance(self.obsoletedBy, str):
            self.obsoletedBy = str(self.obsoletedBy)

        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso] if self.seeAlso is not None else []
        self.seeAlso = [v if isinstance(v, URI) else URI(v) for v in self.seeAlso]

        if self.standardLicenseHeader is not None and not isinstance(self.standardLicenseHeader, str):
            self.standardLicenseHeader = str(self.standardLicenseHeader)

        if self.standardLicenseTemplate is not None and not isinstance(self.standardLicenseTemplate, str):
            self.standardLicenseTemplate = str(self.standardLicenseTemplate)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CustomLicense(License):
    """
    A license that is not listed on the SPDX License List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["CustomLicense"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:CustomLicense"
    class_name: ClassVar[str] = "CustomLicense"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CustomLicense

    spdxId: Union[str, CustomLicenseSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, CustomLicenseSpdxId):
            self.spdxId = CustomLicenseSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LicenseAddition(Element):
    """
    Abstract class for additional text intended to be added to a License, but which is not itself a standalone License.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["LicenseAddition"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:LicenseAddition"
    class_name: ClassVar[str] = "LicenseAddition"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.LicenseAddition

    spdxId: Union[str, LicenseAdditionSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    additionText: str = None
    isDeprecatedAdditionId: Optional[Union[bool, Bool]] = None
    licenseXml: Optional[str] = None
    obsoletedBy: Optional[str] = None
    seeAlso: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    standardAdditionTemplate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.additionText):
            self.MissingRequiredField("additionText")
        if not isinstance(self.additionText, str):
            self.additionText = str(self.additionText)

        if self.isDeprecatedAdditionId is not None and not isinstance(self.isDeprecatedAdditionId, Bool):
            self.isDeprecatedAdditionId = Bool(self.isDeprecatedAdditionId)

        if self.licenseXml is not None and not isinstance(self.licenseXml, str):
            self.licenseXml = str(self.licenseXml)

        if self.obsoletedBy is not None and not isinstance(self.obsoletedBy, str):
            self.obsoletedBy = str(self.obsoletedBy)

        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso] if self.seeAlso is not None else []
        self.seeAlso = [v if isinstance(v, URI) else URI(v) for v in self.seeAlso]

        if self.standardAdditionTemplate is not None and not isinstance(self.standardAdditionTemplate, str):
            self.standardAdditionTemplate = str(self.standardAdditionTemplate)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CustomLicenseAddition(LicenseAddition):
    """
    A license addition that is not listed on the SPDX Exceptions List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["CustomLicenseAddition"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:CustomLicenseAddition"
    class_name: ClassVar[str] = "CustomLicenseAddition"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CustomLicenseAddition

    spdxId: Union[str, CustomLicenseAdditionSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    additionText: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, CustomLicenseAdditionSpdxId):
            self.spdxId = CustomLicenseAdditionSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ListedLicense(License):
    """
    A license that is listed on the SPDX License List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["ListedLicense"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:ListedLicense"
    class_name: ClassVar[str] = "ListedLicense"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ListedLicense

    spdxId: Union[str, ListedLicenseSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None
    deprecatedVersion: Optional[str] = None
    listVersionAdded: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, ListedLicenseSpdxId):
            self.spdxId = ListedLicenseSpdxId(self.spdxId)

        if self.deprecatedVersion is not None and not isinstance(self.deprecatedVersion, str):
            self.deprecatedVersion = str(self.deprecatedVersion)

        if self.listVersionAdded is not None and not isinstance(self.listVersionAdded, str):
            self.listVersionAdded = str(self.listVersionAdded)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ListedLicenseException(LicenseAddition):
    """
    A license exception that is listed on the SPDX Exceptions list.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["ListedLicenseException"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:ListedLicenseException"
    class_name: ClassVar[str] = "ListedLicenseException"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ListedLicenseException

    spdxId: Union[str, ListedLicenseExceptionSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    additionText: str = None
    deprecatedVersion: Optional[str] = None
    listVersionAdded: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, ListedLicenseExceptionSpdxId):
            self.spdxId = ListedLicenseExceptionSpdxId(self.spdxId)

        if self.deprecatedVersion is not None and not isinstance(self.deprecatedVersion, str):
            self.deprecatedVersion = str(self.deprecatedVersion)

        if self.listVersionAdded is not None and not isinstance(self.listVersionAdded, str):
            self.listVersionAdded = str(self.listVersionAdded)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class OrLaterOperator(ExtendableLicense):
    """
    Portion of an AnyLicenseInfo representing this version, or any later version, of the indicated License.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["OrLaterOperator"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:OrLaterOperator"
    class_name: ClassVar[str] = "OrLaterOperator"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.OrLaterOperator

    spdxId: Union[str, OrLaterOperatorSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    subjectLicense: Union[str, LicenseSpdxId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, OrLaterOperatorSpdxId):
            self.spdxId = OrLaterOperatorSpdxId(self.spdxId)

        if self._is_empty(self.subjectLicense):
            self.MissingRequiredField("subjectLicense")
        if not isinstance(self.subjectLicense, LicenseSpdxId):
            self.subjectLicense = LicenseSpdxId(self.subjectLicense)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WithAdditionOperator(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a License which has additional text applied to it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_EXPANDED_LICENSING["WithAdditionOperator"]
    class_class_curie: ClassVar[str] = "spdx_expanded_licensing:WithAdditionOperator"
    class_name: ClassVar[str] = "WithAdditionOperator"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.WithAdditionOperator

    spdxId: Union[str, WithAdditionOperatorSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    subjectAddition: Union[str, LicenseAdditionSpdxId] = None
    subjectExtendableLicense: Union[str, ExtendableLicenseSpdxId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, WithAdditionOperatorSpdxId):
            self.spdxId = WithAdditionOperatorSpdxId(self.spdxId)

        if self._is_empty(self.subjectAddition):
            self.MissingRequiredField("subjectAddition")
        if not isinstance(self.subjectAddition, LicenseAdditionSpdxId):
            self.subjectAddition = LicenseAdditionSpdxId(self.subjectAddition)

        if self._is_empty(self.subjectExtendableLicense):
            self.MissingRequiredField("subjectExtendableLicense")
        if not isinstance(self.subjectExtendableLicense, ExtendableLicenseSpdxId):
            self.subjectExtendableLicense = ExtendableLicenseSpdxId(self.subjectExtendableLicense)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VulnAssessmentRelationship(Relationship):
    """
    Abstract ancestor class for all vulnerability assessments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:VulnAssessmentRelationship"
    class_name: ClassVar[str] = "VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.VulnAssessmentRelationship

    spdxId: Union[str, VulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    assessedElement: Optional[Union[str, SoftwareArtifactSpdxId]] = None
    modifiedTime: Optional[Union[str, DateTimeStamp]] = None
    publishedTime: Optional[Union[str, DateTimeStamp]] = None
    suppliedBy: Optional[Union[str, AgentSpdxId]] = None
    withdrawnTime: Optional[Union[str, DateTimeStamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.assessedElement is not None and not isinstance(self.assessedElement, SoftwareArtifactSpdxId):
            self.assessedElement = SoftwareArtifactSpdxId(self.assessedElement)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, DateTimeStamp):
            self.modifiedTime = DateTimeStamp(self.modifiedTime)

        if self.publishedTime is not None and not isinstance(self.publishedTime, DateTimeStamp):
            self.publishedTime = DateTimeStamp(self.publishedTime)

        if self.suppliedBy is not None and not isinstance(self.suppliedBy, AgentSpdxId):
            self.suppliedBy = AgentSpdxId(self.suppliedBy)

        if self.withdrawnTime is not None and not isinstance(self.withdrawnTime, DateTimeStamp):
            self.withdrawnTime = DateTimeStamp(self.withdrawnTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CvssV2VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 2.0 assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["CvssV2VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:CvssV2VulnAssessmentRelationship"
    class_name: ClassVar[str] = "CvssV2VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CvssV2VulnAssessmentRelationship

    spdxId: Union[str, CvssV2VulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    score: Decimal = None
    vectorString: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, CvssV2VulnAssessmentRelationshipSpdxId):
            self.spdxId = CvssV2VulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, Decimal):
            self.score = Decimal(self.score)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CvssV3VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 3 assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["CvssV3VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:CvssV3VulnAssessmentRelationship"
    class_name: ClassVar[str] = "CvssV3VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CvssV3VulnAssessmentRelationship

    spdxId: Union[str, CvssV3VulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    score: Decimal = None
    severity: Union[str, "CvssSeverityType"] = None
    vectorString: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, CvssV3VulnAssessmentRelationshipSpdxId):
            self.spdxId = CvssV3VulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, Decimal):
            self.score = Decimal(self.score)

        if self._is_empty(self.severity):
            self.MissingRequiredField("severity")
        if not isinstance(self.severity, CvssSeverityType):
            self.severity = CvssSeverityType(self.severity)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CvssV4VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 4 assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["CvssV4VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:CvssV4VulnAssessmentRelationship"
    class_name: ClassVar[str] = "CvssV4VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.CvssV4VulnAssessmentRelationship

    spdxId: Union[str, CvssV4VulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    score: Decimal = None
    severity: Union[str, "CvssSeverityType"] = None
    vectorString: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, CvssV4VulnAssessmentRelationshipSpdxId):
            self.spdxId = CvssV4VulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, Decimal):
            self.score = Decimal(self.score)

        if self._is_empty(self.severity):
            self.MissingRequiredField("severity")
        if not isinstance(self.severity, CvssSeverityType):
            self.severity = CvssSeverityType(self.severity)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EpssVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an EPSS assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["EpssVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:EpssVulnAssessmentRelationship"
    class_name: ClassVar[str] = "EpssVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.EpssVulnAssessmentRelationship

    spdxId: Union[str, EpssVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    percentile: Decimal = None
    probability: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, EpssVulnAssessmentRelationshipSpdxId):
            self.spdxId = EpssVulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.percentile):
            self.MissingRequiredField("percentile")
        if not isinstance(self.percentile, Decimal):
            self.percentile = Decimal(self.percentile)

        if self._is_empty(self.probability):
            self.MissingRequiredField("probability")
        if not isinstance(self.probability, Decimal):
            self.probability = Decimal(self.probability)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ExploitCatalogVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an exploit assessment of a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["ExploitCatalogVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:ExploitCatalogVulnAssessmentRelationship"
    class_name: ClassVar[str] = "ExploitCatalogVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.ExploitCatalogVulnAssessmentRelationship

    spdxId: Union[str, ExploitCatalogVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    catalogType: Union[str, "ExploitCatalogType"] = None
    exploited: Union[bool, Bool] = None
    security_locator: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, ExploitCatalogVulnAssessmentRelationshipSpdxId):
            self.spdxId = ExploitCatalogVulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.catalogType):
            self.MissingRequiredField("catalogType")
        if not isinstance(self.catalogType, ExploitCatalogType):
            self.catalogType = ExploitCatalogType(self.catalogType)

        if self._is_empty(self.exploited):
            self.MissingRequiredField("exploited")
        if not isinstance(self.exploited, Bool):
            self.exploited = Bool(self.exploited)

        if self._is_empty(self.security_locator):
            self.MissingRequiredField("security_locator")
        if not isinstance(self.security_locator, URI):
            self.security_locator = URI(self.security_locator)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SsvcVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an SSVC assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["SsvcVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:SsvcVulnAssessmentRelationship"
    class_name: ClassVar[str] = "SsvcVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.SsvcVulnAssessmentRelationship

    spdxId: Union[str, SsvcVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    decisionType: Union[str, "SsvcDecisionType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, SsvcVulnAssessmentRelationshipSpdxId):
            self.spdxId = SsvcVulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.decisionType):
            self.MissingRequiredField("decisionType")
        if not isinstance(self.decisionType, SsvcDecisionType):
            self.decisionType = SsvcDecisionType(self.decisionType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VexVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Abstract ancestor class for all VEX relationships
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["VexVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:VexVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.VexVulnAssessmentRelationship

    spdxId: Union[str, VexVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    statusNotes: Optional[str] = None
    vexVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.statusNotes is not None and not isinstance(self.statusNotes, str):
            self.statusNotes = str(self.statusNotes)

        if self.vexVersion is not None and not isinstance(self.vexVersion, str):
            self.vexVersion = str(self.vexVersion)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VexAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Connects a vulnerability and an element designating the element as a product affected by the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["VexAffectedVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:VexAffectedVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexAffectedVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.VexAffectedVulnAssessmentRelationship

    spdxId: Union[str, VexAffectedVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    actionStatement: str = None
    actionStatementTime: Optional[Union[str, DateTimeStamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, VexAffectedVulnAssessmentRelationshipSpdxId):
            self.spdxId = VexAffectedVulnAssessmentRelationshipSpdxId(self.spdxId)

        if self._is_empty(self.actionStatement):
            self.MissingRequiredField("actionStatement")
        if not isinstance(self.actionStatement, str):
            self.actionStatement = str(self.actionStatement)

        if self.actionStatementTime is not None and not isinstance(self.actionStatementTime, DateTimeStamp):
            self.actionStatementTime = DateTimeStamp(self.actionStatementTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VexFixedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and elements representing products (in the VEX sense) where a fix has been applied and are
    no longer affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["VexFixedVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:VexFixedVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexFixedVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.VexFixedVulnAssessmentRelationship

    spdxId: Union[str, VexFixedVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, VexFixedVulnAssessmentRelationshipSpdxId):
            self.spdxId = VexFixedVulnAssessmentRelationshipSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VexNotAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and one or more elements designating the latter as products not affected by the
    vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["VexNotAffectedVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:VexNotAffectedVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexNotAffectedVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.VexNotAffectedVulnAssessmentRelationship

    spdxId: Union[str, VexNotAffectedVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None
    impactStatement: Optional[str] = None
    impactStatementTime: Optional[Union[str, DateTimeStamp]] = None
    justificationType: Optional[Union[str, "VexJustificationType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, VexNotAffectedVulnAssessmentRelationshipSpdxId):
            self.spdxId = VexNotAffectedVulnAssessmentRelationshipSpdxId(self.spdxId)

        if self.impactStatement is not None and not isinstance(self.impactStatement, str):
            self.impactStatement = str(self.impactStatement)

        if self.impactStatementTime is not None and not isinstance(self.impactStatementTime, DateTimeStamp):
            self.impactStatementTime = DateTimeStamp(self.impactStatementTime)

        if self.justificationType is not None and not isinstance(self.justificationType, VexJustificationType):
            self.justificationType = VexJustificationType(self.justificationType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VexUnderInvestigationVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Designates elements as products where the impact of a vulnerability is being investigated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["VexUnderInvestigationVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "spdx_security:VexUnderInvestigationVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexUnderInvestigationVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.VexUnderInvestigationVulnAssessmentRelationship

    spdxId: Union[str, VexUnderInvestigationVulnAssessmentRelationshipSpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    from_: Union[str, ElementSpdxId] = None
    relationshipType: Union[str, "RelationshipType"] = None
    to: Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, VexUnderInvestigationVulnAssessmentRelationshipSpdxId):
            self.spdxId = VexUnderInvestigationVulnAssessmentRelationshipSpdxId(self.spdxId)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Vulnerability(Artifact):
    """
    Specifies a vulnerability and its associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX_SECURITY["Vulnerability"]
    class_class_curie: ClassVar[str] = "spdx_security:Vulnerability"
    class_name: ClassVar[str] = "Vulnerability"
    class_model_uri: ClassVar[URIRef] = SPDX_LINKML.Vulnerability

    spdxId: Union[str, VulnerabilitySpdxId] = None
    creationInfo: Union[dict, CreationInfo] = None
    modifiedTime: Optional[Union[str, DateTimeStamp]] = None
    publishedTime: Optional[Union[str, DateTimeStamp]] = None
    withdrawnTime: Optional[Union[str, DateTimeStamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spdxId):
            self.MissingRequiredField("spdxId")
        if not isinstance(self.spdxId, VulnerabilitySpdxId):
            self.spdxId = VulnerabilitySpdxId(self.spdxId)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, DateTimeStamp):
            self.modifiedTime = DateTimeStamp(self.modifiedTime)

        if self.publishedTime is not None and not isinstance(self.publishedTime, DateTimeStamp):
            self.publishedTime = DateTimeStamp(self.publishedTime)

        if self.withdrawnTime is not None and not isinstance(self.withdrawnTime, DateTimeStamp):
            self.withdrawnTime = DateTimeStamp(self.withdrawnTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


# Enumerations
class AnnotationType(EnumDefinitionImpl):
    """
    Specifies the type of an annotation.
    """
    other = PermissibleValue(
        text="other",
        description="""Used to store extra information about an Element which is not part of a review (e.g. extra information provided during the creation of the Element).""",
        meaning=SPDX_CORE["AnnotationType/other"])
    review = PermissibleValue(
        text="review",
        description="Used when someone reviews the Element.",
        meaning=SPDX_CORE["AnnotationType/review"])

    _defn = EnumDefinition(
        name="AnnotationType",
        description="Specifies the type of an annotation.",
    )

class ExternalIdentifierType(EnumDefinitionImpl):
    """
    Specifies the type of an external identifier.
    """
    cpe22 = PermissibleValue(
        text="cpe22",
        description="""[Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)""",
        meaning=SPDX_CORE["ExternalIdentifierType/cpe22"])
    cpe23 = PermissibleValue(
        text="cpe23",
        description="""[Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)""",
        meaning=SPDX_CORE["ExternalIdentifierType/cpe23"])
    cve = PermissibleValue(
        text="cve",
        description="""Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).""",
        meaning=SPDX_CORE["ExternalIdentifierType/cve"])
    email = PermissibleValue(
        text="email",
        description="Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3986/) Section 3.",
        meaning=SPDX_CORE["ExternalIdentifierType/email"])
    gitoid = PermissibleValue(
        text="gitoid",
        description="""[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).""",
        meaning=SPDX_CORE["ExternalIdentifierType/gitoid"])
    other = PermissibleValue(
        text="other",
        description="Used when the type does not match any of the other options.",
        meaning=SPDX_CORE["ExternalIdentifierType/other"])
    packageUrl = PermissibleValue(
        text="packageUrl",
        description="""Package URL, as defined in the corresponding [Annex](https://spdx.github.io/spdx-spec/v3.0.1/annexes/pkg-url-specification/) of this specification.""",
        meaning=SPDX_CORE["ExternalIdentifierType/packageUrl"])
    securityOther = PermissibleValue(
        text="securityOther",
        description="Used when there is a security related identifier of unspecified type.",
        meaning=SPDX_CORE["ExternalIdentifierType/securityOther"])
    swhid = PermissibleValue(
        text="swhid",
        description="""SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.""",
        meaning=SPDX_CORE["ExternalIdentifierType/swhid"])
    swid = PermissibleValue(
        text="swid",
        description="""Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.""",
        meaning=SPDX_CORE["ExternalIdentifierType/swid"])
    urlScheme = PermissibleValue(
        text="urlScheme",
        description="""[Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.""",
        meaning=SPDX_CORE["ExternalIdentifierType/urlScheme"])

    _defn = EnumDefinition(
        name="ExternalIdentifierType",
        description="Specifies the type of an external identifier.",
    )

class ExternalRefType(EnumDefinitionImpl):
    """
    Specifies the type of an external reference.
    """
    altDownloadLocation = PermissibleValue(
        text="altDownloadLocation",
        description="A reference to an alternative download location.",
        meaning=SPDX_CORE["ExternalRefType/altDownloadLocation"])
    altWebPage = PermissibleValue(
        text="altWebPage",
        description="A reference to an alternative web page.",
        meaning=SPDX_CORE["ExternalRefType/altWebPage"])
    binaryArtifact = PermissibleValue(
        text="binaryArtifact",
        description="A reference to binary artifacts related to a package.",
        meaning=SPDX_CORE["ExternalRefType/binaryArtifact"])
    bower = PermissibleValue(
        text="bower",
        description="""A reference to a Bower package. The package locator format, looks like `package#version`, is defined in the \"install\" section of [Bower API documentation](https://bower.io/docs/api/#install).""",
        meaning=SPDX_CORE["ExternalRefType/bower"])
    buildMeta = PermissibleValue(
        text="buildMeta",
        description="A reference build metadata related to a published package.",
        meaning=SPDX_CORE["ExternalRefType/buildMeta"])
    buildSystem = PermissibleValue(
        text="buildSystem",
        description="A reference build system used to create or publish the package.",
        meaning=SPDX_CORE["ExternalRefType/buildSystem"])
    certificationReport = PermissibleValue(
        text="certificationReport",
        description="A reference to a certification report for a package from an accredited/independent body.",
        meaning=SPDX_CORE["ExternalRefType/certificationReport"])
    chat = PermissibleValue(
        text="chat",
        description="A reference to the instant messaging system used by the maintainer for a package.",
        meaning=SPDX_CORE["ExternalRefType/chat"])
    componentAnalysisReport = PermissibleValue(
        text="componentAnalysisReport",
        description="A reference to a Software Composition Analysis (SCA) report.",
        meaning=SPDX_CORE["ExternalRefType/componentAnalysisReport"])
    cwe = PermissibleValue(
        text="cwe",
        description="""[Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/).""",
        meaning=SPDX_CORE["ExternalRefType/cwe"])
    documentation = PermissibleValue(
        text="documentation",
        description="A reference to the documentation for a package.",
        meaning=SPDX_CORE["ExternalRefType/documentation"])
    dynamicAnalysisReport = PermissibleValue(
        text="dynamicAnalysisReport",
        description="A reference to a dynamic analysis report for a package.",
        meaning=SPDX_CORE["ExternalRefType/dynamicAnalysisReport"])
    eolNotice = PermissibleValue(
        text="eolNotice",
        description="""A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package.""",
        meaning=SPDX_CORE["ExternalRefType/eolNotice"])
    exportControlAssessment = PermissibleValue(
        text="exportControlAssessment",
        description="A reference to a export control assessment for a package.",
        meaning=SPDX_CORE["ExternalRefType/exportControlAssessment"])
    funding = PermissibleValue(
        text="funding",
        description="A reference to funding information related to a package.",
        meaning=SPDX_CORE["ExternalRefType/funding"])
    issueTracker = PermissibleValue(
        text="issueTracker",
        description="A reference to the issue tracker for a package.",
        meaning=SPDX_CORE["ExternalRefType/issueTracker"])
    license = PermissibleValue(
        text="license",
        description="A reference to additional license information related to an artifact.",
        meaning=SPDX_CORE["ExternalRefType/license"])
    mailingList = PermissibleValue(
        text="mailingList",
        description="A reference to the mailing list used by the maintainer for a package.",
        meaning=SPDX_CORE["ExternalRefType/mailingList"])
    mavenCentral = PermissibleValue(
        text="mavenCentral",
        description="""A reference to a Maven repository artifact. The artifact locator format is defined in the [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html) and looks like `groupId:artifactId[:version]`.""",
        meaning=SPDX_CORE["ExternalRefType/mavenCentral"])
    metrics = PermissibleValue(
        text="metrics",
        description="A reference to metrics related to package such as OpenSSF scorecards.",
        meaning=SPDX_CORE["ExternalRefType/metrics"])
    npm = PermissibleValue(
        text="npm",
        description="""A reference to an npm package. The package locator format is defined in the [npm documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and looks like `package@version`.""",
        meaning=SPDX_CORE["ExternalRefType/npm"])
    nuget = PermissibleValue(
        text="nuget",
        description="""A reference to a NuGet package. The package locator format is defined in the [NuGet documentation](https://docs.nuget.org) and looks like `package/version`.""",
        meaning=SPDX_CORE["ExternalRefType/nuget"])
    other = PermissibleValue(
        text="other",
        description="Used when the type does not match any of the other options.",
        meaning=SPDX_CORE["ExternalRefType/other"])
    privacyAssessment = PermissibleValue(
        text="privacyAssessment",
        description="A reference to a privacy assessment for a package.",
        meaning=SPDX_CORE["ExternalRefType/privacyAssessment"])
    productMetadata = PermissibleValue(
        text="productMetadata",
        description="""A reference to additional product metadata such as reference within organization's product catalog.""",
        meaning=SPDX_CORE["ExternalRefType/productMetadata"])
    purchaseOrder = PermissibleValue(
        text="purchaseOrder",
        description="A reference to a purchase order for a package.",
        meaning=SPDX_CORE["ExternalRefType/purchaseOrder"])
    qualityAssessmentReport = PermissibleValue(
        text="qualityAssessmentReport",
        description="A reference to a quality assessment for a package.",
        meaning=SPDX_CORE["ExternalRefType/qualityAssessmentReport"])
    releaseHistory = PermissibleValue(
        text="releaseHistory",
        description="A reference to a published list of releases for a package.",
        meaning=SPDX_CORE["ExternalRefType/releaseHistory"])
    releaseNotes = PermissibleValue(
        text="releaseNotes",
        description="A reference to the release notes for a package.",
        meaning=SPDX_CORE["ExternalRefType/releaseNotes"])
    riskAssessment = PermissibleValue(
        text="riskAssessment",
        description="A reference to a risk assessment for a package.",
        meaning=SPDX_CORE["ExternalRefType/riskAssessment"])
    runtimeAnalysisReport = PermissibleValue(
        text="runtimeAnalysisReport",
        description="A reference to a runtime analysis report for a package.",
        meaning=SPDX_CORE["ExternalRefType/runtimeAnalysisReport"])
    secureSoftwareAttestation = PermissibleValue(
        text="secureSoftwareAttestation",
        description="""A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form).""",
        meaning=SPDX_CORE["ExternalRefType/secureSoftwareAttestation"])
    securityAdversaryModel = PermissibleValue(
        text="securityAdversaryModel",
        description="A reference to the security adversary model for a package.",
        meaning=SPDX_CORE["ExternalRefType/securityAdversaryModel"])
    securityAdvisory = PermissibleValue(
        text="securityAdvisory",
        description="""A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries.""",
        meaning=SPDX_CORE["ExternalRefType/securityAdvisory"])
    securityFix = PermissibleValue(
        text="securityFix",
        description="A reference to the patch or source code that fixes a vulnerability.",
        meaning=SPDX_CORE["ExternalRefType/securityFix"])
    securityOther = PermissibleValue(
        text="securityOther",
        description="A reference to related security information of unspecified type.",
        meaning=SPDX_CORE["ExternalRefType/securityOther"])
    securityPenTestReport = PermissibleValue(
        text="securityPenTestReport",
        description="""A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package.""",
        meaning=SPDX_CORE["ExternalRefType/securityPenTestReport"])
    securityPolicy = PermissibleValue(
        text="securityPolicy",
        description="""A reference to instructions for reporting newly discovered security vulnerabilities for a package.""",
        meaning=SPDX_CORE["ExternalRefType/securityPolicy"])
    securityThreatModel = PermissibleValue(
        text="securityThreatModel",
        description="""A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package.""",
        meaning=SPDX_CORE["ExternalRefType/securityThreatModel"])
    socialMedia = PermissibleValue(
        text="socialMedia",
        description="A reference to a social media channel for a package.",
        meaning=SPDX_CORE["ExternalRefType/socialMedia"])
    sourceArtifact = PermissibleValue(
        text="sourceArtifact",
        description="A reference to an artifact containing the sources for a package.",
        meaning=SPDX_CORE["ExternalRefType/sourceArtifact"])
    staticAnalysisReport = PermissibleValue(
        text="staticAnalysisReport",
        description="A reference to a static analysis report for a package.",
        meaning=SPDX_CORE["ExternalRefType/staticAnalysisReport"])
    support = PermissibleValue(
        text="support",
        description="A reference to the software support channel or other support information for a package.",
        meaning=SPDX_CORE["ExternalRefType/support"])
    vcs = PermissibleValue(
        text="vcs",
        description="A reference to a version control system related to a software artifact.",
        meaning=SPDX_CORE["ExternalRefType/vcs"])
    vulnerabilityDisclosureReport = PermissibleValue(
        text="vulnerabilityDisclosureReport",
        description="""A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/final).""",
        meaning=SPDX_CORE["ExternalRefType/vulnerabilityDisclosureReport"])
    vulnerabilityExploitabilityAssessment = PermissibleValue(
        text="vulnerabilityExploitabilityAssessment",
        description="""A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf).""",
        meaning=SPDX_CORE["ExternalRefType/vulnerabilityExploitabilityAssessment"])

    _defn = EnumDefinition(
        name="ExternalRefType",
        description="Specifies the type of an external reference.",
    )

class HashAlgorithm(EnumDefinitionImpl):
    """
    A mathematical algorithm that maps data of arbitrary size to a bit string.
    """
    adler32 = PermissibleValue(
        text="adler32",
        description="""Adler-32 checksum is part of the widely used zlib compression library as defined in [RFC 1950](https://datatracker.ietf.org/doc/rfc1950/) Section 2.3.""",
        meaning=SPDX_CORE["HashAlgorithm/adler32"])
    blake2b256 = PermissibleValue(
        text="blake2b256",
        description="""BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.""",
        meaning=SPDX_CORE["HashAlgorithm/blake2b256"])
    blake2b384 = PermissibleValue(
        text="blake2b384",
        description="""BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.""",
        meaning=SPDX_CORE["HashAlgorithm/blake2b384"])
    blake2b512 = PermissibleValue(
        text="blake2b512",
        description="""BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.""",
        meaning=SPDX_CORE["HashAlgorithm/blake2b512"])
    blake3 = PermissibleValue(
        text="blake3",
        description="[BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)",
        meaning=SPDX_CORE["HashAlgorithm/blake3"])
    crystalsDilithium = PermissibleValue(
        text="crystalsDilithium",
        description="[Dilithium](https://pq-crystals.org/dilithium/)",
        meaning=SPDX_CORE["HashAlgorithm/crystalsDilithium"])
    crystalsKyber = PermissibleValue(
        text="crystalsKyber",
        description="[Kyber](https://pq-crystals.org/kyber/)",
        meaning=SPDX_CORE["HashAlgorithm/crystalsKyber"])
    falcon = PermissibleValue(
        text="falcon",
        description="[FALCON](https://falcon-sign.info/falcon.pdf)",
        meaning=SPDX_CORE["HashAlgorithm/falcon"])
    md2 = PermissibleValue(
        text="md2",
        description="""MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/).""",
        meaning=SPDX_CORE["HashAlgorithm/md2"])
    md4 = PermissibleValue(
        text="md4",
        description="""MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/).""",
        meaning=SPDX_CORE["HashAlgorithm/md4"])
    md5 = PermissibleValue(
        text="md5",
        description="""MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/).""",
        meaning=SPDX_CORE["HashAlgorithm/md5"])
    md6 = PermissibleValue(
        text="md6",
        description="[MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)",
        meaning=SPDX_CORE["HashAlgorithm/md6"])
    other = PermissibleValue(
        text="other",
        description="any hashing algorithm that does not exist in this list of entries",
        meaning=SPDX_CORE["HashAlgorithm/other"])
    sha1 = PermissibleValue(
        text="sha1",
        description="""SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/).""",
        meaning=SPDX_CORE["HashAlgorithm/sha1"])
    sha224 = PermissibleValue(
        text="sha224",
        description="""SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/).""",
        meaning=SPDX_CORE["HashAlgorithm/sha224"])
    sha256 = PermissibleValue(
        text="sha256",
        description="""SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).""",
        meaning=SPDX_CORE["HashAlgorithm/sha256"])
    sha384 = PermissibleValue(
        text="sha384",
        description="""SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).""",
        meaning=SPDX_CORE["HashAlgorithm/sha384"])
    sha3_224 = PermissibleValue(
        text="sha3_224",
        description="""SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=SPDX_CORE["HashAlgorithm/sha3_224"])
    sha3_256 = PermissibleValue(
        text="sha3_256",
        description="""SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=SPDX_CORE["HashAlgorithm/sha3_256"])
    sha3_384 = PermissibleValue(
        text="sha3_384",
        description="""SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=SPDX_CORE["HashAlgorithm/sha3_384"])
    sha3_512 = PermissibleValue(
        text="sha3_512",
        description="""SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=SPDX_CORE["HashAlgorithm/sha3_512"])
    sha512 = PermissibleValue(
        text="sha512",
        description="""SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).""",
        meaning=SPDX_CORE["HashAlgorithm/sha512"])

    _defn = EnumDefinition(
        name="HashAlgorithm",
        description="A mathematical algorithm that maps data of arbitrary size to a bit string.",
    )

class LifecycleScopeType(EnumDefinitionImpl):
    """
    Provide an enumerated set of lifecycle phases that can provide context to relationships.
    """
    build = PermissibleValue(
        text="build",
        description="""A relationship has specific context implications during an element's build phase, during development.""",
        meaning=SPDX_CORE["LifecycleScopeType/build"])
    design = PermissibleValue(
        text="design",
        description="A relationship has specific context implications during an element's design.",
        meaning=SPDX_CORE["LifecycleScopeType/design"])
    development = PermissibleValue(
        text="development",
        description="A relationship has specific context implications during development phase of an element.",
        meaning=SPDX_CORE["LifecycleScopeType/development"])
    other = PermissibleValue(
        text="other",
        description="""A relationship has other specific context information necessary to capture that the above set of enumerations does not handle.""",
        meaning=SPDX_CORE["LifecycleScopeType/other"])
    runtime = PermissibleValue(
        text="runtime",
        description="A relationship has specific context implications during the execution phase of an element.",
        meaning=SPDX_CORE["LifecycleScopeType/runtime"])
    test = PermissibleValue(
        text="test",
        description="""A relationship has specific context implications during an element's testing phase, during development.""",
        meaning=SPDX_CORE["LifecycleScopeType/test"])

    _defn = EnumDefinition(
        name="LifecycleScopeType",
        description="Provide an enumerated set of lifecycle phases that can provide context to relationships.",
    )

class PresenceType(EnumDefinitionImpl):
    """
    Categories of presence or absence.
    """
    no = PermissibleValue(
        text="no",
        description="Indicates absence of the field.",
        meaning=SPDX_CORE["PresenceType/no"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="Makes no assertion about the field.",
        meaning=SPDX_CORE["PresenceType/noAssertion"])
    yes = PermissibleValue(
        text="yes",
        description="Indicates presence of the field.",
        meaning=SPDX_CORE["PresenceType/yes"])

    _defn = EnumDefinition(
        name="PresenceType",
        description="Categories of presence or absence.",
    )

class ProfileIdentifierType(EnumDefinitionImpl):
    """
    Enumeration of the valid profiles.
    """
    ai = PermissibleValue(
        text="ai",
        description="the element follows the AI profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/ai"])
    build = PermissibleValue(
        text="build",
        description="the element follows the Build profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/build"])
    core = PermissibleValue(
        text="core",
        description="the element follows the Core profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/core"])
    dataset = PermissibleValue(
        text="dataset",
        description="the element follows the Dataset profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/dataset"])
    expandedLicensing = PermissibleValue(
        text="expandedLicensing",
        description="the element follows the ExpandedLicensing profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/expandedLicensing"])
    extension = PermissibleValue(
        text="extension",
        description="the element follows the Extension profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/extension"])
    lite = PermissibleValue(
        text="lite",
        description="the element follows the Lite profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/lite"])
    security = PermissibleValue(
        text="security",
        description="the element follows the Security profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/security"])
    simpleLicensing = PermissibleValue(
        text="simpleLicensing",
        description="the element follows the SimpleLicensing profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/simpleLicensing"])
    software = PermissibleValue(
        text="software",
        description="the element follows the Software profile specification",
        meaning=SPDX_CORE["ProfileIdentifierType/software"])

    _defn = EnumDefinition(
        name="ProfileIdentifierType",
        description="Enumeration of the valid profiles.",
    )

class RelationshipCompleteness(EnumDefinitionImpl):
    """
    Indicates whether a relationship is known to be complete, incomplete, or if no assertion is made with respect to
    relationship completeness.
    """
    complete = PermissibleValue(
        text="complete",
        description="The relationship is known to be exhaustive.",
        meaning=SPDX_CORE["RelationshipCompleteness/complete"])
    incomplete = PermissibleValue(
        text="incomplete",
        description="The relationship is known not to be exhaustive.",
        meaning=SPDX_CORE["RelationshipCompleteness/incomplete"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="No assertion can be made about the completeness of the relationship.",
        meaning=SPDX_CORE["RelationshipCompleteness/noAssertion"])

    _defn = EnumDefinition(
        name="RelationshipCompleteness",
        description="""Indicates whether a relationship is known to be complete, incomplete, or if no assertion is made with respect to relationship completeness.""",
    )

class RelationshipType(EnumDefinitionImpl):
    """
    Information about the relationship between two Elements.
    """
    affects = PermissibleValue(
        text="affects",
        description="""The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships.""",
        meaning=SPDX_CORE["RelationshipType/affects"])
    amendedBy = PermissibleValue(
        text="amendedBy",
        description="The `from` Element is amended by each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/amendedBy"])
    ancestorOf = PermissibleValue(
        text="ancestorOf",
        description="The `from` Element is an ancestor of each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/ancestorOf"])
    availableFrom = PermissibleValue(
        text="availableFrom",
        description="The `from` Element is available from the additional supplier described by each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/availableFrom"])
    configures = PermissibleValue(
        text="configures",
        description="""The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/configures"])
    contains = PermissibleValue(
        text="contains",
        description="The `from` Element contains each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/contains"])
    coordinatedBy = PermissibleValue(
        text="coordinatedBy",
        description="""The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).""",
        meaning=SPDX_CORE["RelationshipType/coordinatedBy"])
    copiedTo = PermissibleValue(
        text="copiedTo",
        description="The `from` Element has been copied to each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/copiedTo"])
    delegatedTo = PermissibleValue(
        text="delegatedTo",
        description="""The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).""",
        meaning=SPDX_CORE["RelationshipType/delegatedTo"])
    dependsOn = PermissibleValue(
        text="dependsOn",
        description="The `from` Element depends on each `to` Element, during a LifecycleScopeType period.",
        meaning=SPDX_CORE["RelationshipType/dependsOn"])
    descendantOf = PermissibleValue(
        text="descendantOf",
        description="The `from` Element is a descendant of each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/descendantOf"])
    describes = PermissibleValue(
        text="describes",
        description="""The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used.""",
        meaning=SPDX_CORE["RelationshipType/describes"])
    doesNotAffect = PermissibleValue(
        text="doesNotAffect",
        description="""The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.""",
        meaning=SPDX_CORE["RelationshipType/doesNotAffect"])
    expandsTo = PermissibleValue(
        text="expandsTo",
        description="The `from` archive expands out as an artifact described by each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/expandsTo"])
    exploitCreatedBy = PermissibleValue(
        text="exploitCreatedBy",
        description="The `from` Vulnerability has had an exploit created against it by each `to` Agent.",
        meaning=SPDX_CORE["RelationshipType/exploitCreatedBy"])
    fixedBy = PermissibleValue(
        text="fixedBy",
        description="Designates a `from` Vulnerability has been fixed by the `to` Agent(s).",
        meaning=SPDX_CORE["RelationshipType/fixedBy"])
    fixedIn = PermissibleValue(
        text="fixedIn",
        description="""A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.""",
        meaning=SPDX_CORE["RelationshipType/fixedIn"])
    foundBy = PermissibleValue(
        text="foundBy",
        description="Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).",
        meaning=SPDX_CORE["RelationshipType/foundBy"])
    generates = PermissibleValue(
        text="generates",
        description="The `from` Element generates each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/generates"])
    hasAddedFile = PermissibleValue(
        text="hasAddedFile",
        description="Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).",
        meaning=SPDX_CORE["RelationshipType/hasAddedFile"])
    hasAssessmentFor = PermissibleValue(
        text="hasAssessmentFor",
        description="""Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types.""",
        meaning=SPDX_CORE["RelationshipType/hasAssessmentFor"])
    hasAssociatedVulnerability = PermissibleValue(
        text="hasAssociatedVulnerability",
        description="Used to associate a `from` Artifact with each `to` Vulnerability.",
        meaning=SPDX_CORE["RelationshipType/hasAssociatedVulnerability"])
    hasConcludedLicense = PermissibleValue(
        text="hasConcludedLicense",
        description="""The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license.""",
        meaning=SPDX_CORE["RelationshipType/hasConcludedLicense"])
    hasDataFile = PermissibleValue(
        text="hasDataFile",
        description="""The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup file, and more. For AI training dataset, test dataset, test artifact, configuration data, build input data, and build output data, please consider using the more specific relationship types: `trainedOn`, `testedOn`, `hasTest`, `configures`, `hasInput`, and `hasOutput`, respectively. This relationship does not imply dependency.""",
        meaning=SPDX_CORE["RelationshipType/hasDataFile"])
    hasDeclaredLicense = PermissibleValue(
        text="hasDeclaredLicense",
        description="""The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.""",
        meaning=SPDX_CORE["RelationshipType/hasDeclaredLicense"])
    hasDeletedFile = PermissibleValue(
        text="hasDeletedFile",
        description="Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).",
        meaning=SPDX_CORE["RelationshipType/hasDeletedFile"])
    hasDependencyManifest = PermissibleValue(
        text="hasDependencyManifest",
        description="""The `from` Element has manifest files that contain dependency information in each `to` Element.""",
        meaning=SPDX_CORE["RelationshipType/hasDependencyManifest"])
    hasDistributionArtifact = PermissibleValue(
        text="hasDistributionArtifact",
        description="""The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).""",
        meaning=SPDX_CORE["RelationshipType/hasDistributionArtifact"])
    hasDocumentation = PermissibleValue(
        text="hasDocumentation",
        description="The `from` Element is documented by each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/hasDocumentation"])
    hasDynamicLink = PermissibleValue(
        text="hasDynamicLink",
        description="The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.",
        meaning=SPDX_CORE["RelationshipType/hasDynamicLink"])
    hasEvidence = PermissibleValue(
        text="hasEvidence",
        description="Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).",
        meaning=SPDX_CORE["RelationshipType/hasEvidence"])
    hasExample = PermissibleValue(
        text="hasExample",
        description="Every `to` Element is an example for the `from` Element (`from` hasExample `to`).",
        meaning=SPDX_CORE["RelationshipType/hasExample"])
    hasHost = PermissibleValue(
        text="hasHost",
        description="""The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).""",
        meaning=SPDX_CORE["RelationshipType/hasHost"])
    hasInput = PermissibleValue(
        text="hasInput",
        description="The `from` Build has each `to` Element as an input, during a LifecycleScopeType period.",
        meaning=SPDX_CORE["RelationshipType/hasInput"])
    hasMetadata = PermissibleValue(
        text="hasMetadata",
        description="Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).",
        meaning=SPDX_CORE["RelationshipType/hasMetadata"])
    hasOptionalComponent = PermissibleValue(
        text="hasOptionalComponent",
        description="""Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).""",
        meaning=SPDX_CORE["RelationshipType/hasOptionalComponent"])
    hasOptionalDependency = PermissibleValue(
        text="hasOptionalDependency",
        description="""The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/hasOptionalDependency"])
    hasOutput = PermissibleValue(
        text="hasOutput",
        description="""The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/hasOutput"])
    hasPrerequisite = PermissibleValue(
        text="hasPrerequisite",
        description="""The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/hasPrerequisite"])
    hasProvidedDependency = PermissibleValue(
        text="hasProvidedDependency",
        description="""The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/hasProvidedDependency"])
    hasRequirement = PermissibleValue(
        text="hasRequirement",
        description="The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.",
        meaning=SPDX_CORE["RelationshipType/hasRequirement"])
    hasSpecification = PermissibleValue(
        text="hasSpecification",
        description="""Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/hasSpecification"])
    hasStaticLink = PermissibleValue(
        text="hasStaticLink",
        description="The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.",
        meaning=SPDX_CORE["RelationshipType/hasStaticLink"])
    hasTest = PermissibleValue(
        text="hasTest",
        description="""Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.""",
        meaning=SPDX_CORE["RelationshipType/hasTest"])
    hasTestCase = PermissibleValue(
        text="hasTestCase",
        description="Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).",
        meaning=SPDX_CORE["RelationshipType/hasTestCase"])
    hasVariant = PermissibleValue(
        text="hasVariant",
        description="Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).",
        meaning=SPDX_CORE["RelationshipType/hasVariant"])
    invokedBy = PermissibleValue(
        text="invokedBy",
        description="""The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).""",
        meaning=SPDX_CORE["RelationshipType/invokedBy"])
    modifiedBy = PermissibleValue(
        text="modifiedBy",
        description="The `from` Element is modified by each `to` Element.",
        meaning=SPDX_CORE["RelationshipType/modifiedBy"])
    other = PermissibleValue(
        text="other",
        description="""Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).""",
        meaning=SPDX_CORE["RelationshipType/other"])
    packagedBy = PermissibleValue(
        text="packagedBy",
        description="Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).",
        meaning=SPDX_CORE["RelationshipType/packagedBy"])
    patchedBy = PermissibleValue(
        text="patchedBy",
        description="Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).",
        meaning=SPDX_CORE["RelationshipType/patchedBy"])
    publishedBy = PermissibleValue(
        text="publishedBy",
        description="""Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.""",
        meaning=SPDX_CORE["RelationshipType/publishedBy"])
    reportedBy = PermissibleValue(
        text="reportedBy",
        description="""Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.""",
        meaning=SPDX_CORE["RelationshipType/reportedBy"])
    republishedBy = PermissibleValue(
        text="republishedBy",
        description="""Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.""",
        meaning=SPDX_CORE["RelationshipType/republishedBy"])
    serializedInArtifact = PermissibleValue(
        text="serializedInArtifact",
        description="The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.",
        meaning=SPDX_CORE["RelationshipType/serializedInArtifact"])
    testedOn = PermissibleValue(
        text="testedOn",
        description="The `from` Element has been tested on the `to` Element(s).",
        meaning=SPDX_CORE["RelationshipType/testedOn"])
    trainedOn = PermissibleValue(
        text="trainedOn",
        description="The `from` Element has been trained on the `to` Element(s).",
        meaning=SPDX_CORE["RelationshipType/trainedOn"])
    underInvestigationFor = PermissibleValue(
        text="underInvestigationFor",
        description="""The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.""",
        meaning=SPDX_CORE["RelationshipType/underInvestigationFor"])
    usesTool = PermissibleValue(
        text="usesTool",
        description="The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.",
        meaning=SPDX_CORE["RelationshipType/usesTool"])

    _defn = EnumDefinition(
        name="RelationshipType",
        description="Information about the relationship between two Elements.",
    )

class SupportType(EnumDefinitionImpl):
    """
    Indicates the type of support that is associated with an artifact.
    """
    deployed = PermissibleValue(
        text="deployed",
        description="""in addition to being supported by the supplier, the software is known to have been deployed and is in use. For a software as a service provider, this implies the software is now available as a service.""",
        meaning=SPDX_CORE["SupportType/deployed"])
    development = PermissibleValue(
        text="development",
        description="""the artifact is in active development and is not considered ready for formal support from the supplier.""",
        meaning=SPDX_CORE["SupportType/development"])
    endOfSupport = PermissibleValue(
        text="endOfSupport",
        description="""there is a defined end of support for the artifact from the supplier. This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact.""",
        meaning=SPDX_CORE["SupportType/endOfSupport"])
    limitedSupport = PermissibleValue(
        text="limitedSupport",
        description="""the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.""",
        meaning=SPDX_CORE["SupportType/limitedSupport"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="""no assertion about the type of support is made. This is considered the default if no other support type is used.""",
        meaning=SPDX_CORE["SupportType/noAssertion"])
    noSupport = PermissibleValue(
        text="noSupport",
        description="""there is no support for the artifact from the supplier, consumer assumes any support obligations.""",
        meaning=SPDX_CORE["SupportType/noSupport"])
    support = PermissibleValue(
        text="support",
        description="""the artifact has been released, and is supported from the supplier. There is a validUntilDate that can provide additional information about the duration of support.""",
        meaning=SPDX_CORE["SupportType/support"])

    _defn = EnumDefinition(
        name="SupportType",
        description="Indicates the type of support that is associated with an artifact.",
    )

class ContentIdentifierType(EnumDefinitionImpl):
    """
    Specifies the type of a content identifier.
    """
    gitoid = PermissibleValue(
        text="gitoid",
        description="""[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).""",
        meaning=SPDX_SOFTWARE["ContentIdentifierType/gitoid"])
    swhid = PermissibleValue(
        text="swhid",
        description="""SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.""",
        meaning=SPDX_SOFTWARE["ContentIdentifierType/swhid"])

    _defn = EnumDefinition(
        name="ContentIdentifierType",
        description="Specifies the type of a content identifier.",
    )

class FileKindType(EnumDefinitionImpl):
    """
    Enumeration of the different kinds of SPDX file.
    """
    directory = PermissibleValue(
        text="directory",
        description="The file represents a directory and all content stored in that directory.",
        meaning=SPDX_SOFTWARE["FileKindType/directory"])
    file = PermissibleValue(
        text="file",
        description="The file represents a single file (default).",
        meaning=SPDX_SOFTWARE["FileKindType/file"])

    _defn = EnumDefinition(
        name="FileKindType",
        description="Enumeration of the different kinds of SPDX file.",
    )

class SbomType(EnumDefinitionImpl):
    """
    Provides a set of values to be used to describe the common types of SBOMs that tools may create.
    """
    analyzed = PermissibleValue(
        text="analyzed",
        description="""SBOM generated through analysis of artifacts (e.g., executables, packages, containers, and virtual machine images) after its build. Such analysis generally requires a variety of heuristics. In some contexts, this may also be referred to as a \"3rd party\" SBOM.""",
        meaning=SPDX_SOFTWARE["SbomType/analyzed"])
    build = PermissibleValue(
        text="build",
        description="""SBOM generated as part of the process of building the software to create a releasable artifact (e.g., executable or package) from data such as source files, dependencies, built components, build process ephemeral data, and other SBOMs.""",
        meaning=SPDX_SOFTWARE["SbomType/build"])
    deployed = PermissibleValue(
        text="deployed",
        description="""SBOM provides an inventory of software that is present on a system. This may be an assembly of other SBOMs that combines analysis of configuration options, and examination of execution behavior in a (potentially simulated) deployment environment.""",
        meaning=SPDX_SOFTWARE["SbomType/deployed"])
    design = PermissibleValue(
        text="design",
        description="""SBOM of intended, planned software project or product with included components (some of which may not yet exist) for a new software artifact.""",
        meaning=SPDX_SOFTWARE["SbomType/design"])
    runtime = PermissibleValue(
        text="runtime",
        description="""SBOM generated through instrumenting the system running the software, to capture only components present in the system, as well as external call-outs or dynamically loaded components. In some contexts, this may also be referred to as an \"Instrumented\" or \"Dynamic\" SBOM.""",
        meaning=SPDX_SOFTWARE["SbomType/runtime"])
    source = PermissibleValue(
        text="source",
        description="""SBOM created directly from the development environment, source files, and included dependencies used to build an product artifact.""",
        meaning=SPDX_SOFTWARE["SbomType/source"])

    _defn = EnumDefinition(
        name="SbomType",
        description="Provides a set of values to be used to describe the common types of SBOMs that tools may create.",
    )

class SoftwarePurpose(EnumDefinitionImpl):
    """
    Provides information about the primary purpose of an Element.
    """
    application = PermissibleValue(
        text="application",
        description="The Element is a software application.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/application"])
    archive = PermissibleValue(
        text="archive",
        description="The Element is an archived collection of one or more files (.tar, .zip, etc.).",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/archive"])
    bom = PermissibleValue(
        text="bom",
        description="The Element is a bill of materials.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/bom"])
    configuration = PermissibleValue(
        text="configuration",
        description="The Element is configuration data.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/configuration"])
    container = PermissibleValue(
        text="container",
        description="The Element is a container image which can be used by a container runtime application.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/container"])
    data = PermissibleValue(
        text="data",
        description="The Element is data.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/data"])
    device = PermissibleValue(
        text="device",
        description="The Element refers to a chipset, processor, or electronic board.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/device"])
    deviceDriver = PermissibleValue(
        text="deviceDriver",
        description="The Element represents software that controls hardware devices.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/deviceDriver"])
    diskImage = PermissibleValue(
        text="diskImage",
        description="""The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.""",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/diskImage"])
    documentation = PermissibleValue(
        text="documentation",
        description="The Element is documentation.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/documentation"])
    evidence = PermissibleValue(
        text="evidence",
        description="The Element is the evidence that a specification or requirement has been fulfilled.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/evidence"])
    executable = PermissibleValue(
        text="executable",
        description="The Element is an Artifact that can be run on a computer.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/executable"])
    file = PermissibleValue(
        text="file",
        description="""The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.).""",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/file"])
    filesystemImage = PermissibleValue(
        text="filesystemImage",
        description="The Element is a file system image that can be written to a disk (or virtual) partition.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/filesystemImage"])
    firmware = PermissibleValue(
        text="firmware",
        description="The Element provides low level control over a device's hardware.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/firmware"])
    framework = PermissibleValue(
        text="framework",
        description="The Element is a software framework.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/framework"])
    install = PermissibleValue(
        text="install",
        description="The Element is used to install software on disk.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/install"])
    library = PermissibleValue(
        text="library",
        description="The Element is a software library.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/library"])
    manifest = PermissibleValue(
        text="manifest",
        description="The Element is a software manifest.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/manifest"])
    model = PermissibleValue(
        text="model",
        description="The Element is a machine learning or artificial intelligence model.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/model"])
    module = PermissibleValue(
        text="module",
        description="The Element is a module of a piece of software.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/module"])
    operatingSystem = PermissibleValue(
        text="operatingSystem",
        description="The Element is an operating system.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/operatingSystem"])
    other = PermissibleValue(
        text="other",
        description="The Element doesn't fit into any of the other categories.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/other"])
    patch = PermissibleValue(
        text="patch",
        description="The Element contains a set of changes to update, fix, or improve another Element.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/patch"])
    platform = PermissibleValue(
        text="platform",
        description="The Element represents a runtime environment.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/platform"])
    requirement = PermissibleValue(
        text="requirement",
        description="The Element provides a requirement needed as input for another Element.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/requirement"])
    source = PermissibleValue(
        text="source",
        description="The Element is a single or a collection of source files.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/source"])
    specification = PermissibleValue(
        text="specification",
        description="The Element is a plan, guideline or strategy how to create, perform or analyze an application.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/specification"])
    test = PermissibleValue(
        text="test",
        description="The Element is a test used to verify functionality on an software element.",
        meaning=SPDX_SOFTWARE["SoftwarePurpose/test"])

    _defn = EnumDefinition(
        name="SoftwarePurpose",
        description="Provides information about the primary purpose of an Element.",
    )

class EnergyUnitType(EnumDefinitionImpl):
    """
    Specifies the unit of energy consumption.
    """
    kilowattHour = PermissibleValue(
        text="kilowattHour",
        description="Kilowatt-hour.",
        meaning=SPDX_AI["EnergyUnitType/kilowattHour"])
    megajoule = PermissibleValue(
        text="megajoule",
        description="Megajoule.",
        meaning=SPDX_AI["EnergyUnitType/megajoule"])
    other = PermissibleValue(
        text="other",
        description="Any other units of energy measurement.",
        meaning=SPDX_AI["EnergyUnitType/other"])

    _defn = EnumDefinition(
        name="EnergyUnitType",
        description="Specifies the unit of energy consumption.",
    )

class SafetyRiskAssessmentType(EnumDefinitionImpl):
    """
    Specifies the safety risk level.
    """
    high = PermissibleValue(
        text="high",
        description="The second-highest level of risk posed by an AI system.",
        meaning=SPDX_AI["SafetyRiskAssessmentType/high"])
    low = PermissibleValue(
        text="low",
        description="Low/no risk is posed by an AI system.",
        meaning=SPDX_AI["SafetyRiskAssessmentType/low"])
    medium = PermissibleValue(
        text="medium",
        description="The third-highest level of risk posed by an AI system.",
        meaning=SPDX_AI["SafetyRiskAssessmentType/medium"])
    serious = PermissibleValue(
        text="serious",
        description="The highest level of risk posed by an AI system.",
        meaning=SPDX_AI["SafetyRiskAssessmentType/serious"])

    _defn = EnumDefinition(
        name="SafetyRiskAssessmentType",
        description="Specifies the safety risk level.",
    )

class ConfidentialityLevelType(EnumDefinitionImpl):
    """
    Categories of confidentiality level.
    """
    amber = PermissibleValue(
        text="amber",
        description="""Data points in the dataset can be shared only with specific organizations and their clients on a need to know basis.""",
        meaning=SPDX_DATASET["ConfidentialityLevelType/amber"])
    clear = PermissibleValue(
        text="clear",
        description="Dataset may be distributed freely, without restriction.",
        meaning=SPDX_DATASET["ConfidentialityLevelType/clear"])
    green = PermissibleValue(
        text="green",
        description="Dataset can be shared within a community of peers and partners.",
        meaning=SPDX_DATASET["ConfidentialityLevelType/green"])
    red = PermissibleValue(
        text="red",
        description="""Data points in the dataset are highly confidential and can only be shared with named recipients.""",
        meaning=SPDX_DATASET["ConfidentialityLevelType/red"])

    _defn = EnumDefinition(
        name="ConfidentialityLevelType",
        description="Categories of confidentiality level.",
    )

class DatasetAvailabilityType(EnumDefinitionImpl):
    """
    Availability of dataset.
    """
    clickthrough = PermissibleValue(
        text="clickthrough",
        description="""the dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage.""",
        meaning=SPDX_DATASET["DatasetAvailabilityType/clickthrough"])
    directDownload = PermissibleValue(
        text="directDownload",
        description="the dataset is publicly available and can be downloaded directly.",
        meaning=SPDX_DATASET["DatasetAvailabilityType/directDownload"])
    query = PermissibleValue(
        text="query",
        description="""the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.""",
        meaning=SPDX_DATASET["DatasetAvailabilityType/query"])
    registration = PermissibleValue(
        text="registration",
        description="""the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.""",
        meaning=SPDX_DATASET["DatasetAvailabilityType/registration"])
    scrapingScript = PermissibleValue(
        text="scrapingScript",
        description="""the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data.""",
        meaning=SPDX_DATASET["DatasetAvailabilityType/scrapingScript"])

    _defn = EnumDefinition(
        name="DatasetAvailabilityType",
        description="Availability of dataset.",
    )

class DatasetType(EnumDefinitionImpl):
    """
    Enumeration of dataset types.
    """
    audio = PermissibleValue(
        text="audio",
        description="data is audio based, such as a collection of music from the 80s.",
        meaning=SPDX_DATASET["DatasetType/audio"])
    categorical = PermissibleValue(
        text="categorical",
        description="""data that is classified into a discrete number of categories, such as the eye color of a population of people.""",
        meaning=SPDX_DATASET["DatasetType/categorical"])
    graph = PermissibleValue(
        text="graph",
        description="""data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends.""",
        meaning=SPDX_DATASET["DatasetType/graph"])
    image = PermissibleValue(
        text="image",
        description="data is a collection of images such as pictures of animals.",
        meaning=SPDX_DATASET["DatasetType/image"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="data type is not known.",
        meaning=SPDX_DATASET["DatasetType/noAssertion"])
    numeric = PermissibleValue(
        text="numeric",
        description="data consists only of numeric entries.",
        meaning=SPDX_DATASET["DatasetType/numeric"])
    other = PermissibleValue(
        text="other",
        description="data is of a type not included in this list.",
        meaning=SPDX_DATASET["DatasetType/other"])
    sensor = PermissibleValue(
        text="sensor",
        description="data is recorded from a physical sensor, such as a thermometer reading or biometric device.",
        meaning=SPDX_DATASET["DatasetType/sensor"])
    structured = PermissibleValue(
        text="structured",
        description="data is stored in tabular format or retrieved from a relational database.",
        meaning=SPDX_DATASET["DatasetType/structured"])
    syntactic = PermissibleValue(
        text="syntactic",
        description="""data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing.""",
        meaning=SPDX_DATASET["DatasetType/syntactic"])
    text = PermissibleValue(
        text="text",
        description="""data consists of unstructured text, such as a book, Wikipedia article (without images), or transcript.""",
        meaning=SPDX_DATASET["DatasetType/text"])
    timeseries = PermissibleValue(
        text="timeseries",
        description="""data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day.""",
        meaning=SPDX_DATASET["DatasetType/timeseries"])
    timestamp = PermissibleValue(
        text="timestamp",
        description="""data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends.""",
        meaning=SPDX_DATASET["DatasetType/timestamp"])
    video = PermissibleValue(
        text="video",
        description="data is video based, such as a collection of movie clips featuring Tom Hanks.",
        meaning=SPDX_DATASET["DatasetType/video"])

    _defn = EnumDefinition(
        name="DatasetType",
        description="Enumeration of dataset types.",
    )

class CvssSeverityType(EnumDefinitionImpl):
    """
    Specifies the CVSS base, temporal, threat, or environmental severity type.
    """
    critical = PermissibleValue(
        text="critical",
        description="When a CVSS score is between 9.0 - 10.0",
        meaning=SPDX_SECURITY["CvssSeverityType/critical"])
    high = PermissibleValue(
        text="high",
        description="When a CVSS score is between 7.0 - 8.9",
        meaning=SPDX_SECURITY["CvssSeverityType/high"])
    low = PermissibleValue(
        text="low",
        description="When a CVSS score is between 0.1 - 3.9",
        meaning=SPDX_SECURITY["CvssSeverityType/low"])
    medium = PermissibleValue(
        text="medium",
        description="When a CVSS score is between 4.0 - 6.9",
        meaning=SPDX_SECURITY["CvssSeverityType/medium"])
    none = PermissibleValue(
        text="none",
        description="When a CVSS score is 0.0",
        meaning=SPDX_SECURITY["CvssSeverityType/none"])

    _defn = EnumDefinition(
        name="CvssSeverityType",
        description="Specifies the CVSS base, temporal, threat, or environmental severity type.",
    )

class ExploitCatalogType(EnumDefinitionImpl):
    """
    Specifies the exploit catalog type.
    """
    kev = PermissibleValue(
        text="kev",
        description="CISA's Known Exploited Vulnerability (KEV) Catalog",
        meaning=SPDX_SECURITY["ExploitCatalogType/kev"])
    other = PermissibleValue(
        text="other",
        description="Other exploit catalogs",
        meaning=SPDX_SECURITY["ExploitCatalogType/other"])

    _defn = EnumDefinition(
        name="ExploitCatalogType",
        description="Specifies the exploit catalog type.",
    )

class SsvcDecisionType(EnumDefinitionImpl):
    """
    Specifies the SSVC decision type.
    """
    act = PermissibleValue(
        text="act",
        description="""The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. Typically, internal groups would meet to determine the overall response and then execute agreed upon actions. CISA recommends remediating Act vulnerabilities as soon as possible.""",
        meaning=SPDX_SECURITY["SsvcDecisionType/act"])
    attend = PermissibleValue(
        text="attend",
        description="""The vulnerability requires attention from the organization's internal, supervisory-level individuals. Necessary actions include requesting assistance or information about the vulnerability, and may involve publishing a notification either internally and/or externally. CISA recommends remediating Attend vulnerabilities sooner than standard update timelines.""",
        meaning=SPDX_SECURITY["SsvcDecisionType/attend"])
    track = PermissibleValue(
        text="track",
        description="""The vulnerability does not require action at this time. The organization would continue to track the vulnerability and reassess it if new information becomes available. CISA recommends remediating Track vulnerabilities within standard update timelines.""",
        meaning=SPDX_SECURITY["SsvcDecisionType/track"])
    trackStar = PermissibleValue(
        text="trackStar",
        description="""(\"Track*\" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track* vulnerabilities within standard update timelines.""",
        meaning=SPDX_SECURITY["SsvcDecisionType/trackStar"])

    _defn = EnumDefinition(
        name="SsvcDecisionType",
        description="Specifies the SSVC decision type.",
    )

class VexJustificationType(EnumDefinitionImpl):
    """
    Specifies the VEX justification type.
    """
    componentNotPresent = PermissibleValue(
        text="componentNotPresent",
        description="The software is not affected because the vulnerable component is not in the product.",
        meaning=SPDX_SECURITY["VexJustificationType/componentNotPresent"])
    inlineMitigationsAlreadyExist = PermissibleValue(
        text="inlineMitigationsAlreadyExist",
        description="""Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.""",
        meaning=SPDX_SECURITY["VexJustificationType/inlineMitigationsAlreadyExist"])
    vulnerableCodeCannotBeControlledByAdversary = PermissibleValue(
        text="vulnerableCodeCannotBeControlledByAdversary",
        description="""The vulnerable component is present, and the component contains the vulnerable code. However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.""",
        meaning=SPDX_SECURITY["VexJustificationType/vulnerableCodeCannotBeControlledByAdversary"])
    vulnerableCodeNotInExecutePath = PermissibleValue(
        text="vulnerableCodeNotInExecutePath",
        description="""The affected code is not reachable through the execution of the code, including non-anticipated states of the product.""",
        meaning=SPDX_SECURITY["VexJustificationType/vulnerableCodeNotInExecutePath"])
    vulnerableCodeNotPresent = PermissibleValue(
        text="vulnerableCodeNotPresent",
        description="""The product is not affected because the code underlying the vulnerability is not present in the product.""",
        meaning=SPDX_SECURITY["VexJustificationType/vulnerableCodeNotPresent"])

    _defn = EnumDefinition(
        name="VexJustificationType",
        description="Specifies the VEX justification type.",
    )

# Slots
class slots:
    pass

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=SPDX_LINKML.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.algorithm = Slot(uri=SPDX_CORE.algorithm, name="algorithm", curie=SPDX_CORE.curie('algorithm'),
                   model_uri=SPDX_LINKML.algorithm, domain=None, range=Union[str, "HashAlgorithm"])

slots.annotationType = Slot(uri=SPDX_CORE.annotationType, name="annotationType", curie=SPDX_CORE.curie('annotationType'),
                   model_uri=SPDX_LINKML.annotationType, domain=None, range=Union[str, "AnnotationType"])

slots.beginIntegerRange = Slot(uri=SPDX_CORE.beginIntegerRange, name="beginIntegerRange", curie=SPDX_CORE.curie('beginIntegerRange'),
                   model_uri=SPDX_LINKML.beginIntegerRange, domain=None, range=Union[int, PositiveInteger])

slots.builtTime = Slot(uri=SPDX_CORE.builtTime, name="builtTime", curie=SPDX_CORE.curie('builtTime'),
                   model_uri=SPDX_LINKML.builtTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.comment = Slot(uri=SPDX_CORE.comment, name="comment", curie=SPDX_CORE.curie('comment'),
                   model_uri=SPDX_LINKML.comment, domain=None, range=Optional[str])

slots.completeness = Slot(uri=SPDX_CORE.completeness, name="completeness", curie=SPDX_CORE.curie('completeness'),
                   model_uri=SPDX_LINKML.completeness, domain=None, range=Optional[Union[str, "RelationshipCompleteness"]])

slots.contentType = Slot(uri=SPDX_CORE.contentType, name="contentType", curie=SPDX_CORE.curie('contentType'),
                   model_uri=SPDX_LINKML.contentType, domain=None, range=Optional[Union[str, MediaType]])

slots.context = Slot(uri=SPDX_CORE.context, name="context", curie=SPDX_CORE.curie('context'),
                   model_uri=SPDX_LINKML.context, domain=None, range=Optional[str])

slots.created = Slot(uri=SPDX_CORE.created, name="created", curie=SPDX_CORE.curie('created'),
                   model_uri=SPDX_LINKML.created, domain=None, range=Union[str, DateTimeStamp])

slots.createdBy = Slot(uri=SPDX_CORE.createdBy, name="createdBy", curie=SPDX_CORE.curie('createdBy'),
                   model_uri=SPDX_LINKML.createdBy, domain=None, range=Union[Union[str, AgentSpdxId], list[Union[str, AgentSpdxId]]])

slots.createdUsing = Slot(uri=SPDX_CORE.createdUsing, name="createdUsing", curie=SPDX_CORE.curie('createdUsing'),
                   model_uri=SPDX_LINKML.createdUsing, domain=None, range=Optional[Union[Union[str, ToolSpdxId], list[Union[str, ToolSpdxId]]]])

slots.creationInfo = Slot(uri=SPDX_CORE.creationInfo, name="creationInfo", curie=SPDX_CORE.curie('creationInfo'),
                   model_uri=SPDX_LINKML.creationInfo, domain=None, range=Union[dict, CreationInfo])

slots.dataLicense = Slot(uri=SPDX_CORE.dataLicense, name="dataLicense", curie=SPDX_CORE.curie('dataLicense'),
                   model_uri=SPDX_LINKML.dataLicense, domain=None, range=Optional[Union[str, AnyLicenseInfoSpdxId]])

slots.definingArtifact = Slot(uri=SPDX_CORE.definingArtifact, name="definingArtifact", curie=SPDX_CORE.curie('definingArtifact'),
                   model_uri=SPDX_LINKML.definingArtifact, domain=None, range=Optional[Union[str, ArtifactSpdxId]])

slots.description = Slot(uri=SPDX_CORE.description, name="description", curie=SPDX_CORE.curie('description'),
                   model_uri=SPDX_LINKML.description, domain=None, range=Optional[str])

slots.element = Slot(uri=SPDX_CORE.element, name="element", curie=SPDX_CORE.curie('element'),
                   model_uri=SPDX_LINKML.element, domain=None, range=Optional[Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]]])

slots.endIntegerRange = Slot(uri=SPDX_CORE.endIntegerRange, name="endIntegerRange", curie=SPDX_CORE.curie('endIntegerRange'),
                   model_uri=SPDX_LINKML.endIntegerRange, domain=None, range=Union[int, PositiveInteger])

slots.endTime = Slot(uri=SPDX_CORE.endTime, name="endTime", curie=SPDX_CORE.curie('endTime'),
                   model_uri=SPDX_LINKML.endTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.extension = Slot(uri=SPDX_CORE.extension, name="extension", curie=SPDX_CORE.curie('extension'),
                   model_uri=SPDX_LINKML.extension, domain=None, range=Optional[Union[Union[dict, Extension], list[Union[dict, Extension]]]])

slots.externalIdentifier = Slot(uri=SPDX_CORE.externalIdentifier, name="externalIdentifier", curie=SPDX_CORE.curie('externalIdentifier'),
                   model_uri=SPDX_LINKML.externalIdentifier, domain=None, range=Optional[Union[Union[dict, ExternalIdentifier], list[Union[dict, ExternalIdentifier]]]])

slots.externalIdentifierType = Slot(uri=SPDX_CORE.externalIdentifierType, name="externalIdentifierType", curie=SPDX_CORE.curie('externalIdentifierType'),
                   model_uri=SPDX_LINKML.externalIdentifierType, domain=None, range=Union[str, "ExternalIdentifierType"])

slots.externalRef = Slot(uri=SPDX_CORE.externalRef, name="externalRef", curie=SPDX_CORE.curie('externalRef'),
                   model_uri=SPDX_LINKML.externalRef, domain=None, range=Optional[Union[Union[dict, ExternalRef], list[Union[dict, ExternalRef]]]])

slots.externalRefType = Slot(uri=SPDX_CORE.externalRefType, name="externalRefType", curie=SPDX_CORE.curie('externalRefType'),
                   model_uri=SPDX_LINKML.externalRefType, domain=None, range=Optional[Union[str, "ExternalRefType"]])

slots.externalSpdxId = Slot(uri=SPDX_CORE.externalSpdxId, name="externalSpdxId", curie=SPDX_CORE.curie('externalSpdxId'),
                   model_uri=SPDX_LINKML.externalSpdxId, domain=None, range=Union[str, URI])

slots.from_ = Slot(uri=SPDX_CORE['from'], name="from", curie=SPDX_CORE.curie('from'),
                   model_uri=SPDX_LINKML.from_, domain=None, range=Union[str, ElementSpdxId])

slots.hashValue = Slot(uri=SPDX_CORE.hashValue, name="hashValue", curie=SPDX_CORE.curie('hashValue'),
                   model_uri=SPDX_LINKML.hashValue, domain=None, range=str)

slots.identifier = Slot(uri=SPDX_CORE.identifier, name="identifier", curie=SPDX_CORE.curie('identifier'),
                   model_uri=SPDX_LINKML.identifier, domain=None, range=str)

slots.identifierLocator = Slot(uri=SPDX_CORE.identifierLocator, name="identifierLocator", curie=SPDX_CORE.curie('identifierLocator'),
                   model_uri=SPDX_LINKML.identifierLocator, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.import_ = Slot(uri=SPDX_CORE['import'], name="import", curie=SPDX_CORE.curie('import'),
                   model_uri=SPDX_LINKML.import_, domain=None, range=Optional[Union[Union[dict, ExternalMap], list[Union[dict, ExternalMap]]]])

slots.issuingAuthority = Slot(uri=SPDX_CORE.issuingAuthority, name="issuingAuthority", curie=SPDX_CORE.curie('issuingAuthority'),
                   model_uri=SPDX_LINKML.issuingAuthority, domain=None, range=Optional[str])

slots.key = Slot(uri=SPDX_CORE.key, name="key", curie=SPDX_CORE.curie('key'),
                   model_uri=SPDX_LINKML.key, domain=None, range=str)

slots.locationHint = Slot(uri=SPDX_CORE.locationHint, name="locationHint", curie=SPDX_CORE.curie('locationHint'),
                   model_uri=SPDX_LINKML.locationHint, domain=None, range=Optional[Union[str, URI]])

slots.locator = Slot(uri=SPDX_CORE.locator, name="locator", curie=SPDX_CORE.curie('locator'),
                   model_uri=SPDX_LINKML.locator, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=SPDX_CORE.name, name="name", curie=SPDX_CORE.curie('name'),
                   model_uri=SPDX_LINKML.name, domain=None, range=Optional[str])

slots.namespace = Slot(uri=SPDX_CORE.namespace, name="namespace", curie=SPDX_CORE.curie('namespace'),
                   model_uri=SPDX_LINKML.namespace, domain=None, range=Union[str, URI])

slots.namespaceMap = Slot(uri=SPDX_CORE.namespaceMap, name="namespaceMap", curie=SPDX_CORE.curie('namespaceMap'),
                   model_uri=SPDX_LINKML.namespaceMap, domain=None, range=Optional[Union[Union[dict, NamespaceMap], list[Union[dict, NamespaceMap]]]])

slots.originatedBy = Slot(uri=SPDX_CORE.originatedBy, name="originatedBy", curie=SPDX_CORE.curie('originatedBy'),
                   model_uri=SPDX_LINKML.originatedBy, domain=None, range=Optional[Union[Union[str, AgentSpdxId], list[Union[str, AgentSpdxId]]]])

slots.packageVerificationCodeExcludedFile = Slot(uri=SPDX_CORE.packageVerificationCodeExcludedFile, name="packageVerificationCodeExcludedFile", curie=SPDX_CORE.curie('packageVerificationCodeExcludedFile'),
                   model_uri=SPDX_LINKML.packageVerificationCodeExcludedFile, domain=None, range=Optional[Union[str, list[str]]])

slots.prefix = Slot(uri=SPDX_CORE.prefix, name="prefix", curie=SPDX_CORE.curie('prefix'),
                   model_uri=SPDX_LINKML.prefix, domain=None, range=str)

slots.profileConformance = Slot(uri=SPDX_CORE.profileConformance, name="profileConformance", curie=SPDX_CORE.curie('profileConformance'),
                   model_uri=SPDX_LINKML.profileConformance, domain=None, range=Optional[Union[Union[str, "ProfileIdentifierType"], list[Union[str, "ProfileIdentifierType"]]]])

slots.relationshipType = Slot(uri=SPDX_CORE.relationshipType, name="relationshipType", curie=SPDX_CORE.curie('relationshipType'),
                   model_uri=SPDX_LINKML.relationshipType, domain=None, range=Union[str, "RelationshipType"])

slots.releaseTime = Slot(uri=SPDX_CORE.releaseTime, name="releaseTime", curie=SPDX_CORE.curie('releaseTime'),
                   model_uri=SPDX_LINKML.releaseTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.rootElement = Slot(uri=SPDX_CORE.rootElement, name="rootElement", curie=SPDX_CORE.curie('rootElement'),
                   model_uri=SPDX_LINKML.rootElement, domain=None, range=Optional[Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]]])

slots.scope = Slot(uri=SPDX_CORE.scope, name="scope", curie=SPDX_CORE.curie('scope'),
                   model_uri=SPDX_LINKML.scope, domain=None, range=Optional[Union[str, "LifecycleScopeType"]])

slots.specVersion = Slot(uri=SPDX_CORE.specVersion, name="specVersion", curie=SPDX_CORE.curie('specVersion'),
                   model_uri=SPDX_LINKML.specVersion, domain=None, range=Union[str, Semver])

slots.standardName = Slot(uri=SPDX_CORE.standardName, name="standardName", curie=SPDX_CORE.curie('standardName'),
                   model_uri=SPDX_LINKML.standardName, domain=None, range=Optional[Union[str, list[str]]])

slots.startTime = Slot(uri=SPDX_CORE.startTime, name="startTime", curie=SPDX_CORE.curie('startTime'),
                   model_uri=SPDX_LINKML.startTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.statement = Slot(uri=SPDX_CORE.statement, name="statement", curie=SPDX_CORE.curie('statement'),
                   model_uri=SPDX_LINKML.statement, domain=None, range=Optional[str])

slots.subject = Slot(uri=SPDX_CORE.subject, name="subject", curie=SPDX_CORE.curie('subject'),
                   model_uri=SPDX_LINKML.subject, domain=None, range=Union[str, ElementSpdxId])

slots.summary = Slot(uri=SPDX_CORE.summary, name="summary", curie=SPDX_CORE.curie('summary'),
                   model_uri=SPDX_LINKML.summary, domain=None, range=Optional[str])

slots.suppliedBy = Slot(uri=SPDX_CORE.suppliedBy, name="suppliedBy", curie=SPDX_CORE.curie('suppliedBy'),
                   model_uri=SPDX_LINKML.suppliedBy, domain=None, range=Optional[Union[str, AgentSpdxId]])

slots.supportLevel = Slot(uri=SPDX_CORE.supportLevel, name="supportLevel", curie=SPDX_CORE.curie('supportLevel'),
                   model_uri=SPDX_LINKML.supportLevel, domain=None, range=Optional[Union[Union[str, "SupportType"], list[Union[str, "SupportType"]]]])

slots.to = Slot(uri=SPDX_CORE.to, name="to", curie=SPDX_CORE.curie('to'),
                   model_uri=SPDX_LINKML.to, domain=None, range=Union[Union[str, ElementSpdxId], list[Union[str, ElementSpdxId]]])

slots.validUntilTime = Slot(uri=SPDX_CORE.validUntilTime, name="validUntilTime", curie=SPDX_CORE.curie('validUntilTime'),
                   model_uri=SPDX_LINKML.validUntilTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.value = Slot(uri=SPDX_CORE.value, name="value", curie=SPDX_CORE.curie('value'),
                   model_uri=SPDX_LINKML.value, domain=None, range=Optional[str])

slots.verifiedUsing = Slot(uri=SPDX_CORE.verifiedUsing, name="verifiedUsing", curie=SPDX_CORE.curie('verifiedUsing'),
                   model_uri=SPDX_LINKML.verifiedUsing, domain=None, range=Optional[Union[Union[dict, IntegrityMethod], list[Union[dict, IntegrityMethod]]]])

slots.buildEndTime = Slot(uri=SPDX_BUILD.buildEndTime, name="buildEndTime", curie=SPDX_BUILD.curie('buildEndTime'),
                   model_uri=SPDX_LINKML.buildEndTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.buildId = Slot(uri=SPDX_BUILD.buildId, name="buildId", curie=SPDX_BUILD.curie('buildId'),
                   model_uri=SPDX_LINKML.buildId, domain=None, range=Optional[str])

slots.buildStartTime = Slot(uri=SPDX_BUILD.buildStartTime, name="buildStartTime", curie=SPDX_BUILD.curie('buildStartTime'),
                   model_uri=SPDX_LINKML.buildStartTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.buildType = Slot(uri=SPDX_BUILD.buildType, name="buildType", curie=SPDX_BUILD.curie('buildType'),
                   model_uri=SPDX_LINKML.buildType, domain=None, range=Union[str, URI])

slots.configSourceDigest = Slot(uri=SPDX_BUILD.configSourceDigest, name="configSourceDigest", curie=SPDX_BUILD.curie('configSourceDigest'),
                   model_uri=SPDX_LINKML.configSourceDigest, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.configSourceEntrypoint = Slot(uri=SPDX_BUILD.configSourceEntrypoint, name="configSourceEntrypoint", curie=SPDX_BUILD.curie('configSourceEntrypoint'),
                   model_uri=SPDX_LINKML.configSourceEntrypoint, domain=None, range=Optional[Union[str, list[str]]])

slots.configSourceUri = Slot(uri=SPDX_BUILD.configSourceUri, name="configSourceUri", curie=SPDX_BUILD.curie('configSourceUri'),
                   model_uri=SPDX_LINKML.configSourceUri, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.environment = Slot(uri=SPDX_BUILD.environment, name="environment", curie=SPDX_BUILD.curie('environment'),
                   model_uri=SPDX_LINKML.environment, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.parameter = Slot(uri=SPDX_BUILD.parameter, name="parameter", curie=SPDX_BUILD.curie('parameter'),
                   model_uri=SPDX_LINKML.parameter, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.cdxPropName = Slot(uri=SPDX_EXTENSION.cdxPropName, name="cdxPropName", curie=SPDX_EXTENSION.curie('cdxPropName'),
                   model_uri=SPDX_LINKML.cdxPropName, domain=None, range=str)

slots.cdxPropValue = Slot(uri=SPDX_EXTENSION.cdxPropValue, name="cdxPropValue", curie=SPDX_EXTENSION.curie('cdxPropValue'),
                   model_uri=SPDX_LINKML.cdxPropValue, domain=None, range=Optional[str])

slots.cdxProperty = Slot(uri=SPDX_EXTENSION.cdxProperty, name="cdxProperty", curie=SPDX_EXTENSION.curie('cdxProperty'),
                   model_uri=SPDX_LINKML.cdxProperty, domain=None, range=Union[Union[dict, CdxPropertyEntry], list[Union[dict, CdxPropertyEntry]]])

slots.customIdToUri = Slot(uri=SPDX_SIMPLE_LICENSING.customIdToUri, name="customIdToUri", curie=SPDX_SIMPLE_LICENSING.curie('customIdToUri'),
                   model_uri=SPDX_LINKML.customIdToUri, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.licenseExpression = Slot(uri=SPDX_SIMPLE_LICENSING.licenseExpression, name="licenseExpression", curie=SPDX_SIMPLE_LICENSING.curie('licenseExpression'),
                   model_uri=SPDX_LINKML.licenseExpression, domain=None, range=str)

slots.licenseListVersion = Slot(uri=SPDX_SIMPLE_LICENSING.licenseListVersion, name="licenseListVersion", curie=SPDX_SIMPLE_LICENSING.curie('licenseListVersion'),
                   model_uri=SPDX_LINKML.licenseListVersion, domain=None, range=Optional[Union[str, Semver]])

slots.licenseText = Slot(uri=SPDX_SIMPLE_LICENSING.licenseText, name="licenseText", curie=SPDX_SIMPLE_LICENSING.curie('licenseText'),
                   model_uri=SPDX_LINKML.licenseText, domain=None, range=str)

slots.additionalPurpose = Slot(uri=SPDX_SOFTWARE.additionalPurpose, name="additionalPurpose", curie=SPDX_SOFTWARE.curie('additionalPurpose'),
                   model_uri=SPDX_LINKML.additionalPurpose, domain=None, range=Optional[Union[Union[str, "SoftwarePurpose"], list[Union[str, "SoftwarePurpose"]]]])

slots.attributionText = Slot(uri=SPDX_SOFTWARE.attributionText, name="attributionText", curie=SPDX_SOFTWARE.curie('attributionText'),
                   model_uri=SPDX_LINKML.attributionText, domain=None, range=Optional[Union[str, list[str]]])

slots.byteRange = Slot(uri=SPDX_SOFTWARE.byteRange, name="byteRange", curie=SPDX_SOFTWARE.curie('byteRange'),
                   model_uri=SPDX_LINKML.byteRange, domain=None, range=Optional[Union[dict, PositiveIntegerRange]])

slots.contentIdentifier = Slot(uri=SPDX_SOFTWARE.contentIdentifier, name="contentIdentifier", curie=SPDX_SOFTWARE.curie('contentIdentifier'),
                   model_uri=SPDX_LINKML.contentIdentifier, domain=None, range=Optional[Union[Union[dict, ContentIdentifier], list[Union[dict, ContentIdentifier]]]])

slots.contentIdentifierType = Slot(uri=SPDX_SOFTWARE.contentIdentifierType, name="contentIdentifierType", curie=SPDX_SOFTWARE.curie('contentIdentifierType'),
                   model_uri=SPDX_LINKML.contentIdentifierType, domain=None, range=Union[str, "ContentIdentifierType"])

slots.contentIdentifierValue = Slot(uri=SPDX_SOFTWARE.contentIdentifierValue, name="contentIdentifierValue", curie=SPDX_SOFTWARE.curie('contentIdentifierValue'),
                   model_uri=SPDX_LINKML.contentIdentifierValue, domain=None, range=Union[str, URI])

slots.copyrightText = Slot(uri=SPDX_SOFTWARE.copyrightText, name="copyrightText", curie=SPDX_SOFTWARE.curie('copyrightText'),
                   model_uri=SPDX_LINKML.copyrightText, domain=None, range=Optional[str])

slots.downloadLocation = Slot(uri=SPDX_SOFTWARE.downloadLocation, name="downloadLocation", curie=SPDX_SOFTWARE.curie('downloadLocation'),
                   model_uri=SPDX_LINKML.downloadLocation, domain=None, range=Optional[Union[str, URI]])

slots.fileKind = Slot(uri=SPDX_SOFTWARE.fileKind, name="fileKind", curie=SPDX_SOFTWARE.curie('fileKind'),
                   model_uri=SPDX_LINKML.fileKind, domain=None, range=Optional[Union[str, "FileKindType"]])

slots.homePage = Slot(uri=SPDX_SOFTWARE.homePage, name="homePage", curie=SPDX_SOFTWARE.curie('homePage'),
                   model_uri=SPDX_LINKML.homePage, domain=None, range=Optional[Union[str, URI]])

slots.lineRange = Slot(uri=SPDX_SOFTWARE.lineRange, name="lineRange", curie=SPDX_SOFTWARE.curie('lineRange'),
                   model_uri=SPDX_LINKML.lineRange, domain=None, range=Optional[Union[dict, PositiveIntegerRange]])

slots.packageUrl = Slot(uri=SPDX_SOFTWARE.packageUrl, name="packageUrl", curie=SPDX_SOFTWARE.curie('packageUrl'),
                   model_uri=SPDX_LINKML.packageUrl, domain=None, range=Optional[Union[str, URI]])

slots.packageVersion = Slot(uri=SPDX_SOFTWARE.packageVersion, name="packageVersion", curie=SPDX_SOFTWARE.curie('packageVersion'),
                   model_uri=SPDX_LINKML.packageVersion, domain=None, range=Optional[str])

slots.primaryPurpose = Slot(uri=SPDX_SOFTWARE.primaryPurpose, name="primaryPurpose", curie=SPDX_SOFTWARE.curie('primaryPurpose'),
                   model_uri=SPDX_LINKML.primaryPurpose, domain=None, range=Optional[Union[str, "SoftwarePurpose"]])

slots.sbomType = Slot(uri=SPDX_SOFTWARE.sbomType, name="sbomType", curie=SPDX_SOFTWARE.curie('sbomType'),
                   model_uri=SPDX_LINKML.sbomType, domain=None, range=Optional[Union[Union[str, "SbomType"], list[Union[str, "SbomType"]]]])

slots.snippetFromFile = Slot(uri=SPDX_SOFTWARE.snippetFromFile, name="snippetFromFile", curie=SPDX_SOFTWARE.curie('snippetFromFile'),
                   model_uri=SPDX_LINKML.snippetFromFile, domain=None, range=Union[str, FileSpdxId])

slots.sourceInfo = Slot(uri=SPDX_SOFTWARE.sourceInfo, name="sourceInfo", curie=SPDX_SOFTWARE.curie('sourceInfo'),
                   model_uri=SPDX_LINKML.sourceInfo, domain=None, range=Optional[str])

slots.autonomyType = Slot(uri=SPDX_AI.autonomyType, name="autonomyType", curie=SPDX_AI.curie('autonomyType'),
                   model_uri=SPDX_LINKML.autonomyType, domain=None, range=Optional[Union[str, "PresenceType"]])

slots.domain = Slot(uri=SPDX_AI.domain, name="domain", curie=SPDX_AI.curie('domain'),
                   model_uri=SPDX_LINKML.domain, domain=None, range=Optional[Union[str, list[str]]])

slots.energyConsumption = Slot(uri=SPDX_AI.energyConsumption, name="energyConsumption", curie=SPDX_AI.curie('energyConsumption'),
                   model_uri=SPDX_LINKML.energyConsumption, domain=None, range=Optional[Union[dict, EnergyConsumption]])

slots.energyQuantity = Slot(uri=SPDX_AI.energyQuantity, name="energyQuantity", curie=SPDX_AI.curie('energyQuantity'),
                   model_uri=SPDX_LINKML.energyQuantity, domain=None, range=Decimal)

slots.energyUnit = Slot(uri=SPDX_AI.energyUnit, name="energyUnit", curie=SPDX_AI.curie('energyUnit'),
                   model_uri=SPDX_LINKML.energyUnit, domain=None, range=Union[str, "EnergyUnitType"])

slots.finetuningEnergyConsumption = Slot(uri=SPDX_AI.finetuningEnergyConsumption, name="finetuningEnergyConsumption", curie=SPDX_AI.curie('finetuningEnergyConsumption'),
                   model_uri=SPDX_LINKML.finetuningEnergyConsumption, domain=None, range=Optional[Union[Union[dict, EnergyConsumptionDescription], list[Union[dict, EnergyConsumptionDescription]]]])

slots.hyperparameter = Slot(uri=SPDX_AI.hyperparameter, name="hyperparameter", curie=SPDX_AI.curie('hyperparameter'),
                   model_uri=SPDX_LINKML.hyperparameter, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.inferenceEnergyConsumption = Slot(uri=SPDX_AI.inferenceEnergyConsumption, name="inferenceEnergyConsumption", curie=SPDX_AI.curie('inferenceEnergyConsumption'),
                   model_uri=SPDX_LINKML.inferenceEnergyConsumption, domain=None, range=Optional[Union[Union[dict, EnergyConsumptionDescription], list[Union[dict, EnergyConsumptionDescription]]]])

slots.informationAboutApplication = Slot(uri=SPDX_AI.informationAboutApplication, name="informationAboutApplication", curie=SPDX_AI.curie('informationAboutApplication'),
                   model_uri=SPDX_LINKML.informationAboutApplication, domain=None, range=Optional[str])

slots.informationAboutTraining = Slot(uri=SPDX_AI.informationAboutTraining, name="informationAboutTraining", curie=SPDX_AI.curie('informationAboutTraining'),
                   model_uri=SPDX_LINKML.informationAboutTraining, domain=None, range=Optional[str])

slots.limitation = Slot(uri=SPDX_AI.limitation, name="limitation", curie=SPDX_AI.curie('limitation'),
                   model_uri=SPDX_LINKML.limitation, domain=None, range=Optional[str])

slots.metric = Slot(uri=SPDX_AI.metric, name="metric", curie=SPDX_AI.curie('metric'),
                   model_uri=SPDX_LINKML.metric, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.metricDecisionThreshold = Slot(uri=SPDX_AI.metricDecisionThreshold, name="metricDecisionThreshold", curie=SPDX_AI.curie('metricDecisionThreshold'),
                   model_uri=SPDX_LINKML.metricDecisionThreshold, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.modelDataPreprocessing = Slot(uri=SPDX_AI.modelDataPreprocessing, name="modelDataPreprocessing", curie=SPDX_AI.curie('modelDataPreprocessing'),
                   model_uri=SPDX_LINKML.modelDataPreprocessing, domain=None, range=Optional[Union[str, list[str]]])

slots.modelExplainability = Slot(uri=SPDX_AI.modelExplainability, name="modelExplainability", curie=SPDX_AI.curie('modelExplainability'),
                   model_uri=SPDX_LINKML.modelExplainability, domain=None, range=Optional[Union[str, list[str]]])

slots.safetyRiskAssessment = Slot(uri=SPDX_AI.safetyRiskAssessment, name="safetyRiskAssessment", curie=SPDX_AI.curie('safetyRiskAssessment'),
                   model_uri=SPDX_LINKML.safetyRiskAssessment, domain=None, range=Optional[Union[str, "SafetyRiskAssessmentType"]])

slots.standardCompliance = Slot(uri=SPDX_AI.standardCompliance, name="standardCompliance", curie=SPDX_AI.curie('standardCompliance'),
                   model_uri=SPDX_LINKML.standardCompliance, domain=None, range=Optional[Union[str, list[str]]])

slots.trainingEnergyConsumption = Slot(uri=SPDX_AI.trainingEnergyConsumption, name="trainingEnergyConsumption", curie=SPDX_AI.curie('trainingEnergyConsumption'),
                   model_uri=SPDX_LINKML.trainingEnergyConsumption, domain=None, range=Optional[Union[Union[dict, EnergyConsumptionDescription], list[Union[dict, EnergyConsumptionDescription]]]])

slots.typeOfModel = Slot(uri=SPDX_AI.typeOfModel, name="typeOfModel", curie=SPDX_AI.curie('typeOfModel'),
                   model_uri=SPDX_LINKML.typeOfModel, domain=None, range=Optional[Union[str, list[str]]])

slots.useSensitivePersonalInformation = Slot(uri=SPDX_AI.useSensitivePersonalInformation, name="useSensitivePersonalInformation", curie=SPDX_AI.curie('useSensitivePersonalInformation'),
                   model_uri=SPDX_LINKML.useSensitivePersonalInformation, domain=None, range=Optional[Union[str, "PresenceType"]])

slots.anonymizationMethodUsed = Slot(uri=SPDX_DATASET.anonymizationMethodUsed, name="anonymizationMethodUsed", curie=SPDX_DATASET.curie('anonymizationMethodUsed'),
                   model_uri=SPDX_LINKML.anonymizationMethodUsed, domain=None, range=Optional[Union[str, list[str]]])

slots.confidentialityLevel = Slot(uri=SPDX_DATASET.confidentialityLevel, name="confidentialityLevel", curie=SPDX_DATASET.curie('confidentialityLevel'),
                   model_uri=SPDX_LINKML.confidentialityLevel, domain=None, range=Optional[Union[str, "ConfidentialityLevelType"]])

slots.dataCollectionProcess = Slot(uri=SPDX_DATASET.dataCollectionProcess, name="dataCollectionProcess", curie=SPDX_DATASET.curie('dataCollectionProcess'),
                   model_uri=SPDX_LINKML.dataCollectionProcess, domain=None, range=Optional[str])

slots.dataPreprocessing = Slot(uri=SPDX_DATASET.dataPreprocessing, name="dataPreprocessing", curie=SPDX_DATASET.curie('dataPreprocessing'),
                   model_uri=SPDX_LINKML.dataPreprocessing, domain=None, range=Optional[Union[str, list[str]]])

slots.datasetAvailability = Slot(uri=SPDX_DATASET.datasetAvailability, name="datasetAvailability", curie=SPDX_DATASET.curie('datasetAvailability'),
                   model_uri=SPDX_LINKML.datasetAvailability, domain=None, range=Optional[Union[str, "DatasetAvailabilityType"]])

slots.datasetNoise = Slot(uri=SPDX_DATASET.datasetNoise, name="datasetNoise", curie=SPDX_DATASET.curie('datasetNoise'),
                   model_uri=SPDX_LINKML.datasetNoise, domain=None, range=Optional[str])

slots.datasetSize = Slot(uri=SPDX_DATASET.datasetSize, name="datasetSize", curie=SPDX_DATASET.curie('datasetSize'),
                   model_uri=SPDX_LINKML.datasetSize, domain=None, range=Optional[Union[int, NonNegativeInteger]])

slots.datasetType = Slot(uri=SPDX_DATASET.datasetType, name="datasetType", curie=SPDX_DATASET.curie('datasetType'),
                   model_uri=SPDX_LINKML.datasetType, domain=None, range=Union[Union[str, "DatasetType"], list[Union[str, "DatasetType"]]])

slots.datasetUpdateMechanism = Slot(uri=SPDX_DATASET.datasetUpdateMechanism, name="datasetUpdateMechanism", curie=SPDX_DATASET.curie('datasetUpdateMechanism'),
                   model_uri=SPDX_LINKML.datasetUpdateMechanism, domain=None, range=Optional[str])

slots.hasSensitivePersonalInformation = Slot(uri=SPDX_DATASET.hasSensitivePersonalInformation, name="hasSensitivePersonalInformation", curie=SPDX_DATASET.curie('hasSensitivePersonalInformation'),
                   model_uri=SPDX_LINKML.hasSensitivePersonalInformation, domain=None, range=Optional[Union[str, "PresenceType"]])

slots.intendedUse = Slot(uri=SPDX_DATASET.intendedUse, name="intendedUse", curie=SPDX_DATASET.curie('intendedUse'),
                   model_uri=SPDX_LINKML.intendedUse, domain=None, range=Optional[str])

slots.knownBias = Slot(uri=SPDX_DATASET.knownBias, name="knownBias", curie=SPDX_DATASET.curie('knownBias'),
                   model_uri=SPDX_LINKML.knownBias, domain=None, range=Optional[Union[str, list[str]]])

slots.sensor = Slot(uri=SPDX_DATASET.sensor, name="sensor", curie=SPDX_DATASET.curie('sensor'),
                   model_uri=SPDX_LINKML.sensor, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.additionText = Slot(uri=SPDX_EXPANDED_LICENSING.additionText, name="additionText", curie=SPDX_EXPANDED_LICENSING.curie('additionText'),
                   model_uri=SPDX_LINKML.additionText, domain=None, range=str)

slots.deprecatedVersion = Slot(uri=SPDX_EXPANDED_LICENSING.deprecatedVersion, name="deprecatedVersion", curie=SPDX_EXPANDED_LICENSING.curie('deprecatedVersion'),
                   model_uri=SPDX_LINKML.deprecatedVersion, domain=None, range=Optional[str])

slots.isDeprecatedAdditionId = Slot(uri=SPDX_EXPANDED_LICENSING.isDeprecatedAdditionId, name="isDeprecatedAdditionId", curie=SPDX_EXPANDED_LICENSING.curie('isDeprecatedAdditionId'),
                   model_uri=SPDX_LINKML.isDeprecatedAdditionId, domain=None, range=Optional[Union[bool, Bool]])

slots.isDeprecatedLicenseId = Slot(uri=SPDX_EXPANDED_LICENSING.isDeprecatedLicenseId, name="isDeprecatedLicenseId", curie=SPDX_EXPANDED_LICENSING.curie('isDeprecatedLicenseId'),
                   model_uri=SPDX_LINKML.isDeprecatedLicenseId, domain=None, range=Optional[Union[bool, Bool]])

slots.isFsfLibre = Slot(uri=SPDX_EXPANDED_LICENSING.isFsfLibre, name="isFsfLibre", curie=SPDX_EXPANDED_LICENSING.curie('isFsfLibre'),
                   model_uri=SPDX_LINKML.isFsfLibre, domain=None, range=Optional[Union[bool, Bool]])

slots.isOsiApproved = Slot(uri=SPDX_EXPANDED_LICENSING.isOsiApproved, name="isOsiApproved", curie=SPDX_EXPANDED_LICENSING.curie('isOsiApproved'),
                   model_uri=SPDX_LINKML.isOsiApproved, domain=None, range=Optional[Union[bool, Bool]])

slots.licenseXml = Slot(uri=SPDX_EXPANDED_LICENSING.licenseXml, name="licenseXml", curie=SPDX_EXPANDED_LICENSING.curie('licenseXml'),
                   model_uri=SPDX_LINKML.licenseXml, domain=None, range=Optional[str])

slots.listVersionAdded = Slot(uri=SPDX_EXPANDED_LICENSING.listVersionAdded, name="listVersionAdded", curie=SPDX_EXPANDED_LICENSING.curie('listVersionAdded'),
                   model_uri=SPDX_LINKML.listVersionAdded, domain=None, range=Optional[str])

slots.member = Slot(uri=SPDX_EXPANDED_LICENSING.member, name="member", curie=SPDX_EXPANDED_LICENSING.curie('member'),
                   model_uri=SPDX_LINKML.member, domain=None, range=Union[Union[str, AnyLicenseInfoSpdxId], list[Union[str, AnyLicenseInfoSpdxId]]])

slots.obsoletedBy = Slot(uri=SPDX_EXPANDED_LICENSING.obsoletedBy, name="obsoletedBy", curie=SPDX_EXPANDED_LICENSING.curie('obsoletedBy'),
                   model_uri=SPDX_LINKML.obsoletedBy, domain=None, range=Optional[str])

slots.seeAlso = Slot(uri=SPDX_EXPANDED_LICENSING.seeAlso, name="seeAlso", curie=SPDX_EXPANDED_LICENSING.curie('seeAlso'),
                   model_uri=SPDX_LINKML.seeAlso, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.standardAdditionTemplate = Slot(uri=SPDX_EXPANDED_LICENSING.standardAdditionTemplate, name="standardAdditionTemplate", curie=SPDX_EXPANDED_LICENSING.curie('standardAdditionTemplate'),
                   model_uri=SPDX_LINKML.standardAdditionTemplate, domain=None, range=Optional[str])

slots.standardLicenseHeader = Slot(uri=SPDX_EXPANDED_LICENSING.standardLicenseHeader, name="standardLicenseHeader", curie=SPDX_EXPANDED_LICENSING.curie('standardLicenseHeader'),
                   model_uri=SPDX_LINKML.standardLicenseHeader, domain=None, range=Optional[str])

slots.standardLicenseTemplate = Slot(uri=SPDX_EXPANDED_LICENSING.standardLicenseTemplate, name="standardLicenseTemplate", curie=SPDX_EXPANDED_LICENSING.curie('standardLicenseTemplate'),
                   model_uri=SPDX_LINKML.standardLicenseTemplate, domain=None, range=Optional[str])

slots.subjectAddition = Slot(uri=SPDX_EXPANDED_LICENSING.subjectAddition, name="subjectAddition", curie=SPDX_EXPANDED_LICENSING.curie('subjectAddition'),
                   model_uri=SPDX_LINKML.subjectAddition, domain=None, range=Union[str, LicenseAdditionSpdxId])

slots.subjectExtendableLicense = Slot(uri=SPDX_EXPANDED_LICENSING.subjectExtendableLicense, name="subjectExtendableLicense", curie=SPDX_EXPANDED_LICENSING.curie('subjectExtendableLicense'),
                   model_uri=SPDX_LINKML.subjectExtendableLicense, domain=None, range=Union[str, ExtendableLicenseSpdxId])

slots.subjectLicense = Slot(uri=SPDX_EXPANDED_LICENSING.subjectLicense, name="subjectLicense", curie=SPDX_EXPANDED_LICENSING.curie('subjectLicense'),
                   model_uri=SPDX_LINKML.subjectLicense, domain=None, range=Union[str, LicenseSpdxId])

slots.actionStatement = Slot(uri=SPDX_SECURITY.actionStatement, name="actionStatement", curie=SPDX_SECURITY.curie('actionStatement'),
                   model_uri=SPDX_LINKML.actionStatement, domain=None, range=str)

slots.actionStatementTime = Slot(uri=SPDX_SECURITY.actionStatementTime, name="actionStatementTime", curie=SPDX_SECURITY.curie('actionStatementTime'),
                   model_uri=SPDX_LINKML.actionStatementTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.assessedElement = Slot(uri=SPDX_SECURITY.assessedElement, name="assessedElement", curie=SPDX_SECURITY.curie('assessedElement'),
                   model_uri=SPDX_LINKML.assessedElement, domain=None, range=Optional[Union[str, SoftwareArtifactSpdxId]])

slots.catalogType = Slot(uri=SPDX_SECURITY.catalogType, name="catalogType", curie=SPDX_SECURITY.curie('catalogType'),
                   model_uri=SPDX_LINKML.catalogType, domain=None, range=Union[str, "ExploitCatalogType"])

slots.decisionType = Slot(uri=SPDX_SECURITY.decisionType, name="decisionType", curie=SPDX_SECURITY.curie('decisionType'),
                   model_uri=SPDX_LINKML.decisionType, domain=None, range=Union[str, "SsvcDecisionType"])

slots.exploited = Slot(uri=SPDX_SECURITY.exploited, name="exploited", curie=SPDX_SECURITY.curie('exploited'),
                   model_uri=SPDX_LINKML.exploited, domain=None, range=Union[bool, Bool])

slots.impactStatement = Slot(uri=SPDX_SECURITY.impactStatement, name="impactStatement", curie=SPDX_SECURITY.curie('impactStatement'),
                   model_uri=SPDX_LINKML.impactStatement, domain=None, range=Optional[str])

slots.impactStatementTime = Slot(uri=SPDX_SECURITY.impactStatementTime, name="impactStatementTime", curie=SPDX_SECURITY.curie('impactStatementTime'),
                   model_uri=SPDX_LINKML.impactStatementTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.justificationType = Slot(uri=SPDX_SECURITY.justificationType, name="justificationType", curie=SPDX_SECURITY.curie('justificationType'),
                   model_uri=SPDX_LINKML.justificationType, domain=None, range=Optional[Union[str, "VexJustificationType"]])

slots.modifiedTime = Slot(uri=SPDX_SECURITY.modifiedTime, name="modifiedTime", curie=SPDX_SECURITY.curie('modifiedTime'),
                   model_uri=SPDX_LINKML.modifiedTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.percentile = Slot(uri=SPDX_SECURITY.percentile, name="percentile", curie=SPDX_SECURITY.curie('percentile'),
                   model_uri=SPDX_LINKML.percentile, domain=None, range=Decimal)

slots.probability = Slot(uri=SPDX_SECURITY.probability, name="probability", curie=SPDX_SECURITY.curie('probability'),
                   model_uri=SPDX_LINKML.probability, domain=None, range=Decimal)

slots.publishedTime = Slot(uri=SPDX_SECURITY.publishedTime, name="publishedTime", curie=SPDX_SECURITY.curie('publishedTime'),
                   model_uri=SPDX_LINKML.publishedTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.score = Slot(uri=SPDX_SECURITY.score, name="score", curie=SPDX_SECURITY.curie('score'),
                   model_uri=SPDX_LINKML.score, domain=None, range=Decimal)

slots.security_locator = Slot(uri=SPDX_SECURITY.locator, name="security_locator", curie=SPDX_SECURITY.curie('locator'),
                   model_uri=SPDX_LINKML.security_locator, domain=None, range=Union[str, URI])

slots.severity = Slot(uri=SPDX_SECURITY.severity, name="severity", curie=SPDX_SECURITY.curie('severity'),
                   model_uri=SPDX_LINKML.severity, domain=None, range=Union[str, "CvssSeverityType"])

slots.statusNotes = Slot(uri=SPDX_SECURITY.statusNotes, name="statusNotes", curie=SPDX_SECURITY.curie('statusNotes'),
                   model_uri=SPDX_LINKML.statusNotes, domain=None, range=Optional[str])

slots.vectorString = Slot(uri=SPDX_SECURITY.vectorString, name="vectorString", curie=SPDX_SECURITY.curie('vectorString'),
                   model_uri=SPDX_LINKML.vectorString, domain=None, range=str)

slots.vexVersion = Slot(uri=SPDX_SECURITY.vexVersion, name="vexVersion", curie=SPDX_SECURITY.curie('vexVersion'),
                   model_uri=SPDX_LINKML.vexVersion, domain=None, range=Optional[str])

slots.withdrawnTime = Slot(uri=SPDX_SECURITY.withdrawnTime, name="withdrawnTime", curie=SPDX_SECURITY.curie('withdrawnTime'),
                   model_uri=SPDX_LINKML.withdrawnTime, domain=None, range=Optional[Union[str, DateTimeStamp]])

slots.element__spdxId = Slot(uri=SPDX_LINKML.spdxId, name="element__spdxId", curie=SPDX_LINKML.curie('spdxId'),
                   model_uri=SPDX_LINKML.element__spdxId, domain=None, range=URIRef)
