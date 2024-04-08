from tkinter import *
from PIL import Image,ImageTk
import cv2
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from utils import *
from matplotlib import pyplot as plt
import os
import subprocess
from gtts import gTTS

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
    
    w.after(5000, kill)
    def save():
    
        # Save the Image
        
        cv2.imwrite(f'imagecaptured.jpg', frame)
        print("Saved")
        yes_btn['state'] = DISABLED
        No_btn['state'] = DISABLED
        
        # Activate scan criminal database button
        
        Scan_btn = Button(w, text = "Start Scanning", bg = "green", font = ("Sitka Small", 8), command = scan)
        Scan_btn.place(x = 600 , y = 400)
        
    def scan():
    
        # Compare one image with another to know its originality
        
        criminal_database = ['Original_image.jpg','Original_image2.jpg','Original_image3.jpg','Original_image4.jpg']
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
            ans.place(x = 670, y = 400)
        else:
            messagebox.showinfo("Information", "No Match Found")
            
    capture_btn['state'] = DISABLED
    upload_btn['state'] = DISABLED
    yes_btn = Button(w, text = "Yes & Confirm", bg = "orange", font = ("Sitka Small", 8), command = save)
    yes_btn.place(x = 550 , y = 300)
    
    
    No_btn = Button(w, text = "No, Re-Scan", bg = "yellow", font = ("Sitka Small", 8), command = capture)
    No_btn.place(x = 640 , y = 300)
    
    
    
def uploadimage():

    # Upload the image from system
    # Open the menu bar 
    
    path = askopenfilename(initialdir = "", filetypes = (('image file', '*.jpg'), ('All File','*.*')), title = "Select Image")
    print(path)
    
    # Set the path into label
    
    if(path== ""):
    
        # Apply Notification
        
        messagebox.showwarning('Warning', 'File Uploading Canceled')
    else:
    
        # Apply split property
        
        a = path.split("/")
        
        #print(a)
        
        newpath = a[-1]
        messagebox.showinfo('Success', 'File Uploaded Sucessfully')
        upload_btn.configure(text = "Re-Upload")
        
    # Save the Image
    
    img = Image.open(path)
    img.save('imagecaptured.jpg')
    print("Saved")
    
    # Activate scan criminal database button
    
    Scan_btn = Button(w, bg = "red", font = ("Sitka Small", 8), text = "Start Scanning")
    Scan_btn.place(x = 600 , y = 400)
    
# Create a Window
  
w = Tk()
w.geometry('1250x1250')
w.title("Camera")

capture_btn = Button(w, text = "Capture Criminal Image", bg = "brown", font = ("Sitka Small", 8), command = capture)
capture_btn.place(x = 550, y = 150)

upload_btn =  Button(w, bg = "purple", font = ("Sitka Small", 8), command = uploadimage)
upload_btn.configure(text = "Upload Criminal Image")
upload_btn.place(x = 550, y = 600)


w.mainloop()
