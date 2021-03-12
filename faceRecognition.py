import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Read the input image
img = cv2.imread('test.jpg')

#Make Size of image
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.04, 2)
#eyes=eye_cascade.detectMultiScale(gray, 1.04, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#for (x, y, w, h) in eyes:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)    
    
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
