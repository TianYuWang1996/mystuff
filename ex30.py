people = 30     #30人（只能选择1种交通工具，巴士不能太多？）
cars = 40      #40辆轿车（坐1人）
buses = 15    #15辆巴士（坐1人以上合算）

if cars > people:      #如果轿车数大于人数，可以选轿车
	print("We should take the cars.")
elif cars < people:    #如果轿车数小于人数，不可以选轿车
	print("We should not take the cars.")
else:                  #如果轿车数等于人数，选择困难
	print("We can't decide.")

if buses > cars:       #如果巴士数大于轿车数，
	print("That's too many buses.")
elif buses < cars:     #如果巴士数小于轿车数，可以选巴士
	print("Maybe we could take the buses.")
else:                  #如果巴士数等于轿车数，选择困难
	print("We still can't decide.")

if people > buses:     #如果人数大于巴士数，选巴士
	print("Alright, let's just take the buses.")
else:                  #如果人数小于等于巴士数，家里蹲
	print("Fine, let's stay home then.")