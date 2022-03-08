#!/usr/bin/env python3

import run_python
import run_cython
import time
import argparse

parser = argparse.ArgumentParser(
    prog="test_code.py",
    description="This is a program for cython example.",
    )

parser.add_argument(
    "arg1",
    nargs="*",
    type=int,
    default=100,
    help="n!")

args = parser.parse_args()

number = args.arg1
print(number)

for n in number:
    start = time.time()
    run_python.test(n)
    end =  time.time()

    py_time = end - start
    print("Python time = {}".format(py_time))

    start = time.time()
    run_cython.test(n)
    end =  time.time()

    cy_time = end - start
    print("Cython time = {}".format(cy_time))

    print("Speedup = {}".format(py_time / cy_time))