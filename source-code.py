import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import random
import time
import tkinter as tk
from tkinter.ttk import *

def send_whatsapp_message():
        Number=phoneNumber.get()
        msg=message.get()
        Hours=hours.get()
        Minutes=minutes.get()
        pywhatkit.sendwhatmsg(Number,msg,Hours, Minutes)

   
master = tk.Tk()
master.geometry("700x300")
master.configure(bg='#25D366')
master.title("Sreenath's Automatic Whatsapp Message Sender")

tk.Label(master, text='Enter Phone Number with +91 :' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=0)
tk.Label(master, text='Enter your message:' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=1)
tk.Label(master, text='HOURS:' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=2)
tk.Label(master, text='MINUTES:' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=3, column=0)


phoneNumber = tk.StringVar()
message = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()


phoneNumberEntry = tk.Entry(master, textvariable=phoneNumber).grid(row=0, column=1)
messageentry = tk.Entry(master, textvariable=message).grid(row=1, column=1)
hoursentry = tk.Entry(master, textvariable=hours).grid(row=2, column=1)
minentry = tk.Entry(master, textvariable=minutes).grid(row=3, column=1)


# Create style Object
style = Style()
 
style.configure('TButton', font = ('calibri', 15, 'bold'), borderwidth = '4')

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'green')],background = [('active', 'black')])



btn2 = Button(master, text = 'Send Message', command = send_whatsapp_message)
btn2.grid(row = 4, column = 1, )

tk.mainloop()
