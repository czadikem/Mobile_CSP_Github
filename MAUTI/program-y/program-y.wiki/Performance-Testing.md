# Performance Testing REST API

This will be done using [Locust](http://locust.io/). More data to follow once I have something up and running


# Performance Testing Webchat API

This will be done using [Locust](http://locust.io/). More data to follow once I have something up and running


# Profiling Python Core Code

I currently use a combination of CProfile, pyprof2calltree, and qcachegrind 

Based on the blog [Profiling Python using cProfile](https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara)

cProfile
    Already installed as default to Python 3

Install [pyprof2calltree](https://pypi.python.org/pypi/pyprof2calltree) 
    pip3 install pyprof2calltree

qcachegrind
    brew install qcachegrind

