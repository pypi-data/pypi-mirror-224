#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


// #include "QueryAutomaton.h"

// #include "JSONPathParser.h"
// #include "JSONPathParser.cpp"



// #include "Records.h"

// #include "RecordLoader.h"
// #include "RecordLoader.cpp"


// #include "QueryProcessor.h"
// #include "QueryProcessor.cpp"
#include "../src/RecordLoader.h"
#include "../src/QueryProcessor.h"


string execute_query(const char* input) {
// std::string execute_query(char* input) {
//int main(){
 // char* file_path = "../dataset/twitter_sample_large_record.json";
 // const char* file_path = "../dataset/twitter_sample_large_record.json";
    cout<<"start loading the single large record from "<<input<<endl;
    Record* rec = RecordLoader::loadSingleRecord(input);
    if (rec == NULL) {
        cout<<"record loading fails."<<endl;
        return "record loading fails";
    }
    cout<<"finish loading the single large record"<<endl;

    string query = "$[*].entities.urls[*].url";
    cout<<"\nstart executing query "<<query<<endl;
    QueryProcessor processor(query);
    string output = processor.runQuery(rec);
    cout<<"finish query execution"<<endl;
    cout<<"matches are: "<<output<<endl;
    return output;
}



int add(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(cmake_example, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: cmake_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers

        Some other explanation about the subtract function.
    )pbdoc");

    m.def("execute_query", &execute_query, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
