import os
from PIL import Image

def upscale_image(input_image_path, output_image_path, scale_percent):
    # Open the image
    image = Image.open(input_image_path)
    
    # Define the new size
    width, height = image.size
    new_width = int(width * (scale_percent / 100))
    new_height = int(height * (scale_percent / 100))
    new_size = (new_width, new_height)
    
    # Resize the image using a high-quality resampling method
    resized_image = image.resize(new_size, Image.NEAREST)  # You can try different resampling filters
    
    # Save the resized image as a .bmp file
    resized_image.save(output_image_path, 'BMP')

# Path to the input and output folders
input_folder = 'input'
output_folder = 'output'

# Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # Add more file extensions if needed
        input_path = os.path.join(input_folder, filename)
        
        # Generate the output filename with .bmp extension
        output_filename = os.path.splitext(filename)[0] + '.bmp'
        output_path = os.path.join(output_folder, output_filename)
        
        # Example usage: Upscale the image to 400% and save as a .bmp file
        upscale_image(input_path, output_path, 400)