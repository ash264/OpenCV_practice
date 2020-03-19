import cv2
import matplotlib.pyplot as plt

def main():
    
    path="C:\\Users\\ASH\\Downloads\\Compressed\\standard_test_images\\"
    
    imgpath1=path+"lena_color_512.tif"
    imgpath2=path+"peppers_color.tif"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    
    #for good blending alpha + beta == 1
    alpha=0.5
    beta=0.5
    gamma=0
    
    img1 =cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 =cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    #Blending img1 and img2
    output=cv2.addWeighted(img1,alpha,img2,beta,gamma)
    #Actual output = img1*alpha+img2*beta+gamma
  
    titles=['Lena','Veges','Weighted Addition']
    images=[img1,img2,output]
    
    for i in range(3):
    
        plt.subplot(3,1,1+i)
        plt.imshow(images[i])     
        plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([])      
       
    
    plt.show()  
    
   
    
   
if __name__=="__main__":
    main()
    
    
    
    