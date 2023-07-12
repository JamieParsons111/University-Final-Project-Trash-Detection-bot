# University-Final-Project-Trash-Detection-bot
My University final project- Automated and remote controlled car programmed to find trash with image based Machine Learning

This project was designed to help in research for ocean pollution in detecting trash, with automated and remote control to compare results and discuss which solution may be more ideal.

I created this project using a lego NXT car, I programmed the car to be able to be remotely controlled mainly via (WASD) keys. And then also created code to make it drive autonomously, making it drive on its own and turn after a few seconds to randomise the driving pattern. The automated car was also programmed to brake when nearing an object (Using a sensor to detect the distance between the object and the sensor), it would then reverse change direction and continue as normal.

For the Machine Learning part of the project I downloaded a dataset from Roboflow which had annotated images etc. 
I then began building and training a Convultional Neural Network with Darknet and YOLO, and then once trained I used the open CV library for the object recognition and ran the program through the webcam attached to the car.
The car and webcam was connected to my laptop via bluetooth and ran from there wirelessly.

