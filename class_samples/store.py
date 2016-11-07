
# its welcoming me to the convience store, telling me to write my name and allowing  me enter my name  
print("Welcome to the convenience store!")
print("Enter your age:")
age = input()
# its identifying my age 
age = int(age)
# if my age is 18 or older, its going to tell me if I  want to purchase a lottery ticket
if age >= 18:
  print("Would you like to buy a lottery ticket?")
# if my age is under 18, its going to tell me if I want to purchase a lollypop 
if age < 6:
  print("Would you like to buy a lollipop?")
