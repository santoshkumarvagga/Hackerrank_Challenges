n = int(input())
org = []
for _ in range(n):
    arr = []
    name = input()
    score = float(input())
    arr.append(name)
    arr.append(score)
    org.append(arr)
min = 1000
for i in org:
    if i[1] < min:
        min = i[1]
a = []
for i in org:
    if i[1] == min:
        continue
    a.append(i) 
min = 1000
for i in a:
    if i[1] < min:
        min = i[1]
s = []
for i in a:
    if i[1]== min:
        s.append(i[0])
s.sort()
for i in s:
    print(i)