## 一个显式覆盖的例子
class Parent(object):
	def override(self):
		print("PARENT override()")

class Child(Parent):
	def override(self):
		print("CHILD override()")##定义了一个与父类相同的方法函数
                                 ##对父类的方法进行了覆盖
dad = Parent()
son = Child()

dad.override()
son.override()