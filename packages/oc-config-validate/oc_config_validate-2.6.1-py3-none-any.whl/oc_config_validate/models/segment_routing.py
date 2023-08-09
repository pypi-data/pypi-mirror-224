# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class openconfig_rsvp_sr_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-rsvp-sr-ext - based on the path /openconfig-rsvp-sr-ext. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module adds extensions to the OpenConfig MPLS models to
provide extensions which allow the coexistence of RSVP-TE and
Segment Routing (SR) within the same network. It augments the
existing OpenConfig segment routing (SR) and RSVP-TE models
where required.
  """
  _pyangbind_elements = {}

  

class openconfig_segment_routing_types(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-segment-routing-types - based on the path /openconfig-segment-routing-types. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Types associated with a network instance
  """
  _pyangbind_elements = {}

  

class openconfig_srte_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-srte-policy - based on the path /openconfig-srte-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines a collection of segment routing traffic
engineering policy operational states.

Each policy, identified by a combination of color and endpoint,
has one or more candidate paths learned from one or more sources.
The best valid/usable path is marked as active and programmed in
forwarding plane.

A candidate path, identified by protocol-origin, originator and
discriminator, can have one and more segment-list defining the
path traffic should take. Each segment-list is associated with a
weight for weighted load balancing.

Traffic counters related to SR policies are also defined in this
module.
  """
  _pyangbind_elements = {}

  

class openconfig_segment_routing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-segment-routing - based on the path /openconfig-segment-routing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters relating to the
segment routing. This module defines a number of elements which are
instantiated in multiple places throughout the OpenConfig collection
of models.

Particularly:
 - SRGB+LB dataplane instances - directly instantied by SR.
 - SRGB+LB dataplane reservations - instantiated within MPLS and future SR
                                 dataplanes.
 - SR SID advertisements - instantiated within the relevant IGP.
 - SR-specific counters - instantied within the relevant dataplane.
  """
  _pyangbind_elements = {}

  

