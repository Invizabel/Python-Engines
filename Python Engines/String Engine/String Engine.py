import os

def string_engine():
	os.system("clear")

	print("What do you want to check?")
	check_in = input()

	os.system("clear")

	print("What do you want to check for?")
	check_for = input()

	output = str(check_for) in check_in

	print("")

	print(output)

string_engine()
