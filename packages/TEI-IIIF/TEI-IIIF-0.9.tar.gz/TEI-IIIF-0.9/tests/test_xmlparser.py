import pytest
from lxml import etree
from unittest.mock import Mock
from tei_iiif.xmlparser import getRoot, divList, metadata
from tei_iiif.utils.settings import settings

settings = settings()

