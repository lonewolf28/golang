#!/usr/bin/python3

# seq = [ 1, 2, 3,4,5,6,7 ]

# for i in range(len(seq)):
# 	print("i: {}".format(i))
# 	for j in range(i):
# 		print("j:{}".format(j))
# 		print(seq[j:i+1])


mylist = [ 1,2,2,3,4,5,6,6]

d = {}
result = False
for x in mylist:
	if x in d:
	result = True
	break
		d[x] = True

print(result)
print(d)
