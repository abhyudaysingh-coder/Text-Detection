import cv2
import easyocr

#read image
img = cv2.imread('/Users/abhyudaysingh/Desktop/Text_Detection/images/NEYMAR-IN-SANTOS-2011.jpg')
#instance text detector
reader = easyocr.Reader(['en'] , gpu = True)
#detect text in image
result = reader.readtext(img)
for (bbox, text, score) in result:
    new_bbox = [tuple(map(int , point)) for point in bbox]
    top_left = new_bbox[0]
    bottom_right = new_bbox[2]
    if score > 0.1:
        cv2.rectangle(img , top_left , bottom_right , (0,255,0) , 5)
        cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0 , 255), 2)
cv2.imshow('Image with Detected Text', img)
cv2.waitKey(0)