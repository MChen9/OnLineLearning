import numpy as np
import cv2
import ffmpeg
'this is branch 2 '
class CameraData:
    def getFrame(self):
        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            print(np.array(frame))
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()



        pass

    def getDataArray(self):
        pass



camData = CameraData()
camData.getFrame()