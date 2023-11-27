import cv2

img = cv2.imread('ashKetchumBack.jpg')

# get pixel data in 12 bit rgb and write to file

# Path: mem_gen/img.mem

f = open('ashKetchumBack.mem', 'w')

for row in img:
    for pixel in row:
        # convert to 12 bit rgb
        # write to file
        
        r = pixel[0]/16
        g = pixel[1]/16
        b = pixel[2]/16
        
        # convert to binary 4 bit
        
        r = bin(int(r))[2:].zfill(4)
        g = bin(int(g))[2:].zfill(4)
        b = bin(int(b))[2:].zfill(4)
        
        # write to file
        
        f.write(r)
        f.write(g)
        f.write(b)
        f.write('\n')
        
f.close()

