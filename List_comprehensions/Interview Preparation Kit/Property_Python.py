"""
property() in python: This is used as shortcut if we need to aceess/set value for a private variable in a class. 
"""

class set():
	def __init__(self):
		self.__var = 0
		self.__var2 = 0

	def getter(self):
		return self.__var

	def setter(self, num):
		self.__var = num

	name = property(getter,setter)

	def getter2(self):
		return self.__var2

	def setter2(self, num):
		self.__var2 = num

	name2 = property(getter2, setter2)

obj = set()
print(obj.getter())
print(obj.setter(190))
print(obj.getter())
print(obj.name)
obj.name = 30
print(obj.name)
obj.name2 = 40
print(obj.name2)