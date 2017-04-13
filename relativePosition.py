import cv2
import sys

bodyCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

video_capture = cv2.VideoCapture(0)

while True:
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	body = bodyCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbours=5,
		minSize=(50, 50),
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
	# drawing a box
	for (x,y,w,h) in body:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

	# displaying the resulting field
	cv2.imshow('Video', frame)

	if cv2.waitkey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()