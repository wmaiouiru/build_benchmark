Benchmark 1: bazel
  Time (mean ± σ):     562.5 ms ±  18.1 ms    [User: 39.6 ms, System: 46.1 ms]
  Range (min … max):   544.2 ms … 587.8 ms    5 runs
 
Benchmark 2: run
  Time (mean ± σ):       0.9 ms ±   0.4 ms    [User: 0.1 ms, System: 0.6 ms]
  Range (min … max):     0.3 ms …   1.3 ms    5 runs
 
Benchmark 3: main
  Time (mean ± σ):       1.6 ms ±   0.7 ms    [User: 0.3 ms, System: 1.0 ms]
  Range (min … max):     0.9 ms …   2.5 ms    5 runs
 
Benchmark 4: run
  Time (mean ± σ):       0.8 ms ±   0.6 ms    [User: 0.1 ms, System: 0.4 ms]
  Range (min … max):     0.0 ms …   1.4 ms    5 runs
 
Summary
  'run' ran
    1.13 ± 0.93 times faster than 'run'
    1.96 ± 1.62 times faster than 'main'
  695.42 ± 493.20 times faster than 'bazel'
