# Import OpenCV2 for image processing
import cv2
import lcddriver
from time import *
# Import numpy for matrices calculations
import numpy as np

lcd = lcddriver.lcd()
lcd.lcd_clear()

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.createLBPHFaceRecognizer()

# Load the trained mode
recognizer.load('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id,ref = recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        if(Id == 1):
            Id = "MILIND"
          lcd.lcd_clear()
            lcd.lcd_display_string("WELCOME MILIND",1)
            lcd.lcd_display_string("Member Id :1",2)  
        elif(Id == 2):
            Id = "SURAj"
            lcd.lcd_clear()
            lcd.lcd_display_string("WELCOME SURAJ",1)
            lcd.lcd_display_string("Member Id :2",2)
        elif(Id == 4):
            Id = "BANDA"
            lcd.lcd_clear()
            lcd.lcd_display_string("WELCOME BANDA",1)
            lcd.lcd_display_string("Member Id :4",2)
        elif(Id == 3):
            Id = "AMOL"
            lcd.lcd_clear()
            lcd.lcd_display_string("WELCOME AMOL",1)
            lcd.lcd_display_string("Member Id :3",2)
        elif(Id == 5):
            Id = "SHREYA"
        elif(Id == 6):
            Id = "ARCHANA"    
        else:
            print(Id)
            Id = "Unknown_Person"

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
