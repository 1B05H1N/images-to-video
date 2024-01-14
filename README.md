# Image to Video Converter

This Python script allows you to create a video by combining multiple images from a folder. The script reads image files (with supported extensions) from the "images" folder and converts them into a video.

## Prerequisites

- Python (3.6 or higher)
- OpenCV (`cv2` Python module)

## Usage

1. Place the image files you want to include in the video in the "images" folder.

2. Run the `image_to_video.py` script using Python.

   ```shell
   python image_to_video.py
   ```

3. The script will create a video named `output_video.mp4` in the same directory.

## Customization

- Supported image extensions can be customized in the script by modifying the `supported_extensions` list.

## Example

Here's an example directory structure:

```
project_directory/
│
├── images/
│   ├── image1.jpg
│   ├── image2.png
│   ├── image3.heic
│   └── ...
│
├── image_to_video.py
│
└── output_video.mp4
```

In this example, the script will create a video (`output_video.mp4`) by combining all image files with supported extensions from the "images" folder.
