from tkinter import *

class ColorButtons:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Buttons")
        self.master.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self.master)
        self.frame.pack()

        self.red_button = Button(self.frame, text="Red", fg="red", font=("Arial", 12), padx=10, pady=5, command=lambda: self.change_color("red"))
        self.red_button.pack(side=LEFT, padx=5)

        self.green_button = Button(self.frame, text="Green", fg="green", font=("Arial", 12), padx=10, pady=5, command=lambda: self.change_color("green"))
        self.green_button.pack(side=LEFT, padx=5)

        self.blue_button = Button(self.frame, text="Blue", fg="blue", font=("Arial", 12), padx=10, pady=5, command=lambda: self.change_color("blue"))
        self.blue_button.pack(side=LEFT, padx=5)

        self.black_button = Button(self.master, text="Black", fg="black", font=("Arial", 12), padx=10, pady=5, command=lambda: self.change_color("black"))
        self.black_button.pack(side=BOTTOM, pady=10)

    def change_color(self, color):
        self.master.configure(bg=color)

if __name__ == "__main__":
    root = Tk()
    app = ColorButtons(root)
    root.mainloop()
