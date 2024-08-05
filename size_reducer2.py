from tkinter import Tk, filedialog, Label, Button, Entry
from PIL import Image

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")

        # Create and place widgets
        Label(root, text="Width:").grid(row=0, column=0, padx=10, pady=10)
        Label(root, text="Height:").grid(row=1, column=0, padx=10, pady=10)
        
        self.width_entry = Entry(root)
        self.width_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.height_entry = Entry(root)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.select_button = Button(root, text="Select Image", command=self.select_image)
        self.select_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.resize_button = Button(root, text="Resize Image", command=self.resize_image)
        self.resize_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.image_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            print(f"Selected image: {self.image_path}")

    def resize_image(self):
        if not self.image_path:
            print("No image selected.")
            return
        
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

        if output_path:
            try:
                with Image.open(self.image_path) as img:
                    resized_img = img.resize((width, height))
                    resized_img.save(output_path)
                    print(f"Image resized and saved to {output_path}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    app = ImageResizerApp(root)
    root.mainloop()
