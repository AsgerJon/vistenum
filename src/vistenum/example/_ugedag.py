"""Ugedag provides a translation of the weekdays to Danish."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistenum import VistEnum, auto


class Ugedag(VistEnum):
  """Ugedag provides a translation of the weekdays to Danish."""
  includeValue = True
  MONDAY = auto('Mandag')
  TUESDAY = auto('Tirsdag')
  WEDNESDAY = auto('Onsdag')
  THURSDAY = auto('Torsdag')
  FRIDAY = auto('Fredag')
  SATURDAY = auto('Lørdag')
  SUNDAY = auto('Søndag')
