Image Pixelator with Binary Pattern Filter

A Python-based image processing tool that transforms images into stylized pixel art using structured binary patterns.

This project combines classical pixelation with algorithmic pattern overlays while preserving the original color composition of the image.

Overview

Image Pixelator converts an input image into square blocks of configurable size.
For each block, the average RGB color is applied to a binary pattern (1/0 matrix), producing an abstracted, geometric representation of the original image.

The application includes:

Graphical User Interface (GUI)

Command-Line Interface (CLI)

Configurable block size

Multiple pattern types

Support for common image formats

## Features

- Adjustable pixel block size
- Binary pattern rendering:
  - checkerboard
  - diagonal
  - horizontal
  - vertical
- Average color preservation per block
- CLI support for automation and scripting
- GUI for simplified usage
- Modular and readable Python implementation

Installation

Clone the repository:
```bash
git clone https://github.com/Chaoskjell/image-pixelator.git
cd image-pixelator
```

Install required dependencies:
```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.8 or higher
- Pillow (PIL)
- OpenCV (cv2)
- NumPy

Usage
Graphical Interface (GUI)

Run the GUI:
```bash

python gui_pixelator.py
```


Features:

Select an image

Choose block size

Select a pattern

Export the processed image

Command-Line Interface (CLI)

Basic usage:
```bash
python image_pixelator.py input.jpg
```


With parameters:
```bash

python image_pixelator.py input.jpg -b 20 -p diagonal -o output.png
```

CLI Parameters
| Parameter       | Short | Description               | Default       |
|-----------------|-------|---------------------------|---------------|
| input           | —     | Input image path (required) | —             |
| --block-size    | -b    | Size of square blocks       | 10            |
| --pattern       | -p    | Pattern type               | checkerboard  |
| --output        | -o    | Output file name           | output.png    |

checkerboard – classic alternating blocks

diagonal – diagonal stripes

horizontal – horizontal lines

vertical – vertical lines

Binary pattern rules:

1 → filled with block’s average color

0 → empty/white

How It Works

Load image and convert to RGB format.

Divide image into square blocks (block_size × block_size).

Compute the average RGB value for each block.

Apply the selected binary pattern to each block.

Save the final image in the specified format.

Example
```bash

# Checkerboard pattern with 15x15 blocks
python image_pixelator.py photo.jpg -b 15 -p checkerboard -o result.png

# Diagonal pattern with larger blocks
python image_pixelator.py photo.jpg -b 20 -p diagonal -o stylized.png
```

Project Structure
```bash

image-pixelator/
│
├── image_pixelator.py      # CLI version
├── gui_pixelator.py        # GUI version
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## Performance Considerations

- Small block sizes (5-10): high detail, slower processing
- Medium block sizes (15-25): balanced detail and speed
- Large block sizes (30+): abstracted, fast processing

Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Open a Pull Request

Please keep code clean, documented, and modular.

License

This project is licensed under the MIT License.
