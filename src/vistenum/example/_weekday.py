"""Weekday provides an enumeration of the weekdays."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistenum import VistEnum, auto


class Weekday(VistEnum):
  """Weekday provides an enumeration of the weekdays."""

  MONDAY = auto()
  TUESDAY = auto()
  WEDNESDAY = auto()
  THURSDAY = auto()
  FRIDAY = auto()
  SATURDAY = auto()
  SUNDAY = auto()
