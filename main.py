import os
from tkinter import Tk, filedialog, Label, Frame, Entry, StringVar, Toplevel, messagebox
from tkinter.ttk import Button, Style
from PyPDF2 import PdfReader, PdfWriter

class PDFManager:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Manager")
        self.root.geometry("500x400")
        self.root.configure(bg="#f7f7f7")
        self.root.resizable(False, False)
        
        self.style = Style()
        self.style.theme_use('clam')
        self.style.configure("TButton", font=("Helvetica", 12), padding=5, relief="flat", background="#4CAF50", foreground="white")
        self.style.map("TButton", background=[("active", "#45a049")])
        
        self.style.configure("TLabel", font=("Helvetica", 10), background="#f7f7f7", foreground="#333")

        self.create_widgets()

    def create_widgets(self):
        title_label = Label(self.root, text="PDF Manager", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#4CAF50")
        title_label.pack(pady=20)

        frame = Frame(self.root, bg="#f7f7f7")
        frame.pack(pady=20)

        merge_button = Button(frame, text="Merge PDFs", command=self.merge_pdfs, width=20)
        merge_button.grid(row=0, column=0, padx=10, pady=10)

        split_button = Button(frame, text="Split PDF", command=self.split_pdf, width=20)
        split_button.grid(row=0, column=1, padx=10, pady=10)

        annotate_button = Button(frame, text="Annotate PDF", command=self.annotate_pdf, width=20)
        annotate_button.grid(row=1, column=0, padx=10, pady=10)

        encrypt_button = Button(frame, text="Encrypt PDF", command=self.encrypt_pdf, width=20)
        encrypt_button.grid(row=1, column=1, padx=10, pady=10)

        decrypt_button = Button(frame, text="Decrypt PDF", command=self.decrypt_pdf, width=20)
        decrypt_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.status_label = Label(self.root, text="Status: Ready", anchor="center", font=("Helvetica", 10, "italic"), bg="#f7f7f7", fg="#555")
        self.status_label.pack(pady=10)

    def update_status(self, message):
        self.status_label.config(text=f"Status: {message}")

    def merge_pdfs(self):
        file_paths = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF files", "*.pdf")])
        if not file_paths:
            return

        output_path = filedialog.asksaveasfilename(title="Save Merged PDF As", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return

        pdf_writer = PdfWriter()
        for file_path in file_paths:
            pdf_reader = PdfReader(file_path)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        self.update_status("PDFs Merged Successfully")

    def split_pdf(self):
        file_path = filedialog.askopenfilename(title="Select PDF to Split", filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return

        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return

        pdf_reader = PdfReader(file_path)
        for i, page in enumerate(pdf_reader.pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(page)

            output_path = os.path.join(output_dir, f"page_{i + 1}.pdf")
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

        self.update_status("PDF Split Successfully")

    def annotate_pdf(self):
        file_path = filedialog.askopenfilename(title="Select PDF to Annotate", filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return

        output_path = filedialog.asksaveasfilename(title="Save Annotated PDF As", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return

        annotation_text = "This is an annotation."

        pdf_reader = PdfReader(file_path)
        pdf_writer = PdfWriter()
        for page in pdf_reader.pages:
            page.add_annotation({
                'text': annotation_text,
                'x1': 50,
                'y1': 750,
                'x2': 300,
                'y2': 800,
            })
            pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        self.update_status("PDF Annotated Successfully")

    def encrypt_pdf(self):
        file_path = filedialog.askopenfilename(title="Select PDF to Encrypt", filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return

        output_path = filedialog.asksaveasfilename(title="Save Encrypted PDF As", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return

        password_window = Toplevel(self.root)
        password_window.title("Enter Password")
        password_window.geometry("300x150")
        password_window.configure(bg="#f7f7f7")
        password_window.resizable(False, False)

        Label(password_window, text="Enter Password for Encryption:", font=("Helvetica", 10), bg="#f7f7f7", fg="#333").pack(pady=10)
        password_var = StringVar()
        Entry(password_window, textvariable=password_var, show="*", font=("Helvetica", 12)).pack(pady=5)

        def set_password():
            password = password_var.get()
            if password:
                password_window.destroy()
                pdf_reader = PdfReader(file_path)
                pdf_writer = PdfWriter()

                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

                pdf_writer.encrypt(password)

                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)

                self.update_status("PDF Encrypted Successfully")
            else:
                messagebox.showwarning("Warning", "Password cannot be empty.")

        Button(password_window, text="Set Password", command=set_password).pack(pady=10)

    def decrypt_pdf(self):
        file_path = filedialog.askopenfilename(title="Select PDF to Decrypt", filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return

        output_path = filedialog.asksaveasfilename(title="Save Decrypted PDF As", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_path:
            return

        password_window = Toplevel(self.root)
        password_window.title("Enter Password")
        password_window.geometry("300x150")
        password_window.configure(bg="#f7f7f7")
        password_window.resizable(False, False)

        Label(password_window, text="Enter Password for Decryption:", font=("Helvetica", 10), bg="#f7f7f7", fg="#333").pack(pady=10)
        password_var = StringVar()
        Entry(password_window, textvariable=password_var, show="*", font=("Helvetica", 12)).pack(pady=5)

        def verify_password():
            password = password_var.get()
            if password:
                password_window.destroy()
                pdf_reader = PdfReader(file_path)

                if not pdf_reader.decrypt(password):
                    self.update_status("Incorrect Password")
                    return

                pdf_writer = PdfWriter()
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)

                self.update_status("PDF Decrypted Successfully")
            else:
                messagebox.showwarning("Warning", "Password cannot be empty.")

        Button(password_window, text="Verify Password", command=verify_password).pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    pdf_manager = PDFManager(root)
    root.mainloop()
