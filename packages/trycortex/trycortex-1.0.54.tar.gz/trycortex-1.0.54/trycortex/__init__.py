import os
import importlib.metadata

""" api_key = os.environ.get("OPENAI_API_KEY") """

from trycortex.api import *
from trycortex.callables import *

__version__ = importlib.metadata.version(__name__)