## 三种方法的组合使用
class Parent(object): ##创建一个继承object类的Parent类
	def override(self): ##Parent类的override方法
		print("PARENT override()")
	
	def implicit(self): ##Parent类的implict方法
		print("PARENT implicit()")
	
	def altered(self):  ##Parent类的altered方法
		print("PARENT altered()")

class Child(Parent): ##创建一个继承Parent类的Child类
	def override(self): ##Child类的override方法，覆盖Parent类的override方法
		print("CHILD override()")
	
	def altered(self):  ##Child类的altered方法，覆盖Parent类的altered方法
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered() ##调用Parent类（父类）的altered方法
		print("CHILD, AFTER PARENT altered()")

dad = Parent() ##Parent类的实例化，创建对象dad
son = Child()  ##Child类的实例化，创建对象son

dad.implicit() ##调用Parent类的implicit方法
son.implicit() ##调用Child类的implicit方法（隐式继承）

dad.override() ##调用Parent类的override方法
son.override() ##调用Child类的override方法（显式覆盖）

dad.altered()  ##调用Parent类的altered方法
son.altered()  ##调用Child类的altered方法（在运行前后替换）