# Python Build System Benchmark
This project aims to compare between build systems to understand the performance, ease of use, and maintainability. 

Here are list of build systems considered:
- [Bazel](https://en.wikipedia.org/wiki/Bazel_(software))
- [Pants]
- [Buck]
- [Please](https://please.build/)


The list of build feature I expect is as follows:
- Being able to create a docker image
- Being able to execute on new code changes fast without changing third party dependencies
- It is easy to debug when there is an issue with a build
- It is easy to find dependencies issues between third party packages
- When the codebase is large, the build system is smart enough to build the required parts only

From my research, the best langauge to describe a build is [Starlark](https://github.com/bazelbuild/starlark#build-api) which is a dialect of Python. Using Makefiles seems like didn't scale well according to this [bazel post](https://blog.bazel.build/2017/03/21/design-of-skylark.html).

## [Please Build](https://please.build/)

After giving Please Build a try for an hour trying to get [huggingface](https://huggingface.co/) up and running, I ran into an issue managing dependencies of dependencies that became a show stopper for Python.

Please build [dependencies page](https://please.build/dependencies.html) states the following:

```again we require listing transitive dependencies explicitly, but this is not normally too onerous for Python.```

However, when attempting to install [huggingface](https://huggingface.co/docs/transformers/quicktour) There is a lot of dependencies, so using python in Please build with many dependencies is a non starter.


