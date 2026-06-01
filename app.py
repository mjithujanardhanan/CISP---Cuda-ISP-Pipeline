import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("1200x1000")

        # Path input
        path_frame = tk.Frame(root)
        path_frame.pack(pady=10, fill="x")

        tk.Label(path_frame, text="Image Path:").pack(side="left", padx=5)

        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(path_frame, textvariable=self.path_var, width=80)
        self.path_entry.pack(side="left", padx=5, expand=True, fill="x")

        tk.Button(
            path_frame,
            text="Load Image",
            command=self.load_image
        ).pack(side="left", padx=5)

        # Checkbox grid (3 rows x 3 columns)
        checkbox_frame = tk.LabelFrame(root, text="Options")
        checkbox_frame.pack(side="left",padx=5)

        checkbox_vars = []

        for row in range(3):
            for col in range(3):
                var = tk.BooleanVar()
                checkbox_vars.append(var)

                cb = tk.Checkbutton(
                    checkbox_frame,
                    text=f"Option {row*3 + col + 1}",
                    variable=var
                )

                cb.grid(row=row, column=col, padx=10, pady=5, sticky="w")

        # Image display area
        self.image_label = tk.Label(root)
        self.image_label.pack(expand=True)

        self.tk_image = None

    def load_image(self):
        path = self.path_var.get().strip()

        try:
            image = Image.open(path)

            # Resize image to fit window while maintaining aspect ratio
            image.thumbnail((800, 500))

            self.tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.tk_image)

        except Exception as e:
            messagebox.showerror("Error", f"Could not load image:\n{e}")


root = tk.Tk()
app = ImageViewer(root)
root.mainloop()