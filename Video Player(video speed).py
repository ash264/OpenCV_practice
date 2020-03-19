import cv2
import matplotlib.pyplot as plt
#this code controls the speed of video to be played
def main():
    windowName="OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    
    filename='C:\\Users\\ASH\\Desktop\\New folder\\456.avi'
    
    cap = cv2.VideoCapture(filename)
    
    
    while (cap.isOpened()):  
        
        ret,frame=cap.read()
        
        print(ret)
        
        if ret:
            cv2.imshow(windowName,frame)
            if cv2.waitKey(33)==27: #parameter of waitKey wil determine speed of video(frame rate)
                break
        else:
            break
 
    cap.release()
    
    cv2.destroyAllWindows()
   
    
if __name__=="__main__":
    main()
    
    
    
    