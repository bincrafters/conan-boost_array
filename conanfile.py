#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostArrayConan(base.BoostBaseConan):
    name = "boost_array"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_array"
    lib_short_names = ["array"]
    header_only_libs = ["array"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_static_assert",
        "boost_throw_exception"
    ]
