import cv2
import matplotlib.pyplot as plt

def main():
    windowName="Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    print('Width : '+str(cap.get(3)))
    print('Height : '+str(cap.get(4)))
    
    cap.set(3,400)
    cap.set(4,300)
    
    print('Width : '+str(cap.get(3)))
    print('Height : '+str(cap.get(4)))
    
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
 
    cap.release()       #turn off webcam
    
    cv2.destroyAllWindows()
   
    
if __name__=="__main__":
    main()
    
    
    
    