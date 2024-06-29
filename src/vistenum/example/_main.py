"""Main script for the example package."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import builtins


def main01() -> int:
  """Main function for the example package."""
  print("""Welcome to vistenum!""")
  print("""This package demonstrates the use of the VistEnum class.""")
  print("""The Weekday class provides an enumeration of the weekdays 
  implemented with the VistEnum class. Below is the Weekday class source 
  code provided verbatim:""")
  print("""\n--- BEGINNING OF CODE BLOCK ---""")
  here = __file__
  print(open(here.replace('_main.py', '_weekday.py')).read()[:-1])
  print("""--- END OF CODE BLOCK ---\n""")
  print("""VistEnum provides subclasses with the following features:""")
  print("""- Attributes: """)
  print("""  - 'name': The name of the enum member.""")
  print("""  - 'value': (Optional) Public value of the enum member.""")
  print("""  - private value: Unique integer value of the enum member. 
  This value is private to VistEnum and subclasses. """)
  print("""Iteration: The VistEnum baseclass implements the iteration 
  protocol at the class level. This means that iteration over the Enum 
  class will yield the Enum members in the order they were defined in the
  class definition. Below is an example of how to iterate over the Weekday
  class:""")
  print("""\n--- BEGINNING OF CODE BLOCK ---""")
  print("""from example import Weekday""")
  print("""for weekday in Weekday:""")
  print("""  print(weekday)""")
  print("""--- END OF CODE BLOCK ---\n""")
  print("""The above code will output the following:""")
  print("""\n--- BEGINNING OF OUTPUT ---""")
  from vistenum.example import Weekday
  for weekday in Weekday:
    print(weekday, )
  print("""--- END OF OUTPUT ---\n""")
  print("""The enum members are accessible by their name attribute. The 
  name is case insensitive and can be accessed on the dot as an attribute, 
  by calling the class and even by indexing the class. If an attempt is 
  made to access a non-existing member, an AttributeError is raised. Below
  is an example of how to access the enum members:""")
  print("""\n--- BEGINNING OF CODE BLOCK ---""")
  print("""from example import Weekday""")
  print("""print(Weekday.Monday)""")
  print("""print(Weekday['Tuesday'])""")
  print("""print(Weekday('Wednesday'))""")
  print("""print(Weekday('thursday')""")
  print("""print(Weekday.Monday is Weekday['Monday'] is Weekday(
  'Monday'))""")
  print("""try:""")
  print("""  print(Weekday('Someday'))""")
  print("""except AttributeError as attributeError:""")
  print("""  print(attributeError)""")
  print("""--- END OF CODE BLOCK ---\n""")
  print("""The above code will output the following:""")
  print("""\n--- BEGINNING OF OUTPUT ---""")
  from vistenum.example import Weekday
  print(Weekday.Monday)
  print(Weekday['Tuesday'])
  print(Weekday('Wednesday'))
  print(Weekday.Monday is Weekday['Monday'] is Weekday('Monday'))
  print(Weekday('thursday'))
  try:
    print(Weekday('Someday'))
  except AttributeError as attributeError:
    print(attributeError)
  print("""--- END OF OUTPUT ---\n""")
  print("""VistEnum also implements hashing allowing enum members to be 
  used as dictionary keys. For example:""")
  print("""\n--- BEGINNING OF CODE BLOCK ---""")
  print("""from example import Weekday""")
  print("""weekly = {Weekday.Monday: 'Family Home Evening',
  Weekday.Tuesday: 'None', Weekday.Wednesday: 'None', ...}""")
  print("""print(weekly[Weekday.Monday])""")
  print("""--- END OF CODE BLOCK ---\n""")
  print("""The above code will output the following:""")
  print("""\n--- BEGINNING OF OUTPUT ---""")
  weekly = {Weekday.Monday : 'Family Home Evening',
            Weekday.Tuesday: 'None', Weekday.Wednesday: 'None'}
  print(weekly[Weekday.Monday])
  print("""--- END OF OUTPUT ---\n""")
  print("""VistEnum classes are entirely free to set the value of 
  attribute. This value should be passed to the auto function, but the 
  value is entirely semantic and can be of any value and any type. 
  Consider the following example:""")
  print("""\n--- BEGINNING OF CODE BLOCK ---""")
  here = __file__
  print(open(here.replace('_main.py', '_ugedag.py')).read()[:-1])
  print("""--- END OF CODE BLOCK ---\n""")
  print("""Note how the value at each enum member is changed, but the 
  name is preserved. Iterating through the Ugedag class will yield the 
  same result as for Weekday, except translated to Danish:""")
  print("""\n--- BEGINNING OF CODE BLOCK ---""")
  print("""from example import Ugedag""")
  print("""print('Ugedag.name: Ugedag.value\\n')""")
  print("""for ugedag in Ugedag:""")
  print("""  print('%s: %s' % (ugedag, ugedag.value))""")
  print("""--- END OF CODE BLOCK ---\n""")
  print("""The above code will output the following:""")
  print("""\n--- BEGINNING OF OUTPUT ---""")
  from vistenum.example import Ugedag
  print('Ugedag.name: Ugedag.value\n')
  for ugedag in Ugedag:
    print('%s: %s' % (ugedag, ugedag.value))
  print("""--- END OF OUTPUT ---\n""")

  return 0


def main02() -> int:
  """Tester 2"""
  from vistenum.example import Weekday
  lines = []

  def printLine(*args) -> tuple[str, ...]:
    newLine = ', '.join([str(arg) for arg in args])
    lines.append(newLine)

  oldPrint = builtins.print
  print = printLine  # START
  from vistenum.example import Ugedag

  if __name__ == '__main__' or True:
    for ugedag in Ugedag:
      print(ugedag)
    print("""Toggle public value inclusion off""")
    Ugedag.includeValue = False  # Toggle public value inclusion
    for ugedag in Ugedag:
      print(ugedag)
  print = oldPrint  # END

  print('\n'.join([str(line) for line in lines]))
  return 0


def main03() -> int:
  """LMAO"""

  class Basic:
    pass

  print(Basic)


main = main02
