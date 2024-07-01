from PIL import Image
import numpy as np

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
def load_image(image_path, new_width=200):
    """
    load an image and resize it.
    """
    try:
        img = Image.open(image_path)
    except Exception as e:
        print("Unable to load image.")
        return None
    width, height = img.size
    ratio = height / width 
    new_height = int(new_width * ratio)
    resized_image = img.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """
    convert an image to grayscale
    """
    return image.convert('L')

def pixels_to_ascii(image):
    """
    convert grayscale image to ascii characters
    """
    pixels = np.array(image)
    ascii_str = ""
    for value in pixels.flatten():
        index = int(value / 255 * 9)
        ascii_str += ASCII_CHARS[index]
    return ascii_str

def split_ascii_str(ascii_str, width):
    """
    split the ASCII string into lines of the given width to form the final ASCII art.
    """
    ascii_art = [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]
    return "\n".join(ascii_art)

def image_to_ascii(image_path, width=100):
    """
    convert an image to ascii art
    """
    image = load_image(image_path, width)
    if image is None:
        return ""
    image_gray = grayify(image)
    ascii_str = pixels_to_ascii(image_gray)
    ascii_art = split_ascii_str(ascii_str, width)
    return ascii_art

def save_ascii_art(image_path, ascii_art):
    """
    save the ascii art to a text file
    """
    with open(image_path, "w") as file:
        file.write(ascii_art)
    
if __name__ == "__main__":
    import sys
    image_path = sys.argv[1]
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)
    save_ascii_art("ascii_art.txt", ascii_art)   