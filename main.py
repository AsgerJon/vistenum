"""Main Tester Script"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
import time
from typing import Callable
import unittest


def tester00() -> int:
  """Hello World!"""
  stuff = [os, sys, 'Hello World!']
  for item in stuff:
    try:
      print(item)
    except BaseException as exception:
      print('Exception: %s' % exception)
      break
  else:
    return 0
  return 1


def main(*args: Callable) -> None:
  """Main Tester Script"""
  tic = time.perf_counter_ns()
  print('Running python script located at: \n%s' % sys.argv[0])
  print('Started at: %s' % time.ctime())
  print(77 * '-')
  retCode = 0
  for callMeMaybe in args:
    print('\nRunning: %s\n' % callMeMaybe.__name__)
    try:
      retCode = callMeMaybe()
    except BaseException as exception:
      print('Exception: %s' % exception)
      retCode = -1
  retCode = 0 if retCode is None else retCode
  print(77 * '-')
  print('Return Code: %s' % retCode)
  toc = time.perf_counter_ns() - tic
  if toc < 1000:
    print('Runtime: %d nanoseconds' % (int(toc),))
  elif toc < 1000000:
    print('Runtime: %d microseconds' % (int(toc * 1e-03),))
  elif toc < 1000000000:
    print('Runtime: %d milliseconds' % (int(toc * 1e-06),))


def runTests() -> int:
  """Runs the tests"""
  loader = unittest.TestLoader()
  suite = loader.discover(start_dir='tests', pattern='test*.py')

  runner = unittest.TextTestRunner(verbosity=2)
  res = runner.run(suite)
  return 0 if res.wasSuccessful() else 1


if __name__ == '__main__':
  main(runTests, )
