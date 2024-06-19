import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk membaca data CSV
def read_csv_data(filename):
    df = pd.read_csv(filename, thousands='.', decimal=',')
    return df

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
        plot_candlestick()
    else:
        plot_line()

# Fungsi untuk memplot candlestick chart
def plot_candlestick():
    # Membersihkan plot sebelumnya
    plt.close('all')

    data = read_csv_data(file_entry.get())
    if data.empty:
        messagebox.showerror("Error", "Data tidak tersedia untuk diproses.")
        return

    df = data.copy()

    # Convert 'Tanggal' to datetime format
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d/%m/%Y')

    # Set 'Tanggal' sebagai indeks (DatetimeIndex)
    df.set_index('Tanggal', inplace=True)

    # Membuat DataFrame untuk candlestick chart
    candle_data = df[['Pembukaan', 'Tertinggi', 'Terendah', 'Terakhir']].copy()

    # Pembersihan nilai numerik
    for column in candle_data.columns:
        candle_data[column] = pd.to_numeric(candle_data[column], errors='coerce')  # Konversi ke float

    # Membuat DataFrame untuk candlestick chart dengan nama kolom yang sesuai
    candle_data.columns = ['Open', 'High', 'Low', 'Close']

    # Membuat canvas untuk candlestick chart
    fig, ax = plt.subplots(figsize=(8, 6))
    candlestick_canvas = FigureCanvasTkAgg(fig, master=candlestick_frame)
    candlestick_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Set style menjadi gelap
    plt.style.use('dark_background')

    # Plot candlestick chart
    try:
        mpf.plot(
            candle_data,
            type='candle',
            style='charles',
            title="Candlestick Chart BTC/IDR",
            ylabel="Price",
            ax=ax,
        )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to plot candlestick chart: {str(e)}")
        return

    # Menampilkan candlestick chart
    if fig is not None:  # Pastikan fig bukan NoneType sebelum memanggil suptitle
        fig.suptitle("Candlestick Chart BTC/IDR", fontsize=16)
        candlestick_canvas.draw()

# Fungsi untuk memplot line chart
def plot_line():
    # Membersihkan plot sebelumnya
    plt.close('all')

    data = read_csv_data(file_entry.get())
    if data.empty:
        messagebox.showerror("Error", "Data tidak tersedia untuk diproses.")
        return

    df = data.copy()

    # Convert 'Tanggal' to datetime format
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d/%m/%Y')

    # Set 'Tanggal' sebagai indeks (DatetimeIndex)
    df.set_index('Tanggal', inplace=True)

    # Membuat canvas untuk line chart
    fig, ax = plt.subplots(figsize=(8, 6))
    line_canvas = FigureCanvasTkAgg(fig, master=line_frame)
    line_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Set style menjadi gelap
    plt.style.use('dark_background')

    # Plot the line chart
    ax.plot(df.index, df['Terakhir'], linestyle='-', color='b')
    ax.fill_between(df.index, df['Terakhir'], color='skyblue', alpha=0.3)
    ax.set_title("Line Chart BTC/IDR")
    ax.set_xlabel("Date")
    ax.set_ylabel("Harga Terakhir (IDR)")
    ax.grid(True)
    ax.xaxis.set_tick_params(rotation=45)

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
chart_type_dropdown = ttk.OptionMenu(root, chart_type_var, "candlestick", "candlestick", "line", command=lambda _: show_frame())
chart_type_dropdown.pack(pady=10)

# Entry untuk nama file
file_entry = ttk.Entry(root, width=50)
file_entry.pack(pady=10)

# Button untuk memilih file
browse_button = ttk.Button(root, text="Pilih File", command=browse_file)
browse_button.pack(pady=10)

# Button untuk memplot
plot_button = ttk.Button(root, text="Plot", command=lambda: plot_candlestick() if chart_type_var.get() == "candlestick" else plot_line())
plot_button.pack(pady=10)

# Menampilkan GUI
root.mainloop()
