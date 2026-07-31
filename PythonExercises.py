# Exercise 1

from datetime import datetime

user = 0
# 
birthdays = {}

for i in range(5):
  # there's no ++ in python
  user += 1
  # make sure to parse integers being concatenated
  birthday = input("User " + str(user) + " please enter a birthday: ")
  # add to dictionary
  birthdays["User" + user] = birthday + 2026

# item[1] sorts based on the values
sortedBirthdays = sorted(birthdays.items(), key=lambda item: datetime.strptime(item[1], "%B %d %Y"))

# use this syntax for dictionaries, you can use .items() or .values() for lists
for user, date in sortedBirthdays:
  print(date)

## Approach without datetime

months = {
  "January": 1,
  "February": 2,
  "March": 3,
  "April": 4,
  "May": 5,
  "June": 6,
  "July": 7,
  "August": 8,
  "September": 9,
  "October": 10,
  "November": 11,
  "December": 12
}  

# don't really need to store user, just sort the dates
birthdays = []

for i in range(5):
  # the f turns it into a formatting string, so using brackets allows you to simplify concatenation
  birthday = input(f"User {i+1} please enter a birthday: ")
  # split based on space
  month, day = birthday.split()
  # add the month number 
  # parentheses indicate the creation of a tuple within the list (tuples are immutable and more efficient, lists are mutable)
  birthdays.append((months[month], int(day)))

birthdays.sort()

for month, day in birthdays:
  print(f"{month}/{day}")




  
