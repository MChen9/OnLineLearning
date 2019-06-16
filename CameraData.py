import numpy as np
import cv2
import socket
import sys


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
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as err:
            print("socket creation failed with error %s" % (err))


        # default port for socket
        port = 2000


        try:
            host_ip = "10.0.0.201"
        except socket.gaierror:

            # this means could not resolve the host
            print("there was an error resolving the host")
            sys.exit()

            # connecting to the server
        s.connect((host_ip, port))

        print("the socket has successfully connected to google \
        on port == %s" % (host_ip))

        pass


if __name__ == '__main__':
    camData = CameraData()
    camData.sendDataArray()
