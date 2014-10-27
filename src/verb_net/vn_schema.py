# .\vn_schema.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-10-05 19:24:16.732000 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b90e2ade-4ce6-11e4-86a5-8434976b8d42')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: auxWordnetType
class auxWordnetType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'auxWordnetType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 177, 0)
    _Documentation = None
auxWordnetType._CF_pattern = pyxb.binding.facets.CF_pattern()
auxWordnetType._CF_pattern.addPattern(pattern=u'\\??([a-z]|\\-|_)+%2:\\d{2}:\\d{2}')
auxWordnetType._InitializeFacetMap(auxWordnetType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'auxWordnetType', auxWordnetType)

# Atomic simple type: auxnpType
class auxnpType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'auxnpType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 190, 0)
    _Documentation = None
auxnpType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=auxnpType, enum_prefix=None)
auxnpType.Oblique = auxnpType._CF_enumeration.addEnumeration(unicode_value=u'Oblique', tag=u'Oblique')
auxnpType.Oblique1 = auxnpType._CF_enumeration.addEnumeration(unicode_value=u'Oblique1', tag=u'Oblique1')
auxnpType.Oblique2 = auxnpType._CF_enumeration.addEnumeration(unicode_value=u'Oblique2', tag=u'Oblique2')
auxnpType.NP = auxnpType._CF_enumeration.addEnumeration(unicode_value=u'NP', tag=u'NP')
auxnpType._InitializeFacetMap(auxnpType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'auxnpType', auxnpType)

# Atomic simple type: themRoleType
class themRoleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'themRoleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 203, 0)
    _Documentation = None
themRoleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=themRoleType, enum_prefix=None)
themRoleType.Topic = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Topic', tag=u'Topic')
themRoleType.Experiencer = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Experiencer', tag=u'Experiencer')
themRoleType.Stimulus = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Stimulus', tag=u'Stimulus')
themRoleType.Cause = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Cause', tag=u'Cause')
themRoleType.Actor = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Actor', tag=u'Actor')
themRoleType.Actor1 = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Actor1', tag=u'Actor1')
themRoleType.Actor2 = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Actor2', tag=u'Actor2')
themRoleType.Agent = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Agent', tag=u'Agent')
themRoleType.Asset = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Asset', tag=u'Asset')
themRoleType.Attribute = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Attribute', tag=u'Attribute')
themRoleType.Benefactor = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Benefactor', tag=u'Benefactor')
themRoleType.Beneficiary = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Beneficiary', tag=u'Beneficiary')
themRoleType.Content = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Content', tag=u'Content')
themRoleType.Destination = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Destination', tag=u'Destination')
themRoleType.Instrument = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Instrument', tag=u'Instrument')
themRoleType.Location = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Location', tag=u'Location')
themRoleType.Material = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Material', tag=u'Material')
themRoleType.Patient = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Patient', tag=u'Patient')
themRoleType.Patient1 = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Patient1', tag=u'Patient1')
themRoleType.Patient2 = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Patient2', tag=u'Patient2')
themRoleType.Predicate = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Predicate', tag=u'Predicate')
themRoleType.Proposition = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Proposition', tag=u'Proposition')
themRoleType.Product = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Product', tag=u'Product')
themRoleType.Recipient = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Recipient', tag=u'Recipient')
themRoleType.Source = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Source', tag=u'Source')
themRoleType.Theme = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Theme', tag=u'Theme')
themRoleType.Theme1 = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Theme1', tag=u'Theme1')
themRoleType.Theme2 = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Theme2', tag=u'Theme2')
themRoleType.Time = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Time', tag=u'Time')
themRoleType.Extent = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Extent', tag=u'Extent')
themRoleType.Value = themRoleType._CF_enumeration.addEnumeration(unicode_value=u'Value', tag=u'Value')
themRoleType._InitializeFacetMap(themRoleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'themRoleType', themRoleType)

# Atomic simple type: selrestrValueType
class selrestrValueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'selrestrValueType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 239, 0)
    _Documentation = None
selrestrValueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=selrestrValueType, enum_prefix=None)
selrestrValueType.emptyString = selrestrValueType._CF_enumeration.addEnumeration(unicode_value=u'+', tag='emptyString')
selrestrValueType.emptyString_ = selrestrValueType._CF_enumeration.addEnumeration(unicode_value=u'-', tag='emptyString_')
selrestrValueType._InitializeFacetMap(selrestrValueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'selrestrValueType', selrestrValueType)

# Atomic simple type: selrestrType
class selrestrType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'selrestrType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 246, 0)
    _Documentation = None
selrestrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=selrestrType, enum_prefix=None)
selrestrType.scalar = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'scalar', tag=u'scalar')
selrestrType.concrete = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'concrete', tag=u'concrete')
selrestrType.abstract = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'abstract', tag=u'abstract')
selrestrType.location = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'location', tag=u'location')
selrestrType.organization = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'organization', tag=u'organization')
selrestrType.currency = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'currency', tag=u'currency')
selrestrType.idea = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'idea', tag=u'idea')
selrestrType.sound = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'sound', tag=u'sound')
selrestrType.communication = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'communication', tag=u'communication')
selrestrType.quotation = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'quotation', tag=u'quotation')
selrestrType.region = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'region', tag=u'region')
selrestrType.place = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'place', tag=u'place')
selrestrType.concrete_ = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'concrete', tag=u'concrete_')
selrestrType.company = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'company', tag=u'company')
selrestrType.natural = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'natural', tag=u'natural')
selrestrType.phys_obj = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'phys_obj', tag=u'phys_obj')
selrestrType.plant = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'plant', tag=u'plant')
selrestrType.animal = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'animal', tag=u'animal')
selrestrType.human = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'human', tag=u'human')
selrestrType.animate = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'animate', tag=u'animate')
selrestrType.body_part = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'body_part', tag=u'body_part')
selrestrType.comestible = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'comestible', tag=u'comestible')
selrestrType.artifact = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'artifact', tag=u'artifact')
selrestrType.tool = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'tool', tag=u'tool')
selrestrType.garment = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'garment', tag=u'garment')
selrestrType.machine = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'machine', tag=u'machine')
selrestrType.int_control = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'int_control', tag=u'int_control')
selrestrType.force = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'force', tag=u'force')
selrestrType.vehicle = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'vehicle', tag=u'vehicle')
selrestrType.substance = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'substance', tag=u'substance')
selrestrType.solid = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'solid', tag=u'solid')
selrestrType.elongated = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'elongated', tag=u'elongated')
selrestrType.pointy = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'pointy', tag=u'pointy')
selrestrType.refl = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'refl', tag=u'refl')
selrestrType.rigid = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'rigid', tag=u'rigid')
selrestrType.nonrigid = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'nonrigid', tag=u'nonrigid')
selrestrType.state = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'state', tag=u'state')
selrestrType.plural = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'plural', tag=u'plural')
selrestrType.time = selrestrType._CF_enumeration.addEnumeration(unicode_value=u'time', tag=u'time')
selrestrType._InitializeFacetMap(selrestrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'selrestrType', selrestrType)

# Atomic simple type: preprestrType
class preprestrType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'preprestrType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 290, 0)
    _Documentation = None
preprestrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=preprestrType, enum_prefix=None)
preprestrType.path = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'path', tag=u'path')
preprestrType.src = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'src', tag=u'src')
preprestrType.dest_dir = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'dest_dir', tag=u'dest_dir')
preprestrType.dest_conf = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'dest_conf', tag=u'dest_conf')
preprestrType.loc = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'loc', tag=u'loc')
preprestrType.plural = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'plural', tag=u'plural')
preprestrType.spatial = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'spatial', tag=u'spatial')
preprestrType.dir = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'dir', tag=u'dir')
preprestrType.dest = preprestrType._CF_enumeration.addEnumeration(unicode_value=u'dest', tag=u'dest')
preprestrType._InitializeFacetMap(preprestrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'preprestrType', preprestrType)

# Atomic simple type: synrestrType
class synrestrType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'synrestrType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 304, 0)
    _Documentation = None
synrestrType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=synrestrType, enum_prefix=None)
synrestrType.sentential = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'sentential', tag=u'sentential')
synrestrType.indicative = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'indicative', tag=u'indicative')
synrestrType.that_comp = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'that_comp', tag=u'that_comp')
synrestrType.tensed_that = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'tensed_that', tag=u'tensed_that')
synrestrType.null_comp = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'null_comp', tag=u'null_comp')
synrestrType.wh_comp = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'wh_comp', tag=u'wh_comp')
synrestrType.wheth_comp = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'wheth_comp', tag=u'wheth_comp')
synrestrType.if_comp = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'if_comp', tag=u'if_comp')
synrestrType.extracted = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'extracted', tag=u'extracted')
synrestrType.what_extract = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'what_extract', tag=u'what_extract')
synrestrType.why_extract = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'why_extract', tag=u'why_extract')
synrestrType.who_extract = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'who_extract', tag=u'who_extract')
synrestrType.how_extract = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'how_extract', tag=u'how_extract')
synrestrType.where_extract = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'where_extract', tag=u'where_extract')
synrestrType.when_extract = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'when_extract', tag=u'when_extract')
synrestrType.infinitival = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'infinitival', tag=u'infinitival')
synrestrType.to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'to_inf', tag=u'to_inf')
synrestrType.control_to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'control_to_inf', tag=u'control_to_inf')
synrestrType.sc_to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'sc_to_inf', tag=u'sc_to_inf')
synrestrType.oc_to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'oc_to_inf', tag=u'oc_to_inf')
synrestrType.ac_to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'ac_to_inf', tag=u'ac_to_inf')
synrestrType.vc_to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'vc_to_inf', tag=u'vc_to_inf')
synrestrType.rs_to_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'rs_to_inf', tag=u'rs_to_inf')
synrestrType.bare_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'bare_inf', tag=u'bare_inf')
synrestrType.control_bare_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'control_bare_inf', tag=u'control_bare_inf')
synrestrType.ac_bare_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'ac_bare_inf', tag=u'ac_bare_inf')
synrestrType.oc_bare_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'oc_bare_inf', tag=u'oc_bare_inf')
synrestrType.rs_bare_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'rs_bare_inf', tag=u'rs_bare_inf')
synrestrType.wh_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'wh_inf', tag=u'wh_inf')
synrestrType.how_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'how_inf', tag=u'how_inf')
synrestrType.when_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'when_inf', tag=u'when_inf')
synrestrType.where_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'where_inf', tag=u'where_inf')
synrestrType.what_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'what_inf', tag=u'what_inf')
synrestrType.wheth_inf = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'wheth_inf', tag=u'wheth_inf')
synrestrType.for_comp = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'for_comp', tag=u'for_comp')
synrestrType.small_clause = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'small_clause', tag=u'small_clause')
synrestrType.gerund = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'gerund', tag=u'gerund')
synrestrType.control_ing = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'control_ing', tag=u'control_ing')
synrestrType.sc_ing = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'sc_ing', tag=u'sc_ing')
synrestrType.be_ing_sc = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'be_ing_sc', tag=u'be_ing_sc')
synrestrType.poss_ing_sc = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'poss_ing_sc', tag=u'poss_ing_sc')
synrestrType.oc_ing = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'oc_ing', tag=u'oc_ing')
synrestrType.ac_ing = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'ac_ing', tag=u'ac_ing')
synrestrType.poss_ing = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'poss_ing', tag=u'poss_ing')
synrestrType.np_omit_ing = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'np_omit_ing', tag=u'np_omit_ing')
synrestrType.ppart = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'ppart', tag=u'ppart')
synrestrType.quotation = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'quotation', tag=u'quotation')
synrestrType.plural = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'plural', tag=u'plural')
synrestrType.poss = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'poss', tag=u'poss')
synrestrType.definite = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'definite', tag=u'definite')
synrestrType.adv_loc = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'adv_loc', tag=u'adv_loc')
synrestrType.genitive = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'genitive', tag=u'genitive')
synrestrType.refl = synrestrType._CF_enumeration.addEnumeration(unicode_value=u'refl', tag=u'refl')
synrestrType._InitializeFacetMap(synrestrType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'synrestrType', synrestrType)

# Atomic simple type: predType
class predType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'predType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 362, 0)
    _Documentation = None
predType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=predType, enum_prefix=None)
predType.abstain = predType._CF_enumeration.addEnumeration(unicode_value=u'abstain', tag=u'abstain')
predType.admit = predType._CF_enumeration.addEnumeration(unicode_value=u'admit', tag=u'admit')
predType.Adv = predType._CF_enumeration.addEnumeration(unicode_value=u'Adv', tag=u'Adv')
predType.alive = predType._CF_enumeration.addEnumeration(unicode_value=u'alive', tag=u'alive')
predType.allow = predType._CF_enumeration.addEnumeration(unicode_value=u'allow', tag=u'allow')
predType.apart = predType._CF_enumeration.addEnumeration(unicode_value=u'apart', tag=u'apart')
predType.apply_heat = predType._CF_enumeration.addEnumeration(unicode_value=u'apply_heat', tag=u'apply_heat')
predType.apply_material = predType._CF_enumeration.addEnumeration(unicode_value=u'apply_material', tag=u'apply_material')
predType.associate = predType._CF_enumeration.addEnumeration(unicode_value=u'associate', tag=u'associate')
predType.attached = predType._CF_enumeration.addEnumeration(unicode_value=u'attached', tag=u'attached')
predType.attempt = predType._CF_enumeration.addEnumeration(unicode_value=u'attempt', tag=u'attempt')
predType.benefit = predType._CF_enumeration.addEnumeration(unicode_value=u'benefit', tag=u'benefit')
predType.body_motion = predType._CF_enumeration.addEnumeration(unicode_value=u'body_motion', tag=u'body_motion')
predType.body_process = predType._CF_enumeration.addEnumeration(unicode_value=u'body_process', tag=u'body_process')
predType.body_reflex = predType._CF_enumeration.addEnumeration(unicode_value=u'body_reflex', tag=u'body_reflex')
predType.capacity = predType._CF_enumeration.addEnumeration(unicode_value=u'capacity', tag=u'capacity')
predType.cause = predType._CF_enumeration.addEnumeration(unicode_value=u'cause', tag=u'cause')
predType.change_value = predType._CF_enumeration.addEnumeration(unicode_value=u'change_value', tag=u'change_value')
predType.command = predType._CF_enumeration.addEnumeration(unicode_value=u'command', tag=u'command')
predType.conspire = predType._CF_enumeration.addEnumeration(unicode_value=u'conspire', tag=u'conspire')
predType.contact = predType._CF_enumeration.addEnumeration(unicode_value=u'contact', tag=u'contact')
predType.cooked = predType._CF_enumeration.addEnumeration(unicode_value=u'cooked', tag=u'cooked')
predType.cooperate = predType._CF_enumeration.addEnumeration(unicode_value=u'cooperate', tag=u'cooperate')
predType.cost = predType._CF_enumeration.addEnumeration(unicode_value=u'cost', tag=u'cost')
predType.covered = predType._CF_enumeration.addEnumeration(unicode_value=u'covered', tag=u'covered')
predType.created_image = predType._CF_enumeration.addEnumeration(unicode_value=u'created_image', tag=u'created_image')
predType.dedicate = predType._CF_enumeration.addEnumeration(unicode_value=u'dedicate', tag=u'dedicate')
predType.degradation_material_integrity = predType._CF_enumeration.addEnumeration(unicode_value=u'degradation_material_integrity', tag=u'degradation_material_integrity')
predType.delay = predType._CF_enumeration.addEnumeration(unicode_value=u'delay', tag=u'delay')
predType.depend = predType._CF_enumeration.addEnumeration(unicode_value=u'depend', tag=u'depend')
predType.designated = predType._CF_enumeration.addEnumeration(unicode_value=u'designated', tag=u'designated')
predType.desire = predType._CF_enumeration.addEnumeration(unicode_value=u'desire', tag=u'desire')
predType.destroyed = predType._CF_enumeration.addEnumeration(unicode_value=u'destroyed', tag=u'destroyed')
predType.different = predType._CF_enumeration.addEnumeration(unicode_value=u'different', tag=u'different')
predType.direction = predType._CF_enumeration.addEnumeration(unicode_value=u'direction', tag=u'direction')
predType.disappear = predType._CF_enumeration.addEnumeration(unicode_value=u'disappear', tag=u'disappear')
predType.discomfort = predType._CF_enumeration.addEnumeration(unicode_value=u'discomfort', tag=u'discomfort')
predType.emit = predType._CF_enumeration.addEnumeration(unicode_value=u'emit', tag=u'emit')
predType.emotional_state = predType._CF_enumeration.addEnumeration(unicode_value=u'emotional_state', tag=u'emotional_state')
predType.end = predType._CF_enumeration.addEnumeration(unicode_value=u'end', tag=u'end')
predType.equals = predType._CF_enumeration.addEnumeration(unicode_value=u'equals', tag=u'equals')
predType.exert_force = predType._CF_enumeration.addEnumeration(unicode_value=u'exert_force', tag=u'exert_force')
predType.exist = predType._CF_enumeration.addEnumeration(unicode_value=u'exist', tag=u'exist')
predType.experience = predType._CF_enumeration.addEnumeration(unicode_value=u'experience', tag=u'experience')
predType.express = predType._CF_enumeration.addEnumeration(unicode_value=u'express', tag=u'express')
predType.filled_with = predType._CF_enumeration.addEnumeration(unicode_value=u'filled_with', tag=u'filled_with')
predType.flinch = predType._CF_enumeration.addEnumeration(unicode_value=u'flinch', tag=u'flinch')
predType.forbid = predType._CF_enumeration.addEnumeration(unicode_value=u'forbid', tag=u'forbid')
predType.force = predType._CF_enumeration.addEnumeration(unicode_value=u'force', tag=u'force')
predType.free = predType._CF_enumeration.addEnumeration(unicode_value=u'free', tag=u'free')
predType.future_possession = predType._CF_enumeration.addEnumeration(unicode_value=u'future_possession', tag=u'future_possession')
predType.give_birth = predType._CF_enumeration.addEnumeration(unicode_value=u'give_birth', tag=u'give_birth')
predType.harmed = predType._CF_enumeration.addEnumeration(unicode_value=u'harmed', tag=u'harmed')
predType.has_possession = predType._CF_enumeration.addEnumeration(unicode_value=u'has_possession', tag=u'has_possession')
predType.have_opinion = predType._CF_enumeration.addEnumeration(unicode_value=u'have_opinion', tag=u'have_opinion')
predType.help = predType._CF_enumeration.addEnumeration(unicode_value=u'help', tag=u'help')
predType.hold = predType._CF_enumeration.addEnumeration(unicode_value=u'hold', tag=u'hold')
predType.in_ = predType._CF_enumeration.addEnumeration(unicode_value=u'in', tag=u'in_')
predType.indicate = predType._CF_enumeration.addEnumeration(unicode_value=u'indicate', tag=u'indicate')
predType.in_reaction_to = predType._CF_enumeration.addEnumeration(unicode_value=u'in_reaction_to', tag=u'in_reaction_to')
predType.involuntary = predType._CF_enumeration.addEnumeration(unicode_value=u'involuntary', tag=u'involuntary')
predType.linger = predType._CF_enumeration.addEnumeration(unicode_value=u'linger', tag=u'linger')
predType.location = predType._CF_enumeration.addEnumeration(unicode_value=u'location', tag=u'location')
predType.made_of = predType._CF_enumeration.addEnumeration(unicode_value=u'made_of', tag=u'made_of')
predType.manner = predType._CF_enumeration.addEnumeration(unicode_value=u'manner', tag=u'manner')
predType.masquerade = predType._CF_enumeration.addEnumeration(unicode_value=u'masquerade', tag=u'masquerade')
predType.meets = predType._CF_enumeration.addEnumeration(unicode_value=u'meets', tag=u'meets')
predType.mingled = predType._CF_enumeration.addEnumeration(unicode_value=u'mingled', tag=u'mingled')
predType.motion = predType._CF_enumeration.addEnumeration(unicode_value=u'motion', tag=u'motion')
predType.nonagentive_cause = predType._CF_enumeration.addEnumeration(unicode_value=u'nonagentive_cause', tag=u'nonagentive_cause')
predType.occur = predType._CF_enumeration.addEnumeration(unicode_value=u'occur', tag=u'occur')
predType.occurred = predType._CF_enumeration.addEnumeration(unicode_value=u'occurred', tag=u'occurred')
predType.perform = predType._CF_enumeration.addEnumeration(unicode_value=u'perform', tag=u'perform')
predType.perceive = predType._CF_enumeration.addEnumeration(unicode_value=u'perceive', tag=u'perceive')
predType.physical_form = predType._CF_enumeration.addEnumeration(unicode_value=u'physical_form', tag=u'physical_form')
predType.position = predType._CF_enumeration.addEnumeration(unicode_value=u'position', tag=u'position')
predType.property_ = predType._CF_enumeration.addEnumeration(unicode_value=u'property', tag=u'property_')
predType.Prep = predType._CF_enumeration.addEnumeration(unicode_value=u'Prep', tag=u'Prep')
predType.Prop = predType._CF_enumeration.addEnumeration(unicode_value=u'Prop', tag=u'Prop')
predType.Pred = predType._CF_enumeration.addEnumeration(unicode_value=u'Pred', tag=u'Pred')
predType.rotational_motion = predType._CF_enumeration.addEnumeration(unicode_value=u'rotational_motion', tag=u'rotational_motion')
predType.rushed = predType._CF_enumeration.addEnumeration(unicode_value=u'rushed', tag=u'rushed')
predType.search = predType._CF_enumeration.addEnumeration(unicode_value=u'search', tag=u'search')
predType.sleep = predType._CF_enumeration.addEnumeration(unicode_value=u'sleep', tag=u'sleep')
predType.spend = predType._CF_enumeration.addEnumeration(unicode_value=u'spend', tag=u'spend')
predType.state = predType._CF_enumeration.addEnumeration(unicode_value=u'state', tag=u'state')
predType.suffocate = predType._CF_enumeration.addEnumeration(unicode_value=u'suffocate', tag=u'suffocate')
predType.take_care_of = predType._CF_enumeration.addEnumeration(unicode_value=u'take_care_of', tag=u'take_care_of')
predType.take_in = predType._CF_enumeration.addEnumeration(unicode_value=u'take_in', tag=u'take_in')
predType.together = predType._CF_enumeration.addEnumeration(unicode_value=u'together', tag=u'together')
predType.transfer = predType._CF_enumeration.addEnumeration(unicode_value=u'transfer', tag=u'transfer')
predType.transfer_info = predType._CF_enumeration.addEnumeration(unicode_value=u'transfer_info', tag=u'transfer_info')
predType.urge = predType._CF_enumeration.addEnumeration(unicode_value=u'urge', tag=u'urge')
predType.use = predType._CF_enumeration.addEnumeration(unicode_value=u'use', tag=u'use')
predType.value = predType._CF_enumeration.addEnumeration(unicode_value=u'value', tag=u'value')
predType.visible = predType._CF_enumeration.addEnumeration(unicode_value=u'visible', tag=u'visible')
predType.via = predType._CF_enumeration.addEnumeration(unicode_value=u'via', tag=u'via')
predType.amount_changed = predType._CF_enumeration.addEnumeration(unicode_value=u'amount_changed', tag=u'amount_changed')
predType.wear = predType._CF_enumeration.addEnumeration(unicode_value=u'wear', tag=u'wear')
predType.continue_ = predType._CF_enumeration.addEnumeration(unicode_value=u'continue', tag=u'continue_')
predType.avoid = predType._CF_enumeration.addEnumeration(unicode_value=u'avoid', tag=u'avoid')
predType.begin = predType._CF_enumeration.addEnumeration(unicode_value=u'begin', tag=u'begin')
predType.assess = predType._CF_enumeration.addEnumeration(unicode_value=u'assess', tag=u'assess')
predType.appear = predType._CF_enumeration.addEnumeration(unicode_value=u'appear', tag=u'appear')
predType.weather = predType._CF_enumeration.addEnumeration(unicode_value=u'weather', tag=u'weather')
predType.social_interaction = predType._CF_enumeration.addEnumeration(unicode_value=u'social_interaction', tag=u'social_interaction')
predType.believe = predType._CF_enumeration.addEnumeration(unicode_value=u'believe', tag=u'believe')
predType.financial_relationship = predType._CF_enumeration.addEnumeration(unicode_value=u'financial_relationship', tag=u'financial_relationship')
predType.describe = predType._CF_enumeration.addEnumeration(unicode_value=u'describe', tag=u'describe')
predType.hide = predType._CF_enumeration.addEnumeration(unicode_value=u'hide', tag=u'hide')
predType.declare = predType._CF_enumeration.addEnumeration(unicode_value=u'declare', tag=u'declare')
predType.conflict = predType._CF_enumeration.addEnumeration(unicode_value=u'conflict', tag=u'conflict')
predType.about = predType._CF_enumeration.addEnumeration(unicode_value=u'about', tag=u'about')
predType._InitializeFacetMap(predType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'predType', predType)

# Atomic simple type: primaryDescriptionType
class primaryDescriptionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'primaryDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 481, 0)
    _Documentation = None
primaryDescriptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=primaryDescriptionType, enum_prefix=None)
primaryDescriptionType.Apart_Reciprocal_Alternation_Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Apart Reciprocal Alternation Transitive', tag=u'Apart_Reciprocal_Alternation_Transitive')
primaryDescriptionType.Apart_Reciprocal_Alternation_Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Apart Reciprocal Alternation Intransitive', tag=u'Apart_Reciprocal_Alternation_Intransitive')
primaryDescriptionType.As_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'As Alternation', tag=u'As_Alternation')
primaryDescriptionType.Attribute_Object_Possessor_Attribute_Factoring_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Attribute Object Possessor-Attribute Factoring Alternation', tag=u'Attribute_Object_Possessor_Attribute_Factoring_Alternation')
primaryDescriptionType.Basic_Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Basic Intransitive', tag=u'Basic_Intransitive')
primaryDescriptionType.Basic_Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Basic Transitive', tag=u'Basic_Transitive')
primaryDescriptionType.Benefactive_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Benefactive Alternation', tag=u'Benefactive_Alternation')
primaryDescriptionType.Body_Part_Possessor_Ascension_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Body-Part Possessor Ascension Alternation', tag=u'Body_Part_Possessor_Ascension_Alternation')
primaryDescriptionType.Causative = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Causative', tag=u'Causative')
primaryDescriptionType.CausativeInchoative_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Causative/Inchoative Alternation', tag=u'CausativeInchoative_Alternation')
primaryDescriptionType.Characteristic_Property_of_Instrument = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Characteristic Property of Instrument', tag=u'Characteristic_Property_of_Instrument')
primaryDescriptionType.Collective_NP_Subject = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Collective NP Subject', tag=u'Collective_NP_Subject')
primaryDescriptionType.Conative = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Conative', tag=u'Conative')
primaryDescriptionType.Dative = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Dative', tag=u'Dative')
primaryDescriptionType.Direct_Speech = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Direct Speech', tag=u'Direct_Speech')
primaryDescriptionType.Expletive_Construction = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Expletive Construction', tag=u'Expletive_Construction')
primaryDescriptionType.Fulfilling_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Fulfilling Alternation', tag=u'Fulfilling_Alternation')
primaryDescriptionType.Image_Impression_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Image Impression Alternation', tag=u'Image_Impression_Alternation')
primaryDescriptionType.Induced_Action = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Induced Action', tag=u'Induced_Action')
primaryDescriptionType.Infinitival_Copular_Clause = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Infinitival Copular Clause', tag=u'Infinitival_Copular_Clause')
primaryDescriptionType.Instrument_Subject_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Instrument Subject Alternation', tag=u'Instrument_Subject_Alternation')
primaryDescriptionType.Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Intransitive', tag=u'Intransitive')
primaryDescriptionType.Location_Subject_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Location Subject Alternation', tag=u'Location_Subject_Alternation')
primaryDescriptionType.Locative_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Locative Alternation', tag=u'Locative_Alternation')
primaryDescriptionType.Locative_Inversion = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Locative Inversion', tag=u'Locative_Inversion')
primaryDescriptionType.Locative_Preposition_Drop = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Locative Preposition Drop', tag=u'Locative_Preposition_Drop')
primaryDescriptionType.Locatum_Subject_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Locatum Subject Alternation', tag=u'Locatum_Subject_Alternation')
primaryDescriptionType.MaterialProduct_Alternation_Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Material/Product Alternation Transitive', tag=u'MaterialProduct_Alternation_Transitive')
primaryDescriptionType.MaterialProduct_Alternation_Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Material/Product Alternation Intransitive', tag=u'MaterialProduct_Alternation_Intransitive')
primaryDescriptionType.Middle_Construction = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Middle Construction', tag=u'Middle_Construction')
primaryDescriptionType.Passive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Passive', tag=u'Passive')
primaryDescriptionType.Possessor_Subject_Possessor_Attribute_Factoring_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Possessor Subject Possessor-Attribute Factoring Alternation', tag=u'Possessor_Subject_Possessor_Attribute_Factoring_Alternation')
primaryDescriptionType.PRO_Arb_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PRO-Arb Object Alternation', tag=u'PRO_Arb_Object_Alternation')
primaryDescriptionType.Raw_Material_Subject_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Raw Material Subject Alternation', tag=u'Raw_Material_Subject_Alternation')
primaryDescriptionType.Reflexive_of_Appearance_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Reflexive of Appearance Alternation', tag=u'Reflexive_of_Appearance_Alternation')
primaryDescriptionType.Resultative = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Resultative', tag=u'Resultative')
primaryDescriptionType.Sentential_Complement = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Sentential Complement', tag=u'Sentential_Complement')
primaryDescriptionType.Simple_Reciprocal_Alternation_Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Simple Reciprocal Alternation Transitive', tag=u'Simple_Reciprocal_Alternation_Transitive')
primaryDescriptionType.Simple_Reciprocal_Alternation_Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Simple Reciprocal Alternation Intransitive', tag=u'Simple_Reciprocal_Alternation_Intransitive')
primaryDescriptionType.SubstanceSource_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Substance/Source Alternation', tag=u'SubstanceSource_Alternation')
primaryDescriptionType.Sum_of_Money_Subject_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Sum of Money Subject Alternation', tag=u'Sum_of_Money_Subject_Alternation')
primaryDescriptionType.There_insertion = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'There-insertion', tag=u'There_insertion')
primaryDescriptionType.ThroughWith_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Through/With Alternation', tag=u'ThroughWith_Alternation')
primaryDescriptionType.Together_Reciprocal_Alternation_Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Together Reciprocal Alternation Transitive', tag=u'Together_Reciprocal_Alternation_Transitive')
primaryDescriptionType.Together_Reciprocal_Alternation_Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Together Reciprocal Alternation Intransitive', tag=u'Together_Reciprocal_Alternation_Intransitive')
primaryDescriptionType.Total_Transformation_Alternation_Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Total Transformation Alternation Transitive', tag=u'Total_Transformation_Alternation_Transitive')
primaryDescriptionType.Total_Transformation_Alternation_Intransitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Total Transformation Alternation Intransitive', tag=u'Total_Transformation_Alternation_Intransitive')
primaryDescriptionType.Transitive = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Transitive', tag=u'Transitive')
primaryDescriptionType.Understood_Body_Part_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Understood Body-Part Object Alternation', tag=u'Understood_Body_Part_Object_Alternation')
primaryDescriptionType.Understood_Reciprocal_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Understood Reciprocal Object Alternation', tag=u'Understood_Reciprocal_Object_Alternation')
primaryDescriptionType.Understood_Reflexive_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Understood Reflexive Object Alternation', tag=u'Understood_Reflexive_Object_Alternation')
primaryDescriptionType.Unintentional_Interpretation_of_Object = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Unintentional Interpretation of Object', tag=u'Unintentional_Interpretation_of_Object')
primaryDescriptionType.Unspecified_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Unspecified Object Alternation', tag=u'Unspecified_Object_Alternation')
primaryDescriptionType.Unspecified_Reflexive_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Unspecified Reflexive Object Alternation', tag=u'Unspecified_Reflexive_Object_Alternation')
primaryDescriptionType.Way_Object_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'Way Object Alternation', tag=u'Way_Object_Alternation')
primaryDescriptionType.Withagainst_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'With/against Alternation', tag=u'Withagainst_Alternation')
primaryDescriptionType.With_Preposition_Drop_Alternation = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'With Preposition Drop Alternation', tag=u'With_Preposition_Drop_Alternation')
primaryDescriptionType.AS_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'AS-NP', tag=u'AS_NP')
primaryDescriptionType.EXTRAP_NP_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'EXTRAP-NP-S', tag=u'EXTRAP_NP_S')
primaryDescriptionType.S_SUBJ_NP_OBJ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'S-SUBJ-NP-OBJ', tag=u'S_SUBJ_NP_OBJ')
primaryDescriptionType.TO_INF_SUBJ_NP_OBJ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'TO-INF-SUBJ-NP-OBJ', tag=u'TO_INF_SUBJ_NP_OBJ')
primaryDescriptionType.EXTRAP_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'EXTRAP-TO-INF', tag=u'EXTRAP_TO_INF')
primaryDescriptionType.EXTRAP_FOR_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'EXTRAP-FOR-TO-INF', tag=u'EXTRAP_FOR_TO_INF')
primaryDescriptionType.EXTRAP_NP_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'EXTRAP-NP-TO-INF', tag=u'EXTRAP_NP_TO_INF')
primaryDescriptionType.EXTRAP_TO_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'EXTRAP-TO-NP', tag=u'EXTRAP_TO_NP')
primaryDescriptionType.EXTRAP_TO_NP_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'EXTRAP-TO-NP-TO-INF', tag=u'EXTRAP_TO_NP_TO_INF')
primaryDescriptionType.S_SUBJ_TO_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'S-SUBJ-TO-NP', tag=u'S_SUBJ_TO_NP')
primaryDescriptionType.FOR_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'FOR-TO-INF', tag=u'FOR_TO_INF')
primaryDescriptionType.HOW_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'HOW-S', tag=u'HOW_S')
primaryDescriptionType.HOW_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'HOW-TO-INF', tag=u'HOW_TO_INF')
primaryDescriptionType.INF_AC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'INF-AC', tag=u'INF_AC')
primaryDescriptionType.ING_NP_OMIT = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'ING-NP-OMIT', tag=u'ING_NP_OMIT')
primaryDescriptionType.ING_SCBE_ING_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'ING-SC/BE-ING-SC', tag=u'ING_SCBE_ING_SC')
primaryDescriptionType.ING_AC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'ING-AC', tag=u'ING_AC')
primaryDescriptionType.INTRANS = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'INTRANS', tag=u'INTRANS')
primaryDescriptionType.INTRANS_RECIPSUBJ_PLCOORD = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'INTRANS-RECIP(SUBJ-PL/COORD)', tag=u'INTRANS_RECIPSUBJ_PLCOORD')
primaryDescriptionType.NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP', tag=u'NP')
primaryDescriptionType.NP_ADJP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-ADJP', tag=u'NP_ADJP')
primaryDescriptionType.NP_ADJP_PRED = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-ADJP-PRED', tag=u'NP_ADJP_PRED')
primaryDescriptionType.NP_ADVP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-ADVP', tag=u'NP_ADVP')
primaryDescriptionType.NP_AVDP_PRED = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-AVDP-PRED', tag=u'NP_AVDP_PRED')
primaryDescriptionType.NP_AS_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-AS-NP', tag=u'NP_AS_NP')
primaryDescriptionType.NP_AS_NP_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-AS-NP-SC', tag=u'NP_AS_NP_SC')
primaryDescriptionType.NP_FOR_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-FOR-NP', tag=u'NP_FOR_NP')
primaryDescriptionType.NP_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-INF', tag=u'NP_INF')
primaryDescriptionType.NP_INF_OC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-INF-OC', tag=u'NP_INF_OC')
primaryDescriptionType.NP_ING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-ING', tag=u'NP_ING')
primaryDescriptionType.NP_ING_OC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-ING-OC', tag=u'NP_ING_OC')
primaryDescriptionType.NP_ING_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-ING-SC', tag=u'NP_ING_SC')
primaryDescriptionType.NP_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-NP', tag=u'NP_NP')
primaryDescriptionType.NP_NP_PRED = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-NP-PRED', tag=u'NP_NP_PRED')
primaryDescriptionType.NP_P_ING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-ING', tag=u'NP_P_ING')
primaryDescriptionType.NP_P_ING_OC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-ING-OC', tag=u'NP_P_ING_OC')
primaryDescriptionType.NP_P_ING_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-ING-SC', tag=u'NP_P_ING_SC')
primaryDescriptionType.NP_P_ING_AC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-ING-AC', tag=u'NP_P_ING_AC')
primaryDescriptionType.NP_P_NP_ING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-NP-ING', tag=u'NP_P_NP_ING')
primaryDescriptionType.NP_P_POSSING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-POSSING', tag=u'NP_P_POSSING')
primaryDescriptionType.NP_P_WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-WH-S', tag=u'NP_P_WH_S')
primaryDescriptionType.NP_P_WHAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-WHAT-S', tag=u'NP_P_WHAT_S')
primaryDescriptionType.NP_P_WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-WHAT-TO-INF', tag=u'NP_P_WHAT_TO_INF')
primaryDescriptionType.NP_P_WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-P-WH-TO-INF', tag=u'NP_P_WH_TO_INF')
primaryDescriptionType.NP_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-PP', tag=u'NP_PP')
primaryDescriptionType.NP_PP_PRED = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-PP-PRED', tag=u'NP_PP_PRED')
primaryDescriptionType.NP_PRED_RS = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-PRED-RS', tag=u'NP_PRED_RS')
primaryDescriptionType.NP_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-S', tag=u'NP_S')
primaryDescriptionType.NP_TO_INF_OC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-TO-INF-OC', tag=u'NP_TO_INF_OC')
primaryDescriptionType.NP_TO_INF_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-TO-INF-SC', tag=u'NP_TO_INF_SC')
primaryDescriptionType.NP_TO_INF_VC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-TO-INF-VC', tag=u'NP_TO_INF_VC')
primaryDescriptionType.NP_TO_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-TO-NP', tag=u'NP_TO_NP')
primaryDescriptionType.NP_TOBE = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-TOBE', tag=u'NP_TOBE')
primaryDescriptionType.NP_VEN_NP_OMIT = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-VEN-NP-OMIT', tag=u'NP_VEN_NP_OMIT')
primaryDescriptionType.NP_WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-WH-S', tag=u'NP_WH_S')
primaryDescriptionType.NP_WHAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-WHAT-S', tag=u'NP_WHAT_S')
primaryDescriptionType.NP_WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-WH-TO-INF', tag=u'NP_WH_TO_INF')
primaryDescriptionType.NP_WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-WHAT-TO-INF', tag=u'NP_WHAT_TO_INF')
primaryDescriptionType.P_ING_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-ING-SC', tag=u'P_ING_SC')
primaryDescriptionType.P_ING_AC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-ING-AC', tag=u'P_ING_AC')
primaryDescriptionType.P_NP_ING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-NP-ING', tag=u'P_NP_ING')
primaryDescriptionType.P_NP_TO_INF_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-NP-TO-INF(-SC)', tag=u'P_NP_TO_INF_SC')
primaryDescriptionType.P_NP_TO_INF_OC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-NP-TO-INF-OC', tag=u'P_NP_TO_INF_OC')
primaryDescriptionType.P_NP_TO_INF_VC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-NP-TO-INF-VC', tag=u'P_NP_TO_INF_VC')
primaryDescriptionType.P_POSSING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-POSSING', tag=u'P_POSSING')
primaryDescriptionType.P_WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-WH-S', tag=u'P_WH_S')
primaryDescriptionType.P_WHAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-WHAT-S', tag=u'P_WHAT_S')
primaryDescriptionType.P_WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-WH-TO-INF', tag=u'P_WH_TO_INF')
primaryDescriptionType.P_WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'P-WHAT-TO-INF', tag=u'P_WHAT_TO_INF')
primaryDescriptionType.PART = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART', tag=u'PART')
primaryDescriptionType.PART_ING_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-ING-SC', tag=u'PART_ING_SC')
primaryDescriptionType.PART_NPNP_PART = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-NP/NP-PART', tag=u'PART_NPNP_PART')
primaryDescriptionType.PART_NP_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-NP-PP', tag=u'PART_NP_PP')
primaryDescriptionType.PART_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-PP', tag=u'PART_PP')
primaryDescriptionType.PART_WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-WH-S', tag=u'PART_WH_S')
primaryDescriptionType.PART_WH_S_ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-WH-S', tag=u'PART_WH_S_')
primaryDescriptionType.PART_WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-WH-TO-INF', tag=u'PART_WH_TO_INF')
primaryDescriptionType.PART_WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-WHAT-TO-INF', tag=u'PART_WHAT_TO_INF')
primaryDescriptionType.PART_THAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-THAT-S', tag=u'PART_THAT_S')
primaryDescriptionType.POSSING = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'POSSING', tag=u'POSSING')
primaryDescriptionType.POSSING_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'POSSING-PP', tag=u'POSSING_PP')
primaryDescriptionType.ING_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'ING-PP', tag=u'ING_PP')
primaryDescriptionType.PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP', tag=u'PP')
primaryDescriptionType.PP_FOR_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-FOR-TO-INF', tag=u'PP_FOR_TO_INF')
primaryDescriptionType.PP_HOW_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-HOW-S', tag=u'PP_HOW_S')
primaryDescriptionType.PP_HOW_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-HOW-TO-INF', tag=u'PP_HOW_TO_INF')
primaryDescriptionType.PP_P_WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-P-WH-S', tag=u'PP_P_WH_S')
primaryDescriptionType.PP_P_WHAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-P-WHAT-S', tag=u'PP_P_WHAT_S')
primaryDescriptionType.PP_P_WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-P-WHAT-TO-INF', tag=u'PP_P_WHAT_TO_INF')
primaryDescriptionType.PP_P_WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-P-WH-TO-INF', tag=u'PP_P_WH_TO_INF')
primaryDescriptionType.PP_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-PP', tag=u'PP_PP')
primaryDescriptionType.PP_PRED_RS = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-PRED-RS', tag=u'PP_PRED_RS')
primaryDescriptionType.PP_THAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-THAT-S', tag=u'PP_THAT_S')
primaryDescriptionType.PP_THAT_S_SUBJUNCT = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-THAT-S-SUBJUNCT', tag=u'PP_THAT_S_SUBJUNCT')
primaryDescriptionType.PP_TO_INF_RS = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-TO-INF-RS', tag=u'PP_TO_INF_RS')
primaryDescriptionType.PP_WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-WH-S', tag=u'PP_WH_S')
primaryDescriptionType.PP_WHAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-WHAT-S', tag=u'PP_WHAT_S')
primaryDescriptionType.PP_WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-WH-TO-INF', tag=u'PP_WH_TO_INF')
primaryDescriptionType.PP_WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PP-WHAT-TO-INF', tag=u'PP_WHAT_TO_INF')
primaryDescriptionType.S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'S', tag=u'S')
primaryDescriptionType.S_SUBJ_S_OBJ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'S-SUBJ-S-OBJ', tag=u'S_SUBJ_S_OBJ')
primaryDescriptionType.S_SUBJUNCT = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'S-SUBJUNCT', tag=u'S_SUBJUNCT')
primaryDescriptionType.SEEM_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'SEEM-S', tag=u'SEEM_S')
primaryDescriptionType.SEEM_TO_NP_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'SEEM-TO-NP-S', tag=u'SEEM_TO_NP_S')
primaryDescriptionType.THAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'THAT-S', tag=u'THAT_S')
primaryDescriptionType.TO_INF_AC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'TO-INF-AC', tag=u'TO_INF_AC')
primaryDescriptionType.TO_INF_RS = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'TO-INF-RS', tag=u'TO_INF_RS')
primaryDescriptionType.TO_INF_SC = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'TO-INF-SC', tag=u'TO_INF_SC')
primaryDescriptionType.WH_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'WH-S', tag=u'WH_S')
primaryDescriptionType.WHAT_S = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'WHAT-S', tag=u'WHAT_S')
primaryDescriptionType.WH_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'WH-TO-INF', tag=u'WH_TO_INF')
primaryDescriptionType.WHAT_TO_INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'WHAT-TO_INF', tag=u'WHAT_TO_INF')
primaryDescriptionType.NP_PART_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-PART-PP', tag=u'NP_PART_PP')
primaryDescriptionType.PART_PP_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'PART-PP-PP', tag=u'PART_PP_PP')
primaryDescriptionType.NP_PP_PP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-PP-PP', tag=u'NP_PP_PP')
primaryDescriptionType.NP_ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP', tag=u'NP_')
primaryDescriptionType.NP_NP_ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-NP', tag=u'NP_NP_')
primaryDescriptionType.S_SUBJ = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'S-SUBJ', tag=u'S_SUBJ')
primaryDescriptionType.INF = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'INF', tag=u'INF')
primaryDescriptionType.NP_as_NP = primaryDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'NP-as-NP', tag=u'NP_as_NP')
primaryDescriptionType._InitializeFacetMap(primaryDescriptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'primaryDescriptionType', primaryDescriptionType)

# Atomic simple type: argType
class argType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'argType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 664, 0)
    _Documentation = None
argType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=argType, enum_prefix=None)
argType.Constant = argType._CF_enumeration.addEnumeration(unicode_value=u'Constant', tag=u'Constant')
argType.Event = argType._CF_enumeration.addEnumeration(unicode_value=u'Event', tag=u'Event')
argType.ThemRole = argType._CF_enumeration.addEnumeration(unicode_value=u'ThemRole', tag=u'ThemRole')
argType.VerbSpecific = argType._CF_enumeration.addEnumeration(unicode_value=u'VerbSpecific', tag=u'VerbSpecific')
argType._InitializeFacetMap(argType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'argType', argType)

# Atomic simple type: argConstantType
class argConstantType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'argConstantType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 673, 0)
    _Documentation = None
argConstantType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=argConstantType, enum_prefix=None)
argConstantType.abstract = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'abstract', tag=u'abstract')
argConstantType.abstractphysical = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'abstract/physical', tag=u'abstractphysical')
argConstantType.directedmotion = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'directedmotion', tag=u'directedmotion')
argConstantType.forceful = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'forceful', tag=u'forceful')
argConstantType.from_ = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'from', tag=u'from_')
argConstantType.illegal = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'illegal', tag=u'illegal')
argConstantType.physical = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'physical', tag=u'physical')
argConstantType.physicalabstract = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'physical/abstract', tag=u'physicalabstract')
argConstantType.toward = argConstantType._CF_enumeration.addEnumeration(unicode_value=u'toward', tag=u'toward')
argConstantType._InitializeFacetMap(argConstantType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'argConstantType', argConstantType)

# Atomic simple type: argEventType
class argEventType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'argEventType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 687, 0)
    _Documentation = None
argEventType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=argEventType, enum_prefix=None)
argEventType.E = argEventType._CF_enumeration.addEnumeration(unicode_value=u'E', tag=u'E')
argEventType.E0 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'E0', tag=u'E0')
argEventType.E1 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'E1', tag=u'E1')
argEventType.duringE = argEventType._CF_enumeration.addEnumeration(unicode_value=u'during(E)', tag=u'duringE')
argEventType.duringE0 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'during(E0)', tag=u'duringE0')
argEventType.duringE1 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'during(E1)', tag=u'duringE1')
argEventType.endE = argEventType._CF_enumeration.addEnumeration(unicode_value=u'end(E)', tag=u'endE')
argEventType.endE0 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'end(E0)', tag=u'endE0')
argEventType.endE1 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'end(E1)', tag=u'endE1')
argEventType.resultE = argEventType._CF_enumeration.addEnumeration(unicode_value=u'result(E)', tag=u'resultE')
argEventType.resultE0 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'result(E0)', tag=u'resultE0')
argEventType.resultE1 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'result(E1)', tag=u'resultE1')
argEventType.startE = argEventType._CF_enumeration.addEnumeration(unicode_value=u'start(E)', tag=u'startE')
argEventType.startE0 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'start(E0)', tag=u'startE0')
argEventType.startE1 = argEventType._CF_enumeration.addEnumeration(unicode_value=u'start(E1)', tag=u'startE1')
argEventType._InitializeFacetMap(argEventType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'argEventType', argEventType)

# Atomic simple type: argVerbSpecificType
class argVerbSpecificType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'argVerbSpecificType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 708, 0)
    _Documentation = None
argVerbSpecificType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=argVerbSpecificType, enum_prefix=None)
argVerbSpecificType.Direction = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Direction', tag=u'Direction')
argVerbSpecificType.Endstate = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Endstate', tag=u'Endstate')
argVerbSpecificType.Form = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Form', tag=u'Form')
argVerbSpecificType.Material = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Material', tag=u'Material')
argVerbSpecificType.Motion = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Motion', tag=u'Motion')
argVerbSpecificType.Pos = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Pos', tag=u'Pos')
argVerbSpecificType.Prep = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Prep', tag=u'Prep')
argVerbSpecificType.Prop = argVerbSpecificType._CF_enumeration.addEnumeration(unicode_value=u'Prop', tag=u'Prop')
argVerbSpecificType._InitializeFacetMap(argVerbSpecificType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'argVerbSpecificType', argVerbSpecificType)

# List simple type: wnType
# superclasses pyxb.binding.datatypes.anySimpleType
class wnType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of auxWordnetType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'wnType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 184, 0)
    _Documentation = None

    _ItemType = auxWordnetType
wnType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'wnType', wnType)

# Union simple type: npType
# superclasses pyxb.binding.datatypes.anySimpleType
class npType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of auxnpType, themRoleType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'npType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 199, 0)
    _Documentation = None

    _MemberTypes = ( auxnpType, themRoleType, )
npType._CF_pattern = pyxb.binding.facets.CF_pattern()
npType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=npType)
npType.Oblique = u'Oblique'                       # originally auxnpType.Oblique
npType.Oblique1 = u'Oblique1'                     # originally auxnpType.Oblique1
npType.Oblique2 = u'Oblique2'                     # originally auxnpType.Oblique2
npType.NP = u'NP'                                 # originally auxnpType.NP
npType.Topic = u'Topic'                           # originally themRoleType.Topic
npType.Experiencer = u'Experiencer'               # originally themRoleType.Experiencer
npType.Stimulus = u'Stimulus'                     # originally themRoleType.Stimulus
npType.Cause = u'Cause'                           # originally themRoleType.Cause
npType.Actor = u'Actor'                           # originally themRoleType.Actor
npType.Actor1 = u'Actor1'                         # originally themRoleType.Actor1
npType.Actor2 = u'Actor2'                         # originally themRoleType.Actor2
npType.Agent = u'Agent'                           # originally themRoleType.Agent
npType.Asset = u'Asset'                           # originally themRoleType.Asset
npType.Attribute = u'Attribute'                   # originally themRoleType.Attribute
npType.Benefactor = u'Benefactor'                 # originally themRoleType.Benefactor
npType.Beneficiary = u'Beneficiary'               # originally themRoleType.Beneficiary
npType.Content = u'Content'                       # originally themRoleType.Content
npType.Destination = u'Destination'               # originally themRoleType.Destination
npType.Instrument = u'Instrument'                 # originally themRoleType.Instrument
npType.Location = u'Location'                     # originally themRoleType.Location
npType.Material = u'Material'                     # originally themRoleType.Material
npType.Patient = u'Patient'                       # originally themRoleType.Patient
npType.Patient1 = u'Patient1'                     # originally themRoleType.Patient1
npType.Patient2 = u'Patient2'                     # originally themRoleType.Patient2
npType.Predicate = u'Predicate'                   # originally themRoleType.Predicate
npType.Proposition = u'Proposition'               # originally themRoleType.Proposition
npType.Product = u'Product'                       # originally themRoleType.Product
npType.Recipient = u'Recipient'                   # originally themRoleType.Recipient
npType.Source = u'Source'                         # originally themRoleType.Source
npType.Theme = u'Theme'                           # originally themRoleType.Theme
npType.Theme1 = u'Theme1'                         # originally themRoleType.Theme1
npType.Theme2 = u'Theme2'                         # originally themRoleType.Theme2
npType.Time = u'Time'                             # originally themRoleType.Time
npType.Extent = u'Extent'                         # originally themRoleType.Extent
npType.Value = u'Value'                           # originally themRoleType.Value
npType._InitializeFacetMap(npType._CF_pattern,
   npType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'npType', npType)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MEMBERS uses Python identifier MEMBERS
    __MEMBERS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS'), 'MEMBERS', '__AbsentNamespace0_CTD_ANON_MEMBERS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 23, 0), )

    
    MEMBERS = property(__MEMBERS.value, __MEMBERS.set, None, None)

    
    # Element THEMROLES uses Python identifier THEMROLES
    __THEMROLES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES'), 'THEMROLES', '__AbsentNamespace0_CTD_ANON_THEMROLES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 30, 0), )

    
    THEMROLES = property(__THEMROLES.value, __THEMROLES.set, None, None)

    
    # Element FRAMES uses Python identifier FRAMES
    __FRAMES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FRAMES'), 'FRAMES', '__AbsentNamespace0_CTD_ANON_FRAMES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 63, 0), )

    
    FRAMES = property(__FRAMES.value, __FRAMES.set, None, None)

    
    # Element SUBCLASSES uses Python identifier SUBCLASSES
    __SUBCLASSES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES'), 'SUBCLASSES', '__AbsentNamespace0_CTD_ANON_SUBCLASSES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 151, 0), )

    
    SUBCLASSES = property(__SUBCLASSES.value, __SUBCLASSES.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_ID', pyxb.binding.datatypes.ID, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 19, 4)
    __ID._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 19, 4)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __MEMBERS.name() : __MEMBERS,
        __THEMROLES.name() : __THEMROLES,
        __FRAMES.name() : __FRAMES,
        __SUBCLASSES.name() : __SUBCLASSES
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 23, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MEMBER uses Python identifier MEMBER
    __MEMBER = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MEMBER'), 'MEMBER', '__AbsentNamespace0_CTD_ANON__MEMBER', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 24, 2), )

    
    MEMBER = property(__MEMBER.value, __MEMBER.set, None, None)

    _ElementMap.update({
        __MEMBER.name() : __MEMBER
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 30, 30)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element THEMROLE uses Python identifier THEMROLE
    __THEMROLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'THEMROLE'), 'THEMROLE', '__AbsentNamespace0_CTD_ANON_2_THEMROLE', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 31, 2), )

    
    THEMROLE = property(__THEMROLE.value, __THEMROLE.set, None, None)

    _ElementMap.update({
        __THEMROLE.name() : __THEMROLE
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 30)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SELRESTRS uses Python identifier SELRESTRS
    __SELRESTRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), 'SELRESTRS', '__AbsentNamespace0_CTD_ANON_3_SELRESTRS', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0), )

    
    SELRESTRS = property(__SELRESTRS.value, __SELRESTRS.set, None, None)

    
    # Element SELRESTR uses Python identifier SELRESTR
    __SELRESTR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SELRESTR'), 'SELRESTR', '__AbsentNamespace0_CTD_ANON_3_SELRESTR', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 43, 4), )

    
    SELRESTR = property(__SELRESTR.value, __SELRESTR.set, None, None)

    
    # Attribute logic uses Python identifier logic
    __logic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'logic'), 'logic', '__AbsentNamespace0_CTD_ANON_3_logic', pyxb.binding.datatypes.string)
    __logic._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 49, 2)
    __logic._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 49, 2)
    
    logic = property(__logic.value, __logic.set, None, None)

    _ElementMap.update({
        __SELRESTRS.name() : __SELRESTRS,
        __SELRESTR.name() : __SELRESTR
    })
    _AttributeMap.update({
        __logic.name() : __logic
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 52, 30)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SYNRESTRS uses Python identifier SYNRESTRS
    __SYNRESTRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS'), 'SYNRESTRS', '__AbsentNamespace0_CTD_ANON_4_SYNRESTRS', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 52, 0), )

    
    SYNRESTRS = property(__SYNRESTRS.value, __SYNRESTRS.set, None, None)

    
    # Element SYNRESTR uses Python identifier SYNRESTR
    __SYNRESTR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SYNRESTR'), 'SYNRESTR', '__AbsentNamespace0_CTD_ANON_4_SYNRESTR', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 54, 4), )

    
    SYNRESTR = property(__SYNRESTR.value, __SYNRESTR.set, None, None)

    
    # Attribute logic uses Python identifier logic
    __logic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'logic'), 'logic', '__AbsentNamespace0_CTD_ANON_4_logic', pyxb.binding.datatypes.string)
    __logic._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 60, 2)
    __logic._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 60, 2)
    
    logic = property(__logic.value, __logic.set, None, None)

    _ElementMap.update({
        __SYNRESTRS.name() : __SYNRESTRS,
        __SYNRESTR.name() : __SYNRESTR
    })
    _AttributeMap.update({
        __logic.name() : __logic
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 63, 27)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FRAME uses Python identifier FRAME
    __FRAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'FRAME'), 'FRAME', '__AbsentNamespace0_CTD_ANON_5_FRAME', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 64, 2), )

    
    FRAME = property(__FRAME.value, __FRAME.set, None, None)

    _ElementMap.update({
        __FRAME.name() : __FRAME
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 64, 64)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DESCRIPTION uses Python identifier DESCRIPTION
    __DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'DESCRIPTION'), 'DESCRIPTION', '__AbsentNamespace0_CTD_ANON_6_DESCRIPTION', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 66, 6), )

    
    DESCRIPTION = property(__DESCRIPTION.value, __DESCRIPTION.set, None, None)

    
    # Element EXAMPLES uses Python identifier EXAMPLES
    __EXAMPLES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'EXAMPLES'), 'EXAMPLES', '__AbsentNamespace0_CTD_ANON_6_EXAMPLES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 72, 6), )

    
    EXAMPLES = property(__EXAMPLES.value, __EXAMPLES.set, None, None)

    
    # Element SYNTAX uses Python identifier SYNTAX
    __SYNTAX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SYNTAX'), 'SYNTAX', '__AbsentNamespace0_CTD_ANON_6_SYNTAX', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 110, 0), )

    
    SYNTAX = property(__SYNTAX.value, __SYNTAX.set, None, None)

    
    # Element SEMANTICS uses Python identifier SEMANTICS
    __SEMANTICS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SEMANTICS'), 'SEMANTICS', '__AbsentNamespace0_CTD_ANON_6_SEMANTICS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 130, 0), )

    
    SEMANTICS = property(__SEMANTICS.value, __SEMANTICS.set, None, None)

    _ElementMap.update({
        __DESCRIPTION.name() : __DESCRIPTION,
        __EXAMPLES.name() : __EXAMPLES,
        __SYNTAX.name() : __SYNTAX,
        __SEMANTICS.name() : __SEMANTICS
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 72, 35)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EXAMPLE uses Python identifier EXAMPLE
    __EXAMPLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'EXAMPLE'), 'EXAMPLE', '__AbsentNamespace0_CTD_ANON_7_EXAMPLE', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 73, 8), )

    
    EXAMPLE = property(__EXAMPLE.value, __EXAMPLE.set, None, None)

    _ElementMap.update({
        __EXAMPLE.name() : __EXAMPLE
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 91, 25)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SELRESTRS uses Python identifier SELRESTRS
    __SELRESTRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SELRESTRS'), 'SELRESTRS', '__AbsentNamespace0_CTD_ANON_8_SELRESTRS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 93, 4), )

    
    SELRESTRS = property(__SELRESTRS.value, __SELRESTRS.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__AbsentNamespace0_CTD_ANON_8_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 103, 2)
    __value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 103, 2)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __SELRESTRS.name() : __SELRESTRS
    })
    _AttributeMap.update({
        __value.name() : __value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 93, 34)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SELRESTR uses Python identifier SELRESTR
    __SELRESTR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SELRESTR'), 'SELRESTR', '__AbsentNamespace0_CTD_ANON_9_SELRESTR', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 95, 1), )

    
    SELRESTR = property(__SELRESTR.value, __SELRESTR.set, None, None)

    
    # Attribute logic uses Python identifier logic
    __logic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'logic'), 'logic', '__AbsentNamespace0_CTD_ANON_9_logic', pyxb.binding.datatypes.string)
    __logic._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 100, 6)
    __logic._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 100, 6)
    
    logic = property(__logic.value, __logic.set, None, None)

    _ElementMap.update({
        __SELRESTR.name() : __SELRESTR
    })
    _AttributeMap.update({
        __logic.name() : __logic
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 106, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__AbsentNamespace0_CTD_ANON_10_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 107, 2)
    __value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 107, 2)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 110, 27)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NP uses Python identifier NP
    __NP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NP'), 'NP', '__AbsentNamespace0_CTD_ANON_11_NP', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 81, 0), )

    
    NP = property(__NP.value, __NP.set, None, None)

    
    # Element PREP uses Python identifier PREP
    __PREP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PREP'), 'PREP', '__AbsentNamespace0_CTD_ANON_11_PREP', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 91, 0), )

    
    PREP = property(__PREP.value, __PREP.set, None, None)

    
    # Element LEX uses Python identifier LEX
    __LEX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'LEX'), 'LEX', '__AbsentNamespace0_CTD_ANON_11_LEX', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 106, 0), )

    
    LEX = property(__LEX.value, __LEX.set, None, None)

    
    # Element ADV uses Python identifier ADV
    __ADV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ADV'), 'ADV', '__AbsentNamespace0_CTD_ANON_11_ADV', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 114, 6), )

    
    ADV = property(__ADV.value, __ADV.set, None, None)

    
    # Element ADJ uses Python identifier ADJ
    __ADJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ADJ'), 'ADJ', '__AbsentNamespace0_CTD_ANON_11_ADJ', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 115, 6), )

    
    ADJ = property(__ADJ.value, __ADJ.set, None, None)

    
    # Element VERB uses Python identifier VERB
    __VERB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'VERB'), 'VERB', '__AbsentNamespace0_CTD_ANON_11_VERB', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 119, 4), )

    
    VERB = property(__VERB.value, __VERB.set, None, None)

    _ElementMap.update({
        __NP.name() : __NP,
        __PREP.name() : __PREP,
        __LEX.name() : __LEX,
        __ADV.name() : __ADV,
        __ADJ.name() : __ADJ,
        __VERB.name() : __VERB
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 130, 30)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PRED uses Python identifier PRED
    __PRED = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PRED'), 'PRED', '__AbsentNamespace0_CTD_ANON_12_PRED', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 132, 4), )

    
    PRED = property(__PRED.value, __PRED.set, None, None)

    _ElementMap.update({
        __PRED.name() : __PRED
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 134, 33)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ARG uses Python identifier ARG
    __ARG = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ARG'), 'ARG', '__AbsentNamespace0_CTD_ANON_13_ARG', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 146, 0), )

    
    ARG = property(__ARG.value, __ARG.set, None, None)

    _ElementMap.update({
        __ARG.name() : __ARG
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 151, 31)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element VNSUBCLASS uses Python identifier VNSUBCLASS
    __VNSUBCLASS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'VNSUBCLASS'), 'VNSUBCLASS', '__AbsentNamespace0_CTD_ANON_14_VNSUBCLASS', True, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 155, 0), )

    
    VNSUBCLASS = property(__VNSUBCLASS.value, __VNSUBCLASS.set, None, None)

    _ElementMap.update({
        __VNSUBCLASS.name() : __VNSUBCLASS
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 156, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element MEMBERS uses Python identifier MEMBERS
    __MEMBERS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS'), 'MEMBERS', '__AbsentNamespace0_CTD_ANON_15_MEMBERS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 23, 0), )

    
    MEMBERS = property(__MEMBERS.value, __MEMBERS.set, None, None)

    
    # Element THEMROLES uses Python identifier THEMROLES
    __THEMROLES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES'), 'THEMROLES', '__AbsentNamespace0_CTD_ANON_15_THEMROLES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 30, 0), )

    
    THEMROLES = property(__THEMROLES.value, __THEMROLES.set, None, None)

    
    # Element FRAMES uses Python identifier FRAMES
    __FRAMES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FRAMES'), 'FRAMES', '__AbsentNamespace0_CTD_ANON_15_FRAMES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 63, 0), )

    
    FRAMES = property(__FRAMES.value, __FRAMES.set, None, None)

    
    # Element SUBCLASSES uses Python identifier SUBCLASSES
    __SUBCLASSES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES'), 'SUBCLASSES', '__AbsentNamespace0_CTD_ANON_15_SUBCLASSES', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 151, 0), )

    
    SUBCLASSES = property(__SUBCLASSES.value, __SUBCLASSES.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_15_ID', pyxb.binding.datatypes.ID, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 163, 4)
    __ID._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 163, 4)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __MEMBERS.name() : __MEMBERS,
        __THEMROLES.name() : __THEMROLES,
        __FRAMES.name() : __FRAMES,
        __SUBCLASSES.name() : __SUBCLASSES
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SELRESTRS uses Python identifier SELRESTRS
    __SELRESTRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), 'SELRESTRS', '__AbsentNamespace0_CTD_ANON_16_SELRESTRS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0), )

    
    SELRESTRS = property(__SELRESTRS.value, __SELRESTRS.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_CTD_ANON_16_type', themRoleType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 36, 6)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 36, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __SELRESTRS.name() : __SELRESTRS
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 43, 33)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_CTD_ANON_17_Value', selrestrValueType, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 44, 6)
    __Value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 44, 6)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_CTD_ANON_17_type', selrestrType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 45, 6)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 45, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value,
        __type.name() : __type
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 54, 33)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_CTD_ANON_18_Value', selrestrValueType, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 55, 6)
    __Value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 55, 6)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_CTD_ANON_18_type', synrestrType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 56, 6)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 56, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value,
        __type.name() : __type
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 66, 38)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute descriptionNumber uses Python identifier descriptionNumber
    __descriptionNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'descriptionNumber'), 'descriptionNumber', '__AbsentNamespace0_CTD_ANON_19_descriptionNumber', pyxb.binding.datatypes.string, required=True)
    __descriptionNumber._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 67, 8)
    __descriptionNumber._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 67, 8)
    
    descriptionNumber = property(__descriptionNumber.value, __descriptionNumber.set, None, None)

    
    # Attribute primary uses Python identifier primary
    __primary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'primary'), 'primary', '__AbsentNamespace0_CTD_ANON_19_primary', primaryDescriptionType, required=True)
    __primary._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 68, 8)
    __primary._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 68, 8)
    
    primary = property(__primary.value, __primary.set, None, None)

    
    # Attribute secondary uses Python identifier secondary
    __secondary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'secondary'), 'secondary', '__AbsentNamespace0_CTD_ANON_19_secondary', pyxb.binding.datatypes.string)
    __secondary._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 69, 8)
    __secondary._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 69, 8)
    
    secondary = property(__secondary.value, __secondary.set, None, None)

    
    # Attribute xtag uses Python identifier xtag
    __xtag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'xtag'), 'xtag', '__AbsentNamespace0_CTD_ANON_19_xtag', pyxb.binding.datatypes.string, required=True)
    __xtag._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 70, 1)
    __xtag._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 70, 1)
    
    xtag = property(__xtag.value, __xtag.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __descriptionNumber.name() : __descriptionNumber,
        __primary.name() : __primary,
        __secondary.name() : __secondary,
        __xtag.name() : __xtag
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 95, 30)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_CTD_ANON_20_Value', selrestrValueType, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 96, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 96, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_CTD_ANON_20_type', preprestrType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 97, 3)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 97, 3)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value,
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 132, 29)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ARGS uses Python identifier ARGS
    __ARGS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ARGS'), 'ARGS', '__AbsentNamespace0_CTD_ANON_21_ARGS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 134, 8), )

    
    ARGS = property(__ARGS.value, __ARGS.set, None, None)

    
    # Attribute bool uses Python identifier bool
    __bool = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'bool'), 'bool', '__AbsentNamespace0_CTD_ANON_21_bool', pyxb.binding.datatypes.string)
    __bool._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 140, 6)
    __bool._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 140, 6)
    
    bool = property(__bool.value, __bool.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__AbsentNamespace0_CTD_ANON_21_value', predType, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 141, 6)
    __value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 141, 6)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __ARGS.name() : __ARGS
    })
    _AttributeMap.update({
        __bool.name() : __bool,
        __value.name() : __value
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 146, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_CTD_ANON_22_type', argType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 147, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 147, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__AbsentNamespace0_CTD_ANON_22_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 148, 2)
    __value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 148, 2)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __value.name() : __value
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 24, 65)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_CTD_ANON_23_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 25, 4)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 25, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute wn uses Python identifier wn
    __wn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'wn'), 'wn', '__AbsentNamespace0_CTD_ANON_23_wn', wnType, required=True)
    __wn._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 26, 4)
    __wn._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 26, 4)
    
    wn = property(__wn.value, __wn.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __wn.name() : __wn
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 82, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SELRESTRS uses Python identifier SELRESTRS
    __SELRESTRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), 'SELRESTRS', '__AbsentNamespace0_CTD_ANON_24_SELRESTRS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0), )

    
    SELRESTRS = property(__SELRESTRS.value, __SELRESTRS.set, None, None)

    
    # Element SYNRESTRS uses Python identifier SYNRESTRS
    __SYNRESTRS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS'), 'SYNRESTRS', '__AbsentNamespace0_CTD_ANON_24_SYNRESTRS', False, pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 52, 0), )

    
    SYNRESTRS = property(__SYNRESTRS.value, __SYNRESTRS.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__AbsentNamespace0_CTD_ANON_24_value', npType, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 87, 2)
    __value._UseLocation = pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 87, 2)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __SELRESTRS.name() : __SELRESTRS,
        __SYNRESTRS.name() : __SYNRESTRS
    })
    _AttributeMap.update({
        __value.name() : __value
    })



VNCLASS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VNCLASS'), CTD_ANON, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 11, 0))
Namespace.addCategoryObject('elementBinding', VNCLASS.name().localName(), VNCLASS)

MEMBERS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS'), CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 23, 0))
Namespace.addCategoryObject('elementBinding', MEMBERS.name().localName(), MEMBERS)

THEMROLES = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES'), CTD_ANON_2, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 30, 0))
Namespace.addCategoryObject('elementBinding', THEMROLES.name().localName(), THEMROLES)

SELRESTRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0))
Namespace.addCategoryObject('elementBinding', SELRESTRS.name().localName(), SELRESTRS)

SYNRESTRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS'), CTD_ANON_4, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 52, 0))
Namespace.addCategoryObject('elementBinding', SYNRESTRS.name().localName(), SYNRESTRS)

FRAMES = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FRAMES'), CTD_ANON_5, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 63, 0))
Namespace.addCategoryObject('elementBinding', FRAMES.name().localName(), FRAMES)

PREP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PREP'), CTD_ANON_8, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 91, 0))
Namespace.addCategoryObject('elementBinding', PREP.name().localName(), PREP)

LEX = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LEX'), CTD_ANON_10, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 106, 0))
Namespace.addCategoryObject('elementBinding', LEX.name().localName(), LEX)

SYNTAX = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SYNTAX'), CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 110, 0))
Namespace.addCategoryObject('elementBinding', SYNTAX.name().localName(), SYNTAX)

SEMANTICS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SEMANTICS'), CTD_ANON_12, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 130, 0))
Namespace.addCategoryObject('elementBinding', SEMANTICS.name().localName(), SEMANTICS)

SUBCLASSES = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES'), CTD_ANON_14, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 151, 0))
Namespace.addCategoryObject('elementBinding', SUBCLASSES.name().localName(), SUBCLASSES)

VNSUBCLASS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VNSUBCLASS'), CTD_ANON_15, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 155, 0))
Namespace.addCategoryObject('elementBinding', VNSUBCLASS.name().localName(), VNSUBCLASS)

ARG = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ARG'), CTD_ANON_22, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 146, 0))
Namespace.addCategoryObject('elementBinding', ARG.name().localName(), ARG)

NP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NP'), CTD_ANON_24, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 81, 0))
Namespace.addCategoryObject('elementBinding', NP.name().localName(), NP)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 23, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 30, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FRAMES'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 63, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES'), CTD_ANON_14, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 151, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 15, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FRAMES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 16, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 17, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MEMBER'), CTD_ANON_23, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 24, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 24, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'MEMBER')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 24, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'THEMROLE'), CTD_ANON_16, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 31, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 31, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'THEMROLE')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 31, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), CTD_ANON_3, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SELRESTR'), CTD_ANON_17, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 43, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 42, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'SELRESTR')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 43, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 47, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS'), CTD_ANON_4, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 52, 0)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SYNRESTR'), CTD_ANON_18, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 54, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 53, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'SYNRESTR')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 54, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 58, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FRAME'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 64, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 64, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'FRAME')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 64, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DESCRIPTION'), CTD_ANON_19, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 66, 6)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EXAMPLES'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 72, 6)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SYNTAX'), CTD_ANON_11, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 110, 0)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SEMANTICS'), CTD_ANON_12, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 130, 0)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'DESCRIPTION')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 66, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'EXAMPLES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 72, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SYNTAX')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 75, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SEMANTICS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 76, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'EXAMPLE'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 73, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 73, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'EXAMPLE')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 73, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SELRESTRS'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 93, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'SELRESTRS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 93, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SELRESTR'), CTD_ANON_20, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 95, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 94, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'SELRESTR')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 95, 1))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NP'), CTD_ANON_24, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 81, 0)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PREP'), CTD_ANON_8, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 91, 0)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LEX'), CTD_ANON_10, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 106, 0)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ADV'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 114, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ADJ'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 115, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'VERB'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 119, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 112, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 120, 4))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NP')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 113, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'ADV')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 114, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'ADJ')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 115, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PREP')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 116, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LEX')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 117, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'VERB')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 119, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NP')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 121, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'ADV')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 122, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'ADJ')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 123, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PREP')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 124, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LEX')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 125, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_10()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PRED'), CTD_ANON_21, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 132, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, u'PRED')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 132, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_11()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ARG'), CTD_ANON_22, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 146, 0)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ARG')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 136, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_12()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'VNSUBCLASS'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 155, 0)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 152, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'VNSUBCLASS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 152, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_13()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS'), CTD_ANON_, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 23, 0)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES'), CTD_ANON_2, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 30, 0)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FRAMES'), CTD_ANON_5, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 63, 0)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES'), CTD_ANON_14, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 151, 0)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MEMBERS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 158, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'THEMROLES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 159, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FRAMES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SUBCLASSES')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 161, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_14()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), CTD_ANON_3, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 34, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_15()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ARGS'), CTD_ANON_13, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 134, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, u'ARGS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 134, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_16()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS'), CTD_ANON_3, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 41, 0)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS'), CTD_ANON_4, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 52, 0)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SELRESTRS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 84, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SYNRESTRS')), pyxb.utils.utility.Location('C:\\Python27\\Scripts\\vn_schema-3.xsd', 85, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_17()

