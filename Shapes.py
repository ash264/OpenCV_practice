import cv2
import numpy as np
def main():
    img =np.zeros((512,512,3),np.uint8)
    
   # cv2.line(img, (0,99 ),(99,0),(255,0,0),2)
    
   # cv2.rectangle(img,(200,100),(400,300),(0,255,0),2)
    
  #  cv2.circle(img,(60,60),50,(0,0,255),-1)
    
    cv2.ellipse(img,(160,260),(50,20),0,0,360,(0,0,200),5)
    
    points=np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
    points=points.reshape((-1,1,2))
    cv2.polylines(img,[points],True,(0,255,255))
    
    text="Ashish Sharma"
    cv2.putText(img,text,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))
    
    cv2.imshow('Lena',img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
    
if __name__=="__main__":
    main()    
    