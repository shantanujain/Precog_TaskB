import numpy as np
import urllib
import json
import cv2
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify

app = Flask(__name__)
 
HAARCASCADE_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(base_path=os.path.abspath(os.path.dirname(__file__)))
FACE_RECOGNITION_MODEL_PATH = "{base_path}/models/model_1.yaml".format(base_path=os.path.abspath(os.path.dirname(__file__)))
 
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/detect', methods=['POST'])
def modi_kejriwal():
 
	if request.method == "POST":
		if request.files.get("input", None) is not None:
			image = get_image(path=request.files.get('input', ''))
 
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		face_detector = cv2.CascadeClassifier(HAARCASCADE_PATH)
		rects = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
		print FACE_RECOGNITION_MODEL_PATH

		face_recognizer = cv2.createLBPHFaceRecognizer()
		face_recognizer.load(FACE_RECOGNITION_MODEL_PATH)

		modi = False
		kejriwal = False

		if (len(rects) > 0):
			for (x, y, w, h) in rects:
				image2 = image.copy()
				cropped = image2[y: y + h, x: x + w]
				cropped_gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

				prediction = face_recognizer.predict(cropped_gray)
				print "DISTANCE: " + str(prediction[1])
				if (prediction[1] < 39):
					if (prediction[0] == 1):
						modi = True
					elif (prediction[0] == 2):
						kejriwal = True
 
		faces = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]
 
		response = {"faces": faces, "face_present": len(rects)>0, "modi": modi, "kejriwal": kejriwal}
 
	return jsonify(response)
 
def get_image(path):

	data = path.read()

	image = np.asarray(bytearray(data), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	return image


if __name__ == '__main__':
    app.run(debug=True)
