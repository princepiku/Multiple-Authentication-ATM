import tkinter
from tkinter import *
import pyrebase
from PIL import ImageTk, Image
from tkinter import messagebox
import cv2
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt
import os
import subprocess
from gtts import gTTS


# Window Created

w = Tk()
w.geometry('1366x768')

w.attributes('-fullscreen', False)
w.resizable(0,0)
w.state('zoomed') 

w.title('Dashboard - SECURITY CHECKIN - 1')
w.configure(bg = 'black')

Label(w, height = 2, width = 300, text ="DASHBOARD", bg = "teal", fg = "black", font = ("Sitka Small", 24)).pack()
login_time = "02 : 40 : 60"
Label(w, text = "Login Time - " + login_time, bg = "ivory", fg = "black", font=("Sitka Small", 12)).place(x = 50, y = 120)
last_login_time = "10 : 20 : 30"
Label(w, text = "Last Login Time - ", bg = "ivory", fg = "black", font=("Sitka Small", 12)).place(x = 280, y = 120)
user = "Testing"
Label(w, text = "User - " + user, bg = "ivory", fg = "black", font=("Sitka Small", 12)).place(x = 1200, y = 120)

# Read the image from Real-Time resources
# Step-1 Create a camera object

video_capture_obj = cv2.VideoCapture(0) # Index of camera connected to the system
global path
def capture():

    # Step-2 Capture the image
    
    a, frame = video_capture_obj.read()

    # Step-3 Enable the image
    
    cv2.imshow('image', frame)
    
    # Destroy the capture window
    
    def kill():
    
        # Destroy the capture image
        
        print("Done")
        cv2.destroyAllWindows()
    
    w.after(10000, kill)
    def save():
    
        # Save the Image
        
        cv2.imwrite(f'imagecaptured.jpg', frame)
        print("Saved")
        yes_btn['state'] = DISABLED
        No_btn['state'] = DISABLED
        
        # Activate scan criminal database button
        
        Scan_btn = Button(w, text = "Start Scanning", command = scan)
        Scan_btn.place(x = 200 , y = 400, height=40, width=160)
        
    def scan():
    
        # Compare one image with another to know its originalty
        
        criminal_database = ['img1.jpg','img2.jpg','img3.jpg','img4.jpg']
        test_img = cv2.imread('imagecaptured.jpg')

        # Define the mandatory attribute
        
        max_value = 8   # Acceptable value for detecting face
        max_pt = -1     # Indexing the pictures of database     
        max_kp = 0

        # Create an image object
        
        orb = cv2.ORB_create()
        
        # Calculate the key point and descriptor
        
        (kp1,des1) = orb.detectAndCompute(test_img, None)
        
        # Calculate the key point and descriptor database image
        
        for i in range(0,len(criminal_database)):
            criminal_img = cv2.imread(criminal_database[i])
            (kp2,des2) = orb.detectAndCompute(criminal_img, None)
            
            # Apply Eucledian Formula
            
            e_obj = cv2.BFMatcher()
            distance = e_obj.knnMatch(des1, des2, k = 2) # K is called KNeighbour
            
            # Compare the distance
            
            good = []
            for (m,n) in distance:
                if (m.distance < 0.7*n.distance):
                    good.append([m])
                    
            # Update the latest value
            
            if (len(good) > max_value):
                max_value = len(good)
                max_pt = i
                max_kp = kp2
                
            # Print the Result
            
            print(i, "  ", criminal_database[i], "  ", len(good))

        # print the criminal number
        
        if (max_value > 9):
        
            # Create Label to display message
            
            messagebox.showwarning("Alert", "Authenticated")
            w.destroy()
            import passcode
        else:
            messagebox.showinfo("Information", "No Match Found")
   
    yes_btn = Button(w, text = "Yes & Confirm", command = save)
    yes_btn.place(x = 200 , y = 400, height=40, width=160)
    
    
    No_btn = Button(w, text = "No, Re-Scan", command = capture)
    No_btn.place(x = 400 , y = 400, height=40, width=160)
       
def uploadimage():

    # Upload the image from system
    # Open the menu bar
    
    path = askopenfilename(initialdir = " ", filetypes = (('image file', '*.jpg'), ('All File','*.*')), title = "Select Image")
    print(path)
    
    # Set the path into label
    
    if(path== ""):
    
        # Apply Notification
        
        messagebox.showwarning('Warning', 'File Uploading Cancelled')
    else:
    
        # Apply split property
        
        a = path.split("/")
        
        #print(a)
        
        newpath = a[-1]
        messagebox.showinfo('Sucess', 'File Uploaded Sucessfully')
        upload_btn.configure(text = "Re-Upload")
        
    # Save the Image
    
    img = Image.open(path)
    img.save('imagecaptured.jpg')
    print("Saved")
    def scan():
    
        # Compare one image with another to know its originality
        
        criminal_database =['img1.jpg','img2.jpg','img3.jpg','img4.jpg']
        test_img = cv2.imread('imagecaptured.jpg')

        # Define the mandatory attribute
        
        max_value = 8   # Acceptable value for detecting face
        max_pt = -1     # Indexing the pictures of database     
        max_kp = 0

        # Create an image object
        
        orb = cv2.ORB_create()
        
        # Calculate the key point and descriptor
        
        (kp1,des1) = orb.detectAndCompute(test_img, None)
        
        # Calculate the key point and descriptor database image
        
        for i in range(0,len(criminal_database)):
            criminal_img = cv2.imread(criminal_database[i])
            (kp2,des2) = orb.detectAndCompute(criminal_img, None)
            
            # Apply Eucledian Formula
            
            e_obj = cv2.BFMatcher()
            distance = e_obj.knnMatch(des1, des2, k = 2) # K is called KNeighbour
            
            # Compare the distance
            
            good = []
            for (m,n) in distance:
                if (m.distance < 0.7*n.distance):
                    good.append([m])
                    
            # Update the latest value
            
            if (len(good) > max_value):
                max_value = len(good)
                max_pt = i
                max_kp = kp2
                
            # Print the Result
            
            print(i, "  ", criminal_database[i], "  ", len(good))

        # print the criminal number
        
        if (max_value > 9):
            print("Criminal Face Detected")
            
            # Create Label to display message
            
            ans = Label(w,text = "Criminal Face Detected")
            ans.place(x = 400, y = 400, height=40, width=160)
        else:
            messagebox.showinfo("Information", "No Match Found")
            
    # Activate scan criminal database button
    
    Scan_btn = Button(w, text = "Start Scanning", command = scan)
    Scan_btn.place(x = 200 , y = 400, height=40, width=160) 

capture_btn = Button(w, text = "Capture visitor Image", command = capture, font=("Sitka Small", 10, "bold"), fg= 'black', bg='green')
capture_btn.place(x = 200, y = 160, height=40, width=180)

w.mainloop()

