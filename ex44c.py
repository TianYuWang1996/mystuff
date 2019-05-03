## 在运行前或运行后替换
class Parent(object):
	def altered(self):
		print("PARENT altered()")

class Child(Parent):
	def altered(self):##子类对父类方法覆盖
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()##调用父类方法
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()