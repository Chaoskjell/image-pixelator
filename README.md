# Image Pixelator with Binary Pattern Filter

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Chaoskjell/image-pixelator)](https://github.com/Chaoskjell/image-pixelator)

**Image Pixelator** is a Python-based tool that transforms images into stylized pixel art using structured binary patterns. It combines classic pixelation with algorithmic pattern overlays while preserving the original color composition of your images.  

## Features

- **Pixel Block Transformation**: Convert images into square blocks of configurable size.  
- **Binary Pattern Rendering**: Apply patterns to each block:
  - Checkerboard  
  - Diagonal  
  - Horizontal  
  - Vertical  
- **Average Color Preservation**: Each block retains the average color of its pixels.  
- **Multiple Interfaces**:
  - Graphical User Interface (GUI) for easy use  
  - Command-Line Interface (CLI) for automation  
- **Supports Common Image Formats**: JPG, PNG, etc.  
- **Modular Python Implementation**: Clean, readable, and easy to extend.  

---

## How It Works

1. Load the image and convert it to RGB format.  
2. Divide the image into square blocks of `block_size × block_size`.  
3. Compute the average RGB color of each block.  
4. Apply the selected binary pattern:  
   - `1` → filled with the block’s average color  
   - `0` → empty (white)  
5. Save the final stylized image.  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Chaoskjell/image-pixelator.git
cd image-pixelator
Install dependencies:

pip install -r requirements.txt
```
Requirements:

-Python 3.8+
-Pillow
-OpenCV
-NumPy

Usage
Graphical Interface (GUI)
Launch the GUI:
```bash

python gui_pixelator.py
```

GUI Features:

-Select an input image
-Choose block size
-Select a binary pattern
-Export the processed image
-Command-Line Interface (CLI)

Basic usage:
```bash

python image_pixelator.py input.jpg
```

With parameters:
```bash

python image_pixelator.py input.jpg -b 20 -p diagonal -o output.png
```

CLI Parameters:

Parameter	Short	Description	Default
input	—	Input image path (required)	—
--block-size	-b	Size of square blocks	10
--pattern	-p	Pattern type (checkerboard, diagonal, horizontal, vertical)	checkerboard
--output	-o	Output file name	output.png
Examples
```bash
# Checkerboard pattern with 15x15 blocks

python image_pixelator.py photo.jpg -b 15 -p checkerboard -o result.png
```

# Diagonal pattern with larger blocks
```bash
python image_pixelator.py photo.jpg -b 20 -p diagonal -o stylized.png
Performance Tips
Small block sizes (5–10 px): High detail, slower processing

Medium block sizes (15–25 px): Balanced detail and speed

Large block sizes (30+ px): Abstracted style, fast processing
```
Project Structure
```bash
image-pixelator/
│
├── image_pixelator.py      # CLI version
├── gui_pixelator.py        # GUI version
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```
Contributing
Contributions are welcome!

Fork the repository
```bash
##Create a feature branch 
git checkout -b feature-name


##Commit your changes
git commit -m "Add feature"

##Push to your branch
git push origin feature-name

Open a Pull Request
```
Please keep the code clean, modular, and well-documented.

License
This project is licensed under the MIT License.


---

✅ **Alles ist GitHub-kompatibel:**  
- Überschriften, Listen, Tabellen, Codeblöcke und Bilder behalten ihre Formatierung.  
- Du kannst direkt den Screenshot-Pfad anpassen (`images/demo.png`).  
- Badges zeigen Python-Version, Lizenz und Repo-Größe an.

Wenn du willst, kann ich als **nächsten Schritt direkt fertige Beispielbilder und Screenshots** einfügen, die den Pixelator in Aktion zeigen – das macht die README noch professioneller und klickbarer.  

Willst du, dass ich das mache?
