# ACE Cache Eviction Latency

Small hack to measure and display ACE Cache Eviction latency

```
$ brew install gnuplot --with-qt
$ cat content-service-* | python latency.py | gnuplot -p hist.gpl
```

