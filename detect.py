import requests
import cv2
import os
import sys
import json
 
image_path = sys.argv[1]

url = "http://localhost:5000/detect"

image = cv2.imread(image_path)
payload = {"input": open(image_path, "rb")}
response = requests.post(url, files=payload).json()

print "Face Present: " + str(response["face_present"])
print "Narendra Modi: " + str(response["modi"])
print "Arvind Kejriwal: " + str(response["kejriwal"])
 
for (startX, startY, endX, endY) in response["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
 
cv2.imshow("Faces Found", image)
cv2.waitKey(0)