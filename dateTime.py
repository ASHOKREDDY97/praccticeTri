# datetime
from datetime import date
my_date = date(1996,7,2)
print(my_date)


#  raise a valueError for outside range
from datetime import date
my_date = date(1996,7,32)
print(my_date)

# get current date
from datetime import date
date = date.today()
print('Today date is:',date)


# Get Today’s Year, Month, and Date
from datetime import date
date = date.today()
print('today date is:',date.day)
print('this month is:',date.month)
print('this year is:',date.year)