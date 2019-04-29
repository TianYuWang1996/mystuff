def new_function(i, x, s):
	numbers = []
	while i < x:
		print("At the top i is %d" %i)
		numbers.append(i)
		i += s
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" %i)
	return numbers

numbers = new_function(0,5,2)

print("The numbers: ")

for num in numbers:
	print(num)