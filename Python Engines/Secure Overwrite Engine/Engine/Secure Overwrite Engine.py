#Documentation:
#https://www.geeksforgeeks.org/how-to-open-and-close-a-file-in-python/
#https://www.askpython.com/python/examples/rename-a-file-directory-python

import os

def secure_overwrite_engine():
	os.system("clear")
	
	print("Secure Overwrite Engine!")
	
	file = open("abc.abc", "w+")
	
	while True:
		file.write(str("abc"))
	
	file.close()

secure_overwrite_engine()
