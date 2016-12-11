print("Enter favorite shows to watch.")


show = 0
my_list = []
number = 1
while show < 5:
  print("Enter favorite show")
  shows = input()
  show = show + 1
  my_list.append(shows)
  
print("Okay, here are the shows you've entered.")
print(my_list)
print("We recommend you also watch shows I added to your list.")
my_list.append("The Fosters")
my_list.append("Jane the Virgin")
my_list.sort()


for current_show in my_list:
  print(str(number) + "." + current_show)
  number = number + 1 
