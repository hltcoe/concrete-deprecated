"""
Concrete Core Python Package.

This package defines the basic data structures used by the Concrete
architecture, along with utility classes and functions for processing
those data structures.
"""

# The Concrete protobuf data structures (Communication, Tokenization,
# Vertex, Edge, etc.)
import concrete.proto

# Utility functions & classes
from concrete.id_util import *
from concrete.proto_io import *

