#Ex1
from datetime import date, timedelta

current_day = date.today()

new_day = current_day - timedelta(days = 5)

print("Current Date:", current_day)
print("Changed date:", new_day)


#Ex2
from datetime import date, timedelta

Today = date.today()
Yesterday = Today - timedelta(days = 1)
Tommorow = Today + timedelta(days = 1)

print("Today is: ", Today)
print("Yesterday was: ",Yesterday)
print("Tommorow is: ", Tommorow)

#Ex3
from datetime import datetime

Today = datetime.now()
Today = Today.replace(microsecond = 0)
print(Today)


#Ex4
from datetime import date

Day1 = date(2024, 11, 13)
Day2 = date(2024, 11, 17)

the_difference_in_minutes = (Day2 - Day1).days * 24 * 60

print("The difference is ", the_difference_in_minutes, "minutes")