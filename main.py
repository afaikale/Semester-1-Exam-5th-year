#############
## 4 = integer
## 5.7 = float number 
## True = Boolean
## Good luck = string

##################

### Which datatype would be useful for storing someone's height? (1 mark)
## Answer it could be integer, if it's in cm or float if it's in metres, because it would have number after the point.

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer string


####Create a variable tha will store the users name.(1 mark)

userName = input("Please enter your name:\n ")


# ####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
# print(userName[0:4])

####Convert the user's name to all uppercase characters and print the result
userNameUpper = userName.upper()
print(userNameUpper)

###Find out how many times the letter A occurs in the user's name
a = userName.count("a")
A = userName.count("A")
print(a + A)



### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
userAge = int(input("Enter your age:\n"))
if userAge >= 18:
  print("You can enter the competition!")
if userAge< 18:
  print("We're sorry :( \n You cannot enter the competition.")


#### Create an empty list called squareNumbers (3 marks)
squareNumber = []

#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).
n = 0
for n in range(1, 21):
  squares = n*n
  squareNumber.append(squares)





####Print your list (1 mark)
print(squareNumber)

####Create a variable called userSquare that asks the user for their favourite square number
userSquare = int(input("What's your favourite square number?\n"))


#### Add this variable to the end of your list called SquareNumbers
squareNumber.insert(21, userSquare)
# print(squareNumber)
### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)
import random
choice = int(random.choice(squareNumber))
print(choice)