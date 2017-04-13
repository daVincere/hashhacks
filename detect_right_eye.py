import cv2
import sys


# cascPath = "./haarcascade_eye.xml"

eyesCascade = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")


video_capture = cv2.VideoCapture(1)

while True:
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	eyes = eyesCascade.detectMultiScale(
		gray,
		# as we need both the eyes of the same scale
		scaleFactor=1.1,
		minNeighbors =5,
		minSize = (25, 5),
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	# create rectangles around the face
	for(x,y,w,h) in eyes:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255,0), 2)

	# display the resulting frame 
	cv2.imshow('Video', frame)

	# Just a great way to end stuff when nothing's working
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# releasing the capture
video_capture.release()
cv2.destroyAllWindows()