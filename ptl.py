from PTL import Image
import argparse

ascii_letter = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")



# convert RGB to letter

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '

    # calculate gray value
    # use the gray formula
    gary = int(0.2126 * r +0.7152 * g + 0.0722 * b)
    
    # make the letter version of picture with layers
    length = len(ascii_char)
    unit = (256 + 1)/length
    return ascii_char[int(gray/unit)]
