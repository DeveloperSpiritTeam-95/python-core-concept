"""
from rembg import remove
from PIL import Image

input_path = 'image.jpg'
output_path = "output.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

"""



