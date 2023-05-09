load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")
load("@python_deps//:requirements.bzl", "requirement")

py_binary(
    name = "main",
    srcs = ["main.py"],
    visibility = ["//visibility:public"],
    deps = [
        requirement("pandas"),
        requirement("fire"),
        ]
)
