"""
Image Pixelator with Binary Pattern Filter
A tool to convert images into pixelated blocks filled with 1/0 patterns in their respective colors.
Perfect for creating artistic, retro-looking images with binary patterns.
"""

import argparse
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys


class ImagePixelator:
    """Convert images to pixelated blocks with binary (1/0) patterns."""
    
    def __init__(self, block_size=10, pattern='checkerboard'):
        """
        Initialize the pixelator.
        
        Args:
            block_size (int): Size of each pixel block in pixels
            pattern (str): Pattern type ('checkerboard', 'diagonal', 'horizontal')
        """
        self.block_size = block_size
        self.pattern = pattern.lower()
        self.valid_patterns = ['checkerboard', 'diagonal', 'horizontal', 'vertical']
        
        if self.pattern not in self.valid_patterns:
            raise ValueError(f"Invalid pattern. Choose from: {', '.join(self.valid_patterns)}")
    
    def load_image(self, image_path):
        """Load an image from file."""
        try:
            self.image = Image.open(image_path).convert('RGB')
            print(f"✓ Image loaded: {image_path}")
            print(f"  Size: {self.image.width}x{self.image.height}")
            return self.image
        except Exception as e:
            print(f"✗ Error loading image: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _get_pattern_pixel(self, x, y):
        """
        Get pattern value for a coordinate.
        
        Returns:
            bool: True for "1", False for "0"
        """
        if self.pattern == 'checkerboard':
            return (x + y) % 2 == 0
        elif self.pattern == 'diagonal':
            return (x - y) % 2 == 0
        elif self.pattern == 'horizontal':
            return y % 2 == 0
        elif self.pattern == 'vertical':
            return x % 2 == 0
        return True
    
    def _get_block_average_color(self, x1, y1, x2, y2):
        """Calculate average color of a block."""
        block = self.image.crop((x1, y1, x2, y2))
        img_array = np.array(block, dtype=np.float32)
        avg_color = tuple(np.mean(img_array, axis=(0, 1)).astype(int))
        return avg_color
    
    def _fill_block_with_pattern(self, draw, x1, y1, x2, y2, color):
        """
        Fill a block with binary pattern using the given color.
        
        Args:
            draw: PIL ImageDraw object
            x1, y1, x2, y2: Block coordinates
            color: RGB color tuple
        """
        cell_size = max(1, self.block_size // 4)
        
        for x in range(x1, x2, cell_size):
            for y in range(y1, y2, cell_size):
                # Convert to pattern coordinates
                pattern_x = (x - x1) // cell_size
                pattern_y = (y - y1) // cell_size
                
                if self._get_pattern_pixel(pattern_x, pattern_y):
                    # Draw "1" - solid square
                    draw.rectangle(
                        [(x, y), (min(x + cell_size, x2), min(y + cell_size, y2))],
                        fill=color
                    )
                # "0" is represented by empty space (background shows through)
    
    def process(self):
        """Process the image and create pixelated version."""
        output_image = Image.new('RGB', self.image.size, color='white')
        draw = ImageDraw.Draw(output_image)
        
        width, height = self.image.size
        
        # Process each block
        for y in range(0, height, self.block_size):
            for x in range(0, width, self.block_size):
                x2 = min(x + self.block_size, width)
                y2 = min(y + self.block_size, height)
                
                # Get average color
                color = self._get_block_average_color(x, y, x2, y2)
                
                # Fill block with pattern
                self._fill_block_with_pattern(draw, x, y, x2, y2, color)
        
        self.output = output_image
        print(f"✓ Processing complete with pattern: {self.pattern}")
        return output_image
    
    def save(self, output_path):
        """Save the processed image."""
        try:
            self.output.save(output_path)
            print(f"✓ Image saved: {output_path}")
        except Exception as e:
            print(f"✗ Error saving image: {e}", file=sys.stderr)
            sys.exit(1)
    
    def show_info(self):
        """Display information about the processing."""
        width, height = self.image.size
        blocks_x = (width + self.block_size - 1) // self.block_size
        blocks_y = (height + self.block_size - 1) // self.block_size
        
        print("\n📊 Processing Information:")
        print(f"  Block size: {self.block_size}x{self.block_size} pixels")
        print(f"  Pattern: {self.pattern}")
        print(f"  Total blocks: {blocks_x} × {blocks_y} = {blocks_x * blocks_y}")
        print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Convert images to pixelated blocks with binary (1/0) patterns',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python image_pixelator.py input.jpg -b 10 -p checkerboard -o output.jpg
  python image_pixelator.py photo.png -b 15 -p diagonal
        """
    )
    
    parser.add_argument('input', help='Input image path')
    parser.add_argument('-b', '--block-size', type=int, default=10,
                        help='Size of each pixel block (default: 10)')
    parser.add_argument('-p', '--pattern', default='checkerboard',
                        choices=['checkerboard', 'diagonal', 'horizontal', 'vertical'],
                        help='Pattern type (default: checkerboard)')
    parser.add_argument('-o', '--output', help='Output image path (default: output.png)')
    
    args = parser.parse_args()
    
    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"✗ Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Set output path
    output_path = args.output if args.output else f"output_{args.pattern}.png"
    
    # Create and run pixelator
    print(f"🖼️  Image Pixelator with Binary Pattern Filter")
    print("-" * 50)
    
    try:
        pixelator = ImagePixelator(block_size=args.block_size, pattern=args.pattern)
        pixelator.load_image(args.input)
        pixelator.show_info()
        pixelator.process()
        pixelator.save(output_path)
        
        print("-" * 50)
        print("✓ Success!")
        
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
