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



  
# Exercise 2

secret_word = input("Enter the secret word: ")

while len(secret_word) <= 6:
  print("Please enter a word with at least 6 characters")
  secret_word = input("Enter the secret word: ")

letter = input("Guess a letter: ")

num_guesses = 1

while letter in secret_word:
  letter = input("Guess another letter: ")
  num_guesses += 1

print(f"The secret word is: {secret_word}. You took {num_guesses} guesses!")



  
# Exercise 3

uin = int(input("Enter a UIN: "))

for student in roster:
  if student[0] == uin:
    # to access items in a list of a list use brackets and indexing like an array
    # make sure you're paying attention to the list layers
    print(f"{student[1][0]} {student[1][1]}: {student[1][2]}, {student[1][3]}")




# Exercise 4

letters = ["a", "b", "c", "d", "e"]

for i in range(5):
  print(letters[i] * (i+1)) 




# Exercise 5






