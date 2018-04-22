project(test_package CXX)
cmake_minimum_required(VERSION 3.1.2)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

file(GLOB SOURCE_FILES *.cpp)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} 
  CONAN_PKG::boost_array
  CONAN_PKG::boost_assert
  CONAN_PKG::boost_config
  CONAN_PKG::boost_core
  CONAN_PKG::boost_detail
  CONAN_PKG::boost_integer
  CONAN_PKG::boost_io
  CONAN_PKG::boost_iterator
  CONAN_PKG::boost_move
  CONAN_PKG::boost_mpl
  CONAN_PKG::boost_optional
  CONAN_PKG::boost_predef
  CONAN_PKG::boost_preprocessor
  CONAN_PKG::boost_smart_ptr
  CONAN_PKG::boost_static_assert
  CONAN_PKG::boost_type_traits
  CONAN_PKG::boost_unordered
  CONAN_PKG::boost_utility
  CONAN_PKG::boost_variant)
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 11)
