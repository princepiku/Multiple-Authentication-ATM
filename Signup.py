import tkinter
from tkinter import *
#import pyrebase
from PIL import ImageTk, Image
from tkinter import messagebox
import string
import random
from subprocess import check_call

# Window Created

w = Tk()
w.geometry('1366x768')
w.title('Signup')
w.state('zoomed')
w.configure(bg = 'sky blue')

# Signup Frame Created

signup_form_frame = Frame(w, bd = 2, bg = 'olive', relief = SUNKEN)
signup_form_frame.place(x = 450, y = 100, height = 600, width = 630)

def signup():

    # Step-1 Connect to Server
    
    firebaseConfig= {
    'apiKey': "AIzaSyBPdS3vr00WBM9yMJhfKgQ72radsZuQCHY",
    'authDomain': "appdemo-c904d.firebaseapp.com",
    'databaseURL':"https://appdemo-c904d-default-rtdb.firebaseio.com/",
    'projectId': "appdemo-c904d",
    'storageBucket': "appdemo-c904d.appspot.com",
    'messagingSenderId': "650609176050",
    'appId': "1:650609176050:web:638127333fa381b9750f6b",
    'measurementId': "G-KJGEX9Q4WV"
    }

    # Step-2 Start the Server
    
    firebase = pyrebase.initialize_app(firebaseConfig)

    # Step-3 Create an Object
    
    auth_obj = firebase.auth()
    
    # Create an account
    
    email_id = username.get()
    
    # Create Random Password
    
    def generate_random_password(): 
        global password
        length = 10
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        
     	# shuffling the characters
        
        random.shuffle(characters)
     	
     	# picking random characters from the list
        
        rchar = []
        for i in range(length):
            rchar.append(random.choice(characters))
     
     	# shuffling the resultant password
        # traverse the temporary password array and append the chars
        # to form the password
        
        password = ""
        for x in rchar:
                password = password + x
                
    # Popup window For Password generated  
    
    def popupmsg(msg, title):
        def copy(msg):
        
            # Copy the password
            
            command = 'echo ' + msg.strip() + '|clip'
            
            #print("text copied")
            
            copy_label = tkinter.Label(root, text="Password Copied")
            copy_label.place(x = 100, y = 35)
            okay_btn['state'] = ACTIVE
            copy_btn['state'] = DISABLED
            return check_call(command, shell = True)
            
        root = tkinter.Tk()
        root.title(title)
        root.geometry("300x100")
        root.eval('tk::PlaceWindow . center')
        print(msg)
        password_label = tkinter.Label(root, text = "PASSWORD:  " + msg)
        password_label.pack(side="top", fill="x", pady=10)
        
        # Enable the ctrl + c option
        
        copy_btn = Button(root, text = "Copy Password", command = lambda:copy(msg))
        copy_btn.place(x = 130, y = 60)
        
        # Opening the login window
        
        def login():
            root.destroy()
            w.destroy()
            import login
            
        okay_btn = tkinter.Button(root, text="Okay", command = login)
        okay_btn.place(x = 80, y = 60)
        okay_btn['state'] = DISABLED
        root.mainloop()
           
    try:
        # Generate random password function call
        
        generate_random_password()
        auth_obj.create_user_with_email_and_password(email_id, password) 
        
        #print(password)
        # popupmsg Function call
        
        popupmsg(password, "Password Generated")
    except:
    
        #print("Invalid Credential")
        
        messagebox.showwarning('Alert', 'Account Already Exist')
        

def logoframe():
    logo = Image.open("logo.png")
    img = ImageTk.PhotoImage(logo)
    label = tkinter.Label(image=img)
    label.image = img
    label.place(x = 60, y = 200, height = 400, width = 500)

#logoframe()

# Defining loginform function

def Signupform():

    # Declaring variable
    
    global username
    
    username = StringVar()

    # Creating layout of login form
    
    Label(signup_form_frame, height = 2, width = 300, text ="Create Your Account", bg = "blue", fg = "white", font = ("Sitka Small", 24, "bold")).pack()
    
    # Username Label
    
    Label(signup_form_frame, text = "Enter Your Email-Id", bg = "olive", fg = "white", font = ("Lucida Fax", 14, "bold")).place(x = 210, y = 200)
    
    # Username textbox
    
    Entry(signup_form_frame, textvariable = username, width = 35, font = ("Arial Rounded MT", 12)).place(x = 150, y = 250, height = 30)
    
    # Login button
    
    Button(signup_form_frame, text = "Create Account", width = 20, height = 1, bg = "lime",command = signup, font = ("Sitka Small", 12, "bold")).place(x = 200, y = 350)
    
   
Signupform()
w.mainloop()
