#LCS (without Optimisation)
X = input("Enter first String")
Y = input("Enter second string")
a = len(X)
b= len(Y)
rows, columns = (a,b)
def func(X,Y,i,j):
	X = X[:i+1]
	Y = Y[:j+1]
	print(X, Y)
	if i==0 or j==0:
		return 0
	if X[i-1] == Y[j-1]:
		return 1+func(X,Y,i-1,j-1)
	return max(func(X,Y,i-1,j),func(X,Y,i,j-1))
print("The LCS is: ", func(X,Y,a,b))
