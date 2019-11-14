# Capturing Images from Webcam Using OpenCV Python

Capture an image by accessing the webcam of your system and save it to your machine.

# Softwares and packages required:

1. Python, v3.6.7
2. Matplotlib, v3.0.2 (to view the captured images or images that have been modified. Not required for Windows machines.) `pip3 install matplotlib`
3. OpenCV, v3.4.4 `sudo apt install python3-opencv`

<b> Please read the full document. </b>

# How to use:

1. Run the file webcam-capture-v1.01.py by running the command `python3 webcam-capture-v1.01.py`
1. The webcam will start running.
1. Bring the picture that you want to save in the webcam frame.
1. Once the object is in the right frame, press the key 's' to save a picture.
1. If you want to quit, just press 'q'.
1. After hitting 's' to save the picture,you will get a view of the saved image which will automatically close in 1.6s and a new image file will be created in the same directory as that of the program. The image will be saved as saved_image.jpg
1. The file saved_image is converted to grayscale
1. Do not exit the program by stopping the command. This won't turn off the camera. If you do this, close the terminal to stop the camera from running.
