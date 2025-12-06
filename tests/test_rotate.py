from PIL import Image
from ossimg.proc import rotate

def test_rotate_90():
    img = Image.new("RGB", (100, 50))
    out = rotate(img, 90)
    assert out.size == (50, 100)
