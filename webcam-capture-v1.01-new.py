import cv2 as cv

key = cv.waitKey(1)
webcam = cv.VideoCapture(0)
while True:

    check, frame = webcam.read()
    print(check) #prints true as long as the webcam is running
    print(frame) #prints matrix values of each framecd
    cv.imshow("Capturing", frame)
    key = cv.waitKey(1)
    if key == ord('s'):
        cv.imwrite(filename='saved_img.jpg', img=frame)
        webcam.release()
        img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
        cv.imshow("Captured Image", img_new)
        cv.waitKey(1650)
        cv.destroyAllWindows()
        cv.imwrite(filename='saved_img-final.jpg', img=img_new)
        print("Saved BGR image as grayscale")

        break
    elif key == ord('q'):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv.destroyAllWindows()
        break
