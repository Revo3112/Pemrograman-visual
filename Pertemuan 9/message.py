from tkinter import *

class MessageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Message App")
        self.master.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.master, text="Hey!? How are you doing?", font=("Arial", 14), relief=RAISED, padx=20, pady=20)
        self.label.pack(expand=True, fill=BOTH)

if __name__ == "__main__":
    root = Tk()
    app = MessageApp(root)
    root.mainloop()
