import cv2
import sys

# cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# faceCascade = cv2.CascadeClassifier(cascPath)

# sets the videosource to the default webcam
video_capture = cv2.VideoCapture(1)

while True:
	# capture frame-by-frame
	# reads one frame at a time
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize = (40, 40),
		# flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	for(x,y,w,h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# display the resulting frame
	cv2.imshow('Video', frame)


	# to exit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# when everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()