from PIL import Image
def rotate(img, angle):
  return img.rotate(angle, expand=True)
