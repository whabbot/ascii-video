"""Convert images to ASCII art - helper functions for ASCII Video.

Functions:
    brightnesses_to_asciis(list) -> list. Convert list of brightness
        values to corresponding ASCII characters.
    img_to_ascii(Image object/2D Numpy array, int/float) -> (tuple, 2D map object).
        Convert Image object or Numpy array representing an image into
        2D map object of ASCII characters.
    text_image(2D sequence) -> Image object. Draws ASCII characters
        onto Image object.
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np


def brightnesses_to_asciis(brightness_list):
    """Converts list of brightnesses to corresponding ASCII characters.

    Parameters:
        brightness_list: list. Pixel brightnesses for row of image.
    Returns:
        Map object. The corresponding ASCII characters for each
            brightness.
    """
    ascii = {0: '`', 1: '^', 2: '"', 3: ',', 4: ':', 5: ';', 6: 'I',
        7: 'l', 8: '!', 9: 'i', 10: '~', 11: '+', 12: '_', 13: '-',
        14: '?', 15: ']', 16: '[', 17: '}', 18: '{', 19: '1', 20: ')',
        21: '(', 22: '|', 23: '\\', 24: '/', 25: 't', 26: 'f', 27: 'j',
        28: 'r', 29: 'x', 30: 'n', 31: 'u', 32: 'v', 33: 'c', 34: 'z',
        35: 'X', 36: 'Y', 37: 'U', 38: 'J', 39: 'C', 40: 'L', 41: 'Q',
        42: '0', 43: 'O', 44: 'Z', 45: 'm', 46: 'w', 47: 'q', 48: 'p',
        49: 'd', 50: 'b', 51: 'k', 52: 'h', 53: 'a', 54: 'o', 55: '*',
        56: '#', 57: 'M', 58: 'W', 59: '&', 60: '8', 61: '%', 62: 'B',
        63: '@', 64: '$'}

    return map(lambda brightness: ascii[int(brightness//4)], brightness_list)


def img_to_ascii(img):
    """Convert Image object or Numpy array representing an image into
    2D map object of ASCII characters.

    Parameters:
        img: PIL Image object or Numpy array representing an image.
    Returns:
        Map object. ASCII characters representing each pixel of
            original image.
        Tuple. Shape of the image in pixels (height, width).
    """
    # Convert image to 2d Numpy array of rgb values.
    if type(img) != np.ndarray:
        img = np.array(img)
    # Use average of RGB as measure for brightness.
    brightnesses = np.average(img, axis=2)

    # In doing rgb -> average -> asciis, essentially doing two loops
    # through the data - can we do rgb-->ascii in one step? (change the
    # brightness->ascii map to take rgb, then do average, then do
    # asciis)
    return map(brightnesses_to_asciis, brightnesses), np.shape(brightnesses)


def text_image(ascii_characters, image_shape):
    """Draw 2D sequence of ASCII characters onto PIL Image.

    Parameters:
        ascii_characters: 2D sequence. ASCII characters for drawing
            onto image.
            [
                [row1],
                [row2],
                ...
            ]
    Returns:
        textimage: PIL Image object. Image with ASCII representing
            each pixel of original image.
    """
    text = '\n'.join(''.join(row) for row in ascii_characters)

    # Size of the text in pixels: tuple (width, height).
    default_font = ImageDraw.Draw(Image.new('RGBA', (1, 1), (0, 0, 0, 1))).getfont()
    text_width, text_height = default_font.getsize(text)

    # Calculate size of canvas to draw text onto.
    num_lines = image_shape[0]
    canvas_height = int(num_lines * text_height - num_lines)
    canvas_width = int(text_width / num_lines)

    # Create the canvas for the final picture
    textimage = Image.new('RGB', (canvas_width, canvas_height), (0, 0, 0))
    text_draw = ImageDraw.Draw(textimage)
    text_draw.multiline_text((0,0), text, spacing=-1)

    return textimage
