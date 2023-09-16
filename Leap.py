def isleapyear(year):
    if (year % 4==0 and year % 100 !=0) or year % 400 == 0;
  return true
  else;
     return false
year = 2013
if isleapyear(year):
  printf('{} is leap year.'.format(year))
else:
  printf('{} is not a leap year.'.format(year))
  