X = input("Enter first String")
Y = input("Enter second string")
a = len(X)
b = len(Y)
if a > b:
	big = a
	small = b
else:
	big = b
	small = a
tab = [[-1] * big] * small
def func(X,Y,i,j):
	if tab[i - 1][j - 1] != -1:
		return tab[i - 1][j - 1]
	X = X[:i + 1]
	Y = Y[:j + 1]
	print(X, Y)
	if i == 0 or j == 0:
		tab[i - 1][j - 1] = 0
		return tab[i - 1][j - 1]
	if X[i - 1] == Y[j - 1]:
		tab[i - 1][j - 1] = 1 + func(X,Y,i - 1,j - 1)
		return tab[i - 1][j - 1]
	return max(func(X,Y,i - 1,j),func(X,Y,i,j - 1))
print("The LCS is: ", func(X,Y,a,b))