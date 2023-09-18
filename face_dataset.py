from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2
import os

'''root = Tk()
root.geometry("400x400")

# For each person, enter one numeric face id
def click():
    global face_id
    face_id = StringVar()
    image_id = face_id.get()
    face_id.set(image_id)
    root.destroy()
    

Label(root, text="Enter User ID", font=('Calibri 10')).pack()
a = Entry(root, width=30)
a.pack()

Button(root, text="Submit", command=None).pack()'''

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('\n enter user id end press <return> ==>  ')

messagebox.showinfo("Face Gathering", "Initializing face capture. Look the camera and wait ...")
"""print("\n [INFO] Initializing face capture. Look the camera and wait ...")"""

# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.6, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 50: # Take 50 face sample and stop video
         break

# Do a bit of cleanup
messagebox.showinfo("Face Gathering", "Exiting Program and cleanup stuff")
'''print("\n [INFO] Exiting Program and cleanup stuff")'''
cam.release()
cv2.destroyAllWindows()
#root.mainloop()

