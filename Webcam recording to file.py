import cv2
import matplotlib.pyplot as plt

def main():
    windowName="Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(0)
    
    filename='C:\\Users\\ASH\\Desktop\\New folder\\456.avi'
    
    codec= cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution = (640,480)
#codec examples => WMV2,WMV1,MJPG,DIVX,XVID,H264
    
    VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)
    
    if cap.isOpened():          #check if camera is opened or not
        ret,frame=cap.read()
    else:
        ret=False
    
    
    while ret:
        ret,frame=cap.read()
        
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #to swap blue green color of video
        
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break
 
    cap.release()       #turn off webcam
    
    cv2.destroyAllWindows()
   
    
if __name__=="__main__":
    main()
    
    
    
    