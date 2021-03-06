# Precog_TaskB

## Steps

* Scraped images of Narendra Modi and Arvind Kejriwal from Google
* Used OpenCV to detect faces in the images
* Trained a Face Recognizer using the faces from the previous step and saved the trained model (model_1.yaml)
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

<p align="center">
  <img src="https://raw.githubusercontent.com/shantanujain/Precog_TaskB/master/samples/Sample1.jpg" width="50%" >
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/shantanujain/Precog_TaskB/master/samples/Sample2.jpg" width="50%" >
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/shantanujain/Precog_TaskB/master/samples/Sample3.jpg" width="50%" >
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/shantanujain/Precog_TaskB/master/samples/Sample4.jpg" width="50%" >
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/shantanujain/Precog_TaskB/master/samples/Sample5.jpg" width="50%" >
</p>
