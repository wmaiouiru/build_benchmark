To lock the python dependencies 
```
./pants generate-lockfiles --resolve=python-default
```

Run code:
`./pants run :main -- run`

Benchmark:
```
hyperfine --warmup=1 --runs=5 -i ./pants run :main -- run > BENCHMARK.md
```