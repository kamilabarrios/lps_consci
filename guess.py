import random
number = random.randint(1,1000)


print("I am thinking of a number between 1-1000")
print("Take a guess")
guess = int(input())


while guess != number: 
  if guess < number:
    print("number is too low, guess again")
  guess = int(input())
  if guess > number:
    print("number is too high, guess again")
  guess = int(input())
  if guess == number:
    print("WOAAAH! NICE GUESS!")


