ten_things = "Apples Oranges Cows Telephone Light Sugar"

print("Wait there's not 10 things in that list, "
	"Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", 
	"Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()  #弹出more_stuff列表里的最后一个元素，赋给next_one。
	print("Adding: ", next_one)
	stuff.append(next_one)     #将next_one加到stuff列表的尾部
	print("There's %d items now." %len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #打印stuff列表的第2个元素
print(stuff[-1])  # 打印stuff列表的最后1个元素
print(stuff.pop())  #stuff列表的最后1个元素弹出，并被打印出来
print(' '.join(stuff)) # what? Cool!
print('#'.join(stuff[3:5])) # super stellar!