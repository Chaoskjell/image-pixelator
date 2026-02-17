🎨 Image Pixelator with Binary Pattern Filters

Transform images into stylized pixel art using customizable binary pattern overlays.

Image Pixelator is a Python-based tool that converts images into pixelated blocks filled with structured binary patterns (1/0). Each block preserves the original image’s color by calculating the average RGB value, while applying artistic patterns such as checkerboards or stripes.

📑 Table of Contents

Introduction

Features

Installation

Usage

CLI Arguments

Available Patterns

How It Works

Examples

Dependencies

Project Structure

Troubleshooting

Contributing

License

📌 Introduction

Image Pixelator is a lightweight yet powerful image processing tool designed for:

Creative pixel-art generation

Pattern-based image abstraction

Educational purposes (image processing concepts)

Experimental visual design

It provides both:

🖥️ A graphical user interface (GUI)

💻 A command-line interface (CLI)

✨ Features

✔ Pixelation with adjustable block size
✔ Multiple binary pattern overlays
✔ Average color preservation per block
✔ GUI for beginners
✔ CLI for advanced users & automation
✔ Clean, modular Python structure
✔ Supports common image formats

🚀 Installation
1️⃣ Clone the Repository
git clone https://github.com/Chaoskjell/image-pixelator.git
cd image-pixelator

2️⃣ Install Dependencies
pip install -r requirements.txt

🐍 Requirements

Python 3.8+

pip

🖥️ Usage
Start the GUI (Recommended for Beginners)
python gui_pixelator.py

Use the CLI (Advanced)

Basic usage:

python image_pixelator.py input.jpg


With custom parameters:

python image_pixelator.py input.jpg -b 20 -p diagonal -o output.png

⚙ CLI Arguments
Argument	Short	Description	Default
input	—	Path to input image (required)	—
--block-size	-b	Size of pixel blocks	10
--pattern	-p	Pattern type	checkerboard
--output	-o	Output file name	output.png
🎨 Available Patterns

checkerboard – classic alternating pattern

diagonal – diagonal stripes

horizontal – horizontal lines

vertical – vertical lines

🧠 How It Works

Load Image
The image is opened and converted to RGB.

Divide into Blocks
The image is segmented into square blocks (block_size × block_size).

Calculate Average Color
Each block’s mean RGB value is computed.

Apply Binary Pattern
The selected pattern determines which pixels are:

1 → filled with average block color

0 → white (or empty)

Save Output
The processed image is exported in the chosen format.

🖼️ Examples
# Small detailed blocks
python image_pixelator.py photo.jpg -b 8 -p checkerboard -o detailed.png

# Medium abstraction
python image_pixelator.py photo.jpg -b 20 -p diagonal -o stylized.png

# Large abstract blocks
python image_pixelator.py photo.jpg -b 40 -p vertical -o abstract.png

📦 Dependencies

Pillow (PIL)

OpenCV (cv2)

NumPy

See requirements.txt for exact versions.

📁 Project Structure
image-pixelator/
│
├── image_pixelator.py      # CLI version
├── gui_pixelator.py        # GUI version
├── requirements.txt        # Dependencies
└── README.md

⚡ Performance Notes

Small block sizes (5–10) → More detail, slower processing

Medium block sizes (15–25) → Balanced performance

Large block sizes (30+) → Fast, highly abstract results

🛠 Troubleshooting

ModuleNotFoundError?
→ Make sure all dependencies are installed:

pip install -r requirements.txt


Image not saving?
→ Check file path and permissions.

GUI not launching?
→ Ensure Python 3.8+ is installed and accessible via python.

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Open a Pull Request

Please keep code clean, documented, and modular.

📄 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it for personal and commercial purposes.

❤️ Acknowledgment

Built with Python for creative image experimentation.
