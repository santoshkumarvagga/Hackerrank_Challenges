class Test(object):
	myvar = 12 

	def __init__(self, num = 1):
		self.num = num
		self.__numa = 12

	def get(self):
		return self.__numa

	def set(self, num):
		self.__numa = num

	@property
	def methoda(self):
		print("Im a method")
	
	@staticmethod
	def methodb():
		print("Im a static")

	@classmethod
	def classvar(cls):
		print("Class variable accessed:{}".format(cls.myvar))

	def __str__(self):
		return "Object Test"

class sub(Test):
	def __init__(self):
		super.__init__()
		pass
	def get(self):
		print(super.__numa)

if __name__ == "__main__":
	obj = Test()
	print(obj)
	print(obj.methoda)
	print(obj.methodb)
	print(Test.methodb())
	print(obj.classvar())
	a = sub()
	print(a.get())