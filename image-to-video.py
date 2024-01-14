import cv2
import os

# Input images in the "images" folder
image_folder = 'images'

# Output video file
output_video_path = 'output_video.mp4'

# Supported image extensions
supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.heic']

# Get a list of image files in the folder with supported extensions
image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, filename)) and any(filename.lower().endswith(ext) for ext in supported_extensions)]

# Check if there are any image files in the folder
if not image_files:
    print("No supported image files found in the 'images' folder.")
    exit()

# Initialize dimensions with the first image's dimensions
first_image = cv2.imread(image_files[0])
if first_image is None:
    print(f"Failed to load the first image: {image_files[0]}")
    exit()

height, width, layers = first_image.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID' for AVI format
out = cv2.VideoWriter(output_video_path, fourcc, 1, (width, height))  # 1 is the frames per second

# Add images to the video
for image_path in image_files:
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load an image: {image_path}")
        continue
    out.write(image)

# Release the VideoWriter
out.release()

# Check if the video file was created successfully
if os.path.exists(output_video_path):
    print(f"Video '{output_video_path}' created successfully!")
else:
    print("Failed to create the video.")

# Cleanup
cv2.destroyAllWindows()
