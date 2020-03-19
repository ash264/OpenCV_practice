import cv2
import matplotlib.pyplot as plt

def main():
    
    path="C:\\Users\\ASH\\Downloads\\Compressed\\standard_test_images\\"
    
    imgpath1=path+"lena_color_512.tif"
    imgpath2=path+"peppers_color.tif"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    
    img1 =cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 =cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    add=img1+img2               #addition
    sub=img1-img2               #Subtraction
    mul=img1*img2               #Multiplication
    div=img1/img2               #Division
    
    titles=['Lena','Veges','Add','Sub','mul','div']
    images=[img1,img2,add,sub,mul,div]
    
    for i in range(6):
    
        plt.subplot(1,6,1+i)
        plt.imshow(images[i])     
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([])      
       
    
    plt.show()  
    
   
    
   
if __name__=="__main__":
    main()
    
    
    
    