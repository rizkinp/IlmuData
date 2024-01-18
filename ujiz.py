import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from scipy.stats import norm
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi, satu_sisi):
    # Hitung statistik uji z
    z = (rata2_sampel - rata2_populasi) / (standar_deviasi / math.sqrt(ukuran_sampel))

    # Hitung p-value menggunakan distribusi normal (karena ukuran sampel besar)
    if satu_sisi == "Kiri":
        p_value = norm.cdf(z)
    elif satu_sisi == "Kanan":
        p_value = 1 - norm.cdf(z)
    else:
        p_value = 2 * (1 - norm.cdf(abs(z)))

    # Hitung batas daerah kritis
    if satu_sisi == "Kiri":
        batas_kritis_kiri = norm.ppf(taraf_signifikansi)
        batas_kritis_kanan = float('inf')
    elif satu_sisi == "Kanan":
        batas_kritis_kiri = float('-inf')
        batas_kritis_kanan = norm.ppf(1 - taraf_signifikansi)
    else:
        batas_kritis_kiri = norm.ppf(taraf_signifikansi / 2)
        batas_kritis_kanan = norm.ppf(1 - taraf_signifikansi / 2)

    # Buat grafik distribusi normal
    fig, ax = plt.subplots()
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)
    ax.plot(x, y, label='Distribusi Normal Standar')
    ax.fill_between(x, 0, y, where=(x < batas_kritis_kiri) | (x > batas_kritis_kanan), color='red', alpha=0.5, label='Daerah Kritis')
    ax.scatter(z, norm.pdf(z), color='green', marker='o', label='Statistik Uji z')
    ax.axvline(x=0, color='black', linestyle='-', label='Garis Nol')
    ax.axvline(x=batas_kritis_kiri, color='blue', linestyle='--', label='Titik Kritis (Kiri)')
    ax.axvline(x=batas_kritis_kanan, color='blue', linestyle='--', label='Titik Kritis (Kanan)')

    ax.set_title('Grafik Distribusi Normal dengan Daerah Kritis dan Statistik Uji')
    ax.set_xlabel('Nilai Z')
    ax.set_ylabel('Densitas Probabilitas')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=10, columnspan=2)

    # Bandingkan p-value dengan taraf signifikansi
    if p_value < taraf_signifikansi:
        hasil_uji = f"H0 ditolak, terdapat bukti statistik bahwa rata-rata sampel tidak sama dengan rata-rata populasi (p-value: {p_value:.4f})"
        if satu_sisi == "Kiri":
            hasil_uji += "\nKesimpulan: (Hipotesis Alternatif: rata-rata sampel kurang dari rata-rata populasi)"
        elif satu_sisi == "Kanan":
            hasil_uji += "\nKesimpulan: (Hipotesis Alternatif: rata-rata sampel lebih dari rata-rata populasi)"
        else:
            hasil_uji += "\nKesimpulan: (Hipotesis Alternatif: rata-rata sampel tidak sama dengan rata-rata populasi)"
    else:
        hasil_uji = f"H0 diterima, tidak terdapat bukti statistik bahwa rata-rata sampel berbeda dengan rata-rata populasi (p-value: {p_value:.4f})"
    
    hasil_var.set(hasil_uji)

# Fungsi untuk mendapatkan nilai dari input dan memanggil fungsi uji_z
def hitung_uji_z():
    rata2_sampel = float(rata2_sampel_entry.get())
    rata2_populasi = float(rata2_populasi_entry.get())
    ukuran_sampel = int(ukuran_sampel_entry.get())
    standar_deviasi = float(standar_deviasi_entry.get())
    taraf_signifikansi = float(taraf_signifikansi_entry.get())
    satu_sisi = satu_sisi_var.get()
    
    uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi, satu_sisi)

# Membuat GUI menggunakan Tkinter
window = tk.Tk()
window.title("Uji Hipotesis Rata-Rata dengan Uji z")

# Label dan entry untuk rata-rata sampel
rata2_sampel_label = ttk.Label(window, text="Rata-rata Sampel:")
rata2_sampel_label.grid(row=0, column=0)
rata2_sampel_entry = ttk.Entry(window)
rata2_sampel_entry.grid(row=0, column=1)

# Label dan entry untuk rata-rata populasi
rata2_populasi_label = ttk.Label(window, text="Rata-rata Populasi:")
rata2_populasi_label.grid(row=1, column=0)
rata2_populasi_entry = ttk.Entry(window)
rata2_populasi_entry.grid(row=1, column=1)

# Label dan entry untuk ukuran sampel
ukuran_sampel_label = ttk.Label(window, text="Ukuran Sampel:")
ukuran_sampel_label.grid(row=2, column=0)
ukuran_sampel_entry = ttk.Entry(window)
ukuran_sampel_entry.grid(row=2, column=1)


# Label dan entry untuk standar deviasi
standar_deviasi_label = ttk.Label(window, text="Standar Deviasi:")
standar_deviasi_label.grid(row=3, column=0)
standar_deviasi_entry = ttk.Entry(window)
standar_deviasi_entry.grid(row=3, column=1)

# Label dan entry untuk taraf signifikansi
taraf_signifikansi_label = ttk.Label(window, text="Taraf Signifikansi:")
taraf_signifikansi_label.grid(row=4, column=0)
taraf_signifikansi_entry = ttk.Entry(window)
taraf_signifikansi_entry.grid(row=4, column=1)

# Radio Buttons untuk memilih satu sisi atau dua sisi
satu_sisi_var = StringVar()
satu_sisi_var.set("Dua Sisi")
satu_sisi_label = ttk.Label(window, text="Pilih Sisi:")
satu_sisi_label.grid(row=5, column=0, columnspan=2, pady=5)
satu_sisi_kiri = ttk.Radiobutton(window, text="Kiri", variable=satu_sisi_var, value="Kiri")
satu_sisi_kanan = ttk.Radiobutton(window, text="Kanan", variable=satu_sisi_var, value="Kanan")
satu_sisi_dua_sisi = ttk.Radiobutton(window, text="Dua Sisi", variable=satu_sisi_var, value="Dua Sisi")
satu_sisi_kiri.grid(row=6, column=0, padx=5, sticky="w")
satu_sisi_kanan.grid(row=6, column=1, padx=5, sticky="w")
satu_sisi_dua_sisi.grid(row=6, column=2, padx=5, sticky="w")

# Tombol untuk menghitung uji z
hitung_button = ttk.Button(window, text="Hitung", command=hitung_uji_z)
hitung_button.grid(row=7, columnspan=3, pady=10)

# Variabel String untuk menampilkan hasil uji
hasil_var = tk.StringVar()
hasil_label = ttk.Label(window, textvariable=hasil_var)
hasil_label.grid(row=9, columnspan=3)

window.mainloop()






# import tkinter as tk
# from tkinter import ttk
# from scipy.stats import norm
# import numpy as np
# import math
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# def uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi):
#     # Hitung statistik uji z
#     z = (rata2_sampel - rata2_populasi) / (standar_deviasi / math.sqrt(ukuran_sampel))

#     # Hitung p-value
#     p_value = 2 * (1 - norm.cdf(abs(z)))

#     # Hitung batas daerah kritis
#     batas_kritis_kiri = norm.ppf(taraf_signifikansi / 2)
#     batas_kritis_kanan = norm.ppf(1 - taraf_signifikansi / 2)

#     # Buat grafik distribusi normal
#     fig, ax = plt.subplots()
#     x = np.linspace(-4, 4, 1000)
#     y = norm.pdf(x, 0, 1)
#     ax.plot(x, y, label='Distribusi Normal Standar')
#     ax.fill_between(x, 0, y, where=(x < batas_kritis_kiri) | (x > batas_kritis_kanan), color='red', alpha=0.5, label='Daerah Kritis')
#     ax.scatter(z, norm.pdf(z), color='green', marker='o', label='Statistik Uji z')
#     ax.axvline(x=0, color='black', linestyle='-', label='Garis Nol')
#     ax.axvline(x=batas_kritis_kiri, color='blue', linestyle='--', label='Titik Kritis (Kiri)')
#     ax.axvline(x=batas_kritis_kanan, color='blue', linestyle='--', label='Titik Kritis (Kanan)')

#     ax.set_title('Grafik Distribusi Normal dengan Daerah Kritis dan Statistik Uji')
#     ax.set_xlabel('Nilai Z')
#     ax.set_ylabel('Densitas Probabilitas')
#     ax.legend()

#     canvas = FigureCanvasTkAgg(fig, master=window)
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.grid(row=8, columnspan=2)

#     # Bandingkan p-value dengan taraf signifikansi
#     if p_value < taraf_signifikansi:
#         hasil_uji = f"H0 ditolak, terdapat bukti statistik bahwa rata-rata sampel tidak sama dengan rata-rata populasi (p-value: {p_value:.4f})"
#     else:
#         hasil_uji = f"H0 diterima, tidak terdapat bukti statistik bahwa rata-rata sampel berbeda dengan rata-rata populasi (p-value: {p_value:.4f})"

#     hasil_var.set(hasil_uji)

# # Fungsi untuk mendapatkan nilai dari input dan memanggil fungsi uji_z
# def hitung_uji_z():
#     rata2_sampel = float(rata2_sampel_entry.get())
#     rata2_populasi = float(rata2_populasi_entry.get())
#     ukuran_sampel = int(ukuran_sampel_entry.get())
#     standar_deviasi = float(standar_deviasi_entry.get())
#     taraf_signifikansi = float(taraf_signifikansi_entry.get())
    
#     uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi)

# # Membuat GUI menggunakan Tkinter
# window = tk.Tk()
# window.title("Uji Hipotesis Rata-Rata dengan Uji z")

# # Label dan entry untuk rata-rata sampel
# rata2_sampel_label = ttk.Label(window, text="Rata-rata Sampel:")
# rata2_sampel_label.grid(row=0, column=0)
# rata2_sampel_entry = ttk.Entry(window)
# rata2_sampel_entry.grid(row=0, column=1)

# # Label dan entry untuk rata-rata populasi
# rata2_populasi_label = ttk.Label(window, text="Rata-rata Populasi:")
# rata2_populasi_label.grid(row=1, column=0)
# rata2_populasi_entry = ttk.Entry(window)
# rata2_populasi_entry.grid(row=1, column=1)

# # Label dan entry untuk ukuran sampel
# ukuran_sampel_label = ttk.Label(window, text="Ukuran Sampel:")
# ukuran_sampel_label.grid(row=2, column=0)
# ukuran_sampel_entry = ttk.Entry(window)
# ukuran_sampel_entry.grid(row=2, column=1)

# # Label dan entry untuk standar deviasi
# standar_deviasi_label = ttk.Label(window, text="Standar Deviasi:")
# standar_deviasi_label.grid(row=3, column=0)
# standar_deviasi_entry = ttk.Entry(window)
# standar_deviasi_entry.grid(row=3, column=1)

# # Label dan entry untuk taraf signifikansi
# taraf_signifikansi_label = ttk.Label(window, text="Taraf Signifikansi:")
# taraf_signifikansi_label.grid(row=4, column=0)
# taraf_signifikansi_entry = ttk.Entry(window)
# taraf_signifikansi_entry.grid(row=4, column=1)

# # Tombol untuk menghitung uji z
# hitung_button = ttk.Button(window, text="Hitung", command=hitung_uji_z)
# hitung_button.grid(row=5, columnspan=2)

# # Variabel String untuk menampilkan hasil uji
# hasil_var = tk.StringVar()
# hasil_label = ttk.Label(window, textvariable=hasil_var)
# hasil_label.grid(row=6, columnspan=2)

# window.mainloop()
