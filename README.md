Image Pixelator with Binary Pattern Filter 🟦🟧

A Python program that converts images into pixelated blocks filled with binary (1/0) patterns.
Each block is colored using the average color of the region and filled with patterns such as checkerboard, diagonal, horizontal, or vertical stripes.

✨ Features

Multiple patterns: checkerboard, diagonal, horizontal, vertical

Configurable block size: adjust the size of the pixel blocks

Both GUI and CLI: user-friendly graphical interface + command line support

Color retention: preserves the original colors by calculating average block color

Fully documented and structured for GitHub

🧩 Requirements

Python 3.8+

Pillow (PIL) — image processing

OpenCV (cv2) — image processing

NumPy — numerical computations

Please refer to requirements.txt for exact versions.

🚀 Installation

Clone the repository and install dependencies:

# Clone the repo
git clone https://github.com/Chaoskjell/image-pixelator.git
cd image-pixelator

# Install dependencies
pip install -r requirements.txt


Alternatively, download the ZIP and open it in a code editor like VS Code — just make sure all dependencies are installed.

📌 Usage
🖥️ Start the GUI (simple)
python gui_pixelator.py

📟 Use the CLI (advanced)

Basic usage:

python image_pixelator.py input.jpg


With options:

python image_pixelator.py input.jpg -b 15 -p diagonal -o output.png

🧠 CLI Parameters
Parameter	Short	Description	Default
input	-	Path to input image (required)	—
--block-size	-b	Size of pixel blocks	10
--pattern	-p	Pattern type	checkerboard
--output	-o	Output file path	output.png
🎨 Available Patterns

checkerboard — classic checker pattern

diagonal — diagonal stripes

horizontal — horizontal lines

vertical — vertical lines

📷 Examples
# Run GUI
python gui_pixelator.py

# CLI: Checkerboard with 10x10 blocks
python image_pixelator.py photo.jpg -b 10 -p checkerboard -o output.png

# CLI: Diagonal pattern with larger blocks
python image_pixelator.py photo.jpg -b 20 -p diagonal -o diagonal.png
``` :contentReference[oaicite:5]{index=5}

---

## 🔍 How It Works

1. **Load** — input image is loaded and converted to RGB  
2. **Block Division** — the image is split into `block_size × block_size` blocks  
3. **Color Calculation** — average color is calculated for each block  
4. **Pattern Draw** — the chosen pattern is drawn using:
   * `1` = filled cell with average color  
   * `0` = empty cell (white)  
5. **Save** — the final image is saved as PNG/JPG :contentReference[oaicite:6]{index=6}

---

## 📦 Supported Image Formats

- PNG  
- JPG/JPEG  
- BMP  
- GIF  
- TIFF :contentReference[oaicite:7]{index=7}

---

## ⚡ Performance

- Smaller blocks (5–15): moderate speed with good detail  
- Medium blocks (15–25): faster with less detail  
- Large blocks (25+): very fast with minimal detail :contentReference[oaicite:8]{index=8}

---

## 🧠 Contributing

Contributions are welcome!  
Please see `CONTRIBUTING.md` for details on reporting bugs, opening issues, or submitting pull requests. :contentReference[oaicite:9]{index=9}

---

## 📞 Contact

If you have questions or problems, feel free to open an issue on GitHub. :contentReference[oaicite:10]{index=10}

---

## ❤️ About

Made with ❤️ in Python.  
MIT Licensed — free for personal and commercial use. :contentReference[oaicite:11]{index=11}

---

Wenn du möchtest, kann ich dir die **README auch automatisch als Markdown-Datei** formatieren (z. B. mit TOC, Badges etc.) oder anpassen (z. B. Projektbeschreibung erweitern).
::contentReference[oaicite:12]{index=12}
