#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp

import os
import requests

def web_engine():
	os.system("clear")

	print("1 = data no log | 2 = data log | 3 = file")
	user_input = input()

	if user_input == "1":
		no_log()

	if user_input == "2":
		log()

	if user_input == "3":
		os.system("clear")

		print("1 = image | 2 = pdf")
		user_file = input()

		if user_file == "1":
			image()

		if user_file == "2":
			pdf()

def no_log():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	final = requests.get(output, verify = True)

	print("")
	print("Cookies: " + str(final.cookies))

	final.close()

	print("")
	print("Encoding: " + str(final.encoding))

	final.close()

	print("")
	print("Headers: " + str(final.headers))

	final.close()

	print("")
	print("Is permanent redirect: " + str(final.is_permanent_redirect))

	final.close()

	print("")
	print("Is redirect: " + str(final.is_redirect))

	final.close()

	print("")
	print("Ok: " + str(final.ok))

	final.close()

	print("")
	print("Reason: " + str(final.reason))

	final.close()

	print("")
	print("Status code: " + str(final.status_code))

	final.close()

	print("")
	print("Text: " + str(final.text))

	final.close()

	print("")
	print("URL: " + str(final.url))

	final.close()

def log():
	secure = ""

	os.system("clear")

	file = open("Web Engine Log.txt", "w+")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	final = requests.get(output, verify = True)

	print("")
	print("Cookies: " + str(final.cookies))
	file.write("Cookies: " + str(final.cookies))

	final.close()

	print("")
	print("Encoding: " + str(final.encoding))
	file.write("\n\nEncoding: " + str(final.encoding))

	final.close()

	print("")
	print("Headers: " + str(final.headers))
	file.write("\n\nHeaders: " + str(final.headers))

	final.close()

	print("")
	print("Is permanent redirect: " + str(final.is_permanent_redirect))
	file.write("\n\nIs permanent redirect: " + str(final.is_permanent_redirect))

	final.close()

	print("")
	print("Is redirect: " + str(final.is_redirect))
	file.write("\n\nIs redirect: " + str(final.is_redirect))

	final.close()

	print("")
	print("Ok: " + str(final.ok))
	file.write("\n\nOk: " + str(final.ok))

	final.close()

	print("")
	print("Reason: " + str(final.reason))
	file.write("\n\nReason: " + str(final.reason))

	final.close()

	print("")
	print("Status code: " + str(final.status_code))
	file.write("\n\nStatus code: " + str(final.status_code))

	final.close()

	print("")
	print("Text: " + str(final.text))
	file.write("\n\nText: " + str(final.text))

	final.close()

	print("")
	print("URL: " + str(final.url)) 
	file.write("\n\nURL: " + str(final.url) + "\n\n")

	final.close()
	file.close()

def image():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nEnter desired name:")
	name = input()
	print("\nSecure? y/n")
	secure_input = input()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	picture = str(output)

	data = requests.get(picture, verify = True)

	with open(name, "wb") as file_writer:
		file_writer.write(data.content)

def pdf():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nEnter desired name:")
	name = input()
	print("\nSecure? y/n")
	secure_input = input()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	pdf = output

	data = requests.get(pdf, stream = True, verify = True)

	with open(name, "wb") as pdf:
		for chunk in data.iter_content(chunk_size=1024):
			if chunk:
             			pdf.write(chunk)

web_engine()
