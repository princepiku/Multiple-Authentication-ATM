import tkinter
from tkinter import *
#import pyrebase
from PIL import ImageTk, Image
from tkinter import messagebox

# Window Created

w = Tk()
w.geometry('1366x768')
w.title('Login')
w.configure(bg = 'black')


# Login Frame Created

login_form_frame = Frame(w, bd = 5, bg = 'black', relief = SUNKEN)
login_form_frame.place(x = 650, y = 100, height = 600, width = 630)

def login():

    # Step-1 Connect to Server
    
    firebaseConfig = {
    'apiKey': "AIzaSyA2en7BLCapNB6pwgIBrqCHpTyu6_4E9Hw",
    'authDomain': "cybercrime-cell.firebaseapp.com",
    'databaseURL': "https://cybercrime-cell-default-rtdb.firebaseio.com/",
    'projectId': "cybercrime-cell",
    'storageBucket': "cybercrime-cell.appspot.com",
    'messagingSenderId': "810317709805",
    'appId': "1:810317709805:web:0748db279dcef76b7227e4",
    'measurementId': "G-G7G3SERMVL"
    }

    # Step-2 Start the Server
    
    firebase = pyrebase.initialize_app(firebaseConfig)

    # Step-3 Create an Object
    
    auth_obj = firebase.auth()
    
    # Login to the server
    
    email_id = username.get()
    passcode = password.get()
    try:
        auth_obj.current_user()
    except:
        print()