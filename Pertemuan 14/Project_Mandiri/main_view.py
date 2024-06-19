import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk membaca data CSV
def read_csv_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        messagebox.showerror("Kesalahan", f"File {filename} tidak ditemukan!")
        return None

# Fungsi untuk membuka file dialog dan memilih file
def browse_file():
    filename = filedialog.askopenfilename(
        title="Pilih File Data",
        filetypes=[("File CSV", "*.csv")],
    )
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

# Fungsi untuk menampilkan frame yang sesuai berdasarkan pilihan pengguna
def show_frame():
    if chart_type_var.get() == "candlestick":
        candlestick_frame.tkraise()
    else:
        line_frame.tkraise()

# Fungsi untuk memplot candlestick chart
def plot_candlestick(data, title, ylabel):
    # Membersihkan plot sebelumnya
    for widget in candlestick_frame.winfo_children():
        widget.destroy()

    df = data.copy()

    # Konversi kolom 'Tanggal' ke format datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d/%m/%Y')

    # Setel kolom 'Tanggal' sebagai indeks
    df.set_index('Tanggal', inplace=True)

    # Buat DataFrame baru untuk candlestick chart
    candle_data = df[['Pembukaan', 'Tertinggi', 'Terendah', 'Terakhir']].copy()

    candle_data.sort_index(inplace=True)

    # Mengganti koma dan titik dalam nilai numerik untuk memungkinkan konversi ke float
    for column in candle_data.columns:
        candle_data[column] = candle_data[column].str.replace('.', '').str.replace(',', '.').astype(float)

    # Membuat DataFrame untuk candlestick chart dengan nama kolom yang sesuai
    candle_data.columns = ['Open', 'High', 'Low', 'Close']

    # Membuat canvas untuk candlestick chart
    fig, ax = plt.subplots(figsize=(candlestick_frame.winfo_width() / 100, candlestick_frame.winfo_height() / 100))
    candlestick_canvas = FigureCanvasTkAgg(fig, master=candlestick_frame)
    candlestick_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Set style menjadi gelap
    plt.style.use('dark_background')

    try:
        # Plot candlestick chart
        mpf.plot(
            candle_data,
            type='candle',
            style='charles',
            title=title,
            ylabel=ylabel,
            ax=ax,
        )

        # Menampilkan candlestick chart
        candlestick_canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan dalam plotting: {str(e)}")


# Fungsi untuk memplot line chart
def plot_line(data, title, xlabel, ylabel):
    # Membersihkan plot sebelumnya
    for widget in line_frame.winfo_children():
        widget.destroy()

    df = data.copy()

    # Convert 'Tanggal' to datetime format
    df[xlabel] = pd.to_datetime(df[xlabel], format='%d/%m/%Y')

    # Convert 'Terakhir' to numeric (remove periods and convert to integer)
    df[ylabel] = df[ylabel].str.replace('.', '').astype(int)

    # Sort df by date
    df.sort_values(xlabel, inplace=True)

    # Membuat canvas untuk line chart
    fig, ax = plt.subplots(figsize=(line_frame.winfo_width() / 100, line_frame.winfo_height() / 100))
    line_canvas = FigureCanvasTkAgg(fig, master=line_frame)
    line_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Set style menjadi gelap
    plt.style.use('dark_background')

    # Plot the line chart
    plt.fill_between(df[xlabel], df[ylabel], color='skyblue', alpha=0.3)
    plt.plot(df[xlabel], df[ylabel], linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Harga Terakhir (IDR)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Menampilkan line chart
    line_canvas.draw()

# Membuat GUI
root = tk.Tk()
root.title("Candlestick Chart App")

# Mengatur tema gelap untuk keseluruhan aplikasi
root.configure(bg='black')  # Mengatur latar belakang menjadi hitam

# Frame untuk candlestick chart
candlestick_frame = ttk.Frame(root)
candlestick_frame.pack(fill=tk.BOTH, expand=True)

# Frame untuk line chart
line_frame = ttk.Frame(root)
line_frame.pack(fill=tk.BOTH, expand=True)

# Variable untuk pilihan jenis chart
chart_type_var = tk.StringVar()
chart_type_var.set("candlestick")  # Defaultnya candlestick

# Dropdown untuk memilih jenis chart
chart_type_dropdown = ttk.OptionMenu(root, chart_type_var, "candlestick", "candlestick", "line",
                                     command=lambda _: show_frame())
chart_type_dropdown.pack(pady=10)

# Entry untuk nama file
file_entry = ttk.Entry(root, width=50)
file_entry.pack(pady=10)

# Button untuk memilih file
browse_button = ttk.Button(root, text="Pilih File", command=browse_file)
browse_button.pack(pady=10)

# Button untuk memplot
plot_button = ttk.Button(root, text="Plot", command=lambda: plot_candlestick(read_csv_data(file_entry.get()),
                                                                             "Candlestick Chart BTC/IDR",
                                                                             "Price"))
plot_button.pack(pady=10)

# Menampilkan GUI
root.mainloop()
