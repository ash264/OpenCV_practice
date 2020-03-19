import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath="C:\\Users\\ASH\\Downloads\\Compressed\\standard_test_images\\lena_color_256.tif"
    img=cv2.imread(imgpath,1)
    
    plt.imshow(img)     
    plt.title('Image with Default ColorMap') #giving title to plot
    plt.xticks([])
    plt.yticks([])      #remove x-y scaling
    plt.show()  #show image
    
    
    #To convert BGR-formatImageColor(used by cv2) to RGB-formatImageColor(used by matplotlib) 
    img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    
    
    plt.imshow(img)     
    plt.title('Image with Default ColorMap') #giving title to plot
    plt.xticks([])
    plt.yticks([])      #remove x-y scaling
    plt.show()  #show image
    
   
    
   
if __name__=="__main__":
    main()
    
    
    
    