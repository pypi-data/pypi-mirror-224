#!/usr/bin/env python
from .config import Config


class TestConfig(Config):
    # Application config
    MODE = "test"
    DEBUG = True
    ES_HOST = ""
    SNIFF_ON_START = False
