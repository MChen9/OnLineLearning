import numpy as np
import cv2
import socket


class CameraData:
    # static variables
    def __init__(self):
        self.dataArray = np.array([])
        pass

    def getDataArray(self):
        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            self.dataArray = np.array(frame)

            if cv2.waitKey(300):
                break

        # When everything done, release the capture
        cap.release()
        pass

    def sendDataArray(self):
        self.dataArray
        pass


if __name__ == '__main__':
    camData = CameraData()
    camData.getDataArray()
