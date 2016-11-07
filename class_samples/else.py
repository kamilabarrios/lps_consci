print("How many miles they live from Richmond State?")
miles = int(input())

print("What is your GPA?")
GPA = float(input())

print("What are your ACT scores?")
ACT = int(input())

if miles <= 30 and GPA >=2.0:  
	print("Congrats you have been admitted!")

else:
	if miles > 30 and GPA > 2.5 and ACT > 18:
		print("Congrats you have been admitted!")
