import cv2
import matplotlib.pyplot as plt

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():          #check if camera is opened or not
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret=False
    
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.title('Color image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    cap.release()       #turn off webcam
    
    
if __name__=="__main__":
    main()
    
    
    
    