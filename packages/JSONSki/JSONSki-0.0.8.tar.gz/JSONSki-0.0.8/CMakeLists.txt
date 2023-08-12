cmake_minimum_required(VERSION 3.4...3.18)
project(JSONSki)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx -mavx2 -mpclmul -std=c++11") 

add_subdirectory(pybind11)
pybind11_add_module(JSONSki example/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(JSONSki
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
