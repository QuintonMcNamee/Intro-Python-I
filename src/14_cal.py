"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar(calendar.SUNDAY)

def help():
  print("cmd: python src/14_cal.py month year")

def main(args):
  if len(args) == 0:
    time = datetime.now()
    mon = cal.formatmonth(time.year, time.month)
    print(mon)
  elif len(args) == 1:
    if(args[0] == '-h' or args[0] == '--help'):
      help()
    else:
      time = datetime.now()
      mon = cal.formatmonth(time.year, int(args[0]))
      print(mon)
  elif len(args) == 2:
    s = cal.formatmonth(int(args[1]), int(args[0]))
    print(mon)
  else:
    help()

if __name__ == "__main__":
  main(sys.argv[1:])