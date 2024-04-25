from tkinter import *

class RadioButtonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Radio Button App")
        self.master.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.R1 = Radiobutton(self.master, text="Option 1", variable=var, value=1, command=self.sel, font=("Arial", 12))
        self.R1.pack(anchor=W, pady=5)

        self.R2 = Radiobutton(self.master, text="Option 2", variable=var, value=2, command=self.sel, font=("Arial", 12))
        self.R2.pack(anchor=W, pady=5)

        self.R3 = Radiobutton(self.master, text="Option 3", variable=var, value=3, command=self.sel, font=("Arial", 12))
        self.R3.pack(anchor=W, pady=5)

        self.label = Label(self.master, font=("Arial", 12))
        self.label.pack(pady=10)

    def sel(self):
        selection = "You selected the option " + str(var.get())
        self.label.config(text=selection)

if __name__ == "__main__":
    root = Tk()
    var = IntVar()
    app = RadioButtonApp(root)
    root.mainloop()
