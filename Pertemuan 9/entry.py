from tkinter import *

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = Label(self.master, text="Selamat Datang", font=("Helvetica", 20))
        self.title_label.pack(pady=(20, 10))

        self.username_label = Label(self.master, text="Username", font=("Arial", 12))
        self.username_label.pack()

        self.username_entry = Entry(self.master, font=("Arial", 12), bd=3)
        self.username_entry.pack()

        self.password_label = Label(self.master, text="Password", font=("Arial", 12))
        self.password_label.pack()

        self.password_entry = Entry(self.master, font=("Arial", 12), bd=3, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.master, text="Login", font=("Arial", 12), command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check username and password
        # For demonstration, let's just print them
        print("Username:", username)
        print("Password:", password)

if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
