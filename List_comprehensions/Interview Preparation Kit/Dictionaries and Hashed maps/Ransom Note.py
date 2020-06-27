#Attacker wrote note after thieving. he got doubt of sensing his handwriting. so he finds a magazine and tries to replace the complete words only from magazine to note in any order.
inp = input('enter 2 int').split()
mag_len = inp[0]
note_len = int(inp[1])

mag_list = input('enter mag string').split() #S1, S3
note_list = input('enter note string').split() #S2, S4

#print(mag_list)
#print(note_list)

mag_dict = {} #S5
note_dict = {} #S5

for i in mag_list:
	if i in mag_dict:
		mag_dict[i] = mag_dict[i] + 1
	else:
		mag_dict[i] = 1

for j in note_list:
	if j in note_dict:
		note_dict[j] = note_dict[j] + 1
	else:
		note_dict[j] = 1

Count = 0 

#print(note_dict)
#print(mag_dict)

for key, values in note_dict.items():
	for k,v in mag_dict.items():
		#print("key and k are:", key,k)
		#print("values and v are:", values,v)
		if key == k:
			#print("Matched Key is :", key)
			if values <= v:
				#print("Matched values is :", values)
				Count = Count + 1

#print('Length of note_len', note_len)
#print("Count is :", Count)
if Count == note_len:
	print('Yes')
else:
	print('No')