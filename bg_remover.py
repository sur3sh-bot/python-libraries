from rembg import remove
from PIL import Image

input_path = 'input_photo.jpg'
output_path = 'no_background.png'

# Open the image and remove the background
inp = Image.open(input_path)
output = remove(inp)

# Save the result
output.save(output_path)
print("Background removed successfully!")