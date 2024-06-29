"""TesterClass"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistenum import VistEnum, auto


class TesterClass(VistEnum):
  """TesterClass"""

  Monday = auto('Monday')
  Tuesday = auto('Tuesday')
  Wednesday = auto('Wednesday')
  Thursday = auto('Thursday')
  Friday = auto('Friday')
  Saturday = auto('Saturday')
  Sunday = auto('Sunday')
