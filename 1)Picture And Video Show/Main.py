import cv2

def image_show():
    img = cv2.imread("Akane.jpg")
    cv2.imshow("Akane Kurokawa",img)
    cv2.waitKey(0)


def video_show():
    vid = cv2.VideoCapture("Oshi no ko.mp4")
    while True: #* Тк видео состоит из множества кадров.
        success,img = vid.read()
        cv2.imshow("Vid",img)
        if cv2.waitKey(1) and 0xFF==ord("q"):
            break

#image_show()
video_show()