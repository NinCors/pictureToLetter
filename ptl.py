from PIL import Image
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

PIC = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


# convert RGB to letter
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '

    # calculate gray value
    # use the gray formula
    gray = int(0.2126 * r +0.7152 * g + 0.0722 * b)
    
    # make the letter version of picture with layers
    length = len(ascii_letter)
    unit = (256.0 + 1)/length
    return ascii_letter[int(gray/unit)]

def runner():
    
    pic = Image.open(PIC)
    pic = pic.resize((WIDTH,HEIGHT),Image.NEAREST)
    
    charPic = ''

    for i in range(HEIGHT):
        for w in range(WIDTH):
            charPic += get_char(*pic.getpixel((w,i)))
        charPic += '\n'

    print charPic

runner()
