import tkinter as tk
from tkinter import Button, messagebox

root = tk.Tk()
root.configure(bg='black')  # Set background color to black

#===================================================================================
#------------------------- Membuat Canvas -----------------------------------------
#===================================================================================

canvas = tk.Canvas(root, width=1920, height=1200, bg='black')
canvas.pack()

#===================================================================================
#------------------------- Membuat Frame Utama ------------------------------------
#===================================================================================

main_frame = tk.Frame(canvas, bg='#1e1e1e', padx=20, pady=20)  # Dark gray background
main_frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

# #===================================================================================
# #------------------------- Membuat Button di Frame Utama --------------------------
# #===================================================================================

# button = Button(main_frame, text='Click Me', bg='#db4437', fg='white', font=('Arial', 14, 'bold'))  # Google Red color for button
# button.pack()

#===================================================================================
#------------------------- Membuat Frame Kedua ------------------------------------
#===================================================================================

second_frame = tk.Frame(main_frame, bg='#2d2d2d', padx=20, pady=20)  # Dark gray background
second_frame.place(relheight=0.15, relwidth=0.3, relx=0.35)

#===================================================================================
#------------------------- Membuat Frame Ketiga -----------------------------------
#===================================================================================

third_frame = tk.Frame(second_frame, bg='#2d2d2d', pady=5)  # Dark gray background
third_frame.pack(side=tk.TOP)

#===================================================================================
#------------------------- Membuat Entry ------------------------------------------
#===================================================================================

entry = tk.Entry(third_frame, bg='#ffffff', width=20, fg='black', font=('Arial', 12))  # White background for entry
entry.pack(side=tk.RIGHT)

#===================================================================================
#------------------------- Membuat Label di Samping Entry --------------------------
#===================================================================================

label = tk.Label(third_frame, text='Nama', bg='#2d2d2d', fg='#ffffff', font=('Arial', 12))  # Dark gray background and white text color
label.pack(side=tk.LEFT)

#===================================================================================
#------------------------- Membuat Frame Keempat ----------------------------------
#===================================================================================

fourth_frame = tk.Frame(main_frame, bg='#2d2d2d', pady=5)  # Dark gray background
fourth_frame.place(relheight=0.15, relwidth=0.3, relx=0.35, rely=0.2)

#===================================================================================
#------------------------- Membuat ListBox -----------------------------------------
#===================================================================================

listbox = tk.Listbox(fourth_frame, bg='#ffffff', width=20, fg='black', font=('Arial', 12), justify='left')  # White background for listbox
listbox.pack(side=tk.TOP)

#===================================================================================
#------------------------- Membuat Fungsi Tombol ----------------------------------
#===================================================================================

count_clicked = 0

def clicked():
    global count_clicked
    text = entry.get()
    listbox.insert(count_clicked, text)
    count_clicked += 1
    messagebox.showinfo("Info", "Data berhasil ditambahkan")

def delete_selected():
    text = entry.get()
    items = listbox.get(0, tk.END)
    for i, item in enumerate(items):
        if item == text:
            listbox.delete(i)
            break
    messagebox.showinfo("Info", "Data berhasil dihapus")

#===================================================================================
#------------------------- Membuat Tombol di Frame --------------------------------
#===================================================================================

menu_button = tk.Menubutton(second_frame, text="Menu", relief="raised", bg='#2d2d2d', fg='#ffffff', font=('Arial', 12))  # Dark gray background and white text color
menu_button.pack(side=tk.BOTTOM)

menu = tk.Menu(menu_button, tearoff=0)
menu_button["menu"] = menu

menu.add_command(label="Tambah", command=clicked)
menu.add_command(label="Hapus", command=delete_selected)

#===================================================================================
#------------------------- Menampilkan GUI -----------------------------------------
#===================================================================================

root.mainloop()