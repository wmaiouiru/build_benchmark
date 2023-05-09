Benchmark 1: ./pants
  Time (mean ± σ):      1.949 s ±  0.210 s    [User: 1.258 s, System: 0.249 s]
  Range (min … max):    1.697 s …  2.175 s    5 runs
 
Benchmark 2: run
  Time (mean ± σ):       1.5 ms ±   1.0 ms    [User: 0.2 ms, System: 1.0 ms]
  Range (min … max):     0.0 ms …   2.4 ms    5 runs
 
Benchmark 3: :main
  Time (mean ± σ):       0.3 ms ±   0.3 ms    [User: 0.1 ms, System: 0.3 ms]
  Range (min … max):     0.0 ms …   0.9 ms    5 runs
 
Benchmark 4: run
  Time (mean ± σ):       0.5 ms ±   0.5 ms    [User: 0.1 ms, System: 0.3 ms]
  Range (min … max):     0.0 ms …   1.2 ms    5 runs
 
Summary
  ':main' ran
    1.66 ± 2.42 times faster than 'run'
    4.87 ± 6.43 times faster than 'run'
 6434.81 ± 7410.91 times faster than './pants'
