import to_ascii

class TestBrightnessToAsciis:
    def test_brightnesses_to_asciis(self):
        assert ''.join(to_ascii.brightnesses_to_asciis(range(0, 257, 4))) == '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'