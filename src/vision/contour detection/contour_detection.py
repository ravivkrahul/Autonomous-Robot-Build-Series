import cv2 as cv
import numpy as np

image = cv.imread('traffic_light.jpg')
output = image.copy()

red_lower = np.array([167, 170, 40])
red_upper = np.array([179, 255, 255])
yellow_lower = np.array([20, 157, 40])
yellow_upper = np.array([40, 255, 255])
green_lower = np.array([45, 80, 70])
green_upper = np.array([95, 255, 255])

hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# masks
mask_red = cv.inRange(hsv_image, red_lower, red_upper)
mask_yellow = cv.inRange(hsv_image, yellow_lower, yellow_upper)
mask_green = cv.inRange(hsv_image, green_lower, green_upper)

# Images after applying mask
red_image = cv.bitwise_and(image, image, mask=mask_red)
yellow_image = cv.bitwise_and(image, image, mask=mask_yellow)
green_image = cv.bitwise_and(image, image, mask=mask_green)

contours, hierarchy = cv.findContours(mask_green, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

if len(contours)>0:
    max_contour=max(contours,key=cv.contourArea)
    ((x,y),radius)=cv.minEnclosingCircle(max_contour) #usualy for identifying perfect circles
    M=cv.moments(max_contour)


    if M["m00"] !=0:
        cx= M["m10"] / M["m00"]
        cy= M["m01"] / M["m00"]
    print((x,y)) #centre calculated with cv.minEnclosing Circle of largest contour
    print((cx,cy)) #centre calculated with cv.moments of largest contour
    
    if radius>10:
        cv.circle(output, (int(x),int(y)),4, (0,0,255), -1)
        cv.circle(output, (int(x),int(y)),int(radius),(0,0,255), 3)
'''     
        M["m00"]  # Area
        M["m10"] #It sums up all the x-coordinates of the contour pixels.
        M["m01"] #It sums up all the x-coordinates of the contour pixels.
            '''

cv.imshow('green_contour',output)
cv.waitKey(0)
cv.destroyAllWindows()