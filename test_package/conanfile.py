#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        boost_deps = ['array', 'assert', 'config', 'core', 'detail', 'integer', 'io', 'iterator', 'move', 'mpl', 'optional', 'predef', 'preprocessor', 'smart_ptr', 'static_assert', 'type_traits', 'unordered', 'utility', 'variant']
        for lib in boost_deps:
            self.requires("boost_" + lib + "/1.67.0@" + self.user + "/" + self.channel)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            if self.settings.os == "Windows":
                self.run(os.path.join("bin", "test_package"))
            else:
                self.run("DYLD_LIBRARY_PATH=%s %s" % (os.environ['DYLD_LIBRARY_PATH'], os.path.join("bin", "test_package")))
