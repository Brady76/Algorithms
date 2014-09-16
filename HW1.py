import time
import random

global input1, List
input1 = int(raw_input("Please enter how many random numbers to generate: "))


for x in range(0, 10):
	start = time.time()
	List = range(0, input1+1)

	randomizedList = random.shuffle(List)

	for i in range(0, input1):
		i_min = List[i]
		for j in range(i+1, input1 + 1):
			if List[j] < List[i]:
				temp = List[i]
				List[i] = List[j]
				List[j] = temp
	#print List
	end = time.time()
	print end - start
#0.00115394592285 for 10^1
#0.0357511043549 for 10^2  30.981
#1.69439291954 for 10^3    47.394
#156.499064922 for 10^4    92.3629
#
