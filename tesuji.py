import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi):
    # Hitung statistik uji z
    z = (rata2_sampel - rata2_populasi) / (standar_deviasi / math.sqrt(ukuran_sampel))

    # Hitung p-value menggunakan distribusi normal (karena ukuran sampel besar)
    p_value = 1 - norm.cdf(abs(z))

    # Hitung batas daerah kritis
    batas_kritis_kanan = norm.ppf(1 - taraf_signifikansi)

    # Buat grafik distribusi normal
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)

    plt.plot(x, y, label='Distribusi Normal Standar')
    plt.fill_between(x, 0, y, where=(x > batas_kritis_kanan), color='red', alpha=0.5, label='Daerah Kritis')
    plt.scatter(z, norm.pdf(z), color='green', marker='o', label='Statistik Uji z')
    plt.axvline(x=0, color='black', linestyle='-', label='Garis Nol')
    plt.axvline(x=batas_kritis_kanan, color='blue', linestyle='--', label='Titik Kritis (Kanan)')

    plt.title('Grafik Distribusi Normal dengan Daerah Kritis dan Statistik Uji')
    plt.xlabel('Nilai Z')
    plt.ylabel('Densitas Probabilitas')
    plt.legend()
    plt.show()

    # Bandingkan p-value dengan taraf signifikansi
    if p_value < taraf_signifikansi:
        hasil_uji = f"H0 ditolak, terdapat bukti statistik bahwa rata-rata sampel tidak sama dengan rata-rata populasi (p-value: {p_value:.4f})"
    else:
        hasil_uji = f"H0 diterima, tidak terdapat bukti statistik bahwa rata-rata sampel berbeda dengan rata-rata populasi (p-value: {p_value:.4f})"

    return hasil_uji

# Contoh penggunaan
rata2_sampel = 810
rata2_populasi = 800
ukuran_sampel = 25
standar_deviasi = 20
taraf_signifikansi = 0.05

hasil = uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi)
print(hasil)
