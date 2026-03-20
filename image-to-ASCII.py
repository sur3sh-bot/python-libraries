from PIL import Image #pip install pillow
#Pillow is a Python library used for working with images

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayscale(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""

    for pixel in pixels:
        
        index = pixel * len(ASCII_CHARS) // 256
        ascii_str += ASCII_CHARS[index]

    return ascii_str


path = input("Enter image path: ") #file should be in the same directory as this file

try:
    image = Image.open(path)
except:
    print(" Invalid path or file not found")
    exit()

image = resize_image(image)
image = grayscale(image)

ascii_data = pixels_to_ascii(image)


width = image.width
ascii_img = "\n".join(
    [ascii_data[i:i+width] for i in range(0, len(ascii_data), width)]
)

print(ascii_img)


#optional if we want to save the art 
with open("ascii_art.txt", "w") as f:
    f.write(ascii_img)

print("\n ASCII art saved as ascii_art.txt")