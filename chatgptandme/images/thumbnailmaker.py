from PIL import Image
import os

# Folder where your full images are stored
input_folder = r'G:\Coding Etc\WebsiteGithub\rdfk.github.io\chatgptandme\images'
output_folder = r'G:\Coding Etc\WebsiteGithub\rdfk.github.io\chatgptandme\images'

# Set your thumbnail size (width, height)
thumbnail_size = (200, 200)

# Loop through images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        try:
            img = Image.open(image_path)
            img.thumbnail(thumbnail_size)
            name, ext = os.path.splitext(filename)
            thumb_filename = f"{name}-thumb{ext}"
            thumb_path = os.path.join(output_folder, thumb_filename)
            img.save(thumb_path)
            print(f"Created thumbnail: {thumb_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
