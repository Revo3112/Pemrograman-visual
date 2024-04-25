from tkinter import *
from tkinter import messagebox

class RestaurantApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemesanan Makanan")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.menu_label = Label(self.master, text="Menu Pilihan", font=("Arial", 14))
        self.menu_label.pack(pady=(10, 5))

        self.food_var1 = IntVar()
        self.food_var2 = IntVar()
        self.food_var3 = IntVar()
        self.food_var4 = IntVar()

        self.food_checkbox1 = Checkbutton(self.master, text="Nasi Goreng", variable=self.food_var1)
        self.food_checkbox1.pack(anchor=W)

        self.food_checkbox2 = Checkbutton(self.master, text="Mie Goreng", variable=self.food_var2)
        self.food_checkbox2.pack(anchor=W)

        self.food_checkbox3 = Checkbutton(self.master, text="Ayam Goreng", variable=self.food_var3)
        self.food_checkbox3.pack(anchor=W)

        self.food_checkbox4 = Checkbutton(self.master, text="Sate Ayam", variable=self.food_var4)
        self.food_checkbox4.pack(anchor=W)

        self.order_button = Button(self.master, text="Pesan", command=self.place_order)
        self.order_button.pack(pady=10)

    def place_order(self):
        ordered_items = []
        if self.food_var1.get() == 1:
            ordered_items.append("Nasi Goreng")
        if self.food_var2.get() == 1:
            ordered_items.append("Mie Goreng")
        if self.food_var3.get() == 1:
            ordered_items.append("Ayam Goreng")
        if self.food_var4.get() == 1:
            ordered_items.append("Sate Ayam")

        if ordered_items:
            order_summary = ", ".join(ordered_items)
            messagebox.showinfo("Info", f"Pesanan Anda: {order_summary}")
        else:
            messagebox.showwarning("Peringatan", "Silakan pilih makanan terlebih dahulu.")

if __name__ == "__main__":
    root = Tk()
    app = RestaurantApp(root)
    root.mainloop()
