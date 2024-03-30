import cv2
import random

def slice_images(image):
    height, width = image.shape[:2]
    # Calculate dimensions for each slice
    slice_height = height // 2  # Divide height into 2 equal parts
    slice_width = width // 2   # Divide width into 2 equal parts

    slices = []
    
    for y in range(0, height, slice_height):
        for x in range(0, width, slice_width):
            # Extract slice
            slice_img = image[y:y+slice_height, x:x+slice_width]
            slices.append(slice_img)

    return slices

def compare(simg,img):
    won = cv2.imread("D:/Game/Won.jpg")
    won = cv2.resize(won,(250,250))
    lost = cv2.imread("D:/Game/Lost.jpg")
    lost = cv2.resize(lost,(250,250))
    gray_image1 = cv2.cvtColor(simg, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate MSE
    mse = ((gray_image1 - gray_image2) ** 2).mean()
    if mse <= 25:
        cv2.imshow("Won",won)
        cv2.imshow("Question Image",img)
        cv2.imshow("Your Image",simg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else : 
        cv2.imshow("Lost",lost)
        cv2.imshow("Question Image",img)
        cv2.imshow("Your Image",simg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    

def slice_image(image):
    global csf
    half_height=image.shape[0]//2
    half_width=image.shape[1]//2
    qimg2 = cv2.imread('D:/Game/QUE2.jpg')
    qimg2 = cv2.resize(qimg2,(250,250))
    qimg4 = cv2.imread('D:/Game/QUE4.jpg')
    qimg4 = cv2.resize(qimg4,(250,250))
    sliced_image1=image[:half_height,:]
    sliced_image1 = cv2.resize(sliced_image1,(250,250))
    sliced_image2=image[half_height:,:]
    sliced_image2 = cv2.resize(sliced_image2,(250,250))
    sliced_image3=image[:,:half_width]
    sliced_image3 = cv2.resize(sliced_image3,(250,250))
    sliced_image4=image[:,half_width:]
    sliced_image4 = cv2.resize(sliced_image4,(250,250))
    qimg = cv2.imread('D:/Game/QUE1.jpg')
    qimg = cv2.resize(qimg,(250,250))
    cv2.imshow("Question(H/V)",qimg)
    qhv = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if qhv == 49:
        qimg1 = cv2.imread('D:/Game/QUE3.jpg')
        qimg1 = cv2.resize(qimg1,(250,250))
        cv2.imshow("Question(U/L)",qimg1)
        cv2.imshow("Upper",sliced_image1)
        cv2.imshow("Lower",sliced_image2)
        qul = cv2.waitKey(0)
        cv2.destroyAllWindows()
        if qul == 49:
            cv2.imshow("Image",sliced_image1)
            cv2.imshow("Question(A/N)",qimg2)
            qah1 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qah1 == 49:
                slice_image(sliced_image1)
            elif qah1 == 50:
                if ch == 49:
                    compare(sliced_image1,sqimg)
                elif ch == 50:
                    if k == f:
                        if ch == 50:
                            compare(sliced_image1,fqimg)
                        elif ch == 51:
                            cv2.imshow("Image",img1)
                            cv2.imshow("suggestion",suimg)
                            csf = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if csf == s:
                                con_img(sliced_image1,img1)
                            elif csf == f:
                                con_flip_img(img1,sliced_image1)
                    else:
                        cv2.imshow("Image",sliced_image1)
                        cv2.imshow("Suggestion",suimg)
                        fp = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if fp == f:
                            flip_img(sliced_image1)
                elif ch == 51:
                    if k == f:
                        cv2.imshow("Image",img1)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image1,img1)
                        elif csf == f:
                            con_flip_img(img1,sliced_image1)
                    else:
                        cv2.imshow("Image",sliced_image1)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image1,img1)
                        elif csf == f:
                            flip_img(sliced_image1)
                    
                    
        elif qul == 50:
            cv2.imshow("Image",sliced_image2)
            cv2.imshow("Question4",qimg2)
            qah2 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qah2 == 49:
                slice_image(sliced_image2)
            elif qah2 == 50:
                if ch == 49:
                    compare(sliced_image2,sqimg)
                elif ch == 50 :
                    if k == f:
                        if ch == 50:
                            compare(sliced_image2,fqimg)
                        elif ch == 51:
                            cv2.imshow("Image",img1)
                            cv2.imshow("suggestion",suimg)
                            csf = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if csf == s:
                                con_img(sliced_image2,img1)
                            elif csf == f:
                                con_flip_img(img1,sliced_image2)
                    else:
                        cv2.imshow("Image",sliced_image2)
                        cv2.imshow("Suggestion",suimg)
                        fp = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if fp == f:
                            flip_img(sliced_image2)
                elif ch == 51:
                    if k == f:
                        cv2.imshow("Image",img1)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image2,img1)
                        elif csf == f:
                            con_flip_img(img1,sliced_image2)
                    else:
                        cv2.imshow("Image",sliced_image2)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image2,img1)
                        elif csf == f:
                            flip_img(sliced_image2)
                
    elif qhv == 50:
        cv2.imshow("Question5",qimg4)
        cv2.imshow("Right",sliced_image4)
        cv2.imshow("Left",sliced_image3)
        qrl = cv2.waitKey(0)
        cv2.destroyAllWindows()
        if qrl == 49:
            cv2.imshow("Image",sliced_image4)
            cv2.imshow("Question6",qimg2)
            qva1 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qva1 == 49:
                slice_image(sliced_image4)
            elif qva1 == 50:
                if ch == 49:
                    compare(sliced_image4,sqimg)
                elif ch == 50:
                    if k == f:
                        compare(sliced_image4,fqimg)
                    else:
                        cv2.imshow("Image",sliced_image4)
                        cv2.imshow("Suggestion",suimg)
                        fp = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if fp == f:
                            flip_img(sliced_image4)
                elif ch == 51:
                    if k == f:
                        cv2.imshow("Image",img1)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image4,img1)
                        elif csf == f:
                            con_flip_img(img1,sliced_image4)
                    else:
                        cv2.imshow("Image",sliced_image4)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image4,img1)
                        elif csf == f:
                            flip_img(sliced_image4)
                        
        elif qrl == 50:
            cv2.imshow("Image",sliced_image3)
            cv2.imshow("Question(R/L)",qimg2)
            qva2 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qva2 == 49:
                slice_image(sliced_image3)
            elif qva2 == 50:
                if ch == 49:
                    compare(sliced_image3, sqimg)
                elif ch == 50:
                    if k == f:
                        if ch == 50:
                            compare(sliced_image3,fqimg)
                        elif ch == 51:
                            cv2.imshow("Image",img1)
                            cv2.imshow("suggestion",suimg)
                            csf = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if csf == s:
                                con_img(sliced_image3,img1)
                            elif csf == f:
                                con_flip_img(img1,sliced_image3)
                    else:
                        cv2.imshow("Image",sliced_image3)
                        cv2.imshow("Suggestion",suimg)
                        fp = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if fp == f:
                            flip_img(sliced_image3)
                elif ch == 51:
                    if k == f:
                        cv2.imshow("Image",img1)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image3,img1)
                        elif csf == f:
                            con_flip_img(img1,sliced_image3)
                    else:
                        cv2.imshow("Image",sliced_image3)
                        cv2.imshow("Suggestion",suimg)
                        csf = cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        if csf == s:
                            con_img(sliced_image3,img1)
                        elif csf == f:
                            flip_img(sliced_image3)
                    
def flip_img(img):
    global cfq
    fq = cv2.imread("D:/Game/FLQ.jpg")
    fq = cv2.resize(fq,(250,250))
#image flipped horizontally
    imgh = cv2.flip(img,0)
    imgh = cv2.resize(imgh,(250,250))
#image flipped vertically
    imgv = cv2.flip(img,1)
    imgv = cv2.resize(imgv,(250,250))
    cv2.imshow("Question25",fq)
    cv2.imshow("Horizontally",imgh)
    cv2.imshow("Vertically",imgv)
    q = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if q == 49:
        if k == f:
            slice_image(imgh)
        else:
            if ch == 50:
                compare(imgh,fqimg)
            elif ch == 51:
                cv2.imshow("Question",suimg)
                cv2.imshow("Image2",img1)
                cfq = cv2.waitKey(0)
                cv2.destroyAllWindows()
                if cfq == s:
                    con_img(imgh,img1)
                elif cfq == f:
                    con_flip_img(img1,imgh)
           
    elif q == 50:
        if k == f:
            slice_image(imgv)
        else:
            if ch == 50:
                compare(imgv,fqimg)
            elif ch == 51:
                cv2.imshow("Question",suimg)
                cv2.imshow("Image2",img1)
                cfq = cv2.waitKey(0)
                cv2.destroyAllWindows()
                if cfq == s:
                    con_img(imgv,img1)
                elif cfq == f:
                    con_flip_img(img1,imgv)
        
        
        
def con_img(imagef,img1):
    global csf
    half_height=img1.shape[0]//2
    half_width=img1.shape[1]//2
    qimg2 = cv2.imread('D:/Game/QUE2.jpg')
    qimg2 = cv2.resize(qimg2,(250,250))
    qimg4 = cv2.imread('D:/Game/QUE4.jpg')
    qimg4 = cv2.resize(qimg4,(250,250))
    sliced_image1=img1[:half_height,:]
    sliced_image1 = cv2.resize(sliced_image1,(250,250))
    sliced_image2=img1[half_height:,:]
    sliced_image2 = cv2.resize(sliced_image2,(250,250))
    sliced_image3=img1[:,:half_width]
    sliced_image3 = cv2.resize(sliced_image3,(250,250))
    sliced_image4=img1[:,half_width:]
    sliced_image4 = cv2.resize(sliced_image4,(250,250))
    qimg = cv2.imread('D:/Game/QUE1.jpg')
    qimg = cv2.resize(qimg,(250,250))
    cv2.imshow("Question H/V",qimg)
    cv2.imshow("IMAGE2",img1)
    qhv = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if qhv == 49:
        qimg1 = cv2.imread('D:/Game/QUE3.jpg')
        qimg1 = cv2.resize(qimg1,(250,250))
        cv2.imshow("Question U/L",qimg1)
        cv2.imshow("Upper",sliced_image1)
        cv2.imshow("Lower",sliced_image2)
        qul = cv2.waitKey(0)
        cv2.destroyAllWindows()
        if qul == 49:
            cv2.imshow("Image",sliced_image1)
            cv2.imshow("Question A/N",qimg2)
            qah1 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qah1 == 49:
                con_img(imagef,sliced_image1)
            elif qah1 == 50:
                    if k == f:
                        if csf == f:
                            con_img_join(sliced_image1,imagef)
                        elif csf == s:
                            cv2.imshow("Image",sliced_image1)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image1,imagef)
                            elif cfq == f:
                                con_img_join(sliced_image1,imagef)
                        
                    else:
                        if cfq == s:
                            cv2.imshow("Image",sliced_image1)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image1,imagef)
                        elif cfq == f:
                            con_img_join(sliced_image1,imagef)
                    
        elif qul == 50:
            cv2.imshow("Image",sliced_image2)
            cv2.imshow("Question R/L ",qimg2)
            qah2 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qah2 == 49:
                con_img(imagef,sliced_image2)
            elif qah2 == 50:
                    if k == f:
                        if csf == f:
                            con_img_join(sliced_image2,imagef)
                        elif csf == s:
                            cv2.imshow("Image",sliced_image2)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image2,imagef)
                            elif cfq == f:
                                con_img_join(sliced_image2,imagef)
                    else:
                        if cfq == s:
                            cv2.imshow("Image",sliced_image2)
                            cv2.imshow("Suggestion",suimg)
                            fp =  cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image2,imagef)
                        elif cfq == f:
                            con_img_join(sliced_image2,imagef)
                
    elif qhv == 50:
        cv2.imshow("Question R/F ",qimg4)
        cv2.imshow("Right",sliced_image4)
        cv2.imshow("Left",sliced_image3)
        qrl = cv2.waitKey(0)
        cv2.destroyAllWindows()
        if qrl == 49:
            cv2.imshow("Image",sliced_image4)
            cv2.imshow("Question A/N",qimg2)
            qva1 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qva1 == 49:
                con_img(imagef,sliced_image4)
            elif qva1 == 50:
                    if k == f:
                        if csf == f:
                            con_img_join(sliced_image4,imagef)
                        elif csf == s:
                            cv2.imshow("Image",sliced_image4)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image4,imagef)
                            elif cfq == f:
                                con_img_join(sliced_image4,imagef)
                    else:
                        if cfq == s:
                            cv2.imshow("Image",sliced_image4)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image4,imagef)
                        elif cfq == f:
                            con_img_join(sliced_image4,imagef)
                        
        elif qrl == 50:
            cv2.imshow("Image",sliced_image3)
            cv2.imshow("Question A/N",qimg2)
            qva2 = cv2.waitKey(0)
            cv2.destroyAllWindows()
            if qva2 == 49:
                con_img(imagef,sliced_image3)
            elif qva2 == 50:
                    if k == f:
                        if csf == f:
                            con_img_join(sliced_image3,imagef)
                        elif csf == s:
                            cv2.imshow("Image",sliced_image3)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image3,imagef)
                            elif cfq == f:
                                con_img_join(sliced_image3,imagef)
                    else:
                        if cfq == s:
                            cv2.imshow("Image",sliced_image3)
                            cv2.imshow("Suggestion",suimg)
                            fp = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            if fp == f:
                                con_flip_img(sliced_image3,imagef)
                        elif cfq == f:
                            con_img_join(sliced_image3,imagef)
def con_flip_img(simg,fimg):
    global csf
    fq = cv2.imread("D:/Game/FLQ.jpg")
    fq = cv2.resize(fq,(250,250))
    cv2.imshow("Question H/V",fq)
    simgh = cv2.flip(simg,0)
    simgh = cv2.resize(simgh,(250,250))
    simgv = cv2.flip(simg,1)
    simgv = cv2.resize(simgv,(250,250))
 #image flipped horizontally
    cv2.imshow("Horizontally",simgh)
#image flipped vertically
    cv2.imshow("Vertically",simgv)
    qcf = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if qcf == 49:
        if k == f:
            if csf == f:
                con_img(fimg,simgh)
            elif csf == s:
                con_img_join(simgh,fimg)
        else:
            if cfq == s:
                con_img_join(simgh,fimg)
            elif cfq == f:
                con_img(fimg,simgh)

    elif qcf == 50: 
        if k == f:   
            if csf == f:
                con_img(fimg,simgv)
            elif csf == s:
                con_img_join(simgv,fimg)
        else:
            if cfq == s:
                con_img_join(simgv,fimg)
            elif cfq == f:
                con_img(fimg,simgv)
        

def con_img_join(simg,fimg):
    sugc = cv2.imread("D:/Game/qc.jpg")
    sugc = cv2.resize(sugc,(250,250))
    con_img1 = cv2.hconcat([simg,fimg])
    con_img2 = cv2.hconcat([fimg,simg])
    cv2.imshow("Image1 to Image2",con_img1)
    cv2.imshow("Image2 to Image1",con_img2)
    cv2.imshow("Suggestion",sugc)
    sq = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if sq == 49:
        compare(con_img1,cqimg)
    elif sq == 50:
       compare(con_img2,cqimg)
        
    

    
def ch_1():
# Choose a random slice
    random_slice = random.choice(slices)
    random_slice = cv2.resize(random_slice, (250, 250))

# Display the random slice
    cv2.imshow('Random Slice', random_slice)
    cv2.imshow("Images",img1)
    cv2.imshow('Next',con)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return random_slice

def ch_2():

# Choose a random slice
    random_slice = random.choice(slices)
    random_slice = cv2.resize(random_slice, (250, 250))

# Randomly choose to flip horizontally or vertically
    flip_code = random.choice([0, 1])

# Apply the flip
    if flip_code == 0:
        random_slice = cv2.flip(random_slice, 0)  # Vertical flip
    else:
        random_slice = cv2.flip(random_slice, 1)  # Horizontal flip
        
# Display the random slice
   
    cv2.imshow('Random Slice', random_slice)
    cv2.imshow("Images",img1)
    cv2.imshow('Next',con)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return random_slice

def ch_3():

    # Slice the image
    slices = slice_images(img1)

    # Choose a random slice
    random_slices = random.sample(slices, 2)
    random_slices_resized = [cv2.resize(slice, (250, 250)) for slice in random_slices]

    # Randomly flip the slices horizontally or vertically
    flip_options = [0, 1]  # 0 for vertical filp, 1 for horizontal flip
    random_flip1 = random.choice(flip_options)
    random_flip2 = random.choice(flip_options)

    random_slices_resized[0] = cv2.flip(random_slices_resized[0], random_flip1)
    random_slices_resized[1] = cv2.flip(random_slices_resized[1], random_flip2)

    # Concatenate the two random slices horizontally
    concatenated_image = cv2.hconcat(random_slices_resized)

    # Display the concatenated image
    cv2.imshow('Concatenated Image', concatenated_image)
    cv2.imshow("Images",img1)
    cv2.imshow('Next', con)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return concatenated_image

img1 = cv2.imread('D:/Game/THE_IMAGE.jpg')
suimg = cv2.imread('D:/Game/S.jpg')
con = cv2.imread('D:/Game/CON.jpg')
con = cv2.resize(con,(250,250))
img1 = cv2.resize(img1,(250,250))   
suimg = cv2.resize(suimg,(250,250))  
# Slice the image
slices = slice_images(img1)
first = cv2.imread('D:/Game/First.jpg')
first = cv2.resize(first, (250, 250))
cv2.imshow("The Game",first)
ch = cv2.waitKey(0)
cv2.destroyAllWindows()
if ch == 49:
    sqimg = ch_1()
elif ch == 50:
    fqimg = ch_2()
elif ch == 51:
    cqimg = ch_3()
s = ord("s")  
f = ord("f")
cv2.imshow("Suggestion",suimg)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
if k == s:
    slice_image(img1)
elif k == f:
    flip_img(img1)