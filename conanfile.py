#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostSerializationConan(base.BoostBaseConan):
    name = "boost_serialization"
    url = "https://github.com/bincrafters/conan-boost_serialization"
    lib_short_names = ["serialization"]
    cycle_group = "boost_level11group"
    b2_requires = [
        "boost_level11group",
    ]


