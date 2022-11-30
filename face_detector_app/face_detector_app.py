import cv2

trained_face_data = cv2.CascadeClassifier('/Users/hitu/Vs_Code/Artificial Intelligence in python/face_detector_app/alg.xml')
#img = cv2.imread('/Users/hitu/Vs_Code/Artificial Intelligence in python/face_detector_app/ppl.jpeg')
#grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
webcam = cv2.VideoCapture(0)


#detect faces regardless scale of the face
#face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print(face_coordinates)

'''for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
'''

#cv2.imshow('Face Detector app', img)
#the above command opens the img for a split second we use waitKey() method to take a keyinput so that the running program can stop running
#cv2.waitKey() 
