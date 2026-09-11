septembre 08 2026
### goal: creating the first model that will  reconize the bodie on a webcam

### reflection and problem
* **thinking:** did some reserch in the documentatino of cv2 VideoCapture Class Reference for understand the basic of the library and watching some youtube video
* **probleme:** the camera would'nt open because the windows camera system block it. Had to use cv2.CAP_MSMF for resolving the problem

### next steps
1. creating a new function for calculat the angle
2. more test for accuracy
==============================================================================================================================================================
septembre 10 2026
### goal: new function that calculate angle of three parts of the bodie

### reflection and problem
* **recherch:** reading the cv2 arkan2 section for read the angle of 3 defferent part of the bodi and the section text for putting the result on the screen
* **thinkink:** choosing the way to show the result at the screen by testing different police and different colors
* **problem:** I didn't know what to do when the angle pass 180 degree so I just substract it from 360

### next step
1. creating a dictionary of mouvement and there angle 
