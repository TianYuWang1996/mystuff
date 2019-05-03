## 一个隐式继承的例子
class Parent(object):   ##创建一个Parent类
	def implicit(self):
		print("PRENT implicit()")

class Child(Parent):    ##创建了一个继承Parent类的Child类
	pass

dad = Parent() ##Parent类实例化，创建对象dad
son = Child()  ##Child类实例化，创建对象son

dad.implicit() ##调用Parent类的implicit方法
son.implicit() ##调用Child父类的implicit方法