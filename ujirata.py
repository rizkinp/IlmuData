import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi):
    # Hitung statistik uji z
    z = (rata2_sampel - rata2_populasi) / (standar_deviasi / math.sqrt(ukuran_sampel))

    # Hitung p-value
    p_value = 2 * (1 - norm.cdf(abs(z)))

    # Hitung batas daerah kritis
    batas_kritis_kiri = norm.ppf(taraf_signifikansi / 2)
    batas_kritis_kanan = norm.ppf(1 - taraf_signifikansi / 2)

    # Buat grafik distribusi normal
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)

    plt.plot(x, y, label='Distribusi Normal Standar')
    plt.fill_between(x, 0, y, where=(x < batas_kritis_kiri) | (x > batas_kritis_kanan), color='red', alpha=0.5, label='Daerah Kritis')

    # Tandai nilai statistik uji z
    plt.scatter(z, norm.pdf(z), color='green', marker='o', label='Statistik Uji z')

    # Tandai garis nol
    plt.axvline(x=0, color='black', linestyle='-', label='Garis Nol')

    # Tandai titik kritis
    plt.axvline(x=batas_kritis_kiri, color='blue', linestyle='--', label='Titik Kritis (Kiri)')
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
rata2_sampel = float(input("Masukkan rata-rata sampel: "))
rata2_populasi = float(input("Masukkan rata-rata populasi: "))
ukuran_sampel = int(input("Masukkan ukuran sampel: "))
standar_deviasi = float(input("Masukkan standar deviasi: "))
taraf_signifikansi = float(input("Masukkan taraf signifikansi (misalnya, 0.05): "))

hasil = uji_z(rata2_sampel, rata2_populasi, ukuran_sampel, standar_deviasi, taraf_signifikansi)
print(hasil)
