import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import os
from datetime import datetime

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Enter Data for QR Code", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.data_entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.data_entry.pack(pady=10)

        self.generate_btn = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code,
                                      font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.generate_btn.pack(pady=10)

        self.qr_display = tk.Label(root, bg="#f0f0f0")
        self.qr_display.pack(pady=10)

    def generate_qr_code(self):
        data = self.data_entry.get()
        if not data:
            messagebox.showwarning("Input Required", "Please enter some data to generate QR code.")
            return

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Create 'qr_codes' folder if not exists
        output_dir = "qr_codes"
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"qr_{timestamp}.png"
        img_path = os.path.join(output_dir, filename)
        img.save(img_path)

        self.show_qr_code(img_path)

    def show_qr_code(self, path):
        img = Image.open(path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        qr_img = ImageTk.PhotoImage(img)
        self.qr_display.config(image=qr_img)
        self.qr_display.image = qr_img


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
