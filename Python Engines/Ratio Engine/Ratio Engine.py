#Documentation:
#https://www.w3schools.com/python/python_for_loops.asp
#https://www.w3schools.com/python/python_arrays.asp

import os
import time

def ratio_engine():
	add = 0
	average = 0
	count = 0
	tracker = 0
	data = []
	input1 = 0
	input2 = 0
	output = 0

	os.system("clear")
	print("How many data points?")
	data_points = int(input())
		
	os.system("clear")
	name_1 = input("Name of Entity 1: ")
	
	os.system("clear")
	name_2 = input("Name of Entity 2: ")
	
	for x in range(data_points):
		tracker += 1
		
		os.system("clear")
		print("Data set: " + str(tracker))
		input_1 = int(input(name_1 + ": "))
		
		os.system("clear")
		print("Data set: " + str(tracker))
		input_2 = int(input(name_2 + ": "))
		
		if input_2 == 0:
			input_2 = 1
			
			output = input_1 / input_2
			data.append(output)
			
		if input_2 != 0:
			output = input_1 / input_2
			data.append(output)
		
	os.system("clear")
	print("Calculating...")
	start = time.time()
	
	count = len(data)
	
	for x in range(0, (count)):
		add = add + data[x]
		
	average = add / count
	
	end = time.time()
	
	os.system("clear")
	print(name_1 + ": " + str(average) + "%")
	print()
	print("Time: " + str(end - start) + " seconds.")
	
ratio_engine()
