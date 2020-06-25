def decorator(func):
	def inner(a):
		print('*'*30)
		func(a)
		print('*'*30)
		return 
	return inner

@decorator
def name(a):
	print(a)

print(name('Santoshkumar Vagga'))