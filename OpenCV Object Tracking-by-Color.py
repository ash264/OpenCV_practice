import cv2
import numpy as np

#Object Tracking by Color

def main():
         
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
    
    while ret:
        ret,frame=cap.read()
        #HSV==HUE SATURATION VALID
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
           
        #Blue Color(All Shades are covered)
        low=np.array([100,50,50])
        high=np.array([140,255,255])
        
        #Green Color
        #low=np.array([50,100,50])
        #high=np.array([255,140,255])
        
        #Red Color
        #low=np.array([50,50,100])
        #high=np.array([255,255,140])
        

        image_mask=cv2.inRange(hsv,low,high)   
        
        output=cv2.bitwise_and(frame,frame,mask=image_mask)
        
        cv2.imshow("Image Mask",image_mask)
    #    print(image_mask)
        cv2.imshow("Original Webcam Feed",frame)
        cv2.imshow("Color Tracking",output)
        if cv2.waitKey(1)==27: 
            break
        
          
    cap.release()
    
    cv2.destroyAllWindows()
   
    
if __name__=="__main__":
    main()
    
    
    
    