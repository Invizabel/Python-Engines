import os
import requests

def web_engine():
	os.system("clear")

	print("1 = no log | 2 = log")
	user_input = input()

	if user_input == "1":
		no_log()

	if user_input == "2":
		log()

def no_log():
	os.system("clear")

	print("Enter website:")
	user_input = input()

	secure = "https://"
	output = secure + user_input

	final = requests.get(output)

	print("")
	print("Cookies: " + str(final.cookies))

	print("")
	print("Encoding: " + str(final.encoding))

	print("")
	print("Headers: " + str(final.headers))

	print("")
	print("Is permanent redirect: " + str(final.is_permanent_redirect))

	print("")
	print("Is redirect: " + str(final.is_redirect))

	print("")
	print("Ok: " + str(final.ok))

	print("")
	print("Reason: " + str(final.reason))

	print("")
	print("Status code: " + str(final.status_code))

	print("")
	print("Text: " + str(final.text))

	print("")
	print("URL: " + str(final.url))

	final.close()

def log():
	os.system("clear")

	file = open("Web Engine Log.txt", "w+")

	print("Enter website:")
	user_input = input()

	secure = "https://"
	output = secure + user_input

	final = requests.get(output)

	print("")
	print("Cookies: " + str(final.cookies))
	file.write("Cookies: " + str(final.cookies))

	print("")
	print("Encoding: " + str(final.encoding))
	file.write("\n\nEncoding: " + str(final.encoding))

	print("")
	print("Headers: " + str(final.headers))
	file.write("\n\nHeaders: " + str(final.headers))

	print("")
	print("Is permanent redirect: " + str(final.is_permanent_redirect))
	file.write("\n\nIs permanent redirect: " + str(final.is_permanent_redirect))

	print("")
	print("Is redirect: " + str(final.is_redirect))
	file.write("\n\nIs redirect: " + str(final.is_redirect))

	print("")
	print("Ok: " + str(final.ok))
	file.write("\n\nOk: " + str(final.ok))

	print("")
	print("Reason: " + str(final.reason))
	file.write("\n\nReason: " + str(final.reason))

	print("")
	print("Status code: " + str(final.status_code))
	file.write("\n\nStatus code: " + str(final.status_code))

	print("")
	print("Text: " + str(final.text))
	file.write("\n\nText: " + str(final.text))

	print("")
	print("URL: " + str(final.url))
	file.write("\n\nURL: " + str(final.url) + "\n\n")

	final.close()
	file.close()

web_engine()
