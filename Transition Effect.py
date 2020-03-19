import cv2
import numpy as np
import time

def main():
    
    path="C:\\Users\\ASH\\Downloads\\Compressed\\standard_test_images\\"
    
    imgpath1=path+"lena_color_512.tif"
    imgpath2=path+"peppers_color.tif"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    
    #Transitioning img1 and img2
    for i in np.linspace(0,1,50):
        alpha=i
        beta=1-alpha
        output=cv2.addWeighted(img1,alpha,img2,beta,0)
        cv2.imshow('Transition',output)
        time.sleep(0.01)
        if cv2.waitKey(1)==27:
            break
   
    cv2.destroyAllWindows()
   
if __name__=="__main__":
    main()
    
    
    
    