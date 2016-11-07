# number 2
#going to write out how old are you? Its going to let you insert your age and turn it into a integer.  
print("How old are you?")
age = int(input())
# going to write out how many inches tall are you? Its going to let you insert your height and turn it into a integer.
print("How many inches tall are you?")
height = int(input())
#if your older than 10 and taller than 50 in, its going to say youre old and tall enough to ride the ride
#However, if youre younger than 1o and shorter than 5o in you can not ride the ride 
#also, if youre older than 1o but shorter than 5o in, you still can not ride the ride. Or vice versa 
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
