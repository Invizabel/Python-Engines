#Documentation:
#https://www.geeksforgeeks.org/downloading-files-web-using-python/
#https://www.w3schools.com/PYTHON/ref_requests_get.asp
#https://www.geeksforgeeks.org/python-check-url-string/
#https://www.w3schools.com/python/gloss_python_check_string.asp

import os
import re
import requests
import time

def find_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)       
	return [x[0] for x in url]

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

		print("1 = image | 2 = pdf | 3 = html | 4 = all images | 5 = all data")
		user_file = input()

		if user_file == "1":
			image()

		if user_file == "2":
			pdf()

		if user_file == "3":
			html()

		if user_file == "4":
			all_images()

		if user_file == "5":
			all_data()

def no_log():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	start = time.time()

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

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	final.close()

def log():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	start = time.time()

	file = open("Web Engine Log.txt", "w+")

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

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")
	file.write("\nTime: " + str(end - start) + " seconds.")

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

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	picture = str(output)

	data = requests.get(picture, verify = True)

	with open(name, "wb") as file_writer:
		file_writer.write(data.content)

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	data.close()

def pdf():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nEnter desired name:")
	name = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

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

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	data.close()

def html():
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	final = requests.get(output, verify = True)

	file = open(user_input + ".html", "w+")
	file.write(final.text)

	final.close()
	file.close()

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

def all_images():
	count = 0
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	url = requests.get(output, verify = True)
	out = str(url.text)
	web_list = find_url(out)

	for i in web_list:
		jpeg = "jpeg" in i
		jpg = "jpg" in i
		png = "png" in i
		y = "http" in i

		if jpeg == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpeg == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("image " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	url.close()

def all_data():
	count = 0
	secure = ""

	os.system("clear")

	print("Enter website:")
	user_input = input()
	print("\nSecure? y/n")
	secure_input = input()

	os.system("clear")
	print("Downloading!")

	start = time.time()

	if secure_input == "y":
		secure = "https://"

	if secure_input == "n":
		secure = "http://"

	output = secure + user_input

	url = requests.get(output, verify = True)
	out = str(url.text)
	web_list = find_url(out)

	file = open(user_input + ".html", "w+")
	file.write(url.text)

	url.close()
	file.close()

	for i in web_list:
		css = ".css" in i
		doc = ".doc" in i
		docx = ".docx" in i
		html = ".html" in i
		jar = ".jar" in i
		jpeg = ".jpeg" in i
		jpg = ".jpg" in i
		jss = ".jss" in i
		pdf = ".pdf" in i
		png = ".png" in i
		py = ".py" in i
		txt = ".txt" in i
		xml = ".xml" in i
		y = "http" in i

		if css == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".css", "wb") as file_writer:
				file_writer.write(data.content)

		if css == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".css", "wb") as file_writer:
				file_writer.write(data.content)

		if doc == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".doc", "wb") as file_writer:
				file_writer.write(data.content)

		if doc == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".doc", "wb") as file_writer:
				file_writer.write(data.content)

		if docx == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".docx", "wb") as file_writer:
				file_writer.write(data.content)

		if docx == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".docx", "wb") as file_writer:
				file_writer.write(data.content)

		if html == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".html", "wb") as file_writer:
				file_writer.write(data.content)

		if html == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".html", "wb") as file_writer:
				file_writer.write(data.content)

		if jar == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jar", "wb") as file_writer:
				file_writer.write(data.content)

		if jar == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jar", "wb") as file_writer:
				file_writer.write(data.content)

		if jpeg == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpeg == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jpeg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if jpg == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jpg", "wb") as file_writer:
				file_writer.write(data.content)

		if jss == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jss", "wb") as file_writer:
				file_writer.write(data.content)

		if jss == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".jss", "wb") as file_writer:
				file_writer.write(data.content)

		if pdf == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".pdf", "wb") as file_writer:
				file_writer.write(data.content)

		if pdf == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".pdf", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

		if png == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".png", "wb") as file_writer:
				file_writer.write(data.content)

		if py == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".py", "wb") as file_writer:
				file_writer.write(data.content)

		if py == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".py", "wb") as file_writer:
				file_writer.write(data.content)

		if txt == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".txt", "wb") as file_writer:
				file_writer.write(data.content)

		if txt == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".txt", "wb") as file_writer:
				file_writer.write(data.content)

		if xml == True and y == True:
			count += 1

			picture = str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".xml", "wb") as file_writer:
				file_writer.write(data.content)

		if xml == True and y == False:
			count += 1

			picture = secure + str(i)
			data = requests.get(picture, verify = True)

			with open("file " + str(count)  + ".xml", "wb") as file_writer:
				file_writer.write(data.content)

	end = time.time()
	print("\nTime: " + str(end - start) + " seconds.")

	url.close()

web_engine()
