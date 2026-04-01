# Auto generated from spdx.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-01T16:18:47
# Schema: spdx
#
# id: https://w3id.org/lmodel/spdx
# description: System Package Data Exchange (SPDX), LinkML schema
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

from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI, XSDDateTime

metamodel_version = "1.7.0"
version = "3.0.1"

# Namespaces
AI = CurieNamespace('ai', 'https://spdx.org/rdf/3.0.1/terms/AI/')
BUILD = CurieNamespace('build', 'https://spdx.org/rdf/3.0.1/terms/Build/')
CORE = CurieNamespace('core', 'https://spdx.org/rdf/3.0.1/terms/Core/')
DATASET = CurieNamespace('dataset', 'https://spdx.org/rdf/3.0.1/terms/Dataset/')
EXPANDEDLICENSING = CurieNamespace('expandedlicensing', 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/')
EXTENSION = CurieNamespace('extension', 'https://spdx.org/rdf/3.0.1/terms/Extension/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SECURITY = CurieNamespace('security', 'https://spdx.org/rdf/3.0.1/terms/Security/')
SIMPLELICENSING = CurieNamespace('simplelicensing', 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/')
SOFTWARE = CurieNamespace('software', 'https://spdx.org/rdf/3.0.1/terms/Software/')
SPDX = CurieNamespace('spdx', 'https://spdx.org/rdf/3.0.1/terms/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SPDX


# Types

# Class references



@dataclass(repr=False)
class EnergyConsumption(YAMLRoot):
    """
    A class for describing the energy consumption incurred by an AI model in
    different stages of its lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["EnergyConsumption"]
    class_class_curie: ClassVar[str] = "ai:EnergyConsumption"
    class_name: ClassVar[str] = "EnergyConsumption"
    class_model_uri: ClassVar[URIRef] = SPDX.EnergyConsumption

    finetuningEnergyConsumption: Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]] = empty_list()
    inferenceEnergyConsumption: Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]] = empty_list()
    trainingEnergyConsumption: Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="finetuningEnergyConsumption", slot_type=EnergyConsumptionDescription, key_name="energyQuantity", keyed=False)

        self._normalize_inlined_as_list(slot_name="inferenceEnergyConsumption", slot_type=EnergyConsumptionDescription, key_name="energyQuantity", keyed=False)

        self._normalize_inlined_as_list(slot_name="trainingEnergyConsumption", slot_type=EnergyConsumptionDescription, key_name="energyQuantity", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnergyConsumptionDescription(YAMLRoot):
    """
    The class that helps note down the quantity of energy consumption and the unit
    used for measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["EnergyConsumptionDescription"]
    class_class_curie: ClassVar[str] = "ai:EnergyConsumptionDescription"
    class_name: ClassVar[str] = "EnergyConsumptionDescription"
    class_model_uri: ClassVar[URIRef] = SPDX.EnergyConsumptionDescription

    energyQuantity: Decimal = None
    energyUnit: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.energyQuantity):
            self.MissingRequiredField("energyQuantity")
        if not isinstance(self.energyQuantity, Decimal):
            self.energyQuantity = Decimal(self.energyQuantity)

        if self._is_empty(self.energyUnit):
            self.MissingRequiredField("energyUnit")
        if not isinstance(self.energyUnit, str):
            self.energyUnit = str(self.energyUnit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreationInfo(YAMLRoot):
    """
    Provides information about the creation of the Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["CreationInfo"]
    class_class_curie: ClassVar[str] = "core:CreationInfo"
    class_name: ClassVar[str] = "CreationInfo"
    class_model_uri: ClassVar[URIRef] = SPDX.CreationInfo

    createdBy: Union[Union[dict, "Agent"], list[Union[dict, "Agent"]]] = None
    created: Union[str, XSDDateTime] = None
    specVersion: str = None
    createdUsing: Optional[Union[Union[dict, "Tool"], list[Union[dict, "Tool"]]]] = empty_list()
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.createdBy):
            self.MissingRequiredField("createdBy")
        if not isinstance(self.createdBy, list):
            self.createdBy = [self.createdBy] if self.createdBy is not None else []
        self.createdBy = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.createdBy]

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, XSDDateTime):
            self.created = XSDDateTime(self.created)

        if self._is_empty(self.specVersion):
            self.MissingRequiredField("specVersion")
        if not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.createdUsing, list):
            self.createdUsing = [self.createdUsing] if self.createdUsing is not None else []
        self.createdUsing = [v if isinstance(v, Tool) else Tool(**as_dict(v)) for v in self.createdUsing]

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DictionaryEntry(YAMLRoot):
    """
    A key with an associated value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["DictionaryEntry"]
    class_class_curie: ClassVar[str] = "core:DictionaryEntry"
    class_name: ClassVar[str] = "DictionaryEntry"
    class_model_uri: ClassVar[URIRef] = SPDX.DictionaryEntry

    key: str = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Element(YAMLRoot):
    """
    Base domain class from which all other SPDX-3.0 domain classes derive.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Element"]
    class_class_curie: ClassVar[str] = "core:Element"
    class_name: ClassVar[str] = "Element"
    class_model_uri: ClassVar[URIRef] = SPDX.Element

    creationInfo: Union[dict, CreationInfo] = None
    externalIdentifier: Optional[Union[Union[dict, "ExternalIdentifier"], list[Union[dict, "ExternalIdentifier"]]]] = empty_list()
    extension: Optional[Union[Union[dict, "Extension"], list[Union[dict, "Extension"]]]] = empty_list()
    summary: Optional[str] = None
    description: Optional[str] = None
    comment: Optional[str] = None
    verifiedUsing: Optional[Union[Union[dict, "IntegrityMethod"], list[Union[dict, "IntegrityMethod"]]]] = empty_list()
    externalRef: Optional[Union[Union[dict, "ExternalRef"], list[Union[dict, "ExternalRef"]]]] = empty_list()
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.creationInfo):
            self.MissingRequiredField("creationInfo")
        if not isinstance(self.creationInfo, CreationInfo):
            self.creationInfo = CreationInfo(**as_dict(self.creationInfo))

        self._normalize_inlined_as_list(slot_name="externalIdentifier", slot_type=ExternalIdentifier, key_name="externalIdentifierType", keyed=False)

        if not isinstance(self.extension, list):
            self.extension = [self.extension] if self.extension is not None else []
        self.extension = [v if isinstance(v, Extension) else Extension(**as_dict(v)) for v in self.extension]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if not isinstance(self.verifiedUsing, list):
            self.verifiedUsing = [self.verifiedUsing] if self.verifiedUsing is not None else []
        self.verifiedUsing = [v if isinstance(v, IntegrityMethod) else IntegrityMethod(**as_dict(v)) for v in self.verifiedUsing]

        if not isinstance(self.externalRef, list):
            self.externalRef = [self.externalRef] if self.externalRef is not None else []
        self.externalRef = [v if isinstance(v, ExternalRef) else ExternalRef(**as_dict(v)) for v in self.externalRef]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Build(Element):
    """
    Class that describes a build instance of software/artifacts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BUILD["Build"]
    class_class_curie: ClassVar[str] = "build:Build"
    class_name: ClassVar[str] = "Build"
    class_model_uri: ClassVar[URIRef] = SPDX.Build

    creationInfo: Union[dict, CreationInfo] = None
    buildType: Union[str, URI] = None
    buildEndTime: Optional[Union[str, XSDDateTime]] = None
    buildId: Optional[str] = None
    configSourceDigest: Optional[Union[Union[dict, "Hash"], list[Union[dict, "Hash"]]]] = empty_list()
    buildStartTime: Optional[Union[str, XSDDateTime]] = None
    configSourceUri: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    parameter: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    configSourceEntrypoint: Optional[Union[str, list[str]]] = empty_list()
    environment: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.buildType):
            self.MissingRequiredField("buildType")
        if not isinstance(self.buildType, URI):
            self.buildType = URI(self.buildType)

        if self.buildEndTime is not None and not isinstance(self.buildEndTime, XSDDateTime):
            self.buildEndTime = XSDDateTime(self.buildEndTime)

        if self.buildId is not None and not isinstance(self.buildId, str):
            self.buildId = str(self.buildId)

        self._normalize_inlined_as_list(slot_name="configSourceDigest", slot_type=Hash, key_name="algorithm", keyed=False)

        if self.buildStartTime is not None and not isinstance(self.buildStartTime, XSDDateTime):
            self.buildStartTime = XSDDateTime(self.buildStartTime)

        if not isinstance(self.configSourceUri, list):
            self.configSourceUri = [self.configSourceUri] if self.configSourceUri is not None else []
        self.configSourceUri = [v if isinstance(v, URI) else URI(v) for v in self.configSourceUri]

        self._normalize_inlined_as_list(slot_name="parameter", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if not isinstance(self.configSourceEntrypoint, list):
            self.configSourceEntrypoint = [self.configSourceEntrypoint] if self.configSourceEntrypoint is not None else []
        self.configSourceEntrypoint = [v if isinstance(v, str) else str(v) for v in self.configSourceEntrypoint]

        self._normalize_inlined_as_list(slot_name="environment", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(Element):
    """
    Agent represents anything with the potential to act on a system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Agent"]
    class_class_curie: ClassVar[str] = "core:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = SPDX.Agent

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class Annotation(Element):
    """
    An assertion made in relation to one or more elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Annotation"]
    class_class_curie: ClassVar[str] = "core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = SPDX.Annotation

    creationInfo: Union[dict, CreationInfo] = None
    subject: Union[dict, Element] = None
    annotationType: str = None
    contentType: Optional[str] = None
    statement: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, Element):
            self.subject = Element(**as_dict(self.subject))

        if self._is_empty(self.annotationType):
            self.MissingRequiredField("annotationType")
        if not isinstance(self.annotationType, str):
            self.annotationType = str(self.annotationType)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        if self.statement is not None and not isinstance(self.statement, str):
            self.statement = str(self.statement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Artifact(Element):
    """
    A distinct article or unit within the digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Artifact"]
    class_class_curie: ClassVar[str] = "core:Artifact"
    class_name: ClassVar[str] = "Artifact"
    class_model_uri: ClassVar[URIRef] = SPDX.Artifact

    creationInfo: Union[dict, CreationInfo] = None
    standardName: Optional[Union[str, list[str]]] = empty_list()
    builtTime: Optional[Union[str, XSDDateTime]] = None
    validUntilTime: Optional[Union[str, XSDDateTime]] = None
    supportLevel: Optional[Union[Union[str, "SupportType"], list[Union[str, "SupportType"]]]] = empty_list()
    suppliedBy: Optional[Union[dict, Agent]] = None
    originatedBy: Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]] = empty_list()
    releaseTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.standardName, list):
            self.standardName = [self.standardName] if self.standardName is not None else []
        self.standardName = [v if isinstance(v, str) else str(v) for v in self.standardName]

        if self.builtTime is not None and not isinstance(self.builtTime, XSDDateTime):
            self.builtTime = XSDDateTime(self.builtTime)

        if self.validUntilTime is not None and not isinstance(self.validUntilTime, XSDDateTime):
            self.validUntilTime = XSDDateTime(self.validUntilTime)

        if not isinstance(self.supportLevel, list):
            self.supportLevel = [self.supportLevel] if self.supportLevel is not None else []
        self.supportLevel = [v if isinstance(v, SupportType) else SupportType(v) for v in self.supportLevel]

        if self.suppliedBy is not None and not isinstance(self.suppliedBy, Agent):
            self.suppliedBy = Agent(**as_dict(self.suppliedBy))

        if not isinstance(self.originatedBy, list):
            self.originatedBy = [self.originatedBy] if self.originatedBy is not None else []
        self.originatedBy = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.originatedBy]

        if self.releaseTime is not None and not isinstance(self.releaseTime, XSDDateTime):
            self.releaseTime = XSDDateTime(self.releaseTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementCollection(Element):
    """
    A collection of Elements, not necessarily with unifying context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["ElementCollection"]
    class_class_curie: ClassVar[str] = "core:ElementCollection"
    class_name: ClassVar[str] = "ElementCollection"
    class_model_uri: ClassVar[URIRef] = SPDX.ElementCollection

    creationInfo: Union[dict, CreationInfo] = None
    element: Optional[Union[Union[dict, Element], list[Union[dict, Element]]]] = empty_list()
    profileConformance: Optional[Union[Union[str, "ProfileIdentifierType"], list[Union[str, "ProfileIdentifierType"]]]] = empty_list()
    rootElement: Optional[Union[Union[dict, Element], list[Union[dict, Element]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, Element) else Element(**as_dict(v)) for v in self.element]

        if not isinstance(self.profileConformance, list):
            self.profileConformance = [self.profileConformance] if self.profileConformance is not None else []
        self.profileConformance = [v if isinstance(v, ProfileIdentifierType) else ProfileIdentifierType(v) for v in self.profileConformance]

        if not isinstance(self.rootElement, list):
            self.rootElement = [self.rootElement] if self.rootElement is not None else []
        self.rootElement = [v if isinstance(v, Element) else Element(**as_dict(v)) for v in self.rootElement]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bundle(ElementCollection):
    """
    A collection of Elements that have a shared context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Bundle"]
    class_class_curie: ClassVar[str] = "core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = SPDX.Bundle

    creationInfo: Union[dict, CreationInfo] = None
    context: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bom(Bundle):
    """
    A container for a grouping of SPDX-3.0 content characterizing details
    (provenence, composition, licensing, etc.) about a product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Bom"]
    class_class_curie: ClassVar[str] = "core:Bom"
    class_name: ClassVar[str] = "Bom"
    class_model_uri: ClassVar[URIRef] = SPDX.Bom

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class ExternalIdentifier(YAMLRoot):
    """
    A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an
    Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["ExternalIdentifier"]
    class_class_curie: ClassVar[str] = "core:ExternalIdentifier"
    class_name: ClassVar[str] = "ExternalIdentifier"
    class_model_uri: ClassVar[URIRef] = SPDX.ExternalIdentifier

    externalIdentifierType: str = None
    identifier: str = None
    identifierLocator: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    issuingAuthority: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.externalIdentifierType):
            self.MissingRequiredField("externalIdentifierType")
        if not isinstance(self.externalIdentifierType, str):
            self.externalIdentifierType = str(self.externalIdentifierType)

        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if not isinstance(self.identifierLocator, list):
            self.identifierLocator = [self.identifierLocator] if self.identifierLocator is not None else []
        self.identifierLocator = [v if isinstance(v, URI) else URI(v) for v in self.identifierLocator]

        if self.issuingAuthority is not None and not isinstance(self.issuingAuthority, str):
            self.issuingAuthority = str(self.issuingAuthority)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalMap(YAMLRoot):
    """
    A map of Element identifiers that are used within an SpdxDocument but defined
    external to that SpdxDocument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["ExternalMap"]
    class_class_curie: ClassVar[str] = "core:ExternalMap"
    class_name: ClassVar[str] = "ExternalMap"
    class_model_uri: ClassVar[URIRef] = SPDX.ExternalMap

    externalSpdxId: Union[str, URI] = None
    definingArtifact: Optional[Union[dict, Artifact]] = None
    locationHint: Optional[Union[str, URI]] = None
    verifiedUsing: Optional[Union[Union[dict, "IntegrityMethod"], list[Union[dict, "IntegrityMethod"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.externalSpdxId):
            self.MissingRequiredField("externalSpdxId")
        if not isinstance(self.externalSpdxId, URI):
            self.externalSpdxId = URI(self.externalSpdxId)

        if self.definingArtifact is not None and not isinstance(self.definingArtifact, Artifact):
            self.definingArtifact = Artifact(**as_dict(self.definingArtifact))

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

    class_class_uri: ClassVar[URIRef] = CORE["ExternalRef"]
    class_class_curie: ClassVar[str] = "core:ExternalRef"
    class_name: ClassVar[str] = "ExternalRef"
    class_model_uri: ClassVar[URIRef] = SPDX.ExternalRef

    core_locator: Optional[Union[str, list[str]]] = empty_list()
    externalRefType: Optional[str] = None
    comment: Optional[str] = None
    contentType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.core_locator, list):
            self.core_locator = [self.core_locator] if self.core_locator is not None else []
        self.core_locator = [v if isinstance(v, str) else str(v) for v in self.core_locator]

        if self.externalRefType is not None and not isinstance(self.externalRefType, str):
            self.externalRefType = str(self.externalRefType)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IndividualElement(Element):
    """
    A concrete subclass of Element used by Individuals in the
    Core profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["IndividualElement"]
    class_class_curie: ClassVar[str] = "core:IndividualElement"
    class_name: ClassVar[str] = "IndividualElement"
    class_model_uri: ClassVar[URIRef] = SPDX.IndividualElement

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class IntegrityMethod(YAMLRoot):
    """
    Provides an independently reproducible mechanism that permits verification of a specific Element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["IntegrityMethod"]
    class_class_curie: ClassVar[str] = "core:IntegrityMethod"
    class_name: ClassVar[str] = "IntegrityMethod"
    class_model_uri: ClassVar[URIRef] = SPDX.IntegrityMethod

    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hash(IntegrityMethod):
    """
    A mathematically calculated representation of a grouping of data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Hash"]
    class_class_curie: ClassVar[str] = "core:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = SPDX.Hash

    algorithm: str = None
    hashValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, str):
            self.hashValue = str(self.hashValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamespaceMap(YAMLRoot):
    """
    A mapping between prefixes and namespace partial URIs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["NamespaceMap"]
    class_class_curie: ClassVar[str] = "core:NamespaceMap"
    class_name: ClassVar[str] = "NamespaceMap"
    class_model_uri: ClassVar[URIRef] = SPDX.NamespaceMap

    prefix: str = None
    namespace: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prefix):
            self.MissingRequiredField("prefix")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self._is_empty(self.namespace):
            self.MissingRequiredField("namespace")
        if not isinstance(self.namespace, URI):
            self.namespace = URI(self.namespace)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(Agent):
    """
    A group of people who work together in an organized way for a shared purpose.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Organization"]
    class_class_curie: ClassVar[str] = "core:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = SPDX.Organization

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class PackageVerificationCode(IntegrityMethod):
    """
    An SPDX version 2.X compatible verification method for software packages.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["PackageVerificationCode"]
    class_class_curie: ClassVar[str] = "core:PackageVerificationCode"
    class_name: ClassVar[str] = "PackageVerificationCode"
    class_model_uri: ClassVar[URIRef] = SPDX.PackageVerificationCode

    hashValue: str = None
    algorithm: str = None
    packageVerificationCodeExcludedFile: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, str):
            self.hashValue = str(self.hashValue)

        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        if not isinstance(self.packageVerificationCodeExcludedFile, list):
            self.packageVerificationCodeExcludedFile = [self.packageVerificationCodeExcludedFile] if self.packageVerificationCodeExcludedFile is not None else []
        self.packageVerificationCodeExcludedFile = [v if isinstance(v, str) else str(v) for v in self.packageVerificationCodeExcludedFile]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(Agent):
    """
    An individual human being.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Person"]
    class_class_curie: ClassVar[str] = "core:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = SPDX.Person

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class PositiveIntegerRange(YAMLRoot):
    """
    A tuple of two positive integers that define a range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["PositiveIntegerRange"]
    class_class_curie: ClassVar[str] = "core:PositiveIntegerRange"
    class_name: ClassVar[str] = "PositiveIntegerRange"
    class_model_uri: ClassVar[URIRef] = SPDX.PositiveIntegerRange

    endIntegerRange: int = None
    beginIntegerRange: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.endIntegerRange):
            self.MissingRequiredField("endIntegerRange")
        if not isinstance(self.endIntegerRange, int):
            self.endIntegerRange = int(self.endIntegerRange)

        if self._is_empty(self.beginIntegerRange):
            self.MissingRequiredField("beginIntegerRange")
        if not isinstance(self.beginIntegerRange, int):
            self.beginIntegerRange = int(self.beginIntegerRange)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(Element):
    """
    Describes a relationship between one or more elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Relationship"]
    class_class_curie: ClassVar[str] = "core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = SPDX.Relationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    completeness: Optional[Union[str, "RelationshipCompleteness"]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.to):
            self.MissingRequiredField("to")
        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, Element) else Element(**as_dict(v)) for v in self.to]

        if self._is_empty(self.relationshipType):
            self.MissingRequiredField("relationshipType")
        if not isinstance(self.relationshipType, str):
            self.relationshipType = str(self.relationshipType)

        if self._is_empty(self.from):
            self.MissingRequiredField("from")
        if not isinstance(self.from, Element):
            self.from = Element(**as_dict(self.from))

        if self.completeness is not None and not isinstance(self.completeness, RelationshipCompleteness):
            self.completeness = RelationshipCompleteness(self.completeness)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LifecycleScopedRelationship(Relationship):
    """
    Provide context for a relationship that occurs in the lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["LifecycleScopedRelationship"]
    class_class_curie: ClassVar[str] = "core:LifecycleScopedRelationship"
    class_name: ClassVar[str] = "LifecycleScopedRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.LifecycleScopedRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    scope: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.scope is not None and not isinstance(self.scope, str):
            self.scope = str(self.scope)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoftwareAgent(Agent):
    """
    A software agent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["SoftwareAgent"]
    class_class_curie: ClassVar[str] = "core:SoftwareAgent"
    class_name: ClassVar[str] = "SoftwareAgent"
    class_model_uri: ClassVar[URIRef] = SPDX.SoftwareAgent

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class SpdxDocument(ElementCollection):
    """
    A collection of SPDX Elements that could potentially be serialized.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["SpdxDocument"]
    class_class_curie: ClassVar[str] = "core:SpdxDocument"
    class_name: ClassVar[str] = "SpdxDocument"
    class_model_uri: ClassVar[URIRef] = SPDX.SpdxDocument

    creationInfo: Union[dict, CreationInfo] = None
    namespaceMap: Optional[Union[Union[dict, NamespaceMap], list[Union[dict, NamespaceMap]]]] = empty_list()
    dataLicense: Optional[Union[dict, "AnyLicenseInfo"]] = None
    import: Optional[Union[Union[dict, ExternalMap], list[Union[dict, ExternalMap]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="namespaceMap", slot_type=NamespaceMap, key_name="prefix", keyed=False)

        if self.dataLicense is not None and not isinstance(self.dataLicense, AnyLicenseInfo):
            self.dataLicense = AnyLicenseInfo(**as_dict(self.dataLicense))

        self._normalize_inlined_as_list(slot_name="import", slot_type=ExternalMap, key_name="externalSpdxId", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tool(Element):
    """
    An element of hardware and/or software utilized to carry out a particular function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Tool"]
    class_class_curie: ClassVar[str] = "core:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = SPDX.Tool

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class LicenseAddition(Element):
    """
    Abstract class for additional text intended to be added to a License, but
    which is not itself a standalone License.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["LicenseAddition"]
    class_class_curie: ClassVar[str] = "expandedlicensing:LicenseAddition"
    class_name: ClassVar[str] = "LicenseAddition"
    class_model_uri: ClassVar[URIRef] = SPDX.LicenseAddition

    creationInfo: Union[dict, CreationInfo] = None
    additionText: str = None
    standardAdditionTemplate: Optional[str] = None
    seeAlso: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    obsoletedBy: Optional[str] = None
    licenseXml: Optional[str] = None
    isDeprecatedAdditionId: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.additionText):
            self.MissingRequiredField("additionText")
        if not isinstance(self.additionText, str):
            self.additionText = str(self.additionText)

        if self.standardAdditionTemplate is not None and not isinstance(self.standardAdditionTemplate, str):
            self.standardAdditionTemplate = str(self.standardAdditionTemplate)

        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso] if self.seeAlso is not None else []
        self.seeAlso = [v if isinstance(v, URI) else URI(v) for v in self.seeAlso]

        if self.obsoletedBy is not None and not isinstance(self.obsoletedBy, str):
            self.obsoletedBy = str(self.obsoletedBy)

        if self.licenseXml is not None and not isinstance(self.licenseXml, str):
            self.licenseXml = str(self.licenseXml)

        if self.isDeprecatedAdditionId is not None and not isinstance(self.isDeprecatedAdditionId, Bool):
            self.isDeprecatedAdditionId = Bool(self.isDeprecatedAdditionId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomLicenseAddition(LicenseAddition):
    """
    A license addition that is not listed on the SPDX Exceptions List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["CustomLicenseAddition"]
    class_class_curie: ClassVar[str] = "expandedlicensing:CustomLicenseAddition"
    class_name: ClassVar[str] = "CustomLicenseAddition"
    class_model_uri: ClassVar[URIRef] = SPDX.CustomLicenseAddition

    creationInfo: Union[dict, CreationInfo] = None
    additionText: str = None

@dataclass(repr=False)
class ListedLicenseException(LicenseAddition):
    """
    A license exception that is listed on the SPDX Exceptions list.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["ListedLicenseException"]
    class_class_curie: ClassVar[str] = "expandedlicensing:ListedLicenseException"
    class_name: ClassVar[str] = "ListedLicenseException"
    class_model_uri: ClassVar[URIRef] = SPDX.ListedLicenseException

    creationInfo: Union[dict, CreationInfo] = None
    additionText: str = None
    listVersionAdded: Optional[str] = None
    deprecatedVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.listVersionAdded is not None and not isinstance(self.listVersionAdded, str):
            self.listVersionAdded = str(self.listVersionAdded)

        if self.deprecatedVersion is not None and not isinstance(self.deprecatedVersion, str):
            self.deprecatedVersion = str(self.deprecatedVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CdxPropertyEntry(YAMLRoot):
    """
    A property name with an associated value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXTENSION["CdxPropertyEntry"]
    class_class_curie: ClassVar[str] = "extension:CdxPropertyEntry"
    class_name: ClassVar[str] = "CdxPropertyEntry"
    class_model_uri: ClassVar[URIRef] = SPDX.CdxPropertyEntry

    cdxPropName: str = None
    cdxPropValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cdxPropName):
            self.MissingRequiredField("cdxPropName")
        if not isinstance(self.cdxPropName, str):
            self.cdxPropName = str(self.cdxPropName)

        if self.cdxPropValue is not None and not isinstance(self.cdxPropValue, str):
            self.cdxPropValue = str(self.cdxPropValue)

        super().__post_init__(**kwargs)


class Extension(YAMLRoot):
    """
    A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXTENSION["Extension"]
    class_class_curie: ClassVar[str] = "extension:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = SPDX.Extension


@dataclass(repr=False)
class CdxPropertiesExtension(Extension):
    """
    A type of extension consisting of a list of name value pairs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXTENSION["CdxPropertiesExtension"]
    class_class_curie: ClassVar[str] = "extension:CdxPropertiesExtension"
    class_name: ClassVar[str] = "CdxPropertiesExtension"
    class_model_uri: ClassVar[URIRef] = SPDX.CdxPropertiesExtension

    cdxProperty: Union[Union[dict, CdxPropertyEntry], list[Union[dict, CdxPropertyEntry]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cdxProperty):
            self.MissingRequiredField("cdxProperty")
        self._normalize_inlined_as_list(slot_name="cdxProperty", slot_type=CdxPropertyEntry, key_name="cdxPropName", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VulnAssessmentRelationship(Relationship):
    """
    Abstract ancestor class for all vulnerability assessments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:VulnAssessmentRelationship"
    class_name: ClassVar[str] = "VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.VulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    withdrawnTime: Optional[Union[str, XSDDateTime]] = None
    publishedTime: Optional[Union[str, XSDDateTime]] = None
    assessedElement: Optional[Union[dict, "SoftwareArtifact"]] = None
    suppliedBy: Optional[Union[dict, Agent]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.withdrawnTime is not None and not isinstance(self.withdrawnTime, XSDDateTime):
            self.withdrawnTime = XSDDateTime(self.withdrawnTime)

        if self.publishedTime is not None and not isinstance(self.publishedTime, XSDDateTime):
            self.publishedTime = XSDDateTime(self.publishedTime)

        if self.assessedElement is not None and not isinstance(self.assessedElement, SoftwareArtifact):
            self.assessedElement = SoftwareArtifact(**as_dict(self.assessedElement))

        if self.suppliedBy is not None and not isinstance(self.suppliedBy, Agent):
            self.suppliedBy = Agent(**as_dict(self.suppliedBy))

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV2VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 2.0 assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["CvssV2VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:CvssV2VulnAssessmentRelationship"
    class_name: ClassVar[str] = "CvssV2VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.CvssV2VulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    vectorString: str = None
    score: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, Decimal):
            self.score = Decimal(self.score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV3VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 3 assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["CvssV3VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:CvssV3VulnAssessmentRelationship"
    class_name: ClassVar[str] = "CvssV3VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.CvssV3VulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    severity: Union[str, "CvssSeverityType"] = None
    vectorString: str = None
    score: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.severity):
            self.MissingRequiredField("severity")
        if not isinstance(self.severity, CvssSeverityType):
            self.severity = CvssSeverityType(self.severity)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, Decimal):
            self.score = Decimal(self.score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV4VulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides a CVSS version 4 assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["CvssV4VulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:CvssV4VulnAssessmentRelationship"
    class_name: ClassVar[str] = "CvssV4VulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.CvssV4VulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    severity: Union[str, "CvssSeverityType"] = None
    vectorString: str = None
    score: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.severity):
            self.MissingRequiredField("severity")
        if not isinstance(self.severity, CvssSeverityType):
            self.severity = CvssSeverityType(self.severity)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.score):
            self.MissingRequiredField("score")
        if not isinstance(self.score, Decimal):
            self.score = Decimal(self.score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EpssVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an EPSS assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["EpssVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:EpssVulnAssessmentRelationship"
    class_name: ClassVar[str] = "EpssVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.EpssVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    percentile: Decimal = None
    probability: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.percentile):
            self.MissingRequiredField("percentile")
        if not isinstance(self.percentile, Decimal):
            self.percentile = Decimal(self.percentile)

        if self._is_empty(self.probability):
            self.MissingRequiredField("probability")
        if not isinstance(self.probability, Decimal):
            self.probability = Decimal(self.probability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExploitCatalogVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an exploit assessment of a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["ExploitCatalogVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:ExploitCatalogVulnAssessmentRelationship"
    class_name: ClassVar[str] = "ExploitCatalogVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.ExploitCatalogVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    exploited: Union[bool, Bool] = None
    security_locator: Union[str, URI] = None
    catalogType: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.exploited):
            self.MissingRequiredField("exploited")
        if not isinstance(self.exploited, Bool):
            self.exploited = Bool(self.exploited)

        if self._is_empty(self.security_locator):
            self.MissingRequiredField("security_locator")
        if not isinstance(self.security_locator, URI):
            self.security_locator = URI(self.security_locator)

        if self._is_empty(self.catalogType):
            self.MissingRequiredField("catalogType")
        if not isinstance(self.catalogType, str):
            self.catalogType = str(self.catalogType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SsvcVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Provides an SSVC assessment for a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["SsvcVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:SsvcVulnAssessmentRelationship"
    class_name: ClassVar[str] = "SsvcVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.SsvcVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    decisionType: Union[str, "SsvcDecisionType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.decisionType):
            self.MissingRequiredField("decisionType")
        if not isinstance(self.decisionType, SsvcDecisionType):
            self.decisionType = SsvcDecisionType(self.decisionType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VexVulnAssessmentRelationship(VulnAssessmentRelationship):
    """
    Abstract ancestor class for all VEX relationships
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["VexVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:VexVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.VexVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    vexVersion: Optional[str] = None
    statusNotes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.vexVersion is not None and not isinstance(self.vexVersion, str):
            self.vexVersion = str(self.vexVersion)

        if self.statusNotes is not None and not isinstance(self.statusNotes, str):
            self.statusNotes = str(self.statusNotes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VexAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Connects a vulnerability and an element designating the element as a product
    affected by the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["VexAffectedVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:VexAffectedVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexAffectedVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.VexAffectedVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    actionStatement: str = None
    actionStatementTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.actionStatement):
            self.MissingRequiredField("actionStatement")
        if not isinstance(self.actionStatement, str):
            self.actionStatement = str(self.actionStatement)

        if self.actionStatementTime is not None and not isinstance(self.actionStatementTime, XSDDateTime):
            self.actionStatementTime = XSDDateTime(self.actionStatementTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VexFixedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and elements representing products (in the VEX sense) where
    a fix has been applied and are no longer affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["VexFixedVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:VexFixedVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexFixedVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.VexFixedVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None

@dataclass(repr=False)
class VexNotAffectedVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Links a vulnerability and one or more elements designating the latter as products
    not affected by the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["VexNotAffectedVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:VexNotAffectedVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexNotAffectedVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.VexNotAffectedVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None
    impactStatementTime: Optional[Union[str, XSDDateTime]] = None
    justificationType: Optional[Union[str, "VexJustificationType"]] = None
    impactStatement: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.impactStatementTime is not None and not isinstance(self.impactStatementTime, XSDDateTime):
            self.impactStatementTime = XSDDateTime(self.impactStatementTime)

        if self.justificationType is not None and not isinstance(self.justificationType, VexJustificationType):
            self.justificationType = VexJustificationType(self.justificationType)

        if self.impactStatement is not None and not isinstance(self.impactStatement, str):
            self.impactStatement = str(self.impactStatement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VexUnderInvestigationVulnAssessmentRelationship(VexVulnAssessmentRelationship):
    """
    Designates elements as products where the impact of a vulnerability is being
    investigated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["VexUnderInvestigationVulnAssessmentRelationship"]
    class_class_curie: ClassVar[str] = "security:VexUnderInvestigationVulnAssessmentRelationship"
    class_name: ClassVar[str] = "VexUnderInvestigationVulnAssessmentRelationship"
    class_model_uri: ClassVar[URIRef] = SPDX.VexUnderInvestigationVulnAssessmentRelationship

    creationInfo: Union[dict, CreationInfo] = None
    to: Union[Union[dict, Element], list[Union[dict, Element]]] = None
    relationshipType: str = None
    from: Union[dict, Element] = None

@dataclass(repr=False)
class Vulnerability(Artifact):
    """
    Specifies a vulnerability and its associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECURITY["Vulnerability"]
    class_class_curie: ClassVar[str] = "security:Vulnerability"
    class_name: ClassVar[str] = "Vulnerability"
    class_model_uri: ClassVar[URIRef] = SPDX.Vulnerability

    creationInfo: Union[dict, CreationInfo] = None
    withdrawnTime: Optional[Union[str, XSDDateTime]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    publishedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.withdrawnTime is not None and not isinstance(self.withdrawnTime, XSDDateTime):
            self.withdrawnTime = XSDDateTime(self.withdrawnTime)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.publishedTime is not None and not isinstance(self.publishedTime, XSDDateTime):
            self.publishedTime = XSDDateTime(self.publishedTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnyLicenseInfo(Element):
    """
    Abstract class representing a license combination consisting of one or more licenses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIMPLELICENSING["AnyLicenseInfo"]
    class_class_curie: ClassVar[str] = "simplelicensing:AnyLicenseInfo"
    class_name: ClassVar[str] = "AnyLicenseInfo"
    class_model_uri: ClassVar[URIRef] = SPDX.AnyLicenseInfo

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class ConjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information
    where all elements apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["ConjunctiveLicenseSet"]
    class_class_curie: ClassVar[str] = "expandedlicensing:ConjunctiveLicenseSet"
    class_name: ClassVar[str] = "ConjunctiveLicenseSet"
    class_model_uri: ClassVar[URIRef] = SPDX.ConjunctiveLicenseSet

    creationInfo: Union[dict, CreationInfo] = None
    member: Union[Union[dict, AnyLicenseInfo], list[Union[dict, AnyLicenseInfo]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.member):
            self.MissingRequiredField("member")
        if not isinstance(self.member, list):
            self.member = [self.member] if self.member is not None else []
        self.member = [v if isinstance(v, AnyLicenseInfo) else AnyLicenseInfo(**as_dict(v)) for v in self.member]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DisjunctiveLicenseSet(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a set of licensing information where
    only one of the elements applies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["DisjunctiveLicenseSet"]
    class_class_curie: ClassVar[str] = "expandedlicensing:DisjunctiveLicenseSet"
    class_name: ClassVar[str] = "DisjunctiveLicenseSet"
    class_model_uri: ClassVar[URIRef] = SPDX.DisjunctiveLicenseSet

    creationInfo: Union[dict, CreationInfo] = None
    member: Union[Union[dict, AnyLicenseInfo], list[Union[dict, AnyLicenseInfo]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.member):
            self.MissingRequiredField("member")
        if not isinstance(self.member, list):
            self.member = [self.member] if self.member is not None else []
        self.member = [v if isinstance(v, AnyLicenseInfo) else AnyLicenseInfo(**as_dict(v)) for v in self.member]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtendableLicense(AnyLicenseInfo):
    """
    Abstract class representing a License or an OrLaterOperator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["ExtendableLicense"]
    class_class_curie: ClassVar[str] = "expandedlicensing:ExtendableLicense"
    class_name: ClassVar[str] = "ExtendableLicense"
    class_model_uri: ClassVar[URIRef] = SPDX.ExtendableLicense

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class IndividualLicensingInfo(AnyLicenseInfo):
    """
    A concrete subclass of AnyLicenseInfo used by Individuals in the
    ExpandedLicensing profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["IndividualLicensingInfo"]
    class_class_curie: ClassVar[str] = "expandedlicensing:IndividualLicensingInfo"
    class_name: ClassVar[str] = "IndividualLicensingInfo"
    class_model_uri: ClassVar[URIRef] = SPDX.IndividualLicensingInfo

    creationInfo: Union[dict, CreationInfo] = None

@dataclass(repr=False)
class License(ExtendableLicense):
    """
    Abstract class for the portion of an AnyLicenseInfo representing a license.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["License"]
    class_class_curie: ClassVar[str] = "expandedlicensing:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = SPDX.License

    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None
    obsoletedBy: Optional[str] = None
    standardLicenseHeader: Optional[str] = None
    seeAlso: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    isFsfLibre: Optional[Union[bool, Bool]] = None
    isDeprecatedLicenseId: Optional[Union[bool, Bool]] = None
    isOsiApproved: Optional[Union[bool, Bool]] = None
    licenseXml: Optional[str] = None
    standardLicenseTemplate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.licenseText):
            self.MissingRequiredField("licenseText")
        if not isinstance(self.licenseText, str):
            self.licenseText = str(self.licenseText)

        if self.obsoletedBy is not None and not isinstance(self.obsoletedBy, str):
            self.obsoletedBy = str(self.obsoletedBy)

        if self.standardLicenseHeader is not None and not isinstance(self.standardLicenseHeader, str):
            self.standardLicenseHeader = str(self.standardLicenseHeader)

        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso] if self.seeAlso is not None else []
        self.seeAlso = [v if isinstance(v, URI) else URI(v) for v in self.seeAlso]

        if self.isFsfLibre is not None and not isinstance(self.isFsfLibre, Bool):
            self.isFsfLibre = Bool(self.isFsfLibre)

        if self.isDeprecatedLicenseId is not None and not isinstance(self.isDeprecatedLicenseId, Bool):
            self.isDeprecatedLicenseId = Bool(self.isDeprecatedLicenseId)

        if self.isOsiApproved is not None and not isinstance(self.isOsiApproved, Bool):
            self.isOsiApproved = Bool(self.isOsiApproved)

        if self.licenseXml is not None and not isinstance(self.licenseXml, str):
            self.licenseXml = str(self.licenseXml)

        if self.standardLicenseTemplate is not None and not isinstance(self.standardLicenseTemplate, str):
            self.standardLicenseTemplate = str(self.standardLicenseTemplate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomLicense(License):
    """
    A license that is not listed on the SPDX License List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["CustomLicense"]
    class_class_curie: ClassVar[str] = "expandedlicensing:CustomLicense"
    class_name: ClassVar[str] = "CustomLicense"
    class_model_uri: ClassVar[URIRef] = SPDX.CustomLicense

    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None

@dataclass(repr=False)
class ListedLicense(License):
    """
    A license that is listed on the SPDX License List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["ListedLicense"]
    class_class_curie: ClassVar[str] = "expandedlicensing:ListedLicense"
    class_name: ClassVar[str] = "ListedLicense"
    class_model_uri: ClassVar[URIRef] = SPDX.ListedLicense

    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None
    deprecatedVersion: Optional[str] = None
    listVersionAdded: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.deprecatedVersion is not None and not isinstance(self.deprecatedVersion, str):
            self.deprecatedVersion = str(self.deprecatedVersion)

        if self.listVersionAdded is not None and not isinstance(self.listVersionAdded, str):
            self.listVersionAdded = str(self.listVersionAdded)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrLaterOperator(ExtendableLicense):
    """
    Portion of an AnyLicenseInfo representing this version, or any later version,
    of the indicated License.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["OrLaterOperator"]
    class_class_curie: ClassVar[str] = "expandedlicensing:OrLaterOperator"
    class_name: ClassVar[str] = "OrLaterOperator"
    class_model_uri: ClassVar[URIRef] = SPDX.OrLaterOperator

    creationInfo: Union[dict, CreationInfo] = None
    subjectLicense: Union[dict, License] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subjectLicense):
            self.MissingRequiredField("subjectLicense")
        if not isinstance(self.subjectLicense, License):
            self.subjectLicense = License(**as_dict(self.subjectLicense))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithAdditionOperator(AnyLicenseInfo):
    """
    Portion of an AnyLicenseInfo representing a License which has additional
    text applied to it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPANDEDLICENSING["WithAdditionOperator"]
    class_class_curie: ClassVar[str] = "expandedlicensing:WithAdditionOperator"
    class_name: ClassVar[str] = "WithAdditionOperator"
    class_model_uri: ClassVar[URIRef] = SPDX.WithAdditionOperator

    creationInfo: Union[dict, CreationInfo] = None
    subjectExtendableLicense: Union[dict, ExtendableLicense] = None
    subjectAddition: Union[dict, LicenseAddition] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subjectExtendableLicense):
            self.MissingRequiredField("subjectExtendableLicense")
        if not isinstance(self.subjectExtendableLicense, ExtendableLicense):
            self.subjectExtendableLicense = ExtendableLicense(**as_dict(self.subjectExtendableLicense))

        if self._is_empty(self.subjectAddition):
            self.MissingRequiredField("subjectAddition")
        if not isinstance(self.subjectAddition, LicenseAddition):
            self.subjectAddition = LicenseAddition(**as_dict(self.subjectAddition))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LicenseExpression(AnyLicenseInfo):
    """
    An SPDX Element containing an SPDX license expression string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIMPLELICENSING["LicenseExpression"]
    class_class_curie: ClassVar[str] = "simplelicensing:LicenseExpression"
    class_name: ClassVar[str] = "LicenseExpression"
    class_model_uri: ClassVar[URIRef] = SPDX.LicenseExpression

    creationInfo: Union[dict, CreationInfo] = None
    licenseExpression: str = None
    customIdToUri: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    licenseListVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.licenseExpression):
            self.MissingRequiredField("licenseExpression")
        if not isinstance(self.licenseExpression, str):
            self.licenseExpression = str(self.licenseExpression)

        self._normalize_inlined_as_list(slot_name="customIdToUri", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if self.licenseListVersion is not None and not isinstance(self.licenseListVersion, str):
            self.licenseListVersion = str(self.licenseListVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SimpleLicensingText(Element):
    """
    A license or addition that is not listed on the SPDX License List.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIMPLELICENSING["SimpleLicensingText"]
    class_class_curie: ClassVar[str] = "simplelicensing:SimpleLicensingText"
    class_name: ClassVar[str] = "SimpleLicensingText"
    class_model_uri: ClassVar[URIRef] = SPDX.SimpleLicensingText

    creationInfo: Union[dict, CreationInfo] = None
    licenseText: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.licenseText):
            self.MissingRequiredField("licenseText")
        if not isinstance(self.licenseText, str):
            self.licenseText = str(self.licenseText)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContentIdentifier(IntegrityMethod):
    """
    A canonical, unique, immutable identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTWARE["ContentIdentifier"]
    class_class_curie: ClassVar[str] = "software:ContentIdentifier"
    class_name: ClassVar[str] = "ContentIdentifier"
    class_model_uri: ClassVar[URIRef] = SPDX.ContentIdentifier

    contentIdentifierValue: Union[str, URI] = None
    contentIdentifierType: Union[str, "ContentIdentifierType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.contentIdentifierValue):
            self.MissingRequiredField("contentIdentifierValue")
        if not isinstance(self.contentIdentifierValue, URI):
            self.contentIdentifierValue = URI(self.contentIdentifierValue)

        if self._is_empty(self.contentIdentifierType):
            self.MissingRequiredField("contentIdentifierType")
        if not isinstance(self.contentIdentifierType, ContentIdentifierType):
            self.contentIdentifierType = ContentIdentifierType(self.contentIdentifierType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sbom(Bom):
    """
    A collection of SPDX Elements describing a single package.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTWARE["Sbom"]
    class_class_curie: ClassVar[str] = "software:Sbom"
    class_name: ClassVar[str] = "Sbom"
    class_model_uri: ClassVar[URIRef] = SPDX.Sbom

    creationInfo: Union[dict, CreationInfo] = None
    sbomType: Optional[Union[Union[str, "SbomType"], list[Union[str, "SbomType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.sbomType, list):
            self.sbomType = [self.sbomType] if self.sbomType is not None else []
        self.sbomType = [v if isinstance(v, SbomType) else SbomType(v) for v in self.sbomType]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoftwareArtifact(Artifact):
    """
    A distinct article or unit related to Software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTWARE["SoftwareArtifact"]
    class_class_curie: ClassVar[str] = "software:SoftwareArtifact"
    class_name: ClassVar[str] = "SoftwareArtifact"
    class_model_uri: ClassVar[URIRef] = SPDX.SoftwareArtifact

    creationInfo: Union[dict, CreationInfo] = None
    attributionText: Optional[Union[str, list[str]]] = empty_list()
    primaryPurpose: Optional[str] = None
    additionalPurpose: Optional[Union[str, list[str]]] = empty_list()
    contentIdentifier: Optional[Union[Union[dict, ContentIdentifier], list[Union[dict, ContentIdentifier]]]] = empty_list()
    copyrightText: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.attributionText, list):
            self.attributionText = [self.attributionText] if self.attributionText is not None else []
        self.attributionText = [v if isinstance(v, str) else str(v) for v in self.attributionText]

        if self.primaryPurpose is not None and not isinstance(self.primaryPurpose, str):
            self.primaryPurpose = str(self.primaryPurpose)

        if not isinstance(self.additionalPurpose, list):
            self.additionalPurpose = [self.additionalPurpose] if self.additionalPurpose is not None else []
        self.additionalPurpose = [v if isinstance(v, str) else str(v) for v in self.additionalPurpose]

        self._normalize_inlined_as_list(slot_name="contentIdentifier", slot_type=ContentIdentifier, key_name="contentIdentifierValue", keyed=False)

        if self.copyrightText is not None and not isinstance(self.copyrightText, str):
            self.copyrightText = str(self.copyrightText)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(SoftwareArtifact):
    """
    Refers to any object that stores content on a computer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTWARE["File"]
    class_class_curie: ClassVar[str] = "software:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = SPDX.File

    creationInfo: Union[dict, CreationInfo] = None
    fileKind: Optional[Union[str, "FileKindType"]] = None
    contentType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fileKind is not None and not isinstance(self.fileKind, FileKindType):
            self.fileKind = FileKindType(self.fileKind)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Package(SoftwareArtifact):
    """
    Refers to any unit of content that can be associated with a distribution of
    software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTWARE["Package"]
    class_class_curie: ClassVar[str] = "software:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = SPDX.Package

    creationInfo: Union[dict, CreationInfo] = None
    sourceInfo: Optional[str] = None
    homePage: Optional[Union[str, URI]] = None
    downloadLocation: Optional[Union[str, URI]] = None
    packageVersion: Optional[str] = None
    packageUrl: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sourceInfo is not None and not isinstance(self.sourceInfo, str):
            self.sourceInfo = str(self.sourceInfo)

        if self.homePage is not None and not isinstance(self.homePage, URI):
            self.homePage = URI(self.homePage)

        if self.downloadLocation is not None and not isinstance(self.downloadLocation, URI):
            self.downloadLocation = URI(self.downloadLocation)

        if self.packageVersion is not None and not isinstance(self.packageVersion, str):
            self.packageVersion = str(self.packageVersion)

        if self.packageUrl is not None and not isinstance(self.packageUrl, URI):
            self.packageUrl = URI(self.packageUrl)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIPackage(Package):
    """
    Specifies an AI package and its associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["AIPackage"]
    class_class_curie: ClassVar[str] = "ai:AIPackage"
    class_name: ClassVar[str] = "AIPackage"
    class_model_uri: ClassVar[URIRef] = SPDX.AIPackage

    creationInfo: Union[dict, CreationInfo] = None
    informationAboutTraining: Optional[str] = None
    modelDataPreprocessing: Optional[Union[str, list[str]]] = empty_list()
    typeOfModel: Optional[Union[str, list[str]]] = empty_list()
    safetyRiskAssessment: Optional[Union[str, "SafetyRiskAssessmentType"]] = None
    metricDecisionThreshold: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    useSensitivePersonalInformation: Optional[Union[str, "PresenceType"]] = None
    energyConsumption: Optional[Union[dict, EnergyConsumption]] = None
    limitation: Optional[str] = None
    hyperparameter: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    autonomyType: Optional[Union[str, "PresenceType"]] = None
    domain: Optional[Union[str, list[str]]] = empty_list()
    modelExplainability: Optional[Union[str, list[str]]] = empty_list()
    informationAboutApplication: Optional[str] = None
    metric: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    standardCompliance: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.informationAboutTraining is not None and not isinstance(self.informationAboutTraining, str):
            self.informationAboutTraining = str(self.informationAboutTraining)

        if not isinstance(self.modelDataPreprocessing, list):
            self.modelDataPreprocessing = [self.modelDataPreprocessing] if self.modelDataPreprocessing is not None else []
        self.modelDataPreprocessing = [v if isinstance(v, str) else str(v) for v in self.modelDataPreprocessing]

        if not isinstance(self.typeOfModel, list):
            self.typeOfModel = [self.typeOfModel] if self.typeOfModel is not None else []
        self.typeOfModel = [v if isinstance(v, str) else str(v) for v in self.typeOfModel]

        if self.safetyRiskAssessment is not None and not isinstance(self.safetyRiskAssessment, SafetyRiskAssessmentType):
            self.safetyRiskAssessment = SafetyRiskAssessmentType(self.safetyRiskAssessment)

        self._normalize_inlined_as_list(slot_name="metricDecisionThreshold", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if self.useSensitivePersonalInformation is not None and not isinstance(self.useSensitivePersonalInformation, PresenceType):
            self.useSensitivePersonalInformation = PresenceType(self.useSensitivePersonalInformation)

        if self.energyConsumption is not None and not isinstance(self.energyConsumption, EnergyConsumption):
            self.energyConsumption = EnergyConsumption(**as_dict(self.energyConsumption))

        if self.limitation is not None and not isinstance(self.limitation, str):
            self.limitation = str(self.limitation)

        self._normalize_inlined_as_list(slot_name="hyperparameter", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if self.autonomyType is not None and not isinstance(self.autonomyType, PresenceType):
            self.autonomyType = PresenceType(self.autonomyType)

        if not isinstance(self.domain, list):
            self.domain = [self.domain] if self.domain is not None else []
        self.domain = [v if isinstance(v, str) else str(v) for v in self.domain]

        if not isinstance(self.modelExplainability, list):
            self.modelExplainability = [self.modelExplainability] if self.modelExplainability is not None else []
        self.modelExplainability = [v if isinstance(v, str) else str(v) for v in self.modelExplainability]

        if self.informationAboutApplication is not None and not isinstance(self.informationAboutApplication, str):
            self.informationAboutApplication = str(self.informationAboutApplication)

        self._normalize_inlined_as_list(slot_name="metric", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if not isinstance(self.standardCompliance, list):
            self.standardCompliance = [self.standardCompliance] if self.standardCompliance is not None else []
        self.standardCompliance = [v if isinstance(v, str) else str(v) for v in self.standardCompliance]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetPackage(Package):
    """
    Specifies a data package and its associated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASET["DatasetPackage"]
    class_class_curie: ClassVar[str] = "dataset:DatasetPackage"
    class_name: ClassVar[str] = "DatasetPackage"
    class_model_uri: ClassVar[URIRef] = SPDX.DatasetPackage

    creationInfo: Union[dict, CreationInfo] = None
    datasetType: Union[str, list[str]] = None
    datasetSize: Optional[int] = None
    anonymizationMethodUsed: Optional[Union[str, list[str]]] = empty_list()
    datasetUpdateMechanism: Optional[str] = None
    dataCollectionProcess: Optional[str] = None
    knownBias: Optional[Union[str, list[str]]] = empty_list()
    sensor: Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]] = empty_list()
    dataPreprocessing: Optional[Union[str, list[str]]] = empty_list()
    intendedUse: Optional[str] = None
    confidentialityLevel: Optional[Union[str, "ConfidentialityLevelType"]] = None
    datasetAvailability: Optional[Union[str, "DatasetAvailabilityType"]] = None
    hasSensitivePersonalInformation: Optional[Union[str, "PresenceType"]] = None
    datasetNoise: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.datasetType):
            self.MissingRequiredField("datasetType")
        if not isinstance(self.datasetType, list):
            self.datasetType = [self.datasetType] if self.datasetType is not None else []
        self.datasetType = [v if isinstance(v, str) else str(v) for v in self.datasetType]

        if self.datasetSize is not None and not isinstance(self.datasetSize, int):
            self.datasetSize = int(self.datasetSize)

        if not isinstance(self.anonymizationMethodUsed, list):
            self.anonymizationMethodUsed = [self.anonymizationMethodUsed] if self.anonymizationMethodUsed is not None else []
        self.anonymizationMethodUsed = [v if isinstance(v, str) else str(v) for v in self.anonymizationMethodUsed]

        if self.datasetUpdateMechanism is not None and not isinstance(self.datasetUpdateMechanism, str):
            self.datasetUpdateMechanism = str(self.datasetUpdateMechanism)

        if self.dataCollectionProcess is not None and not isinstance(self.dataCollectionProcess, str):
            self.dataCollectionProcess = str(self.dataCollectionProcess)

        if not isinstance(self.knownBias, list):
            self.knownBias = [self.knownBias] if self.knownBias is not None else []
        self.knownBias = [v if isinstance(v, str) else str(v) for v in self.knownBias]

        self._normalize_inlined_as_list(slot_name="sensor", slot_type=DictionaryEntry, key_name="key", keyed=False)

        if not isinstance(self.dataPreprocessing, list):
            self.dataPreprocessing = [self.dataPreprocessing] if self.dataPreprocessing is not None else []
        self.dataPreprocessing = [v if isinstance(v, str) else str(v) for v in self.dataPreprocessing]

        if self.intendedUse is not None and not isinstance(self.intendedUse, str):
            self.intendedUse = str(self.intendedUse)

        if self.confidentialityLevel is not None and not isinstance(self.confidentialityLevel, ConfidentialityLevelType):
            self.confidentialityLevel = ConfidentialityLevelType(self.confidentialityLevel)

        if self.datasetAvailability is not None and not isinstance(self.datasetAvailability, DatasetAvailabilityType):
            self.datasetAvailability = DatasetAvailabilityType(self.datasetAvailability)

        if self.hasSensitivePersonalInformation is not None and not isinstance(self.hasSensitivePersonalInformation, PresenceType):
            self.hasSensitivePersonalInformation = PresenceType(self.hasSensitivePersonalInformation)

        if self.datasetNoise is not None and not isinstance(self.datasetNoise, str):
            self.datasetNoise = str(self.datasetNoise)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Snippet(SoftwareArtifact):
    """
    Describes a certain part of a file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTWARE["Snippet"]
    class_class_curie: ClassVar[str] = "software:Snippet"
    class_name: ClassVar[str] = "Snippet"
    class_model_uri: ClassVar[URIRef] = SPDX.Snippet

    creationInfo: Union[dict, CreationInfo] = None
    snippetFromFile: Union[dict, File] = None
    lineRange: Optional[Union[dict, PositiveIntegerRange]] = None
    byteRange: Optional[Union[dict, PositiveIntegerRange]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.snippetFromFile):
            self.MissingRequiredField("snippetFromFile")
        if not isinstance(self.snippetFromFile, File):
            self.snippetFromFile = File(**as_dict(self.snippetFromFile))

        if self.lineRange is not None and not isinstance(self.lineRange, PositiveIntegerRange):
            self.lineRange = PositiveIntegerRange(**as_dict(self.lineRange))

        if self.byteRange is not None and not isinstance(self.byteRange, PositiveIntegerRange):
            self.byteRange = PositiveIntegerRange(**as_dict(self.byteRange))

        super().__post_init__(**kwargs)


# Enumerations
class EnergyUnitType(EnumDefinitionImpl):
    """
    Specifies the unit of energy consumption.
    """
    kilowattHour = PermissibleValue(
        text="kilowattHour",
        description="Kilowatt-hour.",
        meaning=AI["EnergyUnitType/kilowattHour"])
    megajoule = PermissibleValue(
        text="megajoule",
        description="Megajoule.",
        meaning=AI["EnergyUnitType/megajoule"])
    other = PermissibleValue(
        text="other",
        description="Any other units of energy measurement.",
        meaning=AI["EnergyUnitType/other"])

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
        meaning=AI["SafetyRiskAssessmentType/high"])
    low = PermissibleValue(
        text="low",
        description="Low/no risk is posed by an AI system.",
        meaning=AI["SafetyRiskAssessmentType/low"])
    medium = PermissibleValue(
        text="medium",
        description="The third-highest level of risk posed by an AI system.",
        meaning=AI["SafetyRiskAssessmentType/medium"])
    serious = PermissibleValue(
        text="serious",
        description="The highest level of risk posed by an AI system.",
        meaning=AI["SafetyRiskAssessmentType/serious"])

    _defn = EnumDefinition(
        name="SafetyRiskAssessmentType",
        description="Specifies the safety risk level.",
    )

class AnnotationType(EnumDefinitionImpl):
    """
    Specifies the type of an annotation.
    """
    other = PermissibleValue(
        text="other",
        description="""Used to store extra information about an Element which is not part of a review (e.g. extra information provided during the creation of the Element).""",
        meaning=CORE["AnnotationType/other"])
    review = PermissibleValue(
        text="review",
        description="Used when someone reviews the Element.",
        meaning=CORE["AnnotationType/review"])

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
        meaning=CORE["ExternalIdentifierType/cpe22"])
    cpe23 = PermissibleValue(
        text="cpe23",
        description="""[Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)""",
        meaning=CORE["ExternalIdentifierType/cpe23"])
    cve = PermissibleValue(
        text="cve",
        description="""Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).""",
        meaning=CORE["ExternalIdentifierType/cve"])
    email = PermissibleValue(
        text="email",
        description="Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3986/) Section 3.",
        meaning=CORE["ExternalIdentifierType/email"])
    gitoid = PermissibleValue(
        text="gitoid",
        description="""[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).""",
        meaning=CORE["ExternalIdentifierType/gitoid"])
    other = PermissibleValue(
        text="other",
        description="Used when the type does not match any of the other options.",
        meaning=CORE["ExternalIdentifierType/other"])
    packageUrl = PermissibleValue(
        text="packageUrl",
        description="""Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this specification.""",
        meaning=CORE["ExternalIdentifierType/packageUrl"])
    securityOther = PermissibleValue(
        text="securityOther",
        description="Used when there is a security related identifier of unspecified type.",
        meaning=CORE["ExternalIdentifierType/securityOther"])
    swhid = PermissibleValue(
        text="swhid",
        description="""SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.""",
        meaning=CORE["ExternalIdentifierType/swhid"])
    swid = PermissibleValue(
        text="swid",
        description="""Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.""",
        meaning=CORE["ExternalIdentifierType/swid"])
    urlScheme = PermissibleValue(
        text="urlScheme",
        description="""[Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.""",
        meaning=CORE["ExternalIdentifierType/urlScheme"])

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
        meaning=CORE["ExternalRefType/altDownloadLocation"])
    altWebPage = PermissibleValue(
        text="altWebPage",
        description="A reference to an alternative web page.",
        meaning=CORE["ExternalRefType/altWebPage"])
    binaryArtifact = PermissibleValue(
        text="binaryArtifact",
        description="A reference to binary artifacts related to a package.",
        meaning=CORE["ExternalRefType/binaryArtifact"])
    bower = PermissibleValue(
        text="bower",
        description="""A reference to a Bower package. The package locator format, looks like `package#version`, is defined in the \"install\" section of [Bower API documentation](https://bower.io/docs/api/#install).""",
        meaning=CORE["ExternalRefType/bower"])
    buildMeta = PermissibleValue(
        text="buildMeta",
        description="A reference build metadata related to a published package.",
        meaning=CORE["ExternalRefType/buildMeta"])
    buildSystem = PermissibleValue(
        text="buildSystem",
        description="A reference build system used to create or publish the package.",
        meaning=CORE["ExternalRefType/buildSystem"])
    certificationReport = PermissibleValue(
        text="certificationReport",
        description="A reference to a certification report for a package from an accredited/independent body.",
        meaning=CORE["ExternalRefType/certificationReport"])
    chat = PermissibleValue(
        text="chat",
        description="A reference to the instant messaging system used by the maintainer for a package.",
        meaning=CORE["ExternalRefType/chat"])
    componentAnalysisReport = PermissibleValue(
        text="componentAnalysisReport",
        description="A reference to a Software Composition Analysis (SCA) report.",
        meaning=CORE["ExternalRefType/componentAnalysisReport"])
    cwe = PermissibleValue(
        text="cwe",
        description="""[Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/).""",
        meaning=CORE["ExternalRefType/cwe"])
    documentation = PermissibleValue(
        text="documentation",
        description="A reference to the documentation for a package.",
        meaning=CORE["ExternalRefType/documentation"])
    dynamicAnalysisReport = PermissibleValue(
        text="dynamicAnalysisReport",
        description="A reference to a dynamic analysis report for a package.",
        meaning=CORE["ExternalRefType/dynamicAnalysisReport"])
    eolNotice = PermissibleValue(
        text="eolNotice",
        description="""A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package.""",
        meaning=CORE["ExternalRefType/eolNotice"])
    exportControlAssessment = PermissibleValue(
        text="exportControlAssessment",
        description="A reference to a export control assessment for a package.",
        meaning=CORE["ExternalRefType/exportControlAssessment"])
    funding = PermissibleValue(
        text="funding",
        description="A reference to funding information related to a package.",
        meaning=CORE["ExternalRefType/funding"])
    issueTracker = PermissibleValue(
        text="issueTracker",
        description="A reference to the issue tracker for a package.",
        meaning=CORE["ExternalRefType/issueTracker"])
    license = PermissibleValue(
        text="license",
        description="A reference to additional license information related to an artifact.",
        meaning=CORE["ExternalRefType/license"])
    mailingList = PermissibleValue(
        text="mailingList",
        description="A reference to the mailing list used by the maintainer for a package.",
        meaning=CORE["ExternalRefType/mailingList"])
    mavenCentral = PermissibleValue(
        text="mavenCentral",
        description="""A reference to a Maven repository artifact. The artifact locator format is defined in the [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html) and looks like `groupId:artifactId[:version]`.""",
        meaning=CORE["ExternalRefType/mavenCentral"])
    metrics = PermissibleValue(
        text="metrics",
        description="A reference to metrics related to package such as OpenSSF scorecards.",
        meaning=CORE["ExternalRefType/metrics"])
    npm = PermissibleValue(
        text="npm",
        description="""A reference to an npm package. The package locator format is defined in the [npm documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and looks like `package@version`.""",
        meaning=CORE["ExternalRefType/npm"])
    nuget = PermissibleValue(
        text="nuget",
        description="""A reference to a NuGet package. The package locator format is defined in the [NuGet documentation](https://docs.nuget.org) and looks like `package/version`.""",
        meaning=CORE["ExternalRefType/nuget"])
    other = PermissibleValue(
        text="other",
        description="Used when the type does not match any of the other options.",
        meaning=CORE["ExternalRefType/other"])
    privacyAssessment = PermissibleValue(
        text="privacyAssessment",
        description="A reference to a privacy assessment for a package.",
        meaning=CORE["ExternalRefType/privacyAssessment"])
    productMetadata = PermissibleValue(
        text="productMetadata",
        description="""A reference to additional product metadata such as reference within organization's product catalog.""",
        meaning=CORE["ExternalRefType/productMetadata"])
    purchaseOrder = PermissibleValue(
        text="purchaseOrder",
        description="A reference to a purchase order for a package.",
        meaning=CORE["ExternalRefType/purchaseOrder"])
    qualityAssessmentReport = PermissibleValue(
        text="qualityAssessmentReport",
        description="A reference to a quality assessment for a package.",
        meaning=CORE["ExternalRefType/qualityAssessmentReport"])
    releaseHistory = PermissibleValue(
        text="releaseHistory",
        description="A reference to a published list of releases for a package.",
        meaning=CORE["ExternalRefType/releaseHistory"])
    releaseNotes = PermissibleValue(
        text="releaseNotes",
        description="A reference to the release notes for a package.",
        meaning=CORE["ExternalRefType/releaseNotes"])
    riskAssessment = PermissibleValue(
        text="riskAssessment",
        description="A reference to a risk assessment for a package.",
        meaning=CORE["ExternalRefType/riskAssessment"])
    runtimeAnalysisReport = PermissibleValue(
        text="runtimeAnalysisReport",
        description="A reference to a runtime analysis report for a package.",
        meaning=CORE["ExternalRefType/runtimeAnalysisReport"])
    secureSoftwareAttestation = PermissibleValue(
        text="secureSoftwareAttestation",
        description="""A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form).""",
        meaning=CORE["ExternalRefType/secureSoftwareAttestation"])
    securityAdversaryModel = PermissibleValue(
        text="securityAdversaryModel",
        description="A reference to the security adversary model for a package.",
        meaning=CORE["ExternalRefType/securityAdversaryModel"])
    securityAdvisory = PermissibleValue(
        text="securityAdvisory",
        description="""A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries.""",
        meaning=CORE["ExternalRefType/securityAdvisory"])
    securityFix = PermissibleValue(
        text="securityFix",
        description="A reference to the patch or source code that fixes a vulnerability.",
        meaning=CORE["ExternalRefType/securityFix"])
    securityOther = PermissibleValue(
        text="securityOther",
        description="A reference to related security information of unspecified type.",
        meaning=CORE["ExternalRefType/securityOther"])
    securityPenTestReport = PermissibleValue(
        text="securityPenTestReport",
        description="""A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package.""",
        meaning=CORE["ExternalRefType/securityPenTestReport"])
    securityPolicy = PermissibleValue(
        text="securityPolicy",
        description="""A reference to instructions for reporting newly discovered security vulnerabilities for a package.""",
        meaning=CORE["ExternalRefType/securityPolicy"])
    securityThreatModel = PermissibleValue(
        text="securityThreatModel",
        description="""A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package.""",
        meaning=CORE["ExternalRefType/securityThreatModel"])
    socialMedia = PermissibleValue(
        text="socialMedia",
        description="A reference to a social media channel for a package.",
        meaning=CORE["ExternalRefType/socialMedia"])
    sourceArtifact = PermissibleValue(
        text="sourceArtifact",
        description="A reference to an artifact containing the sources for a package.",
        meaning=CORE["ExternalRefType/sourceArtifact"])
    staticAnalysisReport = PermissibleValue(
        text="staticAnalysisReport",
        description="A reference to a static analysis report for a package.",
        meaning=CORE["ExternalRefType/staticAnalysisReport"])
    support = PermissibleValue(
        text="support",
        description="A reference to the software support channel or other support information for a package.",
        meaning=CORE["ExternalRefType/support"])
    vcs = PermissibleValue(
        text="vcs",
        description="A reference to a version control system related to a software artifact.",
        meaning=CORE["ExternalRefType/vcs"])
    vulnerabilityDisclosureReport = PermissibleValue(
        text="vulnerabilityDisclosureReport",
        description="""A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/final).""",
        meaning=CORE["ExternalRefType/vulnerabilityDisclosureReport"])
    vulnerabilityExploitabilityAssessment = PermissibleValue(
        text="vulnerabilityExploitabilityAssessment",
        description="""A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf).""",
        meaning=CORE["ExternalRefType/vulnerabilityExploitabilityAssessment"])

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
        meaning=CORE["HashAlgorithm/adler32"])
    blake2b256 = PermissibleValue(
        text="blake2b256",
        description="""BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.""",
        meaning=CORE["HashAlgorithm/blake2b256"])
    blake2b384 = PermissibleValue(
        text="blake2b384",
        description="""BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.""",
        meaning=CORE["HashAlgorithm/blake2b384"])
    blake2b512 = PermissibleValue(
        text="blake2b512",
        description="""BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.""",
        meaning=CORE["HashAlgorithm/blake2b512"])
    blake3 = PermissibleValue(
        text="blake3",
        description="[BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)",
        meaning=CORE["HashAlgorithm/blake3"])
    crystalsDilithium = PermissibleValue(
        text="crystalsDilithium",
        description="[Dilithium](https://pq-crystals.org/dilithium/)",
        meaning=CORE["HashAlgorithm/crystalsDilithium"])
    crystalsKyber = PermissibleValue(
        text="crystalsKyber",
        description="[Kyber](https://pq-crystals.org/kyber/)",
        meaning=CORE["HashAlgorithm/crystalsKyber"])
    falcon = PermissibleValue(
        text="falcon",
        description="[FALCON](https://falcon-sign.info/falcon.pdf)",
        meaning=CORE["HashAlgorithm/falcon"])
    md2 = PermissibleValue(
        text="md2",
        description="""MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/).""",
        meaning=CORE["HashAlgorithm/md2"])
    md4 = PermissibleValue(
        text="md4",
        description="""MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/).""",
        meaning=CORE["HashAlgorithm/md4"])
    md5 = PermissibleValue(
        text="md5",
        description="""MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/).""",
        meaning=CORE["HashAlgorithm/md5"])
    md6 = PermissibleValue(
        text="md6",
        description="[MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)",
        meaning=CORE["HashAlgorithm/md6"])
    other = PermissibleValue(
        text="other",
        description="any hashing algorithm that does not exist in this list of entries",
        meaning=CORE["HashAlgorithm/other"])
    sha1 = PermissibleValue(
        text="sha1",
        description="""SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/).""",
        meaning=CORE["HashAlgorithm/sha1"])
    sha224 = PermissibleValue(
        text="sha224",
        description="""SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/).""",
        meaning=CORE["HashAlgorithm/sha224"])
    sha256 = PermissibleValue(
        text="sha256",
        description="""SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).""",
        meaning=CORE["HashAlgorithm/sha256"])
    sha384 = PermissibleValue(
        text="sha384",
        description="""SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).""",
        meaning=CORE["HashAlgorithm/sha384"])
    sha3_224 = PermissibleValue(
        text="sha3_224",
        description="""SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=CORE["HashAlgorithm/sha3_224"])
    sha3_256 = PermissibleValue(
        text="sha3_256",
        description="""SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=CORE["HashAlgorithm/sha3_256"])
    sha3_384 = PermissibleValue(
        text="sha3_384",
        description="""SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=CORE["HashAlgorithm/sha3_384"])
    sha3_512 = PermissibleValue(
        text="sha3_512",
        description="""SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).""",
        meaning=CORE["HashAlgorithm/sha3_512"])
    sha512 = PermissibleValue(
        text="sha512",
        description="""SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).""",
        meaning=CORE["HashAlgorithm/sha512"])

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
        meaning=CORE["LifecycleScopeType/build"])
    design = PermissibleValue(
        text="design",
        description="A relationship has specific context implications during an element's design.",
        meaning=CORE["LifecycleScopeType/design"])
    development = PermissibleValue(
        text="development",
        description="A relationship has specific context implications during development phase of an element.",
        meaning=CORE["LifecycleScopeType/development"])
    other = PermissibleValue(
        text="other",
        description="""A relationship has other specific context information necessary to capture that the above set of enumerations does not handle.""",
        meaning=CORE["LifecycleScopeType/other"])
    runtime = PermissibleValue(
        text="runtime",
        description="A relationship has specific context implications during the execution phase of an element.",
        meaning=CORE["LifecycleScopeType/runtime"])
    test = PermissibleValue(
        text="test",
        description="""A relationship has specific context implications during an element's testing phase, during development.""",
        meaning=CORE["LifecycleScopeType/test"])

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
        meaning=CORE["PresenceType/no"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="Makes no assertion about the field.",
        meaning=CORE["PresenceType/noAssertion"])
    yes = PermissibleValue(
        text="yes",
        description="Indicates presence of the field.",
        meaning=CORE["PresenceType/yes"])

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
        meaning=CORE["ProfileIdentifierType/ai"])
    build = PermissibleValue(
        text="build",
        description="the element follows the Build profile specification",
        meaning=CORE["ProfileIdentifierType/build"])
    core = PermissibleValue(
        text="core",
        description="the element follows the Core profile specification",
        meaning=CORE["ProfileIdentifierType/core"])
    dataset = PermissibleValue(
        text="dataset",
        description="the element follows the Dataset profile specification",
        meaning=CORE["ProfileIdentifierType/dataset"])
    expandedLicensing = PermissibleValue(
        text="expandedLicensing",
        description="the element follows the ExpandedLicensing profile specification",
        meaning=CORE["ProfileIdentifierType/expandedLicensing"])
    extension = PermissibleValue(
        text="extension",
        description="the element follows the Extension profile specification",
        meaning=CORE["ProfileIdentifierType/extension"])
    lite = PermissibleValue(
        text="lite",
        description="the element follows the Lite profile specification",
        meaning=CORE["ProfileIdentifierType/lite"])
    security = PermissibleValue(
        text="security",
        description="the element follows the Security profile specification",
        meaning=CORE["ProfileIdentifierType/security"])
    simpleLicensing = PermissibleValue(
        text="simpleLicensing",
        description="the element follows the SimpleLicensing profile specification",
        meaning=CORE["ProfileIdentifierType/simpleLicensing"])
    software = PermissibleValue(
        text="software",
        description="the element follows the Software profile specification",
        meaning=CORE["ProfileIdentifierType/software"])

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
        meaning=CORE["RelationshipCompleteness/complete"])
    incomplete = PermissibleValue(
        text="incomplete",
        description="The relationship is known not to be exhaustive.",
        meaning=CORE["RelationshipCompleteness/incomplete"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="No assertion can be made about the completeness of the relationship.",
        meaning=CORE["RelationshipCompleteness/noAssertion"])

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
        meaning=CORE["RelationshipType/affects"])
    amendedBy = PermissibleValue(
        text="amendedBy",
        description="The `from` Element is amended by each `to` Element.",
        meaning=CORE["RelationshipType/amendedBy"])
    ancestorOf = PermissibleValue(
        text="ancestorOf",
        description="The `from` Element is an ancestor of each `to` Element.",
        meaning=CORE["RelationshipType/ancestorOf"])
    availableFrom = PermissibleValue(
        text="availableFrom",
        description="The `from` Element is available from the additional supplier described by each `to` Element.",
        meaning=CORE["RelationshipType/availableFrom"])
    configures = PermissibleValue(
        text="configures",
        description="""The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/configures"])
    contains = PermissibleValue(
        text="contains",
        description="The `from` Element contains each `to` Element.",
        meaning=CORE["RelationshipType/contains"])
    coordinatedBy = PermissibleValue(
        text="coordinatedBy",
        description="""The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).""",
        meaning=CORE["RelationshipType/coordinatedBy"])
    copiedTo = PermissibleValue(
        text="copiedTo",
        description="The `from` Element has been copied to each `to` Element.",
        meaning=CORE["RelationshipType/copiedTo"])
    delegatedTo = PermissibleValue(
        text="delegatedTo",
        description="""The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).""",
        meaning=CORE["RelationshipType/delegatedTo"])
    dependsOn = PermissibleValue(
        text="dependsOn",
        description="The `from` Element depends on each `to` Element, during a LifecycleScopeType period.",
        meaning=CORE["RelationshipType/dependsOn"])
    descendantOf = PermissibleValue(
        text="descendantOf",
        description="The `from` Element is a descendant of each `to` Element.",
        meaning=CORE["RelationshipType/descendantOf"])
    describes = PermissibleValue(
        text="describes",
        description="""The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used.""",
        meaning=CORE["RelationshipType/describes"])
    doesNotAffect = PermissibleValue(
        text="doesNotAffect",
        description="""The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.""",
        meaning=CORE["RelationshipType/doesNotAffect"])
    expandsTo = PermissibleValue(
        text="expandsTo",
        description="The `from` archive expands out as an artifact described by each `to` Element.",
        meaning=CORE["RelationshipType/expandsTo"])
    exploitCreatedBy = PermissibleValue(
        text="exploitCreatedBy",
        description="The `from` Vulnerability has had an exploit created against it by each `to` Agent.",
        meaning=CORE["RelationshipType/exploitCreatedBy"])
    fixedBy = PermissibleValue(
        text="fixedBy",
        description="Designates a `from` Vulnerability has been fixed by the `to` Agent(s).",
        meaning=CORE["RelationshipType/fixedBy"])
    fixedIn = PermissibleValue(
        text="fixedIn",
        description="""A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.""",
        meaning=CORE["RelationshipType/fixedIn"])
    foundBy = PermissibleValue(
        text="foundBy",
        description="Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).",
        meaning=CORE["RelationshipType/foundBy"])
    generates = PermissibleValue(
        text="generates",
        description="The `from` Element generates each `to` Element.",
        meaning=CORE["RelationshipType/generates"])
    hasAddedFile = PermissibleValue(
        text="hasAddedFile",
        description="Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).",
        meaning=CORE["RelationshipType/hasAddedFile"])
    hasAssessmentFor = PermissibleValue(
        text="hasAssessmentFor",
        description="""Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types.""",
        meaning=CORE["RelationshipType/hasAssessmentFor"])
    hasAssociatedVulnerability = PermissibleValue(
        text="hasAssociatedVulnerability",
        description="Used to associate a `from` Artifact with each `to` Vulnerability.",
        meaning=CORE["RelationshipType/hasAssociatedVulnerability"])
    hasConcludedLicense = PermissibleValue(
        text="hasConcludedLicense",
        description="""The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license.""",
        meaning=CORE["RelationshipType/hasConcludedLicense"])
    hasDataFile = PermissibleValue(
        text="hasDataFile",
        description="""The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup file, and more. For AI training dataset, test dataset, test artifact, configuration data, build input data, and build output data, please consider using the more specific relationship types: `trainedOn`, `testedOn`, `hasTest`, `configures`, `hasInput`, and `hasOutput`, respectively. This relationship does not imply dependency.""",
        meaning=CORE["RelationshipType/hasDataFile"])
    hasDeclaredLicense = PermissibleValue(
        text="hasDeclaredLicense",
        description="""The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.""",
        meaning=CORE["RelationshipType/hasDeclaredLicense"])
    hasDeletedFile = PermissibleValue(
        text="hasDeletedFile",
        description="Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).",
        meaning=CORE["RelationshipType/hasDeletedFile"])
    hasDependencyManifest = PermissibleValue(
        text="hasDependencyManifest",
        description="""The `from` Element has manifest files that contain dependency information in each `to` Element.""",
        meaning=CORE["RelationshipType/hasDependencyManifest"])
    hasDistributionArtifact = PermissibleValue(
        text="hasDistributionArtifact",
        description="""The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).""",
        meaning=CORE["RelationshipType/hasDistributionArtifact"])
    hasDocumentation = PermissibleValue(
        text="hasDocumentation",
        description="The `from` Element is documented by each `to` Element.",
        meaning=CORE["RelationshipType/hasDocumentation"])
    hasDynamicLink = PermissibleValue(
        text="hasDynamicLink",
        description="The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.",
        meaning=CORE["RelationshipType/hasDynamicLink"])
    hasEvidence = PermissibleValue(
        text="hasEvidence",
        description="Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).",
        meaning=CORE["RelationshipType/hasEvidence"])
    hasExample = PermissibleValue(
        text="hasExample",
        description="Every `to` Element is an example for the `from` Element (`from` hasExample `to`).",
        meaning=CORE["RelationshipType/hasExample"])
    hasHost = PermissibleValue(
        text="hasHost",
        description="""The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).""",
        meaning=CORE["RelationshipType/hasHost"])
    hasInput = PermissibleValue(
        text="hasInput",
        description="The `from` Build has each `to` Element as an input, during a LifecycleScopeType period.",
        meaning=CORE["RelationshipType/hasInput"])
    hasMetadata = PermissibleValue(
        text="hasMetadata",
        description="Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).",
        meaning=CORE["RelationshipType/hasMetadata"])
    hasOptionalComponent = PermissibleValue(
        text="hasOptionalComponent",
        description="""Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).""",
        meaning=CORE["RelationshipType/hasOptionalComponent"])
    hasOptionalDependency = PermissibleValue(
        text="hasOptionalDependency",
        description="""The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/hasOptionalDependency"])
    hasOutput = PermissibleValue(
        text="hasOutput",
        description="""The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/hasOutput"])
    hasPrerequisite = PermissibleValue(
        text="hasPrerequisite",
        description="""The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/hasPrerequisite"])
    hasProvidedDependency = PermissibleValue(
        text="hasProvidedDependency",
        description="""The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/hasProvidedDependency"])
    hasRequirement = PermissibleValue(
        text="hasRequirement",
        description="The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.",
        meaning=CORE["RelationshipType/hasRequirement"])
    hasSpecification = PermissibleValue(
        text="hasSpecification",
        description="""Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/hasSpecification"])
    hasStaticLink = PermissibleValue(
        text="hasStaticLink",
        description="The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.",
        meaning=CORE["RelationshipType/hasStaticLink"])
    hasTest = PermissibleValue(
        text="hasTest",
        description="""Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.""",
        meaning=CORE["RelationshipType/hasTest"])
    hasTestCase = PermissibleValue(
        text="hasTestCase",
        description="Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).",
        meaning=CORE["RelationshipType/hasTestCase"])
    hasVariant = PermissibleValue(
        text="hasVariant",
        description="Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).",
        meaning=CORE["RelationshipType/hasVariant"])
    invokedBy = PermissibleValue(
        text="invokedBy",
        description="""The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).""",
        meaning=CORE["RelationshipType/invokedBy"])
    modifiedBy = PermissibleValue(
        text="modifiedBy",
        description="The `from` Element is modified by each `to` Element.",
        meaning=CORE["RelationshipType/modifiedBy"])
    other = PermissibleValue(
        text="other",
        description="""Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).""",
        meaning=CORE["RelationshipType/other"])
    packagedBy = PermissibleValue(
        text="packagedBy",
        description="Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).",
        meaning=CORE["RelationshipType/packagedBy"])
    patchedBy = PermissibleValue(
        text="patchedBy",
        description="Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).",
        meaning=CORE["RelationshipType/patchedBy"])
    publishedBy = PermissibleValue(
        text="publishedBy",
        description="""Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.""",
        meaning=CORE["RelationshipType/publishedBy"])
    reportedBy = PermissibleValue(
        text="reportedBy",
        description="""Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.""",
        meaning=CORE["RelationshipType/reportedBy"])
    republishedBy = PermissibleValue(
        text="republishedBy",
        description="""Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.""",
        meaning=CORE["RelationshipType/republishedBy"])
    serializedInArtifact = PermissibleValue(
        text="serializedInArtifact",
        description="The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.",
        meaning=CORE["RelationshipType/serializedInArtifact"])
    testedOn = PermissibleValue(
        text="testedOn",
        description="The `from` Element has been tested on the `to` Element(s).",
        meaning=CORE["RelationshipType/testedOn"])
    trainedOn = PermissibleValue(
        text="trainedOn",
        description="The `from` Element has been trained on the `to` Element(s).",
        meaning=CORE["RelationshipType/trainedOn"])
    underInvestigationFor = PermissibleValue(
        text="underInvestigationFor",
        description="""The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.""",
        meaning=CORE["RelationshipType/underInvestigationFor"])
    usesTool = PermissibleValue(
        text="usesTool",
        description="The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.",
        meaning=CORE["RelationshipType/usesTool"])

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
        description="""in addition to being supported by the supplier, the software is known to have been deployed and is in use.  For a software as a service provider, this implies the software is now available as a service.""",
        meaning=CORE["SupportType/deployed"])
    development = PermissibleValue(
        text="development",
        description="""the artifact is in active development and is not considered ready for formal support from the supplier.""",
        meaning=CORE["SupportType/development"])
    endOfSupport = PermissibleValue(
        text="endOfSupport",
        description="""there is a defined end of support for the artifact from the supplier.  This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact.""",
        meaning=CORE["SupportType/endOfSupport"])
    limitedSupport = PermissibleValue(
        text="limitedSupport",
        description="""the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.""",
        meaning=CORE["SupportType/limitedSupport"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="""no assertion about the type of support is made.   This is considered the default if no other support type is used.""",
        meaning=CORE["SupportType/noAssertion"])
    noSupport = PermissibleValue(
        text="noSupport",
        description="""there is no support for the artifact from the supplier, consumer assumes any support obligations.""",
        meaning=CORE["SupportType/noSupport"])
    support = PermissibleValue(
        text="support",
        description="""the artifact has been released, and is supported from the supplier.   There is a validUntilDate that can provide additional information about the duration of support.""",
        meaning=CORE["SupportType/support"])

    _defn = EnumDefinition(
        name="SupportType",
        description="Indicates the type of support that is associated with an artifact.",
    )

class ConfidentialityLevelType(EnumDefinitionImpl):
    """
    Categories of confidentiality level.
    """
    amber = PermissibleValue(
        text="amber",
        description="""Data points in the dataset can be shared only with specific organizations and their clients on a need to know basis.""",
        meaning=DATASET["ConfidentialityLevelType/amber"])
    clear = PermissibleValue(
        text="clear",
        description="Dataset may be distributed freely, without restriction.",
        meaning=DATASET["ConfidentialityLevelType/clear"])
    green = PermissibleValue(
        text="green",
        description="Dataset can be shared within a community of peers and partners.",
        meaning=DATASET["ConfidentialityLevelType/green"])
    red = PermissibleValue(
        text="red",
        description="""Data points in the dataset are highly confidential and can only be shared with named recipients.""",
        meaning=DATASET["ConfidentialityLevelType/red"])

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
        meaning=DATASET["DatasetAvailabilityType/clickthrough"])
    directDownload = PermissibleValue(
        text="directDownload",
        description="the dataset is publicly available and can be downloaded directly.",
        meaning=DATASET["DatasetAvailabilityType/directDownload"])
    query = PermissibleValue(
        text="query",
        description="""the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.""",
        meaning=DATASET["DatasetAvailabilityType/query"])
    registration = PermissibleValue(
        text="registration",
        description="""the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.""",
        meaning=DATASET["DatasetAvailabilityType/registration"])
    scrapingScript = PermissibleValue(
        text="scrapingScript",
        description="""the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data.""",
        meaning=DATASET["DatasetAvailabilityType/scrapingScript"])

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
        meaning=DATASET["DatasetType/audio"])
    categorical = PermissibleValue(
        text="categorical",
        description="""data that is classified into a discrete number of categories, such as the eye color of a population of people.""",
        meaning=DATASET["DatasetType/categorical"])
    graph = PermissibleValue(
        text="graph",
        description="""data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends.""",
        meaning=DATASET["DatasetType/graph"])
    image = PermissibleValue(
        text="image",
        description="data is a collection of images such as pictures of animals.",
        meaning=DATASET["DatasetType/image"])
    noAssertion = PermissibleValue(
        text="noAssertion",
        description="data type is not known.",
        meaning=DATASET["DatasetType/noAssertion"])
    numeric = PermissibleValue(
        text="numeric",
        description="data consists only of numeric entries.",
        meaning=DATASET["DatasetType/numeric"])
    other = PermissibleValue(
        text="other",
        description="data is of a type not included in this list.",
        meaning=DATASET["DatasetType/other"])
    sensor = PermissibleValue(
        text="sensor",
        description="data is recorded from a physical sensor, such as a thermometer reading or biometric device.",
        meaning=DATASET["DatasetType/sensor"])
    structured = PermissibleValue(
        text="structured",
        description="data is stored in tabular format or retrieved from a relational database.",
        meaning=DATASET["DatasetType/structured"])
    syntactic = PermissibleValue(
        text="syntactic",
        description="""data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing.""",
        meaning=DATASET["DatasetType/syntactic"])
    text = PermissibleValue(
        text="text",
        description="""data consists of unstructured text, such as a book, Wikipedia article (without images), or transcript.""",
        meaning=DATASET["DatasetType/text"])
    timeseries = PermissibleValue(
        text="timeseries",
        description="""data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day.""",
        meaning=DATASET["DatasetType/timeseries"])
    timestamp = PermissibleValue(
        text="timestamp",
        description="""data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends.""",
        meaning=DATASET["DatasetType/timestamp"])
    video = PermissibleValue(
        text="video",
        description="data is video based, such as a collection of movie clips featuring Tom Hanks.",
        meaning=DATASET["DatasetType/video"])

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
        meaning=SECURITY["CvssSeverityType/critical"])
    high = PermissibleValue(
        text="high",
        description="When a CVSS score is between 7.0 - 8.9",
        meaning=SECURITY["CvssSeverityType/high"])
    low = PermissibleValue(
        text="low",
        description="When a CVSS score is between 0.1 - 3.9",
        meaning=SECURITY["CvssSeverityType/low"])
    medium = PermissibleValue(
        text="medium",
        description="When a CVSS score is between 4.0 - 6.9",
        meaning=SECURITY["CvssSeverityType/medium"])
    none = PermissibleValue(
        text="none",
        description="When a CVSS score is 0.0",
        meaning=SECURITY["CvssSeverityType/none"])

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
        meaning=SECURITY["ExploitCatalogType/kev"])
    other = PermissibleValue(
        text="other",
        description="Other exploit catalogs",
        meaning=SECURITY["ExploitCatalogType/other"])

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
        meaning=SECURITY["SsvcDecisionType/act"])
    attend = PermissibleValue(
        text="attend",
        description="""The vulnerability requires attention from the organization's internal, supervisory-level individuals. Necessary actions include requesting assistance or information about the vulnerability, and may involve publishing a notification either internally and/or externally. CISA recommends remediating Attend vulnerabilities sooner than standard update timelines.""",
        meaning=SECURITY["SsvcDecisionType/attend"])
    track = PermissibleValue(
        text="track",
        description="""The vulnerability does not require action at this time. The organization would continue to track the vulnerability and reassess it if new information becomes available. CISA recommends remediating Track vulnerabilities within standard update timelines.""",
        meaning=SECURITY["SsvcDecisionType/track"])
    trackStar = PermissibleValue(
        text="trackStar",
        description="""(\"Track\*\" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track\* vulnerabilities within standard update timelines.""",
        meaning=SECURITY["SsvcDecisionType/trackStar"])

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
        meaning=SECURITY["VexJustificationType/componentNotPresent"])
    inlineMitigationsAlreadyExist = PermissibleValue(
        text="inlineMitigationsAlreadyExist",
        description="""Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.""",
        meaning=SECURITY["VexJustificationType/inlineMitigationsAlreadyExist"])
    vulnerableCodeCannotBeControlledByAdversary = PermissibleValue(
        text="vulnerableCodeCannotBeControlledByAdversary",
        description="""The vulnerable component is present, and the component contains the vulnerable code. However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.""",
        meaning=SECURITY["VexJustificationType/vulnerableCodeCannotBeControlledByAdversary"])
    vulnerableCodeNotInExecutePath = PermissibleValue(
        text="vulnerableCodeNotInExecutePath",
        description="""The affected code is not reachable through the execution of the code, including non-anticipated states of the product.""",
        meaning=SECURITY["VexJustificationType/vulnerableCodeNotInExecutePath"])
    vulnerableCodeNotPresent = PermissibleValue(
        text="vulnerableCodeNotPresent",
        description="""The product is not affected because the code underlying the vulnerability is not present in the product.""",
        meaning=SECURITY["VexJustificationType/vulnerableCodeNotPresent"])

    _defn = EnumDefinition(
        name="VexJustificationType",
        description="Specifies the VEX justification type.",
    )

class ContentIdentifierType(EnumDefinitionImpl):
    """
    Specifies the type of a content identifier.
    """
    gitoid = PermissibleValue(
        text="gitoid",
        description="""[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).""",
        meaning=SOFTWARE["ContentIdentifierType/gitoid"])
    swhid = PermissibleValue(
        text="swhid",
        description="""SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.""",
        meaning=SOFTWARE["ContentIdentifierType/swhid"])

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
        meaning=SOFTWARE["FileKindType/directory"])
    file = PermissibleValue(
        text="file",
        description="The file represents a single file (default).",
        meaning=SOFTWARE["FileKindType/file"])

    _defn = EnumDefinition(
        name="FileKindType",
        description="Enumeration of the different kinds of SPDX file.",
    )

class SbomType(EnumDefinitionImpl):
    """
    Provides a set of values to be used to describe the common types of SBOMs that
    tools may create.
    """
    analyzed = PermissibleValue(
        text="analyzed",
        description="""SBOM generated through analysis of artifacts (e.g., executables, packages, containers, and virtual machine images) after its build. Such analysis generally requires a variety of heuristics. In some contexts, this may also be referred to as a \"3rd party\" SBOM.""",
        meaning=SOFTWARE["SbomType/analyzed"])
    build = PermissibleValue(
        text="build",
        description="""SBOM generated as part of the process of building the software to create a releasable artifact (e.g., executable or package) from data such as source files, dependencies, built components, build process ephemeral data, and other SBOMs.""",
        meaning=SOFTWARE["SbomType/build"])
    deployed = PermissibleValue(
        text="deployed",
        description="""SBOM provides an inventory of software that is present on a system. This may be an assembly of other SBOMs that combines analysis of configuration options, and examination of execution behavior in a (potentially simulated) deployment environment.""",
        meaning=SOFTWARE["SbomType/deployed"])
    design = PermissibleValue(
        text="design",
        description="""SBOM of intended, planned software project or product with included components (some of which may not yet exist) for a new software artifact.""",
        meaning=SOFTWARE["SbomType/design"])
    runtime = PermissibleValue(
        text="runtime",
        description="""SBOM generated through instrumenting the system running the software, to capture only components present in the system, as well as external call-outs or dynamically loaded components. In some contexts, this may also be referred to as an \"Instrumented\" or \"Dynamic\" SBOM.""",
        meaning=SOFTWARE["SbomType/runtime"])
    source = PermissibleValue(
        text="source",
        description="""SBOM created directly from the development environment, source files, and included dependencies used to build an product artifact.""",
        meaning=SOFTWARE["SbomType/source"])

    _defn = EnumDefinition(
        name="SbomType",
        description="""Provides a set of values to be used to describe the common types of SBOMs that
tools may create.""",
    )

class SoftwarePurpose(EnumDefinitionImpl):
    """
    Provides information about the primary purpose of an Element.
    """
    application = PermissibleValue(
        text="application",
        description="The Element is a software application.",
        meaning=SOFTWARE["SoftwarePurpose/application"])
    archive = PermissibleValue(
        text="archive",
        description="The Element is an archived collection of one or more files (.tar, .zip, etc.).",
        meaning=SOFTWARE["SoftwarePurpose/archive"])
    bom = PermissibleValue(
        text="bom",
        description="The Element is a bill of materials.",
        meaning=SOFTWARE["SoftwarePurpose/bom"])
    configuration = PermissibleValue(
        text="configuration",
        description="The Element is configuration data.",
        meaning=SOFTWARE["SoftwarePurpose/configuration"])
    container = PermissibleValue(
        text="container",
        description="The Element is a container image which can be used by a container runtime application.",
        meaning=SOFTWARE["SoftwarePurpose/container"])
    data = PermissibleValue(
        text="data",
        description="The Element is data.",
        meaning=SOFTWARE["SoftwarePurpose/data"])
    device = PermissibleValue(
        text="device",
        description="The Element refers to a chipset, processor, or electronic board.",
        meaning=SOFTWARE["SoftwarePurpose/device"])
    deviceDriver = PermissibleValue(
        text="deviceDriver",
        description="The Element represents software that controls hardware devices.",
        meaning=SOFTWARE["SoftwarePurpose/deviceDriver"])
    diskImage = PermissibleValue(
        text="diskImage",
        description="""The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.""",
        meaning=SOFTWARE["SoftwarePurpose/diskImage"])
    documentation = PermissibleValue(
        text="documentation",
        description="The Element is documentation.",
        meaning=SOFTWARE["SoftwarePurpose/documentation"])
    evidence = PermissibleValue(
        text="evidence",
        description="The Element is the evidence that a specification or requirement has been fulfilled.",
        meaning=SOFTWARE["SoftwarePurpose/evidence"])
    executable = PermissibleValue(
        text="executable",
        description="The Element is an Artifact that can be run on a computer.",
        meaning=SOFTWARE["SoftwarePurpose/executable"])
    file = PermissibleValue(
        text="file",
        description="""The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.).""",
        meaning=SOFTWARE["SoftwarePurpose/file"])
    filesystemImage = PermissibleValue(
        text="filesystemImage",
        description="The Element is a file system image that can be written to a disk (or virtual) partition.",
        meaning=SOFTWARE["SoftwarePurpose/filesystemImage"])
    firmware = PermissibleValue(
        text="firmware",
        description="The Element provides low level control over a device's hardware.",
        meaning=SOFTWARE["SoftwarePurpose/firmware"])
    framework = PermissibleValue(
        text="framework",
        description="The Element is a software framework.",
        meaning=SOFTWARE["SoftwarePurpose/framework"])
    install = PermissibleValue(
        text="install",
        description="The Element is used to install software on disk.",
        meaning=SOFTWARE["SoftwarePurpose/install"])
    library = PermissibleValue(
        text="library",
        description="The Element is a software library.",
        meaning=SOFTWARE["SoftwarePurpose/library"])
    manifest = PermissibleValue(
        text="manifest",
        description="The Element is a software manifest.",
        meaning=SOFTWARE["SoftwarePurpose/manifest"])
    model = PermissibleValue(
        text="model",
        description="The Element is a machine learning or artificial intelligence model.",
        meaning=SOFTWARE["SoftwarePurpose/model"])
    module = PermissibleValue(
        text="module",
        description="The Element is a module of a piece of software.",
        meaning=SOFTWARE["SoftwarePurpose/module"])
    operatingSystem = PermissibleValue(
        text="operatingSystem",
        description="The Element is an operating system.",
        meaning=SOFTWARE["SoftwarePurpose/operatingSystem"])
    other = PermissibleValue(
        text="other",
        description="The Element doesn't fit into any of the other categories.",
        meaning=SOFTWARE["SoftwarePurpose/other"])
    patch = PermissibleValue(
        text="patch",
        description="The Element contains a set of changes to update, fix, or improve another Element.",
        meaning=SOFTWARE["SoftwarePurpose/patch"])
    platform = PermissibleValue(
        text="platform",
        description="The Element represents a runtime environment.",
        meaning=SOFTWARE["SoftwarePurpose/platform"])
    requirement = PermissibleValue(
        text="requirement",
        description="The Element provides a requirement needed as input for another Element.",
        meaning=SOFTWARE["SoftwarePurpose/requirement"])
    source = PermissibleValue(
        text="source",
        description="The Element is a single or a collection of source files.",
        meaning=SOFTWARE["SoftwarePurpose/source"])
    specification = PermissibleValue(
        text="specification",
        description="The Element is a plan, guideline or strategy how to create, perform or analyze an application.",
        meaning=SOFTWARE["SoftwarePurpose/specification"])
    test = PermissibleValue(
        text="test",
        description="The Element is a test used to verify functionality on an software element.",
        meaning=SOFTWARE["SoftwarePurpose/test"])

    _defn = EnumDefinition(
        name="SoftwarePurpose",
        description="Provides information about the primary purpose of an Element.",
    )

# Slots
class slots:
    pass

slots.autonomyType = Slot(uri=AI.autonomyType, name="autonomyType", curie=AI.curie('autonomyType'),
                   model_uri=SPDX.autonomyType, domain=None, range=Optional[Union[str, "PresenceType"]])

slots.domain = Slot(uri=AI.domain, name="domain", curie=AI.curie('domain'),
                   model_uri=SPDX.domain, domain=None, range=Optional[str])

slots.energyConsumption = Slot(uri=AI.energyConsumption, name="energyConsumption", curie=AI.curie('energyConsumption'),
                   model_uri=SPDX.energyConsumption, domain=None, range=Optional[Union[dict, EnergyConsumption]])

slots.energyQuantity = Slot(uri=AI.energyQuantity, name="energyQuantity", curie=AI.curie('energyQuantity'),
                   model_uri=SPDX.energyQuantity, domain=None, range=Optional[Decimal])

slots.energyUnit = Slot(uri=AI.energyUnit, name="energyUnit", curie=AI.curie('energyUnit'),
                   model_uri=SPDX.energyUnit, domain=None, range=Optional[str])

slots.finetuningEnergyConsumption = Slot(uri=AI.finetuningEnergyConsumption, name="finetuningEnergyConsumption", curie=AI.curie('finetuningEnergyConsumption'),
                   model_uri=SPDX.finetuningEnergyConsumption, domain=None, range=Optional[Union[dict, EnergyConsumptionDescription]])

slots.hyperparameter = Slot(uri=AI.hyperparameter, name="hyperparameter", curie=AI.curie('hyperparameter'),
                   model_uri=SPDX.hyperparameter, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.inferenceEnergyConsumption = Slot(uri=AI.inferenceEnergyConsumption, name="inferenceEnergyConsumption", curie=AI.curie('inferenceEnergyConsumption'),
                   model_uri=SPDX.inferenceEnergyConsumption, domain=None, range=Optional[Union[dict, EnergyConsumptionDescription]])

slots.informationAboutApplication = Slot(uri=AI.informationAboutApplication, name="informationAboutApplication", curie=AI.curie('informationAboutApplication'),
                   model_uri=SPDX.informationAboutApplication, domain=None, range=Optional[str])

slots.informationAboutTraining = Slot(uri=AI.informationAboutTraining, name="informationAboutTraining", curie=AI.curie('informationAboutTraining'),
                   model_uri=SPDX.informationAboutTraining, domain=None, range=Optional[str])

slots.limitation = Slot(uri=AI.limitation, name="limitation", curie=AI.curie('limitation'),
                   model_uri=SPDX.limitation, domain=None, range=Optional[str])

slots.metric = Slot(uri=AI.metric, name="metric", curie=AI.curie('metric'),
                   model_uri=SPDX.metric, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.metricDecisionThreshold = Slot(uri=AI.metricDecisionThreshold, name="metricDecisionThreshold", curie=AI.curie('metricDecisionThreshold'),
                   model_uri=SPDX.metricDecisionThreshold, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.modelDataPreprocessing = Slot(uri=AI.modelDataPreprocessing, name="modelDataPreprocessing", curie=AI.curie('modelDataPreprocessing'),
                   model_uri=SPDX.modelDataPreprocessing, domain=None, range=Optional[str])

slots.modelExplainability = Slot(uri=AI.modelExplainability, name="modelExplainability", curie=AI.curie('modelExplainability'),
                   model_uri=SPDX.modelExplainability, domain=None, range=Optional[str])

slots.safetyRiskAssessment = Slot(uri=AI.safetyRiskAssessment, name="safetyRiskAssessment", curie=AI.curie('safetyRiskAssessment'),
                   model_uri=SPDX.safetyRiskAssessment, domain=None, range=Optional[Union[str, "SafetyRiskAssessmentType"]])

slots.standardCompliance = Slot(uri=AI.standardCompliance, name="standardCompliance", curie=AI.curie('standardCompliance'),
                   model_uri=SPDX.standardCompliance, domain=None, range=Optional[str])

slots.trainingEnergyConsumption = Slot(uri=AI.trainingEnergyConsumption, name="trainingEnergyConsumption", curie=AI.curie('trainingEnergyConsumption'),
                   model_uri=SPDX.trainingEnergyConsumption, domain=None, range=Optional[Union[dict, EnergyConsumptionDescription]])

slots.typeOfModel = Slot(uri=AI.typeOfModel, name="typeOfModel", curie=AI.curie('typeOfModel'),
                   model_uri=SPDX.typeOfModel, domain=None, range=Optional[str])

slots.useSensitivePersonalInformation = Slot(uri=AI.useSensitivePersonalInformation, name="useSensitivePersonalInformation", curie=AI.curie('useSensitivePersonalInformation'),
                   model_uri=SPDX.useSensitivePersonalInformation, domain=None, range=Optional[Union[str, "PresenceType"]])

slots.buildEndTime = Slot(uri=BUILD.buildEndTime, name="buildEndTime", curie=BUILD.curie('buildEndTime'),
                   model_uri=SPDX.buildEndTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.buildId = Slot(uri=BUILD.buildId, name="buildId", curie=BUILD.curie('buildId'),
                   model_uri=SPDX.buildId, domain=None, range=Optional[str])

slots.buildStartTime = Slot(uri=BUILD.buildStartTime, name="buildStartTime", curie=BUILD.curie('buildStartTime'),
                   model_uri=SPDX.buildStartTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.buildType = Slot(uri=BUILD.buildType, name="buildType", curie=BUILD.curie('buildType'),
                   model_uri=SPDX.buildType, domain=None, range=Optional[Union[str, URI]])

slots.configSourceDigest = Slot(uri=BUILD.configSourceDigest, name="configSourceDigest", curie=BUILD.curie('configSourceDigest'),
                   model_uri=SPDX.configSourceDigest, domain=None, range=Optional[Union[dict, Hash]])

slots.configSourceEntrypoint = Slot(uri=BUILD.configSourceEntrypoint, name="configSourceEntrypoint", curie=BUILD.curie('configSourceEntrypoint'),
                   model_uri=SPDX.configSourceEntrypoint, domain=None, range=Optional[str])

slots.configSourceUri = Slot(uri=BUILD.configSourceUri, name="configSourceUri", curie=BUILD.curie('configSourceUri'),
                   model_uri=SPDX.configSourceUri, domain=None, range=Optional[Union[str, URI]])

slots.environment = Slot(uri=BUILD.environment, name="environment", curie=BUILD.curie('environment'),
                   model_uri=SPDX.environment, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.parameter = Slot(uri=BUILD.parameter, name="parameter", curie=BUILD.curie('parameter'),
                   model_uri=SPDX.parameter, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.algorithm = Slot(uri=CORE.algorithm, name="algorithm", curie=CORE.curie('algorithm'),
                   model_uri=SPDX.algorithm, domain=None, range=Optional[str])

slots.annotationType = Slot(uri=CORE.annotationType, name="annotationType", curie=CORE.curie('annotationType'),
                   model_uri=SPDX.annotationType, domain=None, range=Optional[str])

slots.beginIntegerRange = Slot(uri=CORE.beginIntegerRange, name="beginIntegerRange", curie=CORE.curie('beginIntegerRange'),
                   model_uri=SPDX.beginIntegerRange, domain=None, range=Optional[int])

slots.builtTime = Slot(uri=CORE.builtTime, name="builtTime", curie=CORE.curie('builtTime'),
                   model_uri=SPDX.builtTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.comment = Slot(uri=CORE.comment, name="comment", curie=CORE.curie('comment'),
                   model_uri=SPDX.comment, domain=None, range=Optional[str])

slots.completeness = Slot(uri=CORE.completeness, name="completeness", curie=CORE.curie('completeness'),
                   model_uri=SPDX.completeness, domain=None, range=Optional[Union[str, "RelationshipCompleteness"]])

slots.contentType = Slot(uri=CORE.contentType, name="contentType", curie=CORE.curie('contentType'),
                   model_uri=SPDX.contentType, domain=None, range=Optional[str])

slots.context = Slot(uri=CORE.context, name="context", curie=CORE.curie('context'),
                   model_uri=SPDX.context, domain=None, range=Optional[str])

slots.created = Slot(uri=CORE.created, name="created", curie=CORE.curie('created'),
                   model_uri=SPDX.created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.createdBy = Slot(uri=CORE.createdBy, name="createdBy", curie=CORE.curie('createdBy'),
                   model_uri=SPDX.createdBy, domain=None, range=Optional[Union[dict, Agent]])

slots.createdUsing = Slot(uri=CORE.createdUsing, name="createdUsing", curie=CORE.curie('createdUsing'),
                   model_uri=SPDX.createdUsing, domain=None, range=Optional[Union[dict, Tool]])

slots.creationInfo = Slot(uri=CORE.creationInfo, name="creationInfo", curie=CORE.curie('creationInfo'),
                   model_uri=SPDX.creationInfo, domain=None, range=Optional[Union[dict, CreationInfo]])

slots.dataLicense = Slot(uri=CORE.dataLicense, name="dataLicense", curie=CORE.curie('dataLicense'),
                   model_uri=SPDX.dataLicense, domain=None, range=Optional[Union[dict, AnyLicenseInfo]])

slots.definingArtifact = Slot(uri=CORE.definingArtifact, name="definingArtifact", curie=CORE.curie('definingArtifact'),
                   model_uri=SPDX.definingArtifact, domain=None, range=Optional[Union[dict, Artifact]])

slots.description = Slot(uri=CORE.description, name="description", curie=CORE.curie('description'),
                   model_uri=SPDX.description, domain=None, range=Optional[str])

slots.element = Slot(uri=CORE.element, name="element", curie=CORE.curie('element'),
                   model_uri=SPDX.element, domain=None, range=Optional[Union[dict, Element]])

slots.endIntegerRange = Slot(uri=CORE.endIntegerRange, name="endIntegerRange", curie=CORE.curie('endIntegerRange'),
                   model_uri=SPDX.endIntegerRange, domain=None, range=Optional[int])

slots.endTime = Slot(uri=CORE.endTime, name="endTime", curie=CORE.curie('endTime'),
                   model_uri=SPDX.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extension = Slot(uri=CORE.extension, name="extension", curie=CORE.curie('extension'),
                   model_uri=SPDX.extension, domain=None, range=Optional[Union[dict, Extension]])

slots.externalIdentifier = Slot(uri=CORE.externalIdentifier, name="externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=SPDX.externalIdentifier, domain=None, range=Optional[Union[dict, ExternalIdentifier]])

slots.externalIdentifierType = Slot(uri=CORE.externalIdentifierType, name="externalIdentifierType", curie=CORE.curie('externalIdentifierType'),
                   model_uri=SPDX.externalIdentifierType, domain=None, range=Optional[str])

slots.externalRef = Slot(uri=CORE.externalRef, name="externalRef", curie=CORE.curie('externalRef'),
                   model_uri=SPDX.externalRef, domain=None, range=Optional[Union[dict, ExternalRef]])

slots.externalRefType = Slot(uri=CORE.externalRefType, name="externalRefType", curie=CORE.curie('externalRefType'),
                   model_uri=SPDX.externalRefType, domain=None, range=Optional[str])

slots.externalSpdxId = Slot(uri=CORE.externalSpdxId, name="externalSpdxId", curie=CORE.curie('externalSpdxId'),
                   model_uri=SPDX.externalSpdxId, domain=None, range=Optional[Union[str, URI]])

slots.from = Slot(uri=CORE.from, name="from", curie=CORE.curie('from'),
                   model_uri=SPDX.from, domain=None, range=Optional[Union[dict, Element]])

slots.hashValue = Slot(uri=CORE.hashValue, name="hashValue", curie=CORE.curie('hashValue'),
                   model_uri=SPDX.hashValue, domain=None, range=Optional[str])

slots.identifier = Slot(uri=CORE.identifier, name="identifier", curie=CORE.curie('identifier'),
                   model_uri=SPDX.identifier, domain=None, range=Optional[str])

slots.identifierLocator = Slot(uri=CORE.identifierLocator, name="identifierLocator", curie=CORE.curie('identifierLocator'),
                   model_uri=SPDX.identifierLocator, domain=None, range=Optional[Union[str, URI]])

slots.import = Slot(uri=CORE.import, name="import", curie=CORE.curie('import'),
                   model_uri=SPDX.import, domain=None, range=Optional[Union[dict, ExternalMap]])

slots.issuingAuthority = Slot(uri=CORE.issuingAuthority, name="issuingAuthority", curie=CORE.curie('issuingAuthority'),
                   model_uri=SPDX.issuingAuthority, domain=None, range=Optional[str])

slots.key = Slot(uri=CORE.key, name="key", curie=CORE.curie('key'),
                   model_uri=SPDX.key, domain=None, range=Optional[str])

slots.locationHint = Slot(uri=CORE.locationHint, name="locationHint", curie=CORE.curie('locationHint'),
                   model_uri=SPDX.locationHint, domain=None, range=Optional[Union[str, URI]])

slots.core_locator = Slot(uri=CORE.locator, name="core_locator", curie=CORE.curie('locator'),
                   model_uri=SPDX.core_locator, domain=None, range=Optional[str])

slots.name = Slot(uri=CORE.name, name="name", curie=CORE.curie('name'),
                   model_uri=SPDX.name, domain=None, range=Optional[str])

slots.namespace = Slot(uri=CORE.namespace, name="namespace", curie=CORE.curie('namespace'),
                   model_uri=SPDX.namespace, domain=None, range=Optional[Union[str, URI]])

slots.namespaceMap = Slot(uri=CORE.namespaceMap, name="namespaceMap", curie=CORE.curie('namespaceMap'),
                   model_uri=SPDX.namespaceMap, domain=None, range=Optional[Union[dict, NamespaceMap]])

slots.originatedBy = Slot(uri=CORE.originatedBy, name="originatedBy", curie=CORE.curie('originatedBy'),
                   model_uri=SPDX.originatedBy, domain=None, range=Optional[Union[dict, Agent]])

slots.packageVerificationCodeExcludedFile = Slot(uri=CORE.packageVerificationCodeExcludedFile, name="packageVerificationCodeExcludedFile", curie=CORE.curie('packageVerificationCodeExcludedFile'),
                   model_uri=SPDX.packageVerificationCodeExcludedFile, domain=None, range=Optional[str])

slots.prefix = Slot(uri=CORE.prefix, name="prefix", curie=CORE.curie('prefix'),
                   model_uri=SPDX.prefix, domain=None, range=Optional[str])

slots.profileConformance = Slot(uri=CORE.profileConformance, name="profileConformance", curie=CORE.curie('profileConformance'),
                   model_uri=SPDX.profileConformance, domain=None, range=Optional[Union[str, "ProfileIdentifierType"]])

slots.relationshipType = Slot(uri=CORE.relationshipType, name="relationshipType", curie=CORE.curie('relationshipType'),
                   model_uri=SPDX.relationshipType, domain=None, range=Optional[str])

slots.releaseTime = Slot(uri=CORE.releaseTime, name="releaseTime", curie=CORE.curie('releaseTime'),
                   model_uri=SPDX.releaseTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.rootElement = Slot(uri=CORE.rootElement, name="rootElement", curie=CORE.curie('rootElement'),
                   model_uri=SPDX.rootElement, domain=None, range=Optional[Union[dict, Element]])

slots.scope = Slot(uri=CORE.scope, name="scope", curie=CORE.curie('scope'),
                   model_uri=SPDX.scope, domain=None, range=Optional[str])

slots.specVersion = Slot(uri=CORE.specVersion, name="specVersion", curie=CORE.curie('specVersion'),
                   model_uri=SPDX.specVersion, domain=None, range=Optional[str])

slots.standardName = Slot(uri=CORE.standardName, name="standardName", curie=CORE.curie('standardName'),
                   model_uri=SPDX.standardName, domain=None, range=Optional[str])

slots.startTime = Slot(uri=CORE.startTime, name="startTime", curie=CORE.curie('startTime'),
                   model_uri=SPDX.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statement = Slot(uri=CORE.statement, name="statement", curie=CORE.curie('statement'),
                   model_uri=SPDX.statement, domain=None, range=Optional[str])

slots.subject = Slot(uri=CORE.subject, name="subject", curie=CORE.curie('subject'),
                   model_uri=SPDX.subject, domain=None, range=Optional[Union[dict, Element]])

slots.summary = Slot(uri=CORE.summary, name="summary", curie=CORE.curie('summary'),
                   model_uri=SPDX.summary, domain=None, range=Optional[str])

slots.suppliedBy = Slot(uri=CORE.suppliedBy, name="suppliedBy", curie=CORE.curie('suppliedBy'),
                   model_uri=SPDX.suppliedBy, domain=None, range=Optional[Union[dict, Agent]])

slots.supportLevel = Slot(uri=CORE.supportLevel, name="supportLevel", curie=CORE.curie('supportLevel'),
                   model_uri=SPDX.supportLevel, domain=None, range=Optional[Union[str, "SupportType"]])

slots.to = Slot(uri=CORE.to, name="to", curie=CORE.curie('to'),
                   model_uri=SPDX.to, domain=None, range=Optional[Union[dict, Element]])

slots.validUntilTime = Slot(uri=CORE.validUntilTime, name="validUntilTime", curie=CORE.curie('validUntilTime'),
                   model_uri=SPDX.validUntilTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.value = Slot(uri=CORE.value, name="value", curie=CORE.curie('value'),
                   model_uri=SPDX.value, domain=None, range=Optional[str])

slots.verifiedUsing = Slot(uri=CORE.verifiedUsing, name="verifiedUsing", curie=CORE.curie('verifiedUsing'),
                   model_uri=SPDX.verifiedUsing, domain=None, range=Optional[Union[dict, IntegrityMethod]])

slots.anonymizationMethodUsed = Slot(uri=DATASET.anonymizationMethodUsed, name="anonymizationMethodUsed", curie=DATASET.curie('anonymizationMethodUsed'),
                   model_uri=SPDX.anonymizationMethodUsed, domain=None, range=Optional[str])

slots.confidentialityLevel = Slot(uri=DATASET.confidentialityLevel, name="confidentialityLevel", curie=DATASET.curie('confidentialityLevel'),
                   model_uri=SPDX.confidentialityLevel, domain=None, range=Optional[Union[str, "ConfidentialityLevelType"]])

slots.dataCollectionProcess = Slot(uri=DATASET.dataCollectionProcess, name="dataCollectionProcess", curie=DATASET.curie('dataCollectionProcess'),
                   model_uri=SPDX.dataCollectionProcess, domain=None, range=Optional[str])

slots.dataPreprocessing = Slot(uri=DATASET.dataPreprocessing, name="dataPreprocessing", curie=DATASET.curie('dataPreprocessing'),
                   model_uri=SPDX.dataPreprocessing, domain=None, range=Optional[str])

slots.datasetAvailability = Slot(uri=DATASET.datasetAvailability, name="datasetAvailability", curie=DATASET.curie('datasetAvailability'),
                   model_uri=SPDX.datasetAvailability, domain=None, range=Optional[Union[str, "DatasetAvailabilityType"]])

slots.datasetNoise = Slot(uri=DATASET.datasetNoise, name="datasetNoise", curie=DATASET.curie('datasetNoise'),
                   model_uri=SPDX.datasetNoise, domain=None, range=Optional[str])

slots.datasetSize = Slot(uri=DATASET.datasetSize, name="datasetSize", curie=DATASET.curie('datasetSize'),
                   model_uri=SPDX.datasetSize, domain=None, range=Optional[int])

slots.datasetType = Slot(uri=DATASET.datasetType, name="datasetType", curie=DATASET.curie('datasetType'),
                   model_uri=SPDX.datasetType, domain=None, range=Optional[str])

slots.datasetUpdateMechanism = Slot(uri=DATASET.datasetUpdateMechanism, name="datasetUpdateMechanism", curie=DATASET.curie('datasetUpdateMechanism'),
                   model_uri=SPDX.datasetUpdateMechanism, domain=None, range=Optional[str])

slots.hasSensitivePersonalInformation = Slot(uri=DATASET.hasSensitivePersonalInformation, name="hasSensitivePersonalInformation", curie=DATASET.curie('hasSensitivePersonalInformation'),
                   model_uri=SPDX.hasSensitivePersonalInformation, domain=None, range=Optional[Union[str, "PresenceType"]])

slots.intendedUse = Slot(uri=DATASET.intendedUse, name="intendedUse", curie=DATASET.curie('intendedUse'),
                   model_uri=SPDX.intendedUse, domain=None, range=Optional[str])

slots.knownBias = Slot(uri=DATASET.knownBias, name="knownBias", curie=DATASET.curie('knownBias'),
                   model_uri=SPDX.knownBias, domain=None, range=Optional[str])

slots.sensor = Slot(uri=DATASET.sensor, name="sensor", curie=DATASET.curie('sensor'),
                   model_uri=SPDX.sensor, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.additionText = Slot(uri=EXPANDEDLICENSING.additionText, name="additionText", curie=EXPANDEDLICENSING.curie('additionText'),
                   model_uri=SPDX.additionText, domain=None, range=Optional[str])

slots.deprecatedVersion = Slot(uri=EXPANDEDLICENSING.deprecatedVersion, name="deprecatedVersion", curie=EXPANDEDLICENSING.curie('deprecatedVersion'),
                   model_uri=SPDX.deprecatedVersion, domain=None, range=Optional[str])

slots.isDeprecatedAdditionId = Slot(uri=EXPANDEDLICENSING.isDeprecatedAdditionId, name="isDeprecatedAdditionId", curie=EXPANDEDLICENSING.curie('isDeprecatedAdditionId'),
                   model_uri=SPDX.isDeprecatedAdditionId, domain=None, range=Optional[Union[bool, Bool]])

slots.isDeprecatedLicenseId = Slot(uri=EXPANDEDLICENSING.isDeprecatedLicenseId, name="isDeprecatedLicenseId", curie=EXPANDEDLICENSING.curie('isDeprecatedLicenseId'),
                   model_uri=SPDX.isDeprecatedLicenseId, domain=None, range=Optional[Union[bool, Bool]])

slots.isFsfLibre = Slot(uri=EXPANDEDLICENSING.isFsfLibre, name="isFsfLibre", curie=EXPANDEDLICENSING.curie('isFsfLibre'),
                   model_uri=SPDX.isFsfLibre, domain=None, range=Optional[Union[bool, Bool]])

slots.isOsiApproved = Slot(uri=EXPANDEDLICENSING.isOsiApproved, name="isOsiApproved", curie=EXPANDEDLICENSING.curie('isOsiApproved'),
                   model_uri=SPDX.isOsiApproved, domain=None, range=Optional[Union[bool, Bool]])

slots.licenseXml = Slot(uri=EXPANDEDLICENSING.licenseXml, name="licenseXml", curie=EXPANDEDLICENSING.curie('licenseXml'),
                   model_uri=SPDX.licenseXml, domain=None, range=Optional[str])

slots.listVersionAdded = Slot(uri=EXPANDEDLICENSING.listVersionAdded, name="listVersionAdded", curie=EXPANDEDLICENSING.curie('listVersionAdded'),
                   model_uri=SPDX.listVersionAdded, domain=None, range=Optional[str])

slots.member = Slot(uri=EXPANDEDLICENSING.member, name="member", curie=EXPANDEDLICENSING.curie('member'),
                   model_uri=SPDX.member, domain=None, range=Optional[Union[dict, AnyLicenseInfo]])

slots.obsoletedBy = Slot(uri=EXPANDEDLICENSING.obsoletedBy, name="obsoletedBy", curie=EXPANDEDLICENSING.curie('obsoletedBy'),
                   model_uri=SPDX.obsoletedBy, domain=None, range=Optional[str])

slots.seeAlso = Slot(uri=EXPANDEDLICENSING.seeAlso, name="seeAlso", curie=EXPANDEDLICENSING.curie('seeAlso'),
                   model_uri=SPDX.seeAlso, domain=None, range=Optional[Union[str, URI]])

slots.standardAdditionTemplate = Slot(uri=EXPANDEDLICENSING.standardAdditionTemplate, name="standardAdditionTemplate", curie=EXPANDEDLICENSING.curie('standardAdditionTemplate'),
                   model_uri=SPDX.standardAdditionTemplate, domain=None, range=Optional[str])

slots.standardLicenseHeader = Slot(uri=EXPANDEDLICENSING.standardLicenseHeader, name="standardLicenseHeader", curie=EXPANDEDLICENSING.curie('standardLicenseHeader'),
                   model_uri=SPDX.standardLicenseHeader, domain=None, range=Optional[str])

slots.standardLicenseTemplate = Slot(uri=EXPANDEDLICENSING.standardLicenseTemplate, name="standardLicenseTemplate", curie=EXPANDEDLICENSING.curie('standardLicenseTemplate'),
                   model_uri=SPDX.standardLicenseTemplate, domain=None, range=Optional[str])

slots.subjectAddition = Slot(uri=EXPANDEDLICENSING.subjectAddition, name="subjectAddition", curie=EXPANDEDLICENSING.curie('subjectAddition'),
                   model_uri=SPDX.subjectAddition, domain=None, range=Optional[Union[dict, LicenseAddition]])

slots.subjectExtendableLicense = Slot(uri=EXPANDEDLICENSING.subjectExtendableLicense, name="subjectExtendableLicense", curie=EXPANDEDLICENSING.curie('subjectExtendableLicense'),
                   model_uri=SPDX.subjectExtendableLicense, domain=None, range=Optional[Union[dict, ExtendableLicense]])

slots.subjectLicense = Slot(uri=EXPANDEDLICENSING.subjectLicense, name="subjectLicense", curie=EXPANDEDLICENSING.curie('subjectLicense'),
                   model_uri=SPDX.subjectLicense, domain=None, range=Optional[Union[dict, License]])

slots.cdxPropName = Slot(uri=EXTENSION.cdxPropName, name="cdxPropName", curie=EXTENSION.curie('cdxPropName'),
                   model_uri=SPDX.cdxPropName, domain=None, range=Optional[str])

slots.cdxPropValue = Slot(uri=EXTENSION.cdxPropValue, name="cdxPropValue", curie=EXTENSION.curie('cdxPropValue'),
                   model_uri=SPDX.cdxPropValue, domain=None, range=Optional[str])

slots.cdxProperty = Slot(uri=EXTENSION.cdxProperty, name="cdxProperty", curie=EXTENSION.curie('cdxProperty'),
                   model_uri=SPDX.cdxProperty, domain=None, range=Optional[Union[dict, CdxPropertyEntry]])

slots.actionStatement = Slot(uri=SECURITY.actionStatement, name="actionStatement", curie=SECURITY.curie('actionStatement'),
                   model_uri=SPDX.actionStatement, domain=None, range=Optional[str])

slots.actionStatementTime = Slot(uri=SECURITY.actionStatementTime, name="actionStatementTime", curie=SECURITY.curie('actionStatementTime'),
                   model_uri=SPDX.actionStatementTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.assessedElement = Slot(uri=SECURITY.assessedElement, name="assessedElement", curie=SECURITY.curie('assessedElement'),
                   model_uri=SPDX.assessedElement, domain=None, range=Optional[Union[dict, SoftwareArtifact]])

slots.catalogType = Slot(uri=SECURITY.catalogType, name="catalogType", curie=SECURITY.curie('catalogType'),
                   model_uri=SPDX.catalogType, domain=None, range=Optional[str])

slots.decisionType = Slot(uri=SECURITY.decisionType, name="decisionType", curie=SECURITY.curie('decisionType'),
                   model_uri=SPDX.decisionType, domain=None, range=Optional[Union[str, "SsvcDecisionType"]])

slots.exploited = Slot(uri=SECURITY.exploited, name="exploited", curie=SECURITY.curie('exploited'),
                   model_uri=SPDX.exploited, domain=None, range=Optional[Union[bool, Bool]])

slots.impactStatement = Slot(uri=SECURITY.impactStatement, name="impactStatement", curie=SECURITY.curie('impactStatement'),
                   model_uri=SPDX.impactStatement, domain=None, range=Optional[str])

slots.impactStatementTime = Slot(uri=SECURITY.impactStatementTime, name="impactStatementTime", curie=SECURITY.curie('impactStatementTime'),
                   model_uri=SPDX.impactStatementTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.justificationType = Slot(uri=SECURITY.justificationType, name="justificationType", curie=SECURITY.curie('justificationType'),
                   model_uri=SPDX.justificationType, domain=None, range=Optional[Union[str, "VexJustificationType"]])

slots.security_locator = Slot(uri=SECURITY.locator, name="security_locator", curie=SECURITY.curie('locator'),
                   model_uri=SPDX.security_locator, domain=None, range=Optional[Union[str, URI]])

slots.modifiedTime = Slot(uri=SECURITY.modifiedTime, name="modifiedTime", curie=SECURITY.curie('modifiedTime'),
                   model_uri=SPDX.modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.percentile = Slot(uri=SECURITY.percentile, name="percentile", curie=SECURITY.curie('percentile'),
                   model_uri=SPDX.percentile, domain=None, range=Optional[Decimal])

slots.probability = Slot(uri=SECURITY.probability, name="probability", curie=SECURITY.curie('probability'),
                   model_uri=SPDX.probability, domain=None, range=Optional[Decimal])

slots.publishedTime = Slot(uri=SECURITY.publishedTime, name="publishedTime", curie=SECURITY.curie('publishedTime'),
                   model_uri=SPDX.publishedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.score = Slot(uri=SECURITY.score, name="score", curie=SECURITY.curie('score'),
                   model_uri=SPDX.score, domain=None, range=Optional[Decimal])

slots.severity = Slot(uri=SECURITY.severity, name="severity", curie=SECURITY.curie('severity'),
                   model_uri=SPDX.severity, domain=None, range=Optional[Union[str, "CvssSeverityType"]])

slots.statusNotes = Slot(uri=SECURITY.statusNotes, name="statusNotes", curie=SECURITY.curie('statusNotes'),
                   model_uri=SPDX.statusNotes, domain=None, range=Optional[str])

slots.vectorString = Slot(uri=SECURITY.vectorString, name="vectorString", curie=SECURITY.curie('vectorString'),
                   model_uri=SPDX.vectorString, domain=None, range=Optional[str])

slots.vexVersion = Slot(uri=SECURITY.vexVersion, name="vexVersion", curie=SECURITY.curie('vexVersion'),
                   model_uri=SPDX.vexVersion, domain=None, range=Optional[str])

slots.withdrawnTime = Slot(uri=SECURITY.withdrawnTime, name="withdrawnTime", curie=SECURITY.curie('withdrawnTime'),
                   model_uri=SPDX.withdrawnTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.customIdToUri = Slot(uri=SIMPLELICENSING.customIdToUri, name="customIdToUri", curie=SIMPLELICENSING.curie('customIdToUri'),
                   model_uri=SPDX.customIdToUri, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.licenseExpression = Slot(uri=SIMPLELICENSING.licenseExpression, name="licenseExpression", curie=SIMPLELICENSING.curie('licenseExpression'),
                   model_uri=SPDX.licenseExpression, domain=None, range=Optional[str])

slots.licenseListVersion = Slot(uri=SIMPLELICENSING.licenseListVersion, name="licenseListVersion", curie=SIMPLELICENSING.curie('licenseListVersion'),
                   model_uri=SPDX.licenseListVersion, domain=None, range=Optional[str])

slots.licenseText = Slot(uri=SIMPLELICENSING.licenseText, name="licenseText", curie=SIMPLELICENSING.curie('licenseText'),
                   model_uri=SPDX.licenseText, domain=None, range=Optional[str])

slots.additionalPurpose = Slot(uri=SOFTWARE.additionalPurpose, name="additionalPurpose", curie=SOFTWARE.curie('additionalPurpose'),
                   model_uri=SPDX.additionalPurpose, domain=None, range=Optional[str])

slots.attributionText = Slot(uri=SOFTWARE.attributionText, name="attributionText", curie=SOFTWARE.curie('attributionText'),
                   model_uri=SPDX.attributionText, domain=None, range=Optional[str])

slots.byteRange = Slot(uri=SOFTWARE.byteRange, name="byteRange", curie=SOFTWARE.curie('byteRange'),
                   model_uri=SPDX.byteRange, domain=None, range=Optional[Union[dict, PositiveIntegerRange]])

slots.contentIdentifier = Slot(uri=SOFTWARE.contentIdentifier, name="contentIdentifier", curie=SOFTWARE.curie('contentIdentifier'),
                   model_uri=SPDX.contentIdentifier, domain=None, range=Optional[Union[dict, ContentIdentifier]])

slots.contentIdentifierType = Slot(uri=SOFTWARE.contentIdentifierType, name="contentIdentifierType", curie=SOFTWARE.curie('contentIdentifierType'),
                   model_uri=SPDX.contentIdentifierType, domain=None, range=Optional[Union[str, "ContentIdentifierType"]])

slots.contentIdentifierValue = Slot(uri=SOFTWARE.contentIdentifierValue, name="contentIdentifierValue", curie=SOFTWARE.curie('contentIdentifierValue'),
                   model_uri=SPDX.contentIdentifierValue, domain=None, range=Optional[Union[str, URI]])

slots.copyrightText = Slot(uri=SOFTWARE.copyrightText, name="copyrightText", curie=SOFTWARE.curie('copyrightText'),
                   model_uri=SPDX.copyrightText, domain=None, range=Optional[str])

slots.downloadLocation = Slot(uri=SOFTWARE.downloadLocation, name="downloadLocation", curie=SOFTWARE.curie('downloadLocation'),
                   model_uri=SPDX.downloadLocation, domain=None, range=Optional[Union[str, URI]])

slots.fileKind = Slot(uri=SOFTWARE.fileKind, name="fileKind", curie=SOFTWARE.curie('fileKind'),
                   model_uri=SPDX.fileKind, domain=None, range=Optional[Union[str, "FileKindType"]])

slots.homePage = Slot(uri=SOFTWARE.homePage, name="homePage", curie=SOFTWARE.curie('homePage'),
                   model_uri=SPDX.homePage, domain=None, range=Optional[Union[str, URI]])

slots.lineRange = Slot(uri=SOFTWARE.lineRange, name="lineRange", curie=SOFTWARE.curie('lineRange'),
                   model_uri=SPDX.lineRange, domain=None, range=Optional[Union[dict, PositiveIntegerRange]])

slots.packageUrl = Slot(uri=SOFTWARE.packageUrl, name="packageUrl", curie=SOFTWARE.curie('packageUrl'),
                   model_uri=SPDX.packageUrl, domain=None, range=Optional[Union[str, URI]])

slots.packageVersion = Slot(uri=SOFTWARE.packageVersion, name="packageVersion", curie=SOFTWARE.curie('packageVersion'),
                   model_uri=SPDX.packageVersion, domain=None, range=Optional[str])

slots.primaryPurpose = Slot(uri=SOFTWARE.primaryPurpose, name="primaryPurpose", curie=SOFTWARE.curie('primaryPurpose'),
                   model_uri=SPDX.primaryPurpose, domain=None, range=Optional[str])

slots.sbomType = Slot(uri=SOFTWARE.sbomType, name="sbomType", curie=SOFTWARE.curie('sbomType'),
                   model_uri=SPDX.sbomType, domain=None, range=Optional[Union[str, "SbomType"]])

slots.snippetFromFile = Slot(uri=SOFTWARE.snippetFromFile, name="snippetFromFile", curie=SOFTWARE.curie('snippetFromFile'),
                   model_uri=SPDX.snippetFromFile, domain=None, range=Optional[Union[dict, File]])

slots.sourceInfo = Slot(uri=SOFTWARE.sourceInfo, name="sourceInfo", curie=SOFTWARE.curie('sourceInfo'),
                   model_uri=SPDX.sourceInfo, domain=None, range=Optional[str])

slots.AIPackage_informationAboutTraining = Slot(uri=AI.informationAboutTraining, name="AIPackage_informationAboutTraining", curie=AI.curie('informationAboutTraining'),
                   model_uri=SPDX.AIPackage_informationAboutTraining, domain=AIPackage, range=Optional[str])

slots.AIPackage_modelDataPreprocessing = Slot(uri=AI.modelDataPreprocessing, name="AIPackage_modelDataPreprocessing", curie=AI.curie('modelDataPreprocessing'),
                   model_uri=SPDX.AIPackage_modelDataPreprocessing, domain=AIPackage, range=Optional[Union[str, list[str]]])

slots.AIPackage_typeOfModel = Slot(uri=AI.typeOfModel, name="AIPackage_typeOfModel", curie=AI.curie('typeOfModel'),
                   model_uri=SPDX.AIPackage_typeOfModel, domain=AIPackage, range=Optional[Union[str, list[str]]])

slots.AIPackage_safetyRiskAssessment = Slot(uri=AI.safetyRiskAssessment, name="AIPackage_safetyRiskAssessment", curie=AI.curie('safetyRiskAssessment'),
                   model_uri=SPDX.AIPackage_safetyRiskAssessment, domain=AIPackage, range=Optional[Union[str, "SafetyRiskAssessmentType"]])

slots.AIPackage_metricDecisionThreshold = Slot(uri=AI.metricDecisionThreshold, name="AIPackage_metricDecisionThreshold", curie=AI.curie('metricDecisionThreshold'),
                   model_uri=SPDX.AIPackage_metricDecisionThreshold, domain=AIPackage, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.AIPackage_useSensitivePersonalInformation = Slot(uri=AI.useSensitivePersonalInformation, name="AIPackage_useSensitivePersonalInformation", curie=AI.curie('useSensitivePersonalInformation'),
                   model_uri=SPDX.AIPackage_useSensitivePersonalInformation, domain=AIPackage, range=Optional[Union[str, "PresenceType"]])

slots.AIPackage_energyConsumption = Slot(uri=AI.energyConsumption, name="AIPackage_energyConsumption", curie=AI.curie('energyConsumption'),
                   model_uri=SPDX.AIPackage_energyConsumption, domain=AIPackage, range=Optional[Union[dict, EnergyConsumption]])

slots.AIPackage_limitation = Slot(uri=AI.limitation, name="AIPackage_limitation", curie=AI.curie('limitation'),
                   model_uri=SPDX.AIPackage_limitation, domain=AIPackage, range=Optional[str])

slots.AIPackage_hyperparameter = Slot(uri=AI.hyperparameter, name="AIPackage_hyperparameter", curie=AI.curie('hyperparameter'),
                   model_uri=SPDX.AIPackage_hyperparameter, domain=AIPackage, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.AIPackage_autonomyType = Slot(uri=AI.autonomyType, name="AIPackage_autonomyType", curie=AI.curie('autonomyType'),
                   model_uri=SPDX.AIPackage_autonomyType, domain=AIPackage, range=Optional[Union[str, "PresenceType"]])

slots.AIPackage_domain = Slot(uri=AI.domain, name="AIPackage_domain", curie=AI.curie('domain'),
                   model_uri=SPDX.AIPackage_domain, domain=AIPackage, range=Optional[Union[str, list[str]]])

slots.AIPackage_modelExplainability = Slot(uri=AI.modelExplainability, name="AIPackage_modelExplainability", curie=AI.curie('modelExplainability'),
                   model_uri=SPDX.AIPackage_modelExplainability, domain=AIPackage, range=Optional[Union[str, list[str]]])

slots.AIPackage_informationAboutApplication = Slot(uri=AI.informationAboutApplication, name="AIPackage_informationAboutApplication", curie=AI.curie('informationAboutApplication'),
                   model_uri=SPDX.AIPackage_informationAboutApplication, domain=AIPackage, range=Optional[str])

slots.AIPackage_metric = Slot(uri=AI.metric, name="AIPackage_metric", curie=AI.curie('metric'),
                   model_uri=SPDX.AIPackage_metric, domain=AIPackage, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.AIPackage_standardCompliance = Slot(uri=AI.standardCompliance, name="AIPackage_standardCompliance", curie=AI.curie('standardCompliance'),
                   model_uri=SPDX.AIPackage_standardCompliance, domain=AIPackage, range=Optional[Union[str, list[str]]])

slots.EnergyConsumption_finetuningEnergyConsumption = Slot(uri=AI.finetuningEnergyConsumption, name="EnergyConsumption_finetuningEnergyConsumption", curie=AI.curie('finetuningEnergyConsumption'),
                   model_uri=SPDX.EnergyConsumption_finetuningEnergyConsumption, domain=EnergyConsumption, range=Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]])

slots.EnergyConsumption_inferenceEnergyConsumption = Slot(uri=AI.inferenceEnergyConsumption, name="EnergyConsumption_inferenceEnergyConsumption", curie=AI.curie('inferenceEnergyConsumption'),
                   model_uri=SPDX.EnergyConsumption_inferenceEnergyConsumption, domain=EnergyConsumption, range=Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]])

slots.EnergyConsumption_trainingEnergyConsumption = Slot(uri=AI.trainingEnergyConsumption, name="EnergyConsumption_trainingEnergyConsumption", curie=AI.curie('trainingEnergyConsumption'),
                   model_uri=SPDX.EnergyConsumption_trainingEnergyConsumption, domain=EnergyConsumption, range=Optional[Union[Union[dict, "EnergyConsumptionDescription"], list[Union[dict, "EnergyConsumptionDescription"]]]])

slots.EnergyConsumptionDescription_energyQuantity = Slot(uri=AI.energyQuantity, name="EnergyConsumptionDescription_energyQuantity", curie=AI.curie('energyQuantity'),
                   model_uri=SPDX.EnergyConsumptionDescription_energyQuantity, domain=EnergyConsumptionDescription, range=Decimal)

slots.EnergyConsumptionDescription_energyUnit = Slot(uri=AI.energyUnit, name="EnergyConsumptionDescription_energyUnit", curie=AI.curie('energyUnit'),
                   model_uri=SPDX.EnergyConsumptionDescription_energyUnit, domain=EnergyConsumptionDescription, range=str)

slots.Build_buildType = Slot(uri=BUILD.buildType, name="Build_buildType", curie=BUILD.curie('buildType'),
                   model_uri=SPDX.Build_buildType, domain=Build, range=Union[str, URI])

slots.Build_buildEndTime = Slot(uri=BUILD.buildEndTime, name="Build_buildEndTime", curie=BUILD.curie('buildEndTime'),
                   model_uri=SPDX.Build_buildEndTime, domain=Build, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Build_buildId = Slot(uri=BUILD.buildId, name="Build_buildId", curie=BUILD.curie('buildId'),
                   model_uri=SPDX.Build_buildId, domain=Build, range=Optional[str])

slots.Build_configSourceDigest = Slot(uri=BUILD.configSourceDigest, name="Build_configSourceDigest", curie=BUILD.curie('configSourceDigest'),
                   model_uri=SPDX.Build_configSourceDigest, domain=Build, range=Optional[Union[Union[dict, "Hash"], list[Union[dict, "Hash"]]]])

slots.Build_buildStartTime = Slot(uri=BUILD.buildStartTime, name="Build_buildStartTime", curie=BUILD.curie('buildStartTime'),
                   model_uri=SPDX.Build_buildStartTime, domain=Build, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Build_configSourceUri = Slot(uri=BUILD.configSourceUri, name="Build_configSourceUri", curie=BUILD.curie('configSourceUri'),
                   model_uri=SPDX.Build_configSourceUri, domain=Build, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Build_parameter = Slot(uri=BUILD.parameter, name="Build_parameter", curie=BUILD.curie('parameter'),
                   model_uri=SPDX.Build_parameter, domain=Build, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.Build_configSourceEntrypoint = Slot(uri=BUILD.configSourceEntrypoint, name="Build_configSourceEntrypoint", curie=BUILD.curie('configSourceEntrypoint'),
                   model_uri=SPDX.Build_configSourceEntrypoint, domain=Build, range=Optional[Union[str, list[str]]])

slots.Build_environment = Slot(uri=BUILD.environment, name="Build_environment", curie=BUILD.curie('environment'),
                   model_uri=SPDX.Build_environment, domain=Build, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.Annotation_contentType = Slot(uri=CORE.contentType, name="Annotation_contentType", curie=CORE.curie('contentType'),
                   model_uri=SPDX.Annotation_contentType, domain=Annotation, range=Optional[str],
                   pattern=re.compile(r'^[^\/]+\/[^\/]+$'))

slots.Annotation_statement = Slot(uri=CORE.statement, name="Annotation_statement", curie=CORE.curie('statement'),
                   model_uri=SPDX.Annotation_statement, domain=Annotation, range=Optional[str])

slots.Annotation_subject = Slot(uri=CORE.subject, name="Annotation_subject", curie=CORE.curie('subject'),
                   model_uri=SPDX.Annotation_subject, domain=Annotation, range=Union[dict, Element])

slots.Annotation_annotationType = Slot(uri=CORE.annotationType, name="Annotation_annotationType", curie=CORE.curie('annotationType'),
                   model_uri=SPDX.Annotation_annotationType, domain=Annotation, range=str)

slots.Artifact_standardName = Slot(uri=CORE.standardName, name="Artifact_standardName", curie=CORE.curie('standardName'),
                   model_uri=SPDX.Artifact_standardName, domain=Artifact, range=Optional[Union[str, list[str]]])

slots.Artifact_builtTime = Slot(uri=CORE.builtTime, name="Artifact_builtTime", curie=CORE.curie('builtTime'),
                   model_uri=SPDX.Artifact_builtTime, domain=Artifact, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Artifact_validUntilTime = Slot(uri=CORE.validUntilTime, name="Artifact_validUntilTime", curie=CORE.curie('validUntilTime'),
                   model_uri=SPDX.Artifact_validUntilTime, domain=Artifact, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Artifact_supportLevel = Slot(uri=CORE.supportLevel, name="Artifact_supportLevel", curie=CORE.curie('supportLevel'),
                   model_uri=SPDX.Artifact_supportLevel, domain=Artifact, range=Optional[Union[Union[str, "SupportType"], list[Union[str, "SupportType"]]]])

slots.Artifact_suppliedBy = Slot(uri=CORE.suppliedBy, name="Artifact_suppliedBy", curie=CORE.curie('suppliedBy'),
                   model_uri=SPDX.Artifact_suppliedBy, domain=Artifact, range=Optional[Union[dict, Agent]])

slots.Artifact_originatedBy = Slot(uri=CORE.originatedBy, name="Artifact_originatedBy", curie=CORE.curie('originatedBy'),
                   model_uri=SPDX.Artifact_originatedBy, domain=Artifact, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.Artifact_releaseTime = Slot(uri=CORE.releaseTime, name="Artifact_releaseTime", curie=CORE.curie('releaseTime'),
                   model_uri=SPDX.Artifact_releaseTime, domain=Artifact, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Bundle_context = Slot(uri=CORE.context, name="Bundle_context", curie=CORE.curie('context'),
                   model_uri=SPDX.Bundle_context, domain=Bundle, range=Optional[str])

slots.CreationInfo_createdBy = Slot(uri=CORE.createdBy, name="CreationInfo_createdBy", curie=CORE.curie('createdBy'),
                   model_uri=SPDX.CreationInfo_createdBy, domain=CreationInfo, range=Union[Union[dict, "Agent"], list[Union[dict, "Agent"]]])

slots.CreationInfo_createdUsing = Slot(uri=CORE.createdUsing, name="CreationInfo_createdUsing", curie=CORE.curie('createdUsing'),
                   model_uri=SPDX.CreationInfo_createdUsing, domain=CreationInfo, range=Optional[Union[Union[dict, "Tool"], list[Union[dict, "Tool"]]]])

slots.CreationInfo_created = Slot(uri=CORE.created, name="CreationInfo_created", curie=CORE.curie('created'),
                   model_uri=SPDX.CreationInfo_created, domain=CreationInfo, range=Union[str, XSDDateTime],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.CreationInfo_specVersion = Slot(uri=CORE.specVersion, name="CreationInfo_specVersion", curie=CORE.curie('specVersion'),
                   model_uri=SPDX.CreationInfo_specVersion, domain=CreationInfo, range=str,
                   pattern=re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'))

slots.CreationInfo_comment = Slot(uri=CORE.comment, name="CreationInfo_comment", curie=CORE.curie('comment'),
                   model_uri=SPDX.CreationInfo_comment, domain=CreationInfo, range=Optional[str])

slots.DictionaryEntry_value = Slot(uri=CORE.value, name="DictionaryEntry_value", curie=CORE.curie('value'),
                   model_uri=SPDX.DictionaryEntry_value, domain=DictionaryEntry, range=Optional[str])

slots.DictionaryEntry_key = Slot(uri=CORE.key, name="DictionaryEntry_key", curie=CORE.curie('key'),
                   model_uri=SPDX.DictionaryEntry_key, domain=DictionaryEntry, range=str)

slots.Element_externalIdentifier = Slot(uri=CORE.externalIdentifier, name="Element_externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=SPDX.Element_externalIdentifier, domain=Element, range=Optional[Union[Union[dict, "ExternalIdentifier"], list[Union[dict, "ExternalIdentifier"]]]])

slots.Element_extension = Slot(uri=CORE.extension, name="Element_extension", curie=CORE.curie('extension'),
                   model_uri=SPDX.Element_extension, domain=Element, range=Optional[Union[Union[dict, "Extension"], list[Union[dict, "Extension"]]]])

slots.Element_summary = Slot(uri=CORE.summary, name="Element_summary", curie=CORE.curie('summary'),
                   model_uri=SPDX.Element_summary, domain=Element, range=Optional[str])

slots.Element_description = Slot(uri=CORE.description, name="Element_description", curie=CORE.curie('description'),
                   model_uri=SPDX.Element_description, domain=Element, range=Optional[str])

slots.Element_comment = Slot(uri=CORE.comment, name="Element_comment", curie=CORE.curie('comment'),
                   model_uri=SPDX.Element_comment, domain=Element, range=Optional[str])

slots.Element_verifiedUsing = Slot(uri=CORE.verifiedUsing, name="Element_verifiedUsing", curie=CORE.curie('verifiedUsing'),
                   model_uri=SPDX.Element_verifiedUsing, domain=Element, range=Optional[Union[Union[dict, "IntegrityMethod"], list[Union[dict, "IntegrityMethod"]]]])

slots.Element_externalRef = Slot(uri=CORE.externalRef, name="Element_externalRef", curie=CORE.curie('externalRef'),
                   model_uri=SPDX.Element_externalRef, domain=Element, range=Optional[Union[Union[dict, "ExternalRef"], list[Union[dict, "ExternalRef"]]]])

slots.Element_name = Slot(uri=CORE.name, name="Element_name", curie=CORE.curie('name'),
                   model_uri=SPDX.Element_name, domain=Element, range=Optional[str])

slots.Element_creationInfo = Slot(uri=CORE.creationInfo, name="Element_creationInfo", curie=CORE.curie('creationInfo'),
                   model_uri=SPDX.Element_creationInfo, domain=Element, range=Union[dict, CreationInfo])

slots.ElementCollection_element = Slot(uri=CORE.element, name="ElementCollection_element", curie=CORE.curie('element'),
                   model_uri=SPDX.ElementCollection_element, domain=ElementCollection, range=Optional[Union[Union[dict, Element], list[Union[dict, Element]]]])

slots.ElementCollection_profileConformance = Slot(uri=CORE.profileConformance, name="ElementCollection_profileConformance", curie=CORE.curie('profileConformance'),
                   model_uri=SPDX.ElementCollection_profileConformance, domain=ElementCollection, range=Optional[Union[Union[str, "ProfileIdentifierType"], list[Union[str, "ProfileIdentifierType"]]]])

slots.ElementCollection_rootElement = Slot(uri=CORE.rootElement, name="ElementCollection_rootElement", curie=CORE.curie('rootElement'),
                   model_uri=SPDX.ElementCollection_rootElement, domain=ElementCollection, range=Optional[Union[Union[dict, Element], list[Union[dict, Element]]]])

slots.ExternalIdentifier_identifierLocator = Slot(uri=CORE.identifierLocator, name="ExternalIdentifier_identifierLocator", curie=CORE.curie('identifierLocator'),
                   model_uri=SPDX.ExternalIdentifier_identifierLocator, domain=ExternalIdentifier, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.ExternalIdentifier_externalIdentifierType = Slot(uri=CORE.externalIdentifierType, name="ExternalIdentifier_externalIdentifierType", curie=CORE.curie('externalIdentifierType'),
                   model_uri=SPDX.ExternalIdentifier_externalIdentifierType, domain=ExternalIdentifier, range=str)

slots.ExternalIdentifier_issuingAuthority = Slot(uri=CORE.issuingAuthority, name="ExternalIdentifier_issuingAuthority", curie=CORE.curie('issuingAuthority'),
                   model_uri=SPDX.ExternalIdentifier_issuingAuthority, domain=ExternalIdentifier, range=Optional[str])

slots.ExternalIdentifier_identifier = Slot(uri=CORE.identifier, name="ExternalIdentifier_identifier", curie=CORE.curie('identifier'),
                   model_uri=SPDX.ExternalIdentifier_identifier, domain=ExternalIdentifier, range=str)

slots.ExternalIdentifier_comment = Slot(uri=CORE.comment, name="ExternalIdentifier_comment", curie=CORE.curie('comment'),
                   model_uri=SPDX.ExternalIdentifier_comment, domain=ExternalIdentifier, range=Optional[str])

slots.ExternalMap_definingArtifact = Slot(uri=CORE.definingArtifact, name="ExternalMap_definingArtifact", curie=CORE.curie('definingArtifact'),
                   model_uri=SPDX.ExternalMap_definingArtifact, domain=ExternalMap, range=Optional[Union[dict, Artifact]])

slots.ExternalMap_locationHint = Slot(uri=CORE.locationHint, name="ExternalMap_locationHint", curie=CORE.curie('locationHint'),
                   model_uri=SPDX.ExternalMap_locationHint, domain=ExternalMap, range=Optional[Union[str, URI]])

slots.ExternalMap_externalSpdxId = Slot(uri=CORE.externalSpdxId, name="ExternalMap_externalSpdxId", curie=CORE.curie('externalSpdxId'),
                   model_uri=SPDX.ExternalMap_externalSpdxId, domain=ExternalMap, range=Union[str, URI])

slots.ExternalMap_verifiedUsing = Slot(uri=CORE.verifiedUsing, name="ExternalMap_verifiedUsing", curie=CORE.curie('verifiedUsing'),
                   model_uri=SPDX.ExternalMap_verifiedUsing, domain=ExternalMap, range=Optional[Union[Union[dict, "IntegrityMethod"], list[Union[dict, "IntegrityMethod"]]]])

slots.ExternalRef_core_locator = Slot(uri=CORE.locator, name="ExternalRef_core_locator", curie=CORE.curie('locator'),
                   model_uri=SPDX.ExternalRef_core_locator, domain=ExternalRef, range=Optional[Union[str, list[str]]])

slots.ExternalRef_externalRefType = Slot(uri=CORE.externalRefType, name="ExternalRef_externalRefType", curie=CORE.curie('externalRefType'),
                   model_uri=SPDX.ExternalRef_externalRefType, domain=ExternalRef, range=Optional[str])

slots.ExternalRef_comment = Slot(uri=CORE.comment, name="ExternalRef_comment", curie=CORE.curie('comment'),
                   model_uri=SPDX.ExternalRef_comment, domain=ExternalRef, range=Optional[str])

slots.ExternalRef_contentType = Slot(uri=CORE.contentType, name="ExternalRef_contentType", curie=CORE.curie('contentType'),
                   model_uri=SPDX.ExternalRef_contentType, domain=ExternalRef, range=Optional[str],
                   pattern=re.compile(r'^[^\/]+\/[^\/]+$'))

slots.Hash_algorithm = Slot(uri=CORE.algorithm, name="Hash_algorithm", curie=CORE.curie('algorithm'),
                   model_uri=SPDX.Hash_algorithm, domain=Hash, range=str)

slots.Hash_hashValue = Slot(uri=CORE.hashValue, name="Hash_hashValue", curie=CORE.curie('hashValue'),
                   model_uri=SPDX.Hash_hashValue, domain=Hash, range=str)

slots.IntegrityMethod_comment = Slot(uri=CORE.comment, name="IntegrityMethod_comment", curie=CORE.curie('comment'),
                   model_uri=SPDX.IntegrityMethod_comment, domain=IntegrityMethod, range=Optional[str])

slots.LifecycleScopedRelationship_scope = Slot(uri=CORE.scope, name="LifecycleScopedRelationship_scope", curie=CORE.curie('scope'),
                   model_uri=SPDX.LifecycleScopedRelationship_scope, domain=LifecycleScopedRelationship, range=Optional[str])

slots.NamespaceMap_prefix = Slot(uri=CORE.prefix, name="NamespaceMap_prefix", curie=CORE.curie('prefix'),
                   model_uri=SPDX.NamespaceMap_prefix, domain=NamespaceMap, range=str)

slots.NamespaceMap_namespace = Slot(uri=CORE.namespace, name="NamespaceMap_namespace", curie=CORE.curie('namespace'),
                   model_uri=SPDX.NamespaceMap_namespace, domain=NamespaceMap, range=Union[str, URI])

slots.PackageVerificationCode_packageVerificationCodeExcludedFile = Slot(uri=CORE.packageVerificationCodeExcludedFile, name="PackageVerificationCode_packageVerificationCodeExcludedFile", curie=CORE.curie('packageVerificationCodeExcludedFile'),
                   model_uri=SPDX.PackageVerificationCode_packageVerificationCodeExcludedFile, domain=PackageVerificationCode, range=Optional[Union[str, list[str]]])

slots.PackageVerificationCode_hashValue = Slot(uri=CORE.hashValue, name="PackageVerificationCode_hashValue", curie=CORE.curie('hashValue'),
                   model_uri=SPDX.PackageVerificationCode_hashValue, domain=PackageVerificationCode, range=str)

slots.PackageVerificationCode_algorithm = Slot(uri=CORE.algorithm, name="PackageVerificationCode_algorithm", curie=CORE.curie('algorithm'),
                   model_uri=SPDX.PackageVerificationCode_algorithm, domain=PackageVerificationCode, range=str)

slots.PositiveIntegerRange_endIntegerRange = Slot(uri=CORE.endIntegerRange, name="PositiveIntegerRange_endIntegerRange", curie=CORE.curie('endIntegerRange'),
                   model_uri=SPDX.PositiveIntegerRange_endIntegerRange, domain=PositiveIntegerRange, range=int)

slots.PositiveIntegerRange_beginIntegerRange = Slot(uri=CORE.beginIntegerRange, name="PositiveIntegerRange_beginIntegerRange", curie=CORE.curie('beginIntegerRange'),
                   model_uri=SPDX.PositiveIntegerRange_beginIntegerRange, domain=PositiveIntegerRange, range=int)

slots.Relationship_to = Slot(uri=CORE.to, name="Relationship_to", curie=CORE.curie('to'),
                   model_uri=SPDX.Relationship_to, domain=Relationship, range=Union[Union[dict, Element], list[Union[dict, Element]]])

slots.Relationship_completeness = Slot(uri=CORE.completeness, name="Relationship_completeness", curie=CORE.curie('completeness'),
                   model_uri=SPDX.Relationship_completeness, domain=Relationship, range=Optional[Union[str, "RelationshipCompleteness"]])

slots.Relationship_startTime = Slot(uri=CORE.startTime, name="Relationship_startTime", curie=CORE.curie('startTime'),
                   model_uri=SPDX.Relationship_startTime, domain=Relationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Relationship_relationshipType = Slot(uri=CORE.relationshipType, name="Relationship_relationshipType", curie=CORE.curie('relationshipType'),
                   model_uri=SPDX.Relationship_relationshipType, domain=Relationship, range=str)

slots.Relationship_from = Slot(uri=CORE.from, name="Relationship_from", curie=CORE.curie('from'),
                   model_uri=SPDX.Relationship_from, domain=Relationship, range=Union[dict, Element])

slots.Relationship_endTime = Slot(uri=CORE.endTime, name="Relationship_endTime", curie=CORE.curie('endTime'),
                   model_uri=SPDX.Relationship_endTime, domain=Relationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.SpdxDocument_namespaceMap = Slot(uri=CORE.namespaceMap, name="SpdxDocument_namespaceMap", curie=CORE.curie('namespaceMap'),
                   model_uri=SPDX.SpdxDocument_namespaceMap, domain=SpdxDocument, range=Optional[Union[Union[dict, NamespaceMap], list[Union[dict, NamespaceMap]]]])

slots.SpdxDocument_dataLicense = Slot(uri=CORE.dataLicense, name="SpdxDocument_dataLicense", curie=CORE.curie('dataLicense'),
                   model_uri=SPDX.SpdxDocument_dataLicense, domain=SpdxDocument, range=Optional[Union[dict, "AnyLicenseInfo"]])

slots.SpdxDocument_import = Slot(uri=CORE.import, name="SpdxDocument_import", curie=CORE.curie('import'),
                   model_uri=SPDX.SpdxDocument_import, domain=SpdxDocument, range=Optional[Union[Union[dict, ExternalMap], list[Union[dict, ExternalMap]]]])

slots.DatasetPackage_datasetSize = Slot(uri=DATASET.datasetSize, name="DatasetPackage_datasetSize", curie=DATASET.curie('datasetSize'),
                   model_uri=SPDX.DatasetPackage_datasetSize, domain=DatasetPackage, range=Optional[int])

slots.DatasetPackage_datasetType = Slot(uri=DATASET.datasetType, name="DatasetPackage_datasetType", curie=DATASET.curie('datasetType'),
                   model_uri=SPDX.DatasetPackage_datasetType, domain=DatasetPackage, range=Union[str, list[str]])

slots.DatasetPackage_anonymizationMethodUsed = Slot(uri=DATASET.anonymizationMethodUsed, name="DatasetPackage_anonymizationMethodUsed", curie=DATASET.curie('anonymizationMethodUsed'),
                   model_uri=SPDX.DatasetPackage_anonymizationMethodUsed, domain=DatasetPackage, range=Optional[Union[str, list[str]]])

slots.DatasetPackage_datasetUpdateMechanism = Slot(uri=DATASET.datasetUpdateMechanism, name="DatasetPackage_datasetUpdateMechanism", curie=DATASET.curie('datasetUpdateMechanism'),
                   model_uri=SPDX.DatasetPackage_datasetUpdateMechanism, domain=DatasetPackage, range=Optional[str])

slots.DatasetPackage_dataCollectionProcess = Slot(uri=DATASET.dataCollectionProcess, name="DatasetPackage_dataCollectionProcess", curie=DATASET.curie('dataCollectionProcess'),
                   model_uri=SPDX.DatasetPackage_dataCollectionProcess, domain=DatasetPackage, range=Optional[str])

slots.DatasetPackage_knownBias = Slot(uri=DATASET.knownBias, name="DatasetPackage_knownBias", curie=DATASET.curie('knownBias'),
                   model_uri=SPDX.DatasetPackage_knownBias, domain=DatasetPackage, range=Optional[Union[str, list[str]]])

slots.DatasetPackage_sensor = Slot(uri=DATASET.sensor, name="DatasetPackage_sensor", curie=DATASET.curie('sensor'),
                   model_uri=SPDX.DatasetPackage_sensor, domain=DatasetPackage, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.DatasetPackage_dataPreprocessing = Slot(uri=DATASET.dataPreprocessing, name="DatasetPackage_dataPreprocessing", curie=DATASET.curie('dataPreprocessing'),
                   model_uri=SPDX.DatasetPackage_dataPreprocessing, domain=DatasetPackage, range=Optional[Union[str, list[str]]])

slots.DatasetPackage_intendedUse = Slot(uri=DATASET.intendedUse, name="DatasetPackage_intendedUse", curie=DATASET.curie('intendedUse'),
                   model_uri=SPDX.DatasetPackage_intendedUse, domain=DatasetPackage, range=Optional[str])

slots.DatasetPackage_confidentialityLevel = Slot(uri=DATASET.confidentialityLevel, name="DatasetPackage_confidentialityLevel", curie=DATASET.curie('confidentialityLevel'),
                   model_uri=SPDX.DatasetPackage_confidentialityLevel, domain=DatasetPackage, range=Optional[Union[str, "ConfidentialityLevelType"]])

slots.DatasetPackage_datasetAvailability = Slot(uri=DATASET.datasetAvailability, name="DatasetPackage_datasetAvailability", curie=DATASET.curie('datasetAvailability'),
                   model_uri=SPDX.DatasetPackage_datasetAvailability, domain=DatasetPackage, range=Optional[Union[str, "DatasetAvailabilityType"]])

slots.DatasetPackage_hasSensitivePersonalInformation = Slot(uri=DATASET.hasSensitivePersonalInformation, name="DatasetPackage_hasSensitivePersonalInformation", curie=DATASET.curie('hasSensitivePersonalInformation'),
                   model_uri=SPDX.DatasetPackage_hasSensitivePersonalInformation, domain=DatasetPackage, range=Optional[Union[str, "PresenceType"]])

slots.DatasetPackage_datasetNoise = Slot(uri=DATASET.datasetNoise, name="DatasetPackage_datasetNoise", curie=DATASET.curie('datasetNoise'),
                   model_uri=SPDX.DatasetPackage_datasetNoise, domain=DatasetPackage, range=Optional[str])

slots.ConjunctiveLicenseSet_member = Slot(uri=EXPANDEDLICENSING.member, name="ConjunctiveLicenseSet_member", curie=EXPANDEDLICENSING.curie('member'),
                   model_uri=SPDX.ConjunctiveLicenseSet_member, domain=ConjunctiveLicenseSet, range=Union[Union[dict, AnyLicenseInfo], list[Union[dict, AnyLicenseInfo]]])

slots.DisjunctiveLicenseSet_member = Slot(uri=EXPANDEDLICENSING.member, name="DisjunctiveLicenseSet_member", curie=EXPANDEDLICENSING.curie('member'),
                   model_uri=SPDX.DisjunctiveLicenseSet_member, domain=DisjunctiveLicenseSet, range=Union[Union[dict, AnyLicenseInfo], list[Union[dict, AnyLicenseInfo]]])

slots.License_obsoletedBy = Slot(uri=EXPANDEDLICENSING.obsoletedBy, name="License_obsoletedBy", curie=EXPANDEDLICENSING.curie('obsoletedBy'),
                   model_uri=SPDX.License_obsoletedBy, domain=License, range=Optional[str])

slots.License_standardLicenseHeader = Slot(uri=EXPANDEDLICENSING.standardLicenseHeader, name="License_standardLicenseHeader", curie=EXPANDEDLICENSING.curie('standardLicenseHeader'),
                   model_uri=SPDX.License_standardLicenseHeader, domain=License, range=Optional[str])

slots.License_seeAlso = Slot(uri=EXPANDEDLICENSING.seeAlso, name="License_seeAlso", curie=EXPANDEDLICENSING.curie('seeAlso'),
                   model_uri=SPDX.License_seeAlso, domain=License, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.License_isFsfLibre = Slot(uri=EXPANDEDLICENSING.isFsfLibre, name="License_isFsfLibre", curie=EXPANDEDLICENSING.curie('isFsfLibre'),
                   model_uri=SPDX.License_isFsfLibre, domain=License, range=Optional[Union[bool, Bool]])

slots.License_isDeprecatedLicenseId = Slot(uri=EXPANDEDLICENSING.isDeprecatedLicenseId, name="License_isDeprecatedLicenseId", curie=EXPANDEDLICENSING.curie('isDeprecatedLicenseId'),
                   model_uri=SPDX.License_isDeprecatedLicenseId, domain=License, range=Optional[Union[bool, Bool]])

slots.License_isOsiApproved = Slot(uri=EXPANDEDLICENSING.isOsiApproved, name="License_isOsiApproved", curie=EXPANDEDLICENSING.curie('isOsiApproved'),
                   model_uri=SPDX.License_isOsiApproved, domain=License, range=Optional[Union[bool, Bool]])

slots.License_licenseXml = Slot(uri=EXPANDEDLICENSING.licenseXml, name="License_licenseXml", curie=EXPANDEDLICENSING.curie('licenseXml'),
                   model_uri=SPDX.License_licenseXml, domain=License, range=Optional[str])

slots.License_licenseText = Slot(uri=SIMPLELICENSING.licenseText, name="License_licenseText", curie=SIMPLELICENSING.curie('licenseText'),
                   model_uri=SPDX.License_licenseText, domain=License, range=str)

slots.License_standardLicenseTemplate = Slot(uri=EXPANDEDLICENSING.standardLicenseTemplate, name="License_standardLicenseTemplate", curie=EXPANDEDLICENSING.curie('standardLicenseTemplate'),
                   model_uri=SPDX.License_standardLicenseTemplate, domain=License, range=Optional[str])

slots.LicenseAddition_standardAdditionTemplate = Slot(uri=EXPANDEDLICENSING.standardAdditionTemplate, name="LicenseAddition_standardAdditionTemplate", curie=EXPANDEDLICENSING.curie('standardAdditionTemplate'),
                   model_uri=SPDX.LicenseAddition_standardAdditionTemplate, domain=LicenseAddition, range=Optional[str])

slots.LicenseAddition_seeAlso = Slot(uri=EXPANDEDLICENSING.seeAlso, name="LicenseAddition_seeAlso", curie=EXPANDEDLICENSING.curie('seeAlso'),
                   model_uri=SPDX.LicenseAddition_seeAlso, domain=LicenseAddition, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.LicenseAddition_obsoletedBy = Slot(uri=EXPANDEDLICENSING.obsoletedBy, name="LicenseAddition_obsoletedBy", curie=EXPANDEDLICENSING.curie('obsoletedBy'),
                   model_uri=SPDX.LicenseAddition_obsoletedBy, domain=LicenseAddition, range=Optional[str])

slots.LicenseAddition_licenseXml = Slot(uri=EXPANDEDLICENSING.licenseXml, name="LicenseAddition_licenseXml", curie=EXPANDEDLICENSING.curie('licenseXml'),
                   model_uri=SPDX.LicenseAddition_licenseXml, domain=LicenseAddition, range=Optional[str])

slots.LicenseAddition_isDeprecatedAdditionId = Slot(uri=EXPANDEDLICENSING.isDeprecatedAdditionId, name="LicenseAddition_isDeprecatedAdditionId", curie=EXPANDEDLICENSING.curie('isDeprecatedAdditionId'),
                   model_uri=SPDX.LicenseAddition_isDeprecatedAdditionId, domain=LicenseAddition, range=Optional[Union[bool, Bool]])

slots.LicenseAddition_additionText = Slot(uri=EXPANDEDLICENSING.additionText, name="LicenseAddition_additionText", curie=EXPANDEDLICENSING.curie('additionText'),
                   model_uri=SPDX.LicenseAddition_additionText, domain=LicenseAddition, range=str)

slots.ListedLicense_deprecatedVersion = Slot(uri=EXPANDEDLICENSING.deprecatedVersion, name="ListedLicense_deprecatedVersion", curie=EXPANDEDLICENSING.curie('deprecatedVersion'),
                   model_uri=SPDX.ListedLicense_deprecatedVersion, domain=ListedLicense, range=Optional[str])

slots.ListedLicense_listVersionAdded = Slot(uri=EXPANDEDLICENSING.listVersionAdded, name="ListedLicense_listVersionAdded", curie=EXPANDEDLICENSING.curie('listVersionAdded'),
                   model_uri=SPDX.ListedLicense_listVersionAdded, domain=ListedLicense, range=Optional[str])

slots.ListedLicenseException_listVersionAdded = Slot(uri=EXPANDEDLICENSING.listVersionAdded, name="ListedLicenseException_listVersionAdded", curie=EXPANDEDLICENSING.curie('listVersionAdded'),
                   model_uri=SPDX.ListedLicenseException_listVersionAdded, domain=ListedLicenseException, range=Optional[str])

slots.ListedLicenseException_deprecatedVersion = Slot(uri=EXPANDEDLICENSING.deprecatedVersion, name="ListedLicenseException_deprecatedVersion", curie=EXPANDEDLICENSING.curie('deprecatedVersion'),
                   model_uri=SPDX.ListedLicenseException_deprecatedVersion, domain=ListedLicenseException, range=Optional[str])

slots.OrLaterOperator_subjectLicense = Slot(uri=EXPANDEDLICENSING.subjectLicense, name="OrLaterOperator_subjectLicense", curie=EXPANDEDLICENSING.curie('subjectLicense'),
                   model_uri=SPDX.OrLaterOperator_subjectLicense, domain=OrLaterOperator, range=Union[dict, License])

slots.WithAdditionOperator_subjectExtendableLicense = Slot(uri=EXPANDEDLICENSING.subjectExtendableLicense, name="WithAdditionOperator_subjectExtendableLicense", curie=EXPANDEDLICENSING.curie('subjectExtendableLicense'),
                   model_uri=SPDX.WithAdditionOperator_subjectExtendableLicense, domain=WithAdditionOperator, range=Union[dict, ExtendableLicense])

slots.WithAdditionOperator_subjectAddition = Slot(uri=EXPANDEDLICENSING.subjectAddition, name="WithAdditionOperator_subjectAddition", curie=EXPANDEDLICENSING.curie('subjectAddition'),
                   model_uri=SPDX.WithAdditionOperator_subjectAddition, domain=WithAdditionOperator, range=Union[dict, LicenseAddition])

slots.CdxPropertiesExtension_cdxProperty = Slot(uri=EXTENSION.cdxProperty, name="CdxPropertiesExtension_cdxProperty", curie=EXTENSION.curie('cdxProperty'),
                   model_uri=SPDX.CdxPropertiesExtension_cdxProperty, domain=CdxPropertiesExtension, range=Union[Union[dict, CdxPropertyEntry], list[Union[dict, CdxPropertyEntry]]])

slots.CdxPropertyEntry_cdxPropValue = Slot(uri=EXTENSION.cdxPropValue, name="CdxPropertyEntry_cdxPropValue", curie=EXTENSION.curie('cdxPropValue'),
                   model_uri=SPDX.CdxPropertyEntry_cdxPropValue, domain=CdxPropertyEntry, range=Optional[str])

slots.CdxPropertyEntry_cdxPropName = Slot(uri=EXTENSION.cdxPropName, name="CdxPropertyEntry_cdxPropName", curie=EXTENSION.curie('cdxPropName'),
                   model_uri=SPDX.CdxPropertyEntry_cdxPropName, domain=CdxPropertyEntry, range=str)

slots.CvssV2VulnAssessmentRelationship_vectorString = Slot(uri=SECURITY.vectorString, name="CvssV2VulnAssessmentRelationship_vectorString", curie=SECURITY.curie('vectorString'),
                   model_uri=SPDX.CvssV2VulnAssessmentRelationship_vectorString, domain=CvssV2VulnAssessmentRelationship, range=str)

slots.CvssV2VulnAssessmentRelationship_score = Slot(uri=SECURITY.score, name="CvssV2VulnAssessmentRelationship_score", curie=SECURITY.curie('score'),
                   model_uri=SPDX.CvssV2VulnAssessmentRelationship_score, domain=CvssV2VulnAssessmentRelationship, range=Decimal)

slots.CvssV3VulnAssessmentRelationship_severity = Slot(uri=SECURITY.severity, name="CvssV3VulnAssessmentRelationship_severity", curie=SECURITY.curie('severity'),
                   model_uri=SPDX.CvssV3VulnAssessmentRelationship_severity, domain=CvssV3VulnAssessmentRelationship, range=Union[str, "CvssSeverityType"])

slots.CvssV3VulnAssessmentRelationship_vectorString = Slot(uri=SECURITY.vectorString, name="CvssV3VulnAssessmentRelationship_vectorString", curie=SECURITY.curie('vectorString'),
                   model_uri=SPDX.CvssV3VulnAssessmentRelationship_vectorString, domain=CvssV3VulnAssessmentRelationship, range=str)

slots.CvssV3VulnAssessmentRelationship_score = Slot(uri=SECURITY.score, name="CvssV3VulnAssessmentRelationship_score", curie=SECURITY.curie('score'),
                   model_uri=SPDX.CvssV3VulnAssessmentRelationship_score, domain=CvssV3VulnAssessmentRelationship, range=Decimal)

slots.CvssV4VulnAssessmentRelationship_severity = Slot(uri=SECURITY.severity, name="CvssV4VulnAssessmentRelationship_severity", curie=SECURITY.curie('severity'),
                   model_uri=SPDX.CvssV4VulnAssessmentRelationship_severity, domain=CvssV4VulnAssessmentRelationship, range=Union[str, "CvssSeverityType"])

slots.CvssV4VulnAssessmentRelationship_vectorString = Slot(uri=SECURITY.vectorString, name="CvssV4VulnAssessmentRelationship_vectorString", curie=SECURITY.curie('vectorString'),
                   model_uri=SPDX.CvssV4VulnAssessmentRelationship_vectorString, domain=CvssV4VulnAssessmentRelationship, range=str)

slots.CvssV4VulnAssessmentRelationship_score = Slot(uri=SECURITY.score, name="CvssV4VulnAssessmentRelationship_score", curie=SECURITY.curie('score'),
                   model_uri=SPDX.CvssV4VulnAssessmentRelationship_score, domain=CvssV4VulnAssessmentRelationship, range=Decimal)

slots.EpssVulnAssessmentRelationship_percentile = Slot(uri=SECURITY.percentile, name="EpssVulnAssessmentRelationship_percentile", curie=SECURITY.curie('percentile'),
                   model_uri=SPDX.EpssVulnAssessmentRelationship_percentile, domain=EpssVulnAssessmentRelationship, range=Decimal)

slots.EpssVulnAssessmentRelationship_probability = Slot(uri=SECURITY.probability, name="EpssVulnAssessmentRelationship_probability", curie=SECURITY.curie('probability'),
                   model_uri=SPDX.EpssVulnAssessmentRelationship_probability, domain=EpssVulnAssessmentRelationship, range=Decimal)

slots.ExploitCatalogVulnAssessmentRelationship_exploited = Slot(uri=SECURITY.exploited, name="ExploitCatalogVulnAssessmentRelationship_exploited", curie=SECURITY.curie('exploited'),
                   model_uri=SPDX.ExploitCatalogVulnAssessmentRelationship_exploited, domain=ExploitCatalogVulnAssessmentRelationship, range=Union[bool, Bool])

slots.ExploitCatalogVulnAssessmentRelationship_security_locator = Slot(uri=SECURITY.locator, name="ExploitCatalogVulnAssessmentRelationship_security_locator", curie=SECURITY.curie('locator'),
                   model_uri=SPDX.ExploitCatalogVulnAssessmentRelationship_security_locator, domain=ExploitCatalogVulnAssessmentRelationship, range=Union[str, URI])

slots.ExploitCatalogVulnAssessmentRelationship_catalogType = Slot(uri=SECURITY.catalogType, name="ExploitCatalogVulnAssessmentRelationship_catalogType", curie=SECURITY.curie('catalogType'),
                   model_uri=SPDX.ExploitCatalogVulnAssessmentRelationship_catalogType, domain=ExploitCatalogVulnAssessmentRelationship, range=str)

slots.SsvcVulnAssessmentRelationship_decisionType = Slot(uri=SECURITY.decisionType, name="SsvcVulnAssessmentRelationship_decisionType", curie=SECURITY.curie('decisionType'),
                   model_uri=SPDX.SsvcVulnAssessmentRelationship_decisionType, domain=SsvcVulnAssessmentRelationship, range=Union[str, "SsvcDecisionType"])

slots.VexAffectedVulnAssessmentRelationship_actionStatement = Slot(uri=SECURITY.actionStatement, name="VexAffectedVulnAssessmentRelationship_actionStatement", curie=SECURITY.curie('actionStatement'),
                   model_uri=SPDX.VexAffectedVulnAssessmentRelationship_actionStatement, domain=VexAffectedVulnAssessmentRelationship, range=str)

slots.VexAffectedVulnAssessmentRelationship_actionStatementTime = Slot(uri=SECURITY.actionStatementTime, name="VexAffectedVulnAssessmentRelationship_actionStatementTime", curie=SECURITY.curie('actionStatementTime'),
                   model_uri=SPDX.VexAffectedVulnAssessmentRelationship_actionStatementTime, domain=VexAffectedVulnAssessmentRelationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.VexNotAffectedVulnAssessmentRelationship_impactStatementTime = Slot(uri=SECURITY.impactStatementTime, name="VexNotAffectedVulnAssessmentRelationship_impactStatementTime", curie=SECURITY.curie('impactStatementTime'),
                   model_uri=SPDX.VexNotAffectedVulnAssessmentRelationship_impactStatementTime, domain=VexNotAffectedVulnAssessmentRelationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.VexNotAffectedVulnAssessmentRelationship_justificationType = Slot(uri=SECURITY.justificationType, name="VexNotAffectedVulnAssessmentRelationship_justificationType", curie=SECURITY.curie('justificationType'),
                   model_uri=SPDX.VexNotAffectedVulnAssessmentRelationship_justificationType, domain=VexNotAffectedVulnAssessmentRelationship, range=Optional[Union[str, "VexJustificationType"]])

slots.VexNotAffectedVulnAssessmentRelationship_impactStatement = Slot(uri=SECURITY.impactStatement, name="VexNotAffectedVulnAssessmentRelationship_impactStatement", curie=SECURITY.curie('impactStatement'),
                   model_uri=SPDX.VexNotAffectedVulnAssessmentRelationship_impactStatement, domain=VexNotAffectedVulnAssessmentRelationship, range=Optional[str])

slots.VexVulnAssessmentRelationship_vexVersion = Slot(uri=SECURITY.vexVersion, name="VexVulnAssessmentRelationship_vexVersion", curie=SECURITY.curie('vexVersion'),
                   model_uri=SPDX.VexVulnAssessmentRelationship_vexVersion, domain=VexVulnAssessmentRelationship, range=Optional[str])

slots.VexVulnAssessmentRelationship_statusNotes = Slot(uri=SECURITY.statusNotes, name="VexVulnAssessmentRelationship_statusNotes", curie=SECURITY.curie('statusNotes'),
                   model_uri=SPDX.VexVulnAssessmentRelationship_statusNotes, domain=VexVulnAssessmentRelationship, range=Optional[str])

slots.VulnAssessmentRelationship_withdrawnTime = Slot(uri=SECURITY.withdrawnTime, name="VulnAssessmentRelationship_withdrawnTime", curie=SECURITY.curie('withdrawnTime'),
                   model_uri=SPDX.VulnAssessmentRelationship_withdrawnTime, domain=VulnAssessmentRelationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.VulnAssessmentRelationship_publishedTime = Slot(uri=SECURITY.publishedTime, name="VulnAssessmentRelationship_publishedTime", curie=SECURITY.curie('publishedTime'),
                   model_uri=SPDX.VulnAssessmentRelationship_publishedTime, domain=VulnAssessmentRelationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.VulnAssessmentRelationship_assessedElement = Slot(uri=SECURITY.assessedElement, name="VulnAssessmentRelationship_assessedElement", curie=SECURITY.curie('assessedElement'),
                   model_uri=SPDX.VulnAssessmentRelationship_assessedElement, domain=VulnAssessmentRelationship, range=Optional[Union[dict, "SoftwareArtifact"]])

slots.VulnAssessmentRelationship_suppliedBy = Slot(uri=CORE.suppliedBy, name="VulnAssessmentRelationship_suppliedBy", curie=CORE.curie('suppliedBy'),
                   model_uri=SPDX.VulnAssessmentRelationship_suppliedBy, domain=VulnAssessmentRelationship, range=Optional[Union[dict, Agent]])

slots.VulnAssessmentRelationship_modifiedTime = Slot(uri=SECURITY.modifiedTime, name="VulnAssessmentRelationship_modifiedTime", curie=SECURITY.curie('modifiedTime'),
                   model_uri=SPDX.VulnAssessmentRelationship_modifiedTime, domain=VulnAssessmentRelationship, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Vulnerability_withdrawnTime = Slot(uri=SECURITY.withdrawnTime, name="Vulnerability_withdrawnTime", curie=SECURITY.curie('withdrawnTime'),
                   model_uri=SPDX.Vulnerability_withdrawnTime, domain=Vulnerability, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Vulnerability_modifiedTime = Slot(uri=SECURITY.modifiedTime, name="Vulnerability_modifiedTime", curie=SECURITY.curie('modifiedTime'),
                   model_uri=SPDX.Vulnerability_modifiedTime, domain=Vulnerability, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.Vulnerability_publishedTime = Slot(uri=SECURITY.publishedTime, name="Vulnerability_publishedTime", curie=SECURITY.curie('publishedTime'),
                   model_uri=SPDX.Vulnerability_publishedTime, domain=Vulnerability, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$'))

slots.LicenseExpression_customIdToUri = Slot(uri=SIMPLELICENSING.customIdToUri, name="LicenseExpression_customIdToUri", curie=SIMPLELICENSING.curie('customIdToUri'),
                   model_uri=SPDX.LicenseExpression_customIdToUri, domain=LicenseExpression, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.LicenseExpression_licenseExpression = Slot(uri=SIMPLELICENSING.licenseExpression, name="LicenseExpression_licenseExpression", curie=SIMPLELICENSING.curie('licenseExpression'),
                   model_uri=SPDX.LicenseExpression_licenseExpression, domain=LicenseExpression, range=str)

slots.LicenseExpression_licenseListVersion = Slot(uri=SIMPLELICENSING.licenseListVersion, name="LicenseExpression_licenseListVersion", curie=SIMPLELICENSING.curie('licenseListVersion'),
                   model_uri=SPDX.LicenseExpression_licenseListVersion, domain=LicenseExpression, range=Optional[str],
                   pattern=re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'))

slots.SimpleLicensingText_licenseText = Slot(uri=SIMPLELICENSING.licenseText, name="SimpleLicensingText_licenseText", curie=SIMPLELICENSING.curie('licenseText'),
                   model_uri=SPDX.SimpleLicensingText_licenseText, domain=SimpleLicensingText, range=str)

slots.ContentIdentifier_contentIdentifierValue = Slot(uri=SOFTWARE.contentIdentifierValue, name="ContentIdentifier_contentIdentifierValue", curie=SOFTWARE.curie('contentIdentifierValue'),
                   model_uri=SPDX.ContentIdentifier_contentIdentifierValue, domain=ContentIdentifier, range=Union[str, URI])

slots.ContentIdentifier_contentIdentifierType = Slot(uri=SOFTWARE.contentIdentifierType, name="ContentIdentifier_contentIdentifierType", curie=SOFTWARE.curie('contentIdentifierType'),
                   model_uri=SPDX.ContentIdentifier_contentIdentifierType, domain=ContentIdentifier, range=Union[str, "ContentIdentifierType"])

slots.File_fileKind = Slot(uri=SOFTWARE.fileKind, name="File_fileKind", curie=SOFTWARE.curie('fileKind'),
                   model_uri=SPDX.File_fileKind, domain=File, range=Optional[Union[str, "FileKindType"]])

slots.File_contentType = Slot(uri=CORE.contentType, name="File_contentType", curie=CORE.curie('contentType'),
                   model_uri=SPDX.File_contentType, domain=File, range=Optional[str],
                   pattern=re.compile(r'^[^\/]+\/[^\/]+$'))

slots.Package_sourceInfo = Slot(uri=SOFTWARE.sourceInfo, name="Package_sourceInfo", curie=SOFTWARE.curie('sourceInfo'),
                   model_uri=SPDX.Package_sourceInfo, domain=Package, range=Optional[str])

slots.Package_homePage = Slot(uri=SOFTWARE.homePage, name="Package_homePage", curie=SOFTWARE.curie('homePage'),
                   model_uri=SPDX.Package_homePage, domain=Package, range=Optional[Union[str, URI]])

slots.Package_downloadLocation = Slot(uri=SOFTWARE.downloadLocation, name="Package_downloadLocation", curie=SOFTWARE.curie('downloadLocation'),
                   model_uri=SPDX.Package_downloadLocation, domain=Package, range=Optional[Union[str, URI]])

slots.Package_packageVersion = Slot(uri=SOFTWARE.packageVersion, name="Package_packageVersion", curie=SOFTWARE.curie('packageVersion'),
                   model_uri=SPDX.Package_packageVersion, domain=Package, range=Optional[str])

slots.Package_packageUrl = Slot(uri=SOFTWARE.packageUrl, name="Package_packageUrl", curie=SOFTWARE.curie('packageUrl'),
                   model_uri=SPDX.Package_packageUrl, domain=Package, range=Optional[Union[str, URI]])

slots.Sbom_sbomType = Slot(uri=SOFTWARE.sbomType, name="Sbom_sbomType", curie=SOFTWARE.curie('sbomType'),
                   model_uri=SPDX.Sbom_sbomType, domain=Sbom, range=Optional[Union[Union[str, "SbomType"], list[Union[str, "SbomType"]]]])

slots.Snippet_lineRange = Slot(uri=SOFTWARE.lineRange, name="Snippet_lineRange", curie=SOFTWARE.curie('lineRange'),
                   model_uri=SPDX.Snippet_lineRange, domain=Snippet, range=Optional[Union[dict, PositiveIntegerRange]])

slots.Snippet_snippetFromFile = Slot(uri=SOFTWARE.snippetFromFile, name="Snippet_snippetFromFile", curie=SOFTWARE.curie('snippetFromFile'),
                   model_uri=SPDX.Snippet_snippetFromFile, domain=Snippet, range=Union[dict, File])

slots.Snippet_byteRange = Slot(uri=SOFTWARE.byteRange, name="Snippet_byteRange", curie=SOFTWARE.curie('byteRange'),
                   model_uri=SPDX.Snippet_byteRange, domain=Snippet, range=Optional[Union[dict, PositiveIntegerRange]])

slots.SoftwareArtifact_attributionText = Slot(uri=SOFTWARE.attributionText, name="SoftwareArtifact_attributionText", curie=SOFTWARE.curie('attributionText'),
                   model_uri=SPDX.SoftwareArtifact_attributionText, domain=SoftwareArtifact, range=Optional[Union[str, list[str]]])

slots.SoftwareArtifact_primaryPurpose = Slot(uri=SOFTWARE.primaryPurpose, name="SoftwareArtifact_primaryPurpose", curie=SOFTWARE.curie('primaryPurpose'),
                   model_uri=SPDX.SoftwareArtifact_primaryPurpose, domain=SoftwareArtifact, range=Optional[str])

slots.SoftwareArtifact_additionalPurpose = Slot(uri=SOFTWARE.additionalPurpose, name="SoftwareArtifact_additionalPurpose", curie=SOFTWARE.curie('additionalPurpose'),
                   model_uri=SPDX.SoftwareArtifact_additionalPurpose, domain=SoftwareArtifact, range=Optional[Union[str, list[str]]])

slots.SoftwareArtifact_contentIdentifier = Slot(uri=SOFTWARE.contentIdentifier, name="SoftwareArtifact_contentIdentifier", curie=SOFTWARE.curie('contentIdentifier'),
                   model_uri=SPDX.SoftwareArtifact_contentIdentifier, domain=SoftwareArtifact, range=Optional[Union[Union[dict, ContentIdentifier], list[Union[dict, ContentIdentifier]]]])

slots.SoftwareArtifact_copyrightText = Slot(uri=SOFTWARE.copyrightText, name="SoftwareArtifact_copyrightText", curie=SOFTWARE.curie('copyrightText'),
                   model_uri=SPDX.SoftwareArtifact_copyrightText, domain=SoftwareArtifact, range=Optional[str])
