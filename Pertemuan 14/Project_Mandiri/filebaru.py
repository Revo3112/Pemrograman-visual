import tkinter as tk
from tkinter import filedialog
import pandas as pd
import mplfinance as mpf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

window = tk.Tk()
file_path = ""
graph_mode = tk.StringVar()
canvas = None  # Menyimpan referensi ke objek canvas

def import_file():
    global file_path
    file_path = filedialog.askopenfilename()
    file_label.config(text="File Path: " + file_path)
    return file_path

def clear_canvas():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()  # Hapus canvas jika ada

def plot_graph():
    global file_path, graph_mode, canvas

    clear_canvas()  # Hapus canvas sebelum membuat yang baru

    if file_path:
        df = pd.read_csv(file_path)
        df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d/%m/%Y')
        df.set_index('Tanggal', inplace=True)

        if graph_mode.get() == 'Candlestick':
            clear_canvas()
            candle_data = df[['Pembukaan', 'Tertinggi', 'Terendah', 'Terakhir']].copy()
            candle_data.sort_values('Tanggal', inplace=True)
            for column in candle_data.columns:
                candle_data[column] = candle_data[column].str.replace('.', '').str.replace(',', '.').astype(float)
            candle_data.columns = ['Open', 'High', 'Low', 'Close']
            fig, ax = mpf.plot(candle_data, type='candle', style='charles', returnfig=True)
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack()

        elif graph_mode.get() == 'Line':
            clear_canvas()
            fig, ax = plt.subplots()
            df['Terakhir'] = df['Terakhir'].str.replace('.', '').astype(int)
            ax.plot(df.index, df['Terakhir'], color='b')
            ax.set_title('Line Chart')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack()

        # Set style menjadi gelap
        plt.style.use('dark_background')
def create_gui():
    global window, graph_mode, file_label

    window.title('Plotting Tool')
    window.geometry("1366x768")
    window.configure(bg="#0C0C0C")
    # Load the logo image with a transparent background
    logo_path = "logo (1).png"
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((216, 44))  # Resize the image to 216x44 pixels
    logo = ImageTk.PhotoImage(logo_img)

    # Create a label for the logo with a transparent background
    logo_lbl = tk.Label(image=logo, background='#0C0C0C')
    logo_lbl.image = logo  # Keep a reference to avoid garbage collection
    logo_lbl.pack()

    import_button = tk.Button(master=window, command=import_file, height=2, width=10, text="Import File", bg="black", fg="white")
    import_button.pack()

    file_label = tk.Label(master=window, text="File Path: ", wraplength=400, bg="black", fg="white")
    file_label.pack()

    candlestick_button = tk.Radiobutton(master=window, text="Candlestick", variable=graph_mode, value="Candlestick", bg="black", fg="white")
    candlestick_button.pack()

    line_button = tk.Radiobutton(master=window, text="Line", variable=graph_mode, value="Line", bg="black", fg="white")
    line_button.pack()

    plot_button = tk.Button(master=window, command=plot_graph, height=2, width=10, text="Plot", bg="black", fg="white")
    plot_button.pack()

    window.mainloop()

if __name__ == '__main__':
    create_gui()
