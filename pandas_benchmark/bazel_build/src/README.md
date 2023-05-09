Run code:
```
bazel run main run
```


Bench mark speed:
```
hyperfine --warmup=1 --runs=5 -i bazel run main run > ../BENCHMARK.md
```