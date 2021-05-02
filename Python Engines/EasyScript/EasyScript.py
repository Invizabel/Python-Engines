import os
import re

def EasyScript():
	os.system("clear")
	
	end = False
	
	print("Enter file name:")
	file_name = input()
	easy_file = open(file_name, "r")
	total = easy_file.readlines()
	
	final = []
	
	for sub in total: 
		final.append(re.sub('\n', '', sub))
		
	python_file = open("EasyScript Shell.py", "a")
	python_file.write("import os\nimport random\nimport re")
	
	for x in final:
		command_check = list(x.split(" "))
		length = len(command_check)
		
		if end == True and command_check[0] != "end":
			python_file.write("\n\t")
		
		if end == False and command_check[0] != "end":
			python_file.write("\n")
		
		if length > 0:
			if command_check[0] == "clear":
				python_file.write("os.system(\"clear\")")
			
			if command_check[0] == "end":
				end = False
				
			if command_check[0] == "if":
				result_1 = x.replace(" is ", " == ")
				result = result_1.replace(" isnt ", " != ")
				
				python_file.write(result + ":")
				end = True
				
			if command_check[0] == "listen" and length <= 2:
				result = x.replace("listen ", "", 1)
				
				python_file.write(result + " = input()")
				
			if command_check[0] == "listen" and length > 2:
				count = -1
				result_1 = ""
				result_2 = ""
				result = command_check[1]
				
				for i in range(length - 2):
					count += 1
					result_2 += command_check[count + 2] + " "
				
				python_file.write(result + " = input(" + result_2 + ")")
		
			if command_check[0] == "say":
				result = x.replace("say ", "", 1)
					
				python_file.write("print(" + result + ")" + "")
				
		if length > 1:
			if command_check[1] == "is":
				result = x.replace(" is ", " = ", 1)
					
				python_file.write(result + "")
				
	easy_file.close()
	python_file

EasyScript()
