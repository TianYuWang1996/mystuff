def new_function(i, x):
	numbers = []
	for i in range(i,x):
		#print("At the top: %d" %i)
		numbers.append(i)
		#i += 1
		#print("At the bottom: %d" %i)
	return numbers

numbers = new_function(0,5)

print("The numbers: ")

for num in numbers:
	print(num)