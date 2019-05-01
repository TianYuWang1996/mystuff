# -*- coding: UTF-8 -*-
from sys import exit

backpack = ["铁剑", "盾牌"]

def Devil_Palace(backpack):
	print("----------------------------")
	print("魔王高踞王座，冷笑着。")
	print("你的背包里有：", backpack)
	next = input("应对> ")
	if next == "使用除魔剑":
		print("你杀死了魔王。")
		print("国王兑现了他的承诺。")
	else:
		print("魔王杀死了你，永远囚禁了你的灵魂。")
		exit(0)

def The_Trap():
	print("你进入了一间昏暗的房间。")
	print("你觉得有些不对劲。")
	print("突然间，你脚下一空，坠入陷阱。")
	print("你死了。")
	exit(0)

def Treasury_House(backpack):
	print("----------------------------")
	print("你进入了一间明亮的的房间。")
	print("你发现房间中央放着一把剑。")
	next_1 = input("拔剑> ")
	if next_1 == "拔剑":
		print("你获得了'除魔剑'。")
		backpack.append("除魔剑")
		print("你的背包里有：", backpack)
	else:
		print("你准备退出房间。")
	print("----------------------------")
	print("突然，大量的毒蛇从房间的角落涌出。")
	print("你的背包里有：", backpack)
	next_2 = input("应对> ")
	if (next_2 == "使用雄黄") & (backpack.count("雄黄") > 0):
		backpack.remove("雄黄")
		print("毒蛇退散！你趁机返回了大厅。")
		print("你的背包里有：", backpack)
		Devil_Maze_2(backpack)
	else:
		print("你被毒蛇咬死。")
		exit(0)

def Devil_Maze_2(backpack):
	print("----------------------------")
	print("大厅中有三扇大门。")
	print("左边的大门是黄色的，已经封闭。")
	print("中间的大门是红色的。")
	print("右边的大门是蓝色的。")
	print("你选择那扇大门？")
	next = input("中/右> ")
	if next == "中":
		The_Trap()
	elif next == "右":
		Devil_Palace(backpack)
	else:
		print("你在大厅中徘徊不断。")
		print("恐怖降临到你的身上。")
		exit(0)

def Devil_Maze_1(backpack):
	print("----------------------------")
	print("大厅中有三扇大门。")
	print("左边的大门是黄色的。")
	print("中间的大门是红色的。")
	print("右边的大门是蓝色的。")
	print("你选择那扇大门？")
	next = input("左/中/右> ")
	if next == "中":
		The_Trap()
	elif next == "左":
		Treasury_House(backpack)
	elif next == "右":
		Devil_Palace(backpack)
	else:
		print("你在大厅中徘徊不断。")
		print("恐怖降临到你的身上。")
		exit(0)

def Notice_B(backpack):
	Room_Count = 0
	print("----------------------------")
	print("你来到迷宫的门口。")
	print("你发现了一个巨大的石碑，上书：")
	print("""
		不要试图挑战魔王的权威！
		凡人的剑不能触碰到伟大的存在。
		""")
	next = input("进入/逃跑> ")
	if next == "进入":
		Devil_Maze_1(backpack)
	else:
		print("骗子！国王的卫兵逮捕了你。")
		print("你被处死了。")
		exit(0)

def The_Shop(backpack):
	print("----------------------------")
	print("你进入了城中的商店。")
	print("你向老板说明了来意。")
	print("你花费100金采购了雄黄。")
	backpack.pop()
	backpack.append("雄黄")
	print("你的背包里有：", backpack)
	input("出发> ")
	Notice_B(backpack)

def King_Palace(backpack):
	print("----------------------------")
	print("你到达宫殿，面见了国王。")
	print("你获得了100金。")
	print("你得知了魔王所在迷宫的位置。")
	backpack.append("地图")
	backpack.append("100枚金币")
	print("你的背包里有：", backpack)
	next = input("前往/逃跑> ")
	if next == "前往":
		Notice_B(backpack)
	elif next == "情报":
		print("----------------------------")
		print("国王：聪明的年轻人！")
		print("据说魔王的迷宫里有毒蛇。")
		print("你可以去城里的商店看看。")
		input("商店> ")
		The_Shop(backpack)
	else:
		print("骗子！国王的卫兵逮捕了你。")
		print("你被处死了。")
		exit(0)

def Notice_A(backpack):
	print("----------------------------")
	print("你在路边看见一张告示：")
	print("""
	今有魔王为祸苍生。
	王上欲求勇士除魔。
	应者前往宫殿，赐百金。
	成者赏万金，封侯。
	""")
	next = input("揭榜/路过> ")
	if next == "揭榜":
		print("你接受了任务：迷宫除魔")
		backpack.append("国王告示")
		print("你的背包里有：", backpack)
		King_Palace(backpack)
	elif next == "路过":
		print("你离开了这座城市。")
		exit(0)
	else:
		print("你在做什么！？")
		exit(0)

def start(backpack):
	print("----------------------------")
	print("""
	早上，你从一个房间醒来。
	你是一个游历的冒险者。
	你刚来到一个国家的都城。
	现在，带上你的装备，出门吧！
	""")
	print("你的背包里有：", backpack)
	next = input("出门/待着> ")
	
	if next == "出门":
		Notice_A(backpack)
	else:
		print("你哪儿没去。")
		start()

start(backpack)