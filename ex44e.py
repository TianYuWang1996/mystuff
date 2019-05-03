class Other(object):
	def override(self):
		print("OTHER override()")
	
	def implicit(self):
		print("OTHER implicit()")
	
	def altered(self):
		print("OTHER altered()")

class Child(object):
	def __init__(self):
		self.other = Other() ##在Child类中使用Other类
	
	def implicit(self):
		self.other.implicit()##以合成的形式调用other类型的implicit方法
	
	def override(self):
		print("CHILD override()") ##Child类自己的override方法
	
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		self.other.altered()##以合成的形式调用other类型的altered方法
		print("CHILD, AFTER PARENT altered()")

son = Child()

son.implicit()
son.override()
son.altered()