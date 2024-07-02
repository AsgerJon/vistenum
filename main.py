"""Main Tester Script"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
import time
from typing import Callable
import unittest

from pyperclip import copy

from vistenum import EnumBox, VistEnum, auto


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


def tester01() -> int:
  """Getting AttributeError text"""
  lmao = type('lmao', (object,), {})
  try:
    lmao().__instance_get__
  except AttributeError as exception:
    copy(str(exception))
    return 0
  return 1


def tester02() -> int:
  """Getting TypeError text"""
  box = EnumBox()
  try:
    box.__instance_get__()
  except Exception as exception:
    print(str(exception))
    return 0
  return 1


class Hand(VistEnum):
  """Hand enumeration"""
  LEFT = auto()
  RIGHT = auto()


class Tester:
  """Testing the EnumBox class"""

  hand1 = EnumBox[Hand](Hand.RIGHT)
  hand2 = EnumBox[Hand](Hand.LEFT)
  hand3 = EnumBox[Hand](0)
  hand4 = EnumBox[Hand](1)
  hand5 = EnumBox[Hand]('right')

  def __str__(self, ) -> str:
    hands = [self.hand1, self.hand2, self.hand3, self.hand4]
    hands = '\n  '.join([str(hand) for hand in hands])
    return """Tester with hands: \n  %s""" % hands


def tester03() -> int:
  """Testing the EnumBox class"""
  tester = Tester()
  print(type(Hand))
  try:
    print(tester)
  except BaseException as exception:
    print('Exception: %s' % exception)
    return 1
  return 0


def runTests() -> int:
  """Runs the tests"""
  loader = unittest.TestLoader()
  suite = loader.discover(start_dir='tests', pattern='test*.py')

  runner = unittest.TextTestRunner(verbosity=2)
  res = runner.run(suite)
  return 0 if res.wasSuccessful() else 1


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


if __name__ == '__main__':
  main(runTests, tester03)
