from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk

# USER ENTRIES
width = 0
height = 0
file_path = ""
nama_file = ""
method = "pixel"

def upload_image():
    global width, height, file_path, nama_file, img_label
    
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("JPG files", "*.jpg"), ("PNG files", "*.png"), ("JPEG files", "*.jpeg")]
    )

    # Membuka gambar menggunakan PIL
    image = Image.open(file_path)
    
    # Mengambil ukuran gambar
    width, height = image.size

    # Memisahkan nama file dari path
    nama_file = file_path.split("/")
    nama_file = nama_file[-1]

    # Convert PIL Image to PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Create a label and add the image to it
    label = Label(img_frame, image=photo)
    label.image = photo  # keep a reference to the image
    label.place(x=400, y=50)

    img = PhotoImage(file=file_path)
    img_label = Label(img_frame, image=img)
    img_label.image = img  # Simpan referensi agar gambar tidak terhapus oleh garbage collector
    img_label.pack()
    
def resize_method():
    global width, height, file_path, nama_file, method

    resized_image = None
    
    if method == "pixel":
        new_width  = int(w_spinbox.get())
        new_height = int(h_spinbox.get())
        resized_image = resize_image_pixel(new_width, new_height)
    elif method == "percent":
        percent = int(w_spinbox.get())
        resize_image_percent()

    # Menyimpan gambar yang telah diresize
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    resized_image.save(save_path)

    # Menampilkan pesan berhasil
    messagebox.show_info("Resize Image", "Image resized and saved successfully!")

def resize_image_pixel(new_width, new_height):
    global file_path, nama_file
    
    image = Image.open(file_path)
    
    # Mengubah ukuran gambar menjadi setengah dari ukuran aslinya
    resized_image = image.resize((new_width, new_height))
    return resized_image

def resize_image_percent(percent):
    global width, height, file_path, nama_file

    new_width(int)
    new_height(int)

    if percent == 25:
        new_width = width - (width * 1/4)
        new_height = height - (height * 1/4)
    elif percent == 50:
        new_width = width - (width * 1/2)
        new_height = height - (height * 1/2)
    elif percent == 75:
        new_width = width - (width * 3/4)
        new_height = height - (height * 3/4)
    
    print("Adjust the size")
    return percent

def set_method(selected_method):
    global method

    method = selected_method

# UI Start
# colors
bg_win_c = "#171717"
bg_frame_c = "#1E1E1E"

# window config
window = Tk()
window.geometry("1920x1200")
window.configure(bg=bg_win_c)
window.title("iHateIMG")

# Top Frame
topbar_frame = Frame(
    window, height=120, 
    width=window.winfo_screenwidth(), 
    background=bg_frame_c
    )
topbar_frame.pack(side=TOP)
# logo image
logo_img = PhotoImage(file='Pertemuan 10/logo.png')
new_img = logo_img.subsample(2, 2)
label_logo = Label(window, image=new_img, bg=bg_frame_c).place(x=40, y=10)
# tools image
tools_img = PhotoImage(file='Pertemuan 10/tools.png')
new_tools_img = tools_img.subsample(2, 2)
tools_img_logo = Label(window, image=new_tools_img, bg=bg_frame_c).place(x=350, y=50)
# support image
support_img = PhotoImage(file='Pertemuan 10/support.png')
new_support_img = support_img.subsample(2, 2)
support_img_logo = Label(window, image=new_support_img, bg=bg_frame_c).place(x=window.winfo_screenwidth() - 210, y=80)

# SideBar Frame
sidebar_frame = Frame(
    window,
    height=window.winfo_screenheight() - 140,
    width=380,
    background=bg_frame_c,
    highlightbackground=bg_win_c,
    highlightthickness=6
    )
sidebar_frame.pack(side=RIGHT)

# resize txt img
resize_img = PhotoImage(file='Pertemuan 10/resize_txt.png').subsample(2,2)
resize_img_lbl = Label(window, image=resize_img, bg=bg_frame_c).place(x=window.winfo_screenwidth() - 300, y=150)

# button pixel
pixel_img = PhotoImage(file='Pertemuan 10/pixel.png').subsample(2,2)
pixel_button = Button(window, image=pixel_img, width=150, height=150, bg=bg_frame_c, command=lambda : set_method("pixel"))
pixel_button.place(x=window.winfo_screenwidth() - 350, y=200)

# button percentage
percent_img = PhotoImage(file='Pertemuan 10/percent.png').subsample(2,2)
percent_button = Button(window, image=percent_img, width=150, height=150, bg=bg_frame_c, command=lambda : set_method("percent"))
percent_button.place(x=window.winfo_screenwidth() - 170, y=200)

# info img
info_img = PhotoImage(file='Pertemuan 10/info.png').subsample(2,2)
info_img_lbl = Label(window, image=info_img, bg=bg_frame_c).place(x=window.winfo_screenwidth() - 300, y=380)

# width img
width_img = PhotoImage(file='Pertemuan 10/width.png').subsample(2,2)
width_img_lbl = Label(window, image=width_img, bg=bg_frame_c).place(x=window.winfo_screenwidth() - 350, y=430)

# height img
height_img = PhotoImage(file='Pertemuan 10/height.png').subsample(2,2)
height_img_lbl = Label(window, image=height_img, bg=bg_frame_c).place(x=window.winfo_screenwidth() - 350, y=480)

# spinbox
w_spinbox = Spinbox(window, from_=0)
w_spinbox.place(x=window.winfo_screenwidth() - 250, y=430)
h_spinbox = Spinbox(window, from_=0)
h_spinbox.place(x=window.winfo_screenwidth() - 250, y=480)

# button resize
button_resize_img = PhotoImage(file='Pertemuan 10/button-resize.png').subsample(2,2)
button_resize_button = Button(window, image=button_resize_img, bg=bg_frame_c, command=resize_method)
button_resize_button.place(x=window.winfo_screenwidth() - 290, y=550)

# Image Frame
img_frame = Frame(
    window,
    height=window.winfo_screenheight() - 150,
    width=window.winfo_screenwidth() - 280,
    background=bg_win_c
    )
img_frame.pack(side=LEFT)

# import button
button_import = Button(img_frame, text="Click Here to import image", bg=bg_frame_c, foreground='white', font=20, command=upload_image)
button_import.place(x=400, y=350)

window.mainloop()
# UI End


