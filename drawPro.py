
import matplotlib.pyplot as plt
import cv2

print("You will get an Edit #: Original: 0 || Daiz: 1 || Big Sketch: 2 || Original vs Sketh: 3")
 
 
run="";
    
while  run !="END":

    photo = input("Copy and Paste URL: ") 

    #cv2 way to set photo 
    img=cv2.imread(photo)

    
    #print orig pic
    cv2.imshow('Original image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    #matplotlib print of the photo color daiz
    plt.imshow(img)
    plt.axis(False)
    plt.show()

    #setting photo color to gray
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #inverting photo
    invert_img=cv2.bitwise_not(gray_img)

    #blur to get prominent features from photo large phone need large kernel size (more blur)small photo size (3x3)(5x5) need small kernel
    #No even numbers ex(222,222)
    blur_img=cv2.GaussianBlur(invert_img,(51,51),0)

    invblur_img=cv2.bitwise_not(blur_img)

    #to get the sketch of photo
    sketch_img=cv2.divide(gray_img,invblur_img, scale=256.0)

    #saving the sketch
    cv2.imwrite('Sketch.png',sketch_img)

    
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    
        #orig vs sketch

    plt.figure(figsize=(14,8))

    plt.subplot(1,2,1)
    plt.title('Orig',size=18)
    rgb_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title('Sketch',size=18)
    rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()

    run= input('Enter "END" if you do not have another photo else press ENTER: ')
