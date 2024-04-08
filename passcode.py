import tkinter
from tkinter import *
import pyrebase
from PIL import ImageTk, Image
from tkinter import messagebox
import cv2
from tkinter.filedialog import askopenfilename
from utils import *
from matplotlib import pyplot as plt
import os
import subprocess
from gtts import gTTS
import pyrebase
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#
from PIL import Image,ImageTk
from openpyxl import *
    

def verify():
    p = passcode.get()
   
    # establishing the connection with firebase
    
    firebaseConfig = {
    'apiKey': "AIzaSyBcesiRxeX9GR9aid6-0SgvSXcRsMUO-8o",
    'authDomain': "web-development--id-0120-i.firebaseapp.com",
    'databaseURL': "https://web-development--id-0120-i.firebaseio.com",
    'projectId': "web-development--id-0120-i",
    'storageBucket': "web-development--id-0120-i.appspot.com",
    'messagingSenderId': "265841411938",
    'appId': "1:265841411938:web:ee3b0fe4403973c0030e3b",
    'measurementId': "G-DPQ9BCTCVM"
    }


    def code():
        def key_create(self):
            key = Fernet.generate_key()
            return key

        def key_write(self, key, key_name):
            with open(key_name, 'wb') as mykey:
                mykey.write(key)
    
        def key_load(self, key_name):
            with open(key_name, 'rb') as mykey:
                key = mykey.read()
            return key
    
        def file_encrypt(self, key, original_file, encrypted_file):
            
            f = Fernet(key)
    
            with open(original_file, 'rb') as file:
                original = file.read()
    
            encrypted = f.encrypt(original)
    
            with open (encrypted_file, 'wb') as file:
                file.write(encrypted)
    
        def file_decrypt(self, key, encrypted_file, decrypted_file):
            
            f = Fernet(key)
    
            with open(encrypted_file, 'rb') as file:
                encrypted = file.read()
    
            decrypted = f.decrypt(encrypted)
    
            with open(decrypted_file, 'wb') as file:
                file.write(decrypted)
        
    # start the server
    
    firebase=pyrebase.initialize_app(firebaseConfig)
    
    # retrieve the data from firebase server
    
    db=firebase.database()  # creating an object to retrieve data from realtime database
    
    data=db.child('passcode').get()
    passs=[]
    for eachdata in data:
        dbname=eachdata.val()['passcode']
        passs.append(dbname)
        
    print(passs)
    f=0
    for i in passs:
        if(str(i)==p):
            f=1
    if(f==1):
       messagebox.showinfo("Success",'Passscode Verified')
       os.system('cmd /k "python get_pulse.py"')
    else:
       messagebox.showerror("Success",'Wrong Verified')   
    
    
# Window Created

w = Tk()
w.geometry('1366x768')
w.configure(background='black')

#w.attributes('-fullscreen', False)
#w.resizable(0,0)

w.state('zoomed') 

w.title('Dashboard - SECURITY CHECKIN - 2')

Label(w, text="Dashboard - SECURITY CHECKIN - 2", font = ('Arial, 20'), bg='black', fg='white').place(x=550, y=50)
    
passcode=Entry(w)
passcode.place(x=220, y=230, height=50, width=200)
capture_btn = Button(w, text = "Verify Passcode", bg='orange', font = ('Arial, 12'), command=verify)
capture_btn.place(x=220, y=330, height=50, width=200)


#create an image

image=Image.open('pic1.jpg' )
image.thumbnail((1550,1550),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label=Label(w,image=photo)
label.place(x=600,y=150)

w.mainloop()
