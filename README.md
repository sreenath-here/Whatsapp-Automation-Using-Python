# Whatsapp-Automation-Using-Python
### Whatsapp Automation With A Simple GUI ( Tkinter Module )

Python made Whatsapp automation very easy . with the use of Python's pywhatkit module we can send automated whatsapp messages

There are many Python codes out there in the internet for automatic whatsapp messages but every code out there is to be executed in a terminal or any code editing environments.

but it would be easy for everyone if it has a simple GUI to use that 

So , here is the step by step tutorial for building a simple GUI to use whatsapp automation

## Prerequisites
### Whatsapp Web :
For this to work you have to login to whatsapp web from your default web-browser ( Chrome is preferable )
### Modules:
### Tkinter 
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

##### Import Tkinter from command prompt with the syntax given below
```python
  pip install tkinter
```
### Pywhatkit
pywhatkit is a Python library for sending WhatsApp messages at a certain time, it has several other features too.
##### Import pywhatkit from command prompt with the syntax given below
```python
pip install pywhatkit
```
### Pyautogui
Python pyautogui library is an automation library that allows mouse and keyboard control. Or we can say that it facilitates us to automate the movement of the mouse and keyboard to establish the interaction with the other application using the Python script.
```python
  pip install pyautogui
```
### Pynput
pynput is a Python library that makes it incredibly easy to control and monitor input devices such as your mouse and keyboard. With pynput, you can press keys on your keyboard, or move your mouse, all from your Python program!
```python
  pip install pynput
```
## Source-Code

```python
# importing modules 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import random
import time
import tkinter as tk
from tkinter.ttk import *

# function for sending message
def send_whatsapp_message():
        Number=phoneNumber.get()
        msg=message.get()
        Hours=hours.get()
        Minutes=minutes.get()
        pywhatkit.sendwhatmsg(Number,msg,Hours, Minutes)

# initialising GUI window   
master = tk.Tk()
master.geometry("700x300")
master.configure(bg='#25D366')
master.title("Sreenath's Automatic Whatsapp Message Sender")

#adding labels 
tk.Label(master, text='Enter Phone Number with +91 :' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=0)
tk.Label(master, text='Enter your message:' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=1)
tk.Label(master, text='HOURS:' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=2)
tk.Label(master, text='MINUTES:' , font = ('calibre',10,'bold') , bg='#25D366' , fg='#FFFFFF').grid(row=3, column=0)

# variables declaration
phoneNumber = tk.StringVar()
message = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()

# entry fields
phoneNumberEntry = tk.Entry(master, textvariable=phoneNumber).grid(row=0, column=1)
messageentry = tk.Entry(master, textvariable=message).grid(row=1, column=1)
hoursentry = tk.Entry(master, textvariable=hours).grid(row=2, column=1)
minentry = tk.Entry(master, textvariable=minutes).grid(row=3, column=1)

# button styling
# Create style Object
style = Style()
 
style.configure('TButton', font = ('calibri', 15, 'bold'), borderwidth = '4')

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'green')],background = [('active', 'black')])

# adding button
btn2 = Button(master, text = 'Send Message', command = send_whatsapp_message)
btn2.grid(row = 4, column = 1, )

tk.mainloop()
```
## So this is how the GUI applicaton looks like

### Landing Page
<img width="351" alt="image 1" src="https://user-images.githubusercontent.com/122635878/218301094-2a6d29f0-252e-4e18-a01e-0b748c79175f.png">

#### Entering details

##### Enter the recievers phone number with country code
##### Enter your message 
##### Enter at which hours and minutes the message need to be sent 
##### And press the send message button 
<img width="351" alt="image 2" src="https://user-images.githubusercontent.com/122635878/218301297-6285df91-9654-4b86-ac91-cb7e7726a9fb.png">

### And boom whatsapp will automatically opens the browser and sends whatsapp message through whatsapp web
