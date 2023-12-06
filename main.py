import os
from PIL import Image

# Configuration variables

# Defines the name of the input and output folders
input_folder = 'input'
output_folder = 'output'
# Defines the percentage the image should be scaled to
upscale_percentage = 400
# Defines the supported input file extensions
supported_extensions = ('.jpg', '.png', '.jpeg', '.bmp')
# Defines the desired output format. Default: BMP
output_format = 'BMP'

# Function that upscales the image
def upscale_image(input_image_path, output_image_path, scale_percent):
    image = Image.open(input_image_path)

    # Shows a message if the file is not found
    if not os.path.exists(input_image_path):
        raise FileNotFoundError(f"File '{input_image_path}' not found.")
    
    # Lowers the text of the file extension for easy universal handling
    file_extension = os.path.splitext(input_image_path)[1].lower()
    
    # Raises an error if the file extension is not listed in the suported extensions
    if file_extension not in supported_extensions:
        raise ValueError("File format not supported.")
    
    # Sets the image size
    width, height = image.size
    new_width = int(width * (scale_percent / 100))
    new_height = int(height * (scale_percent / 100))
    new_size = (new_width, new_height)
    
    # Resizes the image using a high-quality resampling method 
    resized_image = image.resize(new_size, Image.NEAREST)

    # Saves the resized image in the desired output format
    resized_image.save(output_image_path, output_format)

# Processes each file in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    # Generates the output filename with the desired file extension
    output_filename = os.path.splitext(filename)[0] + f'.{output_format.lower()}'
    output_path = os.path.join(output_folder, output_filename)
    
    # Upscales the image based on the specified percentage and saves it
    upscale_image(input_path, output_path, upscale_percentage)
