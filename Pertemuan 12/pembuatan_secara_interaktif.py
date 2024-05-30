import tkinter as tk

def tombol_ditekan():
    teks = entryku.get()
    print(teks)

root = tk.Tk()

frameku = tk.Frame(root, bg='blue')
frameku.place(relwidth=0.8, relheight=0.8)

tombolku = tk.Button(frameku, text="Tes Tombol", bg='gray', fg='red', command=tombol_ditekan)
tombolku.pack()

entryku = tk.Entry(frameku, bg='green')
entryku.pack()

root.mainloop()
