Image Pixelator with Binary Pattern Filter

A Python-based image processing tool that transforms images into stylized pixel art using structured binary patterns.

This project focuses on combining classical pixelation techniques with algorithmic pattern overlays while preserving the original color composition of the image.

Overview

Image Pixelator converts an input image into square blocks of configurable size.
For each block, the average RGB color is calculated and applied to a binary pattern structure (1/0 matrix).

The result is a clean, abstracted representation of the original image with geometric texture.

The application includes:

A graphical user interface (GUI)

A command-line interface (CLI)

Configurable block size

Multiple pattern types

Support for common image formats

Features

Adjustable pixel block size

Binary pattern rendering (checkerboard, diagonal, horizontal, vertical)

Average color preservation per block

CLI support for automation and scripting

GUI for simplified usage

Modular and readable Python implementation

Installation

Clone the repository:

git clone https://github.com/Chaoskjell/image-pixelator.git
cd image-pixelator


Install required dependencies:

pip install -r requirements.txt

Requirements

Python 3.8+

Pillow (PIL)

OpenCV (cv2)

NumPy

Usage
Graphical Interface

Run:

python gui_pixelator.py


This opens the graphical interface where you can:

Select an image

Choose block size

Select a pattern

Export the processed image

Command Line Interface

Basic usage:

python image_pixelator.py input.jpg


With parameters:

python image_pixelator.py input.jpg -b 20 -p diagonal -o output.png

CLI Parameters
Parameter	Short	Description	Default
input	—	Input image path (required)	—
--block-size	-b	Size of square blocks	10
--pattern	-p	Pattern type	checkerboard
--output	-o	Output file name	output.png
Available Patterns

checkerboard

diagonal

horizontal

vertical

Each pattern uses a binary structure:

1 → colored with block average

0 → white pixel

How It Works

The image is loaded and converted to RGB format.

It is divided into square blocks of size block_size × block_size.

The average RGB value is computed for each block.

A predefined binary matrix determines which pixels inside the block are filled.

The final image is saved in the specified format.

Example
python image_pixelator.py photo.jpg -b 15 -p checkerboard -o result.png

Project Structure
image-pixelator/
│
├── image_pixelator.py
├── gui_pixelator.py
├── requirements.txt
└── README.md

Performance Considerations

Smaller block sizes produce higher detail and require more processing time.

Larger block sizes increase abstraction and improve performance.

Contributing

Contributions and improvements are welcome.
Please open an issue or submit a pull request.

License

This project is licensed under the MIT License.
