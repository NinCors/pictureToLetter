from PTL import Image
import argparse

ascii_letter = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# Input argument parser
parser = argparse.ArgumentParser()

parser.add_argument('file')    # input file
parser.add_argument('-o', '--output')   #output file
parser.add_argument('--width', type = int, default = 80) # width of output letter graph
parser.add_argument('--height', type = int, default = 80) # height of output letter grap

# Get the infomation from user input
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


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
