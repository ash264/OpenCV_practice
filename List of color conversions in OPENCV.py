import cv2
import matplotlib.pyplot as plt

def main():
    
    j=0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j+=1
            
    print('There are '+str(j+1)+'color conversion flags in OPENCV.')
   
    
   
if __name__=="__main__":
    main()
    
    
    
    