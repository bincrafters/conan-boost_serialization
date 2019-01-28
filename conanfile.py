#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostSerializationConan(base.BoostBaseConan):
    name = "boost_serialization"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_serialization"
    lib_short_names = ["serialization"]
    cycle_group = "boost_cycle_group_c"
    b2_requires = ["boost_cycle_group_c"]
