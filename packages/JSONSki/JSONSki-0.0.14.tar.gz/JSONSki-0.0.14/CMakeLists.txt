cmake_minimum_required(VERSION 3.4...3.18)
project(JSONSki)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx -mavx2 -mpclmul -std=c++11") 

add_subdirectory(pybind11)
pybind11_add_module(cmake_example source/main.cpp)

add_library(mymath STATIC src/QueryProcessor.cpp)
set_target_properties(mymath PROPERTIES POSITION_INDEPENDENT_CODE ON)
add_library(mymath1 STATIC src/RecordLoader.cpp)
set_target_properties(mymath1 PROPERTIES POSITION_INDEPENDENT_CODE ON)
add_library(mymath2 STATIC src/JSONPathParser.cpp)
set_target_properties(mymath1 PROPERTIES POSITION_INDEPENDENT_CODE ON)



#set_target_properties(mymath PROPERTIES POSITION_INDEPENDENT_CODE ON)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(cmake_example
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})

target_link_libraries(cmake_example PRIVATE mymath)

target_link_libraries(cmake_example PRIVATE mymath1)

target_link_libraries(cmake_example PRIVATE mymath2)
