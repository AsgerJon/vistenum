"""Main Tester Script"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
import time
from typing import Callable

from icecream import ic

from tester_class_01 import TesterClass


def tester00() -> int:
  """Hello World!"""
  stuff = [os, sys, ic, ]
  for item in stuff:
    try:
      print(item)
    except BaseException as exception:
      print('Exception: %s' % exception)
      break
  else:
    return 0
  return 1


def tester01() -> int:
  """Test of the BaseEnum class"""
  # TUE = TesterClass.Tuesday
  # TUE = 'tuesday'
  TUE = 1
  for item in TesterClass:
    print(item, end=' | ')
    print('Tuesday?: %s' % ('YES' if item == TUE else 'NO'))
  ic(TesterClass['tuesday'])
  ic(TesterClass['Tuesday'])
  ic(TesterClass('Tuesday'))


def main(callMeMaybe: Callable) -> None:
  """Main Tester Script"""
  tic = time.perf_counter_ns()
  print('Running python script located at: \n%s' % sys.argv[0])
  print('Started at: %s' % time.ctime())
  print(77 * '-')
  retCode = 0
  try:
    retCode = callMeMaybe()
  except BaseException as exception:
    print('Exception: %s' % exception)
    retCode = -1
    raise exception
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


if __name__ == '__main__':
  main(tester01)
