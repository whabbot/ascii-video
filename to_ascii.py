from PIL import Image, ImageDraw, ImageFont
import numpy as np

import sys

def brightnesses_to_asciis(averages_list):
    '''Returns list of ASCII characters from list of brightnesses'''
    ascii = {0: '`', 1: '^', 2: '"', 3: ',', 4: ':', 5: ';', 6: 'I', 7: 'l', 8: '!', 9: 'i', 10: '~', 11: '+', 12: '_', 13: '-', 14: '?', 15: ']', 16: '[', 17: '}', 18: '{', 19: '1', 20: ')', 21: '(', 22: '|', 23: '\\', 24: '/', 25: 't', 26: 'f', 27: 'j', 28: 'r', 29: 'x', 30: 'n', 31: 'u', 32: 'v', 33: 'c', 34: 'z', 35: 'X', 36: 'Y', 37: 'U', 38: 'J', 39: 'C', 40: 'L', 41: 'Q', 42: '0', 43: 'O', 44: 'Z', 45: 'm', 46: 'w', 47: 'q', 48: 'p', 49: 'd', 50: 'b', 51: 'k', 52: 'h', 53: 'a', 54: 'o', 55: '*', 56: '#', 57: 'M', 58: 'W', 59: '&', 60: '8', 61: '%', 62: 'B', 63: '@', 64: '$'}
    return map(lambda brightness: ascii[int(brightness//4)], averages_list)

def img_to_nparray(img, factor):
    with Image.open(img) as im:
        size = im.size
        new_size = (int(size[0]/factor), int(size[1]/(1.5*factor)))
        im = im.resize(new_size)
        # 2D list of rgb pixel data
        return new_size, np.array(im)

def img_to_ascii(img, factor=1):
    '''
    Opens image file and creates 2D list of ASCII characters
    corresponding to brightness of pixels of source image.
    '''
    # Convert image to 2d numpy array of rgb values.
    if type(img) != np.ndarray:
        new_size, img = img_to_nparray(img, factor)
    else:
        new_size = img.shape
    # Use average of RGB as measure for brightness.
    averages_2d = np.average(img, axis=2) # In doing rgb -> average -> asciis, I'm essentially doing two loops through the data - can we do rgb-->ascii in one step? (change the brightness->ascii map to take rgb, then do average, then do asciis)
    return new_size, map(brightnesses_to_asciis, averages_2d)

def write_to_file(data, dest):
    '''Takes ascii pixels as a 2D list and writes to the specified file'''
    with open(dest, 'w') as f:
        for row in data:
            f.write(''.join(row)+ '\n')

def text_image(data):
    text = '\n'.join(''.join(row) for row in data)
    # text = '\n \n'.join(' '.join(row) for row in data) # Spaced out variant

    # Get the length of the text in pixels in the ImageDraw default
    # font. Returns a tuple (length, height)
    text_length = ImageDraw.Draw(Image.new('RGBA', (1, 1), (0, 0, 0, 1))).getfont().getsize(text)
    # No of lines in text
    no_lines = text.count('\n')
    # The size of the final picture
    size = (int(text_length[0] / no_lines), int(no_lines * text_length[1]))
    # size = (int(text_length[0] * 2 / no_lines), int(no_lines * text_length[1])) # Spaced out variant

    # Create the canvas for the final picture
    txt = Image.new('RGB', size, (0, 0, 0))
    d = ImageDraw.Draw(txt)
    d.multiline_text((0,0), text, spacing=-1)

    return txt


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 to_ascii.py [-tofile <txt destination>] [-factor <reduction factor>] <image source>")
    # If two arguments, convert image to ASCII image and show
    elif len(sys.argv) == 2:
        src = sys.argv[1]
        size, data = img_to_ascii(src)
        text_image(data).show()
    # Shrink image by factor, convert to ASCII and show
    elif sys.argv[1] == '-factor':
        factor = int(sys.argv[2])
        src = sys.argv[3]
        size, data = img_to_ascii(src, factor)
        text_image(data).show()
    # Save convert image to ASCII and save to textfile, optionally resizing
    elif sys.argv[1] == '-tofile':
        dest = sys.argv[2]
        if sys.argv[3] == '-factor':
            factor = int(sys.argv[4])
            src = sys.argv[5]
        else:
            factor = 1
            src = sys.argv[3]
        size, data = img_to_ascii(src, factor)
        write_to_file(data, dest)
    else:
        print("Usage: python3 to_ascii.py [-tofile <txt destination>] [-factor <reduction factor>] <image source>")
        sys.exit()
        

if __name__ == '__main__':
    main()