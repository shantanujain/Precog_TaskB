# Precog_TaskB

## Steps

* Scraped images of Narendra Modi and Arvind Kejriwal from Google
* Used OpenCV to detect faces in the images
* Trained a Face Recognizer using the faces from the previous step
* 5-fold cross validation was done by splitting the dataset into 80:20 (training:testing). Average testing accuracy: 68.7%

## Prerequisites

* Flask
* OpenCV
* numpy

## To Run

```shell
python app.py
python detect.py *path-to-image*
```

## Test Cases

"Samples" contains some test cases with output

## Observations

* OpenCV's face detector is prone to false-positives (can be seen in one of the test cases)