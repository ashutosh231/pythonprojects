from tkinter import Tk, filedialog, Label, Button, Entry
from PIL import Image
import os

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer by File Size")

        # Create and place widgets
        Label(root, text="Target File Size (KB):").grid(row=0, column=0, padx=10, pady=10)
        
        self.size_entry = Entry(root)
        self.size_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.select_button = Button(root, text="Select Image", command=self.select_image)
        self.select_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.resize_button = Button(root, text="Resize Image", command=self.resize_image)
        self.resize_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.image_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            print(f"Selected image: {self.image_path}")

    def resize_image(self):
        if not self.image_path:
            print("No image selected.")
            return
        
        target_size_kb = float(self.size_entry.get())
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

        if output_path:
            try:
                self.resize_image_to_target_size(self.image_path, output_path, target_size_kb)
            except Exception as e:
                print(f"An error occurred: {e}")

    def resize_image_to_target_size(self, input_path, output_path, target_size_kb):
        try:
            with Image.open(input_path) as img:
                quality = 95  # Start with high quality
                step = 5       # Quality step to decrease
                min_quality = 10  # Minimum quality threshold
                target_size_bytes = target_size_kb * 1024
                
                while quality >= min_quality:
                    img.save(output_path, quality=quality)
                    file_size = os.path.getsize(output_path)
                    if file_size <= target_size_bytes:
                        print(f"Image saved with quality={quality}. File size: {file_size / 1024:.2f} KB")
                        return
                    
                    quality -= step
                
                print(f"Image saved with minimum quality={min_quality}. Final file size: {file_size / 1024:.2f} KB")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    app = ImageResizerApp(root)
    root.mainloop()
