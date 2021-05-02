from tkinter import *
from tkinter import messagebox

import os
import re
import requests
import time
import tkinter
#cursor = "dotbox" (not select)
#cursor = "fleur" (select)
#cursor = "watch" (loading)

main_frame = tkinter.Tk()
'''log_frame = tkinter.Tk()
no_log_frame = tkinter.Tk()
secure_frame = tkinter.Tk()'''

secure_var = IntVar()
secure_var = 1
data_var = IntVar()
data_var = 1

def find_url(string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,string)
        return [x[0] for x in url]

'''def web_engine_gui():
         messagebox.showinfo( "Result", "Hello World")'''

def web_engine_gui():

        website_label = Label(main_frame, text = "Website", bg = "lime", fg = "blue")
        website_label.pack()
        website_label.place(height = 100, width = 400, x = 0, y = 0)

        website_input = Entry(main_frame, bg = "blue", fg = "lime")
        website_input.pack()
        website_input.place(height = 100, width = 400, x = 400, y = 0)
        
        exit_button = tkinter.Button(main_frame, text = "Exit", cursor = "fleur", bg = "black", fg = "white", activebackground = "white", activeforeground = "black", command = exit)
        exit_button.pack()
        exit_button.place(height = 100, width = 400, x = 0, y = 100)

        cookie_button = tkinter.Button(main_frame, text = "Cookies", cursor = "fleur", bg = "cyan", fg = "red", activebackground = "red", activeforeground = "cyan", command = cookies)
        cookie_button.pack()
        cookie_button.place(height = 100, width = 400, x = 0, y = 200)

        '''no_log_button = Radiobutton(main_frame, text = "No Log", variable = data_var, value = 1, cursor = "fleur", bg = "cyan", fg = "red", activebackground = "red", activeforeground = "black", command = logic)
        no_log_button.pack(anchor = W)
        no_log_button.place(height = 100, width = 400, x = 0, y = 200)

        log_button = Radiobutton(main_frame, text = "Log", variable = data_var, value = 2, cursor = "fleur", bg = "cyan", fg = "red", activebackground = "red", activeforeground = "cyan", command = logic)
        log_button.pack(anchor = W)
        log_button.place(height = 100, width = 400, x = 0, y = 300)

        secure_button = Radiobutton(main_frame, text = "Secure", variable = secure_var, value = 1, cursor = "fleur", bg = "cyan", fg = "red", activebackground = "red", activeforeground = "cyan", command = logic)
        secure_button.pack(anchor = W)
        secure_button.place(height = 100, width = 400, x = 0, y = 400)

        not_secure_button = Radiobutton(main_frame, text = "Not Secure", variable = secure_var, cursor = "fleur", value = 0, bg = "cyan", fg = "red", activebackground = "red", activeforeground = "cyan", command = logic)
        not_secure_button.pack(anchor = W)
        not_secure_button.place(height = 100, width = 400, x = 0, y = 500)'''

        '''data_log_button = tkinter.Button(start_frame, text ="data log", command = log_check)
        data_log_button.pack()
        data_log_button.place(bordermode=OUTSIDE, height = 100, width = 400)

        file_button = tkinter.Button(start_frame, text ="file", command = file_check)
        file_button.pack()
        file_button.place(bordermode=OUTSIDE, height = 100, width = 400)'''

        main_frame.attributes("-fullscreen", True)

        #print(no_log_check())

def cookies():
        output = "http://" + user_input
        
        final = requests.get(output, verify = True)

        print("")
        print("Cookies: " + str(final.cookies))

        final.close()
        
        web_engine()
        
def logic():
        print()

def no_log_check():
         log_boolean = False

         return log_boolean

def log_check():
        print()

def file_check():
        print()

'''data_no_log_button = tkinter.Button(start_frame, text ="data no log", command = no_log_check)
data_no_log_button.pack()
data_no_log_button.place(bordermode=OUTSIDE, height = 100, width = 400)

data_log_button = tkinter.Button(start_frame, text ="data log", command = log_check)
data_log_button.pack()
data_log_button.place(bordermode=OUTSIDE, height = 100, width = 400)

file_button = tkinter.Button(start_frame, text ="file", command = file_check)
file_button.pack()
file_button.place(bordermode=OUTSIDE, height = 100, width = 400)'''

'''start_frame.attributes("-fullscreen", True)
log_frame.attributes("-fullscreen", True)
no_log_frame.attributes("-fullscreen", True)
secure_frame.attributes("-fullscreen", True)'''

web_engine_gui()
#start_frame.mainloop()
