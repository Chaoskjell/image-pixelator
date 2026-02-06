"""
Image Pixelator GUI Application
A user-friendly graphical interface for the Image Pixelator tool.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading
import sys
from PIL import Image, ImageTk
import io

# Import the pixelator class
from image_pixelator import ImagePixelator


class PixelatorGUI:
    """GUI Application for Image Pixelator."""
    
    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.root.title("Image Pixelator - Binary Pattern Filter")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.block_size = tk.IntVar(value=10)
        self.pattern = tk.StringVar(value='checkerboard')
        self.is_processing = False
        self.pixelator = None
        
        self._build_gui()
        self._configure_styles()
    
    def _configure_styles(self):
        """Configure ttk styles."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button style
        style.configure('Accent.TButton',
                       foreground='white',
                       background='#0078d4')
    
    def _build_gui(self):
        """Build the GUI components."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🖼️  Image Pixelator", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # --- Input Section ---
        input_frame = ttk.LabelFrame(main_frame, text="Input Image", padding="10")
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        input_frame.columnconfigure(1, weight=1)
        
        ttk.Label(input_frame, text="Select Image:").grid(row=0, column=0, sticky=tk.W, padx=5)
        ttk.Entry(input_frame, textvariable=self.input_path, state='readonly', width=50).grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
        ttk.Button(input_frame, text="Browse", command=self._select_input).grid(row=0, column=2, padx=5)
        
        ttk.Label(input_frame, text="Image Info:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        self.info_label = ttk.Label(input_frame, text="No image selected", foreground='gray')
        self.info_label.grid(row=1, column=1, columnspan=2, sticky=tk.W, padx=5, pady=(5, 0))
        
        # --- Settings Section ---
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.grid(row=1, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        
        # Block size
        ttk.Label(settings_frame, text="Block Size:").grid(row=0, column=0, sticky=tk.W, pady=5)
        block_frame = ttk.Frame(settings_frame)
        block_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.size_spin = ttk.Spinbox(block_frame, from_=1, to=100, textvariable=self.block_size, width=5)
        self.size_spin.grid(row=0, column=0)
        ttk.Label(block_frame, text="px").grid(row=0, column=1, padx=5)
        self.size_slider = ttk.Scale(block_frame, from_=1, to=100, variable=self.block_size, orient=tk.HORIZONTAL)
        self.size_slider.grid(row=0, column=2, sticky=(tk.W, tk.E), padx=5)
        block_frame.columnconfigure(2, weight=1)
        
        # Pattern selection
        ttk.Label(settings_frame, text="Pattern:").grid(row=1, column=0, sticky=tk.W, pady=5)
        pattern_combo = ttk.Combobox(settings_frame, textvariable=self.pattern, width=20,
                                     values=['checkerboard', 'diagonal', 'horizontal', 'vertical'],
                                     state='readonly')
        pattern_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Preview checkbox
        self.preview_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(settings_frame, text="Show Preview", variable=self.preview_var,
                       command=self._update_preview).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # --- Preview Section ---
        preview_frame = ttk.LabelFrame(main_frame, text="Preview (Optional)", padding="10")
        preview_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(0, weight=1)
        
        self.preview_label = ttk.Label(preview_frame, text="Enable preview and select an image to see a preview",
                                       foreground='gray', background='white')
        self.preview_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        
        # --- Output Section ---
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="10")
        output_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Save As:").grid(row=0, column=0, sticky=tk.W, padx=5)
        ttk.Entry(output_frame, textvariable=self.output_path, state='readonly', width=50).grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
        ttk.Button(output_frame, text="Browse", command=self._select_output).grid(row=0, column=2, padx=5)
        
        # --- Status/Progress Section ---
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        status_frame.columnconfigure(0, weight=1)
        
        self.status_label = ttk.Label(status_frame, text="Ready", foreground='blue')
        self.status_label.grid(row=0, column=0, sticky=tk.W, padx=5)
        
        self.progress_bar = ttk.Progressbar(status_frame, mode='indeterminate', length=200)
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # --- Button Section ---
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        button_frame.columnconfigure(0, weight=1)
        
        self.process_button = ttk.Button(button_frame, text="▶ Process Image", command=self._process)
        self.process_button.grid(row=0, column=0, padx=5, sticky=tk.W)
        
        ttk.Button(button_frame, text="Reset", command=self._reset).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).grid(row=0, column=2, padx=5, sticky=tk.E)
    
    def _select_input(self):
        """Select input image file."""
        filename = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                      ("All files", "*.*")]
        )
        
        if filename:
            self.input_path.set(filename)
            self._update_image_info()
            self._set_default_output()
            if self.preview_var.get():
                self._update_preview()
    
    def _update_image_info(self):
        """Update image information display."""
        try:
            input_file = Path(self.input_path.get())
            if input_file.exists():
                img = Image.open(input_file)
                size_mb = input_file.stat().st_size / (1024 * 1024)
                self.info_label.config(
                    text=f"{input_file.name} | {img.width}×{img.height} | {size_mb:.2f} MB",
                    foreground='green'
                )
            else:
                self.info_label.config(text="File not found", foreground='red')
        except Exception as e:
            self.info_label.config(text=f"Error: {str(e)}", foreground='red')
    
    def _set_default_output(self):
        """Set default output path based on input."""
        if self.input_path.get():
            input_file = Path(self.input_path.get())
            output_file = input_file.parent / f"output_{self.pattern.get()}.png"
            self.output_path.set(str(output_file))
    
    def _select_output(self):
        """Select output file path."""
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"),
                      ("JPEG files", "*.jpg"),
                      ("All files", "*.*")]
        )
        if filename:
            self.output_path.set(filename)
    
    def _update_preview(self):
        """Update preview image."""
        if not self.preview_var.get():
            self.preview_label.config(image='', text="Preview disabled")
            return
        
        if not self.input_path.get():
            self.preview_label.config(image='', text="Please select an input image first",
                                     foreground='gray')
            return
        
        try:
            self.status_label.config(text="Loading preview...", foreground='blue')
            self.root.update()
            
            img = Image.open(self.input_path.get())
            
            # Resize for preview
            max_size = (250, 300)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img)
            self.preview_label.config(image=photo, text='')
            self.preview_label.image = photo  # Keep a reference
            
            self.status_label.config(text="Ready", foreground='blue')
        except Exception as e:
            self.preview_label.config(image='', text=f"Error loading preview: {str(e)}",
                                     foreground='red')
            self.status_label.config(text=f"Error: {str(e)}", foreground='red')
    
    def _process(self):
        """Process the image."""
        # Validation
        if not self.input_path.get():
            messagebox.showerror("Error", "Please select an input image")
            return
        
        if not Path(self.input_path.get()).exists():
            messagebox.showerror("Error", "Input file not found")
            return
        
        if not self.output_path.get():
            messagebox.showerror("Error", "Please select an output path")
            return
        
        # Disable button and start processing
        self.process_button.config(state='disabled')
        self.is_processing = True
        self.progress_bar.start()
        self.status_label.config(text="Processing...", foreground='orange')
        self.root.update()
        
        # Run in thread to prevent freezing
        thread = threading.Thread(target=self._process_thread)
        thread.start()
    
    def _process_thread(self):
        """Run processing in background thread."""
        try:
            # Create pixelator and process
            pixelator = ImagePixelator(
                block_size=self.block_size.get(),
                pattern=self.pattern.get()
            )
            pixelator.load_image(self.input_path.get())
            pixelator.process()
            pixelator.save(self.output_path.get())
            
            # Update UI in main thread
            self.root.after(0, self._process_complete, True, "Image processed successfully!")
        except Exception as e:
            self.root.after(0, self._process_complete, False, str(e))
    
    def _process_complete(self, success, message):
        """Called when processing completes."""
        self.progress_bar.stop()
        self.process_button.config(state='normal')
        self.is_processing = False
        
        if success:
            self.status_label.config(text="✓ Complete!", foreground='green')
            messagebox.showinfo("Success", message)
            if self.preview_var.get():
                self._update_preview()
        else:
            self.status_label.config(text="✗ Error", foreground='red')
            messagebox.showerror("Error", f"Processing failed:\n{message}")
    
    def _reset(self):
        """Reset all settings."""
        self.input_path.set('')
        self.output_path.set('')
        self.block_size.set(10)
        self.pattern.set('checkerboard')
        self.preview_var.set(False)
        self.info_label.config(text="No image selected", foreground='gray')
        self.preview_label.config(image='', text="Enable preview and select an image to see a preview",
                                 foreground='gray')
        self.status_label.config(text="Ready", foreground='blue')


def main():
    """Main entry point."""
    root = tk.Tk()
    app = PixelatorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
