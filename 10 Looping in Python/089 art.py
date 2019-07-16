# With a for loop
for x in range(3):
	for num in range(1,11): 
		print("\U0001f600" * num)

# With a while loop
times = 1
while times < 11:
	print("\U0001f600" * times)
	times += 1

# Without string multiplication - ugly solution
# for num in range(1,11): 
# 	count = 1
# 	smileys = ""
# 	while count <= num:
# 		smileys += "\U0001f600"
# 		count += 1
# 	print(smileys)
