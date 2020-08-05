import pytest
import numpy as np
from PIL import Image
import to_ascii

class TestBrightnessToAsciis:
    def test_brightnesses_to_asciis(self):
        assert ''.join(to_ascii.brightnesses_to_asciis(range(0, 257, 4))) == '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

class TestImgToAscii:
    def test_accepts_PIL_image(self):
        img = Image.new('RGB', (3, 3), (0, 0, 0))
        ascii, shape = to_ascii.img_to_ascii(img)
        assert shape == (3, 3)
        assert list(list(row) for row in ascii) == [['`', '`', '`'],
        ['`', '`', '`'],
        ['`', '`', '`']]
    
    def test_accepts_RGB_array(self):
        img = np.zeros((3, 3, 3))
        ascii, shape = to_ascii.img_to_ascii(img)
        assert shape == (3, 3)
        assert list(list(row) for row in ascii) == [['`', '`', '`'],
        ['`', '`', '`'],
        ['`', '`', '`']]

    def test_reject_non_RGB(self):
        img = Image.new('RGBA', (3, 3), (0, 0, 0, 1))
        with pytest.raises(ValueError, match=r'Expect data as 3D array of RGB data.'):
            ascii, shape = to_ascii.img_to_ascii(img)

    def test_reject_non_3D(self):
        img = np.zeros((3, 3))
        with pytest.raises(ValueError, match=r'Expect data as 3D array of RGB data.'):
            ascii, shape = to_ascii.img_to_ascii(img)