"""TesterClass"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistenum import BaseEnum, Member


class TesterClass(BaseEnum):
  """TesterClass"""

  Monday = Member(0)
  Tuesday = Member(1)
  Wednesday = Member(2)
  Thursday = Member(3)
  Friday = Member(4)
  Saturday = Member(5)
  Sunday = Member(6)
