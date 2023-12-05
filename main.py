import os
from PIL import Image

def upscale_image(input_image_path, output_image_path, scale_percent):
    # Opens the image
    image = Image.open(input_image_path)
    
    # Defines the new size of the image
    width, height = image.size
    new_width = int(width * (scale_percent / 100))
    new_height = int(height * (scale_percent / 100))
    new_size = (new_width, new_height)
    
    # Resizes the image using a high-quality resampling method
    resized_image = image.resize(new_size, Image.NEAREST)  
    
    # Saves the resized image as a .bmp file
    resized_image.save(output_image_path, 'BMP')

# Path to the input and output folders. Here they are in the same folder as the py file
input_folder = 'input'
output_folder = 'output'

# Processes each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  
        input_path = os.path.join(input_folder, filename)
        
        # Generates the output filename with .bmp extension
        output_filename = os.path.splitext(filename)[0] + '.bmp'
        output_path = os.path.join(output_folder, output_filename)
        
        # Upscales the image to 400% and save as a .bmp file, as previously set
        upscale_image(input_path, output_path, 400)
