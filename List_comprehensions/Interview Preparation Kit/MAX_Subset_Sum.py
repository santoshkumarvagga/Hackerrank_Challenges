a = []
n = int(input('Enter array size').strip())
for _ in range(n):
	a.append(int(input('enter array element').strip()))
S = input('enter sum S').strip()
def c(i,S):
	if i==0 and S != 0:
		return False
	if S == 0:
		return True
	if S < c(i,S):
		return c(i - 1,S)
	return c(i - 1,S) or c(i - 1,S - a)
i = len(a)
print("The max subset sum is", c(i-1,S))