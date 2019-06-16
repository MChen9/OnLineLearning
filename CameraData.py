import numpy as np
import cv2
import os

class CameraData:

    def getDataArray(self):
        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            print(np.array(frame))

            if cv2.waitKey(300):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        pass

    def sendDataArray(self):
        
        pass


if __name__ == '__main__':
    camData = CameraData()
    camData.getDataArray()