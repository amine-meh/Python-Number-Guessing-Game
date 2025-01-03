import random

top_range = int(input("Enter the top range you would like for this game. \n"))
number_generated = random.randint(0, top_range)

user_number = int(input("Enter a number\n"))
number_of_fails = 0

while user_number != number_generated:
  if user_number < number_generated:
    print("The number entered is smaller than the generated number")
    number_of_fails += 1
    user_number = int(input("Enter a number\n"))
  elif user_number > number_generated:
    print("The number entered is larger than the generated number")
    number_of_fails += 1
    user_number = int(input("Enter a number\n"))
  


else :
  print("Congratulations! You guessed the correct number. \n")
  print("You got the correct number in", number_of_fails+1, "tries.\n")