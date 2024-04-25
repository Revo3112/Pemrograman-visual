import tkinter as tk
from tkinter import Button, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced GUI")
        self.geometry("800x600")
        self.configure(bg='#1e1e1e')

        self.main_frame = tk.Frame(self, bg='#1e1e1e')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.create_widgets()

    def create_widgets(self):
        # Entry and Label
        entry_frame = tk.Frame(self.main_frame, bg='#2d2d2d')
        entry_frame.pack(pady=(0, 20))

        label = tk.Label(entry_frame, text='Nama', bg='#2d2d2d', fg='#ffffff', font=('Arial', 12))
        label.pack(side=tk.LEFT, padx=(20, 10))

        self.entry = tk.Entry(entry_frame, bg='#ffffff', fg='black', font=('Arial', 12))
        self.entry.pack(side=tk.LEFT, padx=(0, 20), ipady=5, fill=tk.X, expand=True)

        # ListBox
        listbox_frame = tk.Frame(self.main_frame, bg='#2d2d2d')
        listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(listbox_frame, bg='#ffffff', fg='black', font=('Arial', 12), justify='left')
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Buttons
        button_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        button_frame.pack()

        add_button = Button(button_frame, text="Tambah", command=self.clicked, bg='#007bff', fg='white', font=('Arial', 12))
        add_button.pack(side=tk.LEFT, padx=(0, 10))

        delete_button = Button(button_frame, text="Hapus", command=self.delete_selected, bg='#dc3545', fg='white', font=('Arial', 12))
        delete_button.pack(side=tk.LEFT)

    def clicked(self):
        text = self.entry.get()
        if text:
            self.listbox.insert(tk.END, text)
            messagebox.showinfo("Info", "Data berhasil ditambahkan")
        else:
            messagebox.showerror("Error", "Mohon masukkan teks.")

    def delete_selected(self):
        found = False
        text = self.entry.get()
        items = self.listbox.get(0, tk.END)
        for i, item in enumerate(items):
            if item == text:
                self.listbox.delete(i)
                found = True
                break
        if found:
            messagebox.showinfo("Info", "Data berhasil dihapus")
        else:
            messagebox.showerror("Error", "Tidak ada item yang dipilih.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
