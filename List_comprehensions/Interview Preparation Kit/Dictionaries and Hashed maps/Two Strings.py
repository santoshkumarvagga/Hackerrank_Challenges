#Max common substring in given n strings
n = int(input('enter n for total pairs'))
l = []

for i in range(2 * n):
	a = input('enter string')
	l.append(a)
print(l)

max_sub_len = 0
max_len_string = 0

for i in l:
	if len(i) > max_len_string:
		max_len_string = len(i)
		big_str = i
print("biggest string is:", big_str)

def check_entire(sub):
	cnt = 0
	print("In check, for string:",sub)
	for i in l:
		if i in sub and len(i) == max_len_string:
			cnt = cnt + 1
	print("Value of entire cnt is", cnt)
	if cnt == len(l):
		return True
	else:
		return False

def check(sub):
	cnt = 0
	for i in l:
		if sub in i:
			cnt = cnt + 1
	print("Value of cnt is", cnt)
	if cnt == len(l):
		return True
	else:
		return False

if check_entire(big_str[::]):
	print("The max length of common substring possible is", max_len_string)
	print("The Common substring is ", big_str[::])
	exit(0)

for i in range(len(big_str) - 1):
	for j in range(i + 1,len(big_str)):
		print("val of i and j are :", i, j)
		if check(big_str[i:j+1]):
			print("entered check:", big_str[i:j+1])
			if len(big_str[i:j+1]) > max_sub_len:
				max_sub_len = len(big_str[i:j+1])
				res_str = big_str[i:j+1]

if max_sub_len == 0:
	#check for single chars
	for k in range(len(big_str)):
		if check(big_str[k]):
			print("The max length of common substring possible is", 1)
			print("The Common substring is ", big_str[k])
			exit(0)
	print("No common substring")
else:
	print("The max length of common substring possible is", max_sub_len)
	print("The Common substring is ", res_str)