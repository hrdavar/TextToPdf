import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF

def convert_to_pdf():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warming", "No text has been entered.!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save PDF"
    )
    if not file_path:
        return
    
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Vazir", "", "Vazirmatn-Regular.ttf")
        pdf.set_font("Vazir", size=12)
        pdf.set_text_shaping(True)
        pdf.multi_cell(0, 8, text)
        pdf.output(file_path)
        messagebox.showinfo("successful", f"saved:\n{file_path}")
    except Exception as e:
        messagebox.showerror("ERROR", str(e))


root = tk.Tk()
root.title("Text To PDF")
root.geometry("500x700")

tk.Label(root, text="enter your text:", font=("Tahoma", 11)).pack(pady=5)

text_box = tk.Text(root, wrap="word", font=("Tahoma", 11))
text_box.pack(fill="both", expand=True, padx=10, pady=5)

btn = tk.Button(root, text="Convert PDF", command=convert_to_pdf,
                font=("Tahoma", 11), bg="#4CAF50", fg="white", padx=20, pady=5)
btn.pack(pady=10)

root.mainloop()