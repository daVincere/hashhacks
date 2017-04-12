import cv2
import sys
# The two arguments passed thru the commandline would 
# the image path and the cascade path
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# create the haar cascade
# whatever is getting throught the cascPath
faceCascade = cv2.CascadeClassifier(cascPath)
# cascade is just an xml file that detects
# that contains data to detect faces

# reading the image
# reading the image via the path described via the terminal
image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the image
faces = faceCascade.detectMultiScale(
	gray, 
	# compensates for the variation in the distance of the
	# faces from the camera
	scaleFactor=1.1,
	# how many objects to be detected near the current window
	minNeighbors=5,
	# size of the window in which the face is detected
	minSize=(30,30),
	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)

# detect multiscale detects the objects
# we are calling it on faceCascade, so it detects the same

print "Found {0} faces!".format(len(faces))

# draw the rectangle around the face
for (x,y,w,h) in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)