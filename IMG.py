import cv2
def main():
    imgpath="C:\\Users\\ASH\\Downloads\\Compressed\\standard_test_images\\lena_color_256.tif"
    img=cv2.imread(imgpath,-1)
   # outpath="C:\\Users\\ASH\\Desktop\\New folder\\123.jpeg"
    #cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
    print(type(img))
    
    print(img.dtype)
    
    print(img.shape)    #resolution
    
    print(img.ndim)     #dimensions of images
    
    print(img.size)
    
 #   cv2.imshow('Lena',img)
    #cv2.imwrite(outpath,img)
 #   cv2.waitKey(0)
 #   cv2.destroyWindow('Lena')
    
if __name__=="__main__":
    main()
    
    
    
    