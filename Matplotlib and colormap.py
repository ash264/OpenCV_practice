import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath="C:\\Users\\ASH\\Downloads\\Compressed\\standard_test_images\\lena_color_256.tif"
    img=cv2.imread(imgpath,0)
    
    plt.imshow(img,cmap='gray')     #scaling image or filtering
    plt.title('GrayScale ColorMap') #giving title to plot
    plt.xticks([])
    plt.yticks([])      #remove x-y scaling
    plt.show()  #show image
    
    plt.imshow(img,cmap='Reds')
    plt.title('Default ColorMap')
    plt.show()
    
   
if __name__=="__main__":
    main()
    
    
    
    