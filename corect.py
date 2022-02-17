#16.10.21 Gcode by LEDShack
#Написано с целью повисить качество обрезки фото
#
from PIL import Image
import os
import cv2
import scan

def photo(src, types, done = 0):
    img = Image.open("screenshot/" + src)
    size = img.size
    #print(size[0])
    if(not(size[0] == 626 and size[1] == 1280)):
        img.thumbnail([626, 1280])
        img.save("screenshot/_" + src)
        os.remove("screenshot/" + src)
        src = "_" + src
    if(not done):
        #
        if(types == "pasport"):
            cv2.imwrite('done/' + src, scan.pasport(src))
            #os.remove("screenshot/" + src)
        else:
            cv2.imwrite('done/' + src, scan.student(src))
    return(src)
#print(Image.open("screenshot/photo.jpg").size)
