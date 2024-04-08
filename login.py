import tkinter
from tkinter import *
import pyrebase
from PIL import ImageTk, Image
from tkinter import messagebox

# Window Created

w = Tk()
w.geometry('1366x768')
w.state('zoomed')
w.title('Login')
w.configure(bg = 'teal')


# Login Frame Created

login_form_frame = Frame(w, bd = 2, bg = 'olive', relief = SUNKEN)
login_form_frame.place(x = 450, y = 90, height = 600, width = 650)

def login():

    # Step-1 Connect to Server
    
    firebaseConfig = {
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
    
    # Login to the server
    
    email_id = username.get()
    passcode = password.get()
    try:
        auth_obj.sign_in_with_email_and_password(email_id, passcode)
        
        #print("Login Sucessfully")
        messagebox.showwarning('Success', 'Login Sucessfully')
        
        w.destroy()
        import dashboard
        def user_data():
            return email_id
    except:
        #print("Invalid Credential")
        messagebox.showwarning('Invalid', 'Invalid Credentials')
        
def signup():
    w.destroy()
    import Signup
    
def logoframe():
    logo = Image.open("logo.png")
    img = ImageTk.PhotoImage(logo)
    label = tkinter.Label(image=img)
    label.image = img
    label.place(x = 60, y = 200, height = 400, width = 500)

#logoframe()

# Defining loginform function

def Loginform():

    # Declaring variable
    
    global message;
    global username
    global password
    
    username = StringVar()
    password = StringVar()
    
    # Creating layout of login form
    
    Label(login_form_frame, height = 2, width = 300, text ="LOGIN", bg="indigo", fg="white", font=("Sitka Small", 24, "bold")).pack()
    
    # Username Label
    
    Label(login_form_frame, text = "Username : ", bg="olive", font=("Sitka Small", 12, "bold")).place(x = 100, y = 150)
    
    # Username textbox
    
    Entry(login_form_frame, textvariable = username, font=("Sitka Small", 12, "bold"), width = 30).place(x = 210, y = 150, height = 30)
    
    # Password Label
    
    Label(login_form_frame, text = "Password : ", bg="olive", font=("Sitka Small", 12, "bold")).place(x = 100, y = 210)
    
    # Password textbox
    
    Entry(login_form_frame, textvariable = password, show = "*", font=("Sitka Small", 12, "bold"), width = 30).place(x = 210, y = 210, height = 30)
    
    # Login button
    
    Button(login_form_frame, text="Login", width=12, height=1, bg="chartreuse", command=login, font=("Sitka Small", 12)).place(x = 300, y = 280)
    
    # Create account label
    
    label = Label(login_form_frame, text ="New User? Create Account", bg = "gray", fg = "white", font=("Sitka Small", 12)).place(x = 255, y = 360)
    
    # SignUp button
    
    Button(login_form_frame, text="SIGNUP", width=12, height=1, bg="orange", command=signup, font=("Sitka Small", 12)).place(x = 300, y = 420)
    def user_data():
        return username.get()

Loginform()

w.mainloop()
