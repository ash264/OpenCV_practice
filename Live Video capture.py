import cv2
import matplotlib.pyplot as plt

def main():
    windowName="Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    
    if cap.isOpened():          #check if camera is opened or not
        ret,frame=cap.read()
    else:
        ret=False
    
    
    while ret:
        ret,frame=cap.read()
        
        output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray",output)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break
    
    cv2.destroyAllWindows()
    cap.release()       #turn off webcam
    
    
if __name__=="__main__":
    main()
    
    
    
    