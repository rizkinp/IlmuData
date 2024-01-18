# import numpy as np
# import pandas as pd

# random_data = np.random.randint(100, 151, 200)
# df = pd.DataFrame({'Data': random_data})
# print("Beberapa data pertama:")
# print(df.head())
# summary_stats = df.describe()
# print("\nStatistik Deskriptif:")
# print(summary_stats)
# mode = df['Data'].mode()
# print("\nModus (Mode):")
# print(mode)
# median = df['Data'].median()
# print("\nMedian:")
# print(median)
# mean = df['Data'].mean()
# print("\nMean (Rata-rata):")
# print(mean)
# variance = df['Data'].var()
# print("\nVariansi:")
# print(variance)
# std_deviation = df['Data'].std()
# print("\nDeviasi Standar:")
# print(std_deviation)

# SOAL ===========3========
# import pandas as pd

# # Membaca data set dari file CSV
# data = pd.read_csv('F500.csv', delimiter=';')

# # Menampilkan beberapa data pertama
# print("Beberapa data pertama:")
# print(data.head())

# # Menghitung statistik deskriptif untuk kolom-kolom yang relevan
# summary_stats = data.describe()

# # Menampilkan statistik deskriptif
# print("\nStatistik Deskriptif:")
# print(summary_stats)

# # Menampilkan modus (mode) dari beberapa kolom
# mode_name = data['name'].mode()
# mode_rank = data['rank'].mode()
# print("\nModus (Mode) Nama:")
# print(mode_name)
# print("\nModus (Mode) Rank:")
# print(mode_rank)

# # Menampilkan rata-rata (mean) dan total (sum) dari beberapa kolom
# mean_employees = data['employees'].mean()
# mean_revenues = data['revenues'].mean()
# total_profits = data['profits'].sum()
# print("\nRata-rata (Mean) Jumlah Employees:")
# print(mean_employees)
# print("\nRata-rata (Mean) Revenues:")
# print(mean_revenues)
# print("\nTotal Profits:")
# print(total_profits)

# import pandas as pd
# import matplotlib.pyplot as plt

# # Membaca data set dari file CSV dengan pemisah berupa titik koma (';')
# data = pd.read_csv('F500.csv', delimiter=';')

# # Membersihkan kolom 'employees' dari tanda koma dan mengonversi ke tipe data numerik
# data['employees'] = data['employees'].str.replace(',', '').astype(int)

# # Menghitung statistik deskriptif untuk kolom-kolom yang relevan
# summary_stats = data.describe()

# # Menampilkan statistik deskriptif
# print("\nStatistik Deskriptif:")
# print(summary_stats)

# # Menampilkan modus (mode) dari beberapa kolom
# mode_name = data['name'].mode()
# mode_rank = data['rank'].mode()
# print("\nModus (Mode) Nama:")
# print(mode_name)
# print("\nModus (Mode) Rank:")
# print(mode_rank)

# # Menampilkan rata-rata (mean) dari kolom 'employees'
# mean_employees = data['employees'].mean()
# print("\nRata-rata (Mean) Jumlah Employees:")
# print(mean_employees)
# plt.show()
# # Menampilkan informasi tambahan sesuai kebutuhan Anda




# import pandas as pd
# import matplotlib.pyplot as plt


# data = pd.read_csv('F500.csv', delimiter=';')


# data['employees'] = data['employees'].str.replace(',', '').astype(int)


# summary_stats = data['employees'].describe()

# # Menampilkan statistik deskriptif
# print("\nStatistik Deskriptif:")
# print(summary_stats)

# # # Menampilkan modus (mode) dari kolom 'name'
# # mode_name = data['name'].mode()
# # print("\nModus (Mode) Nama:")
# # print(mode_name)

# # # Menampilkan rata-rata (mean) dari kolom 'employees'
# # mean_employees = data['employees'].mean()
# # print("\nRata-rata (Mean) Jumlah Employees:")
# # print(mean_employees)

# # Menampilkan histogram dari kolom 'employees'
# plt.figure(figsize=(8, 6))
# plt.hist(data['employees'])
# plt.xlabel('Jumlah Employees')
# plt.ylabel('Frekuensi')
# plt.title('Distribusi Jumlah Employees')
# plt.grid(True)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Membaca data set dari file CSV dengan pemisah berupa titik koma (';')
data = pd.read_csv('F500.csv', delimiter=';')

# Membersihkan kolom 'employees' dari tanda koma dan mengonversi ke tipe data numerik
data['employees'] = data['employees'].str.replace(',', '').astype(int)

# Membersihkan kolom 'revenues' dari simbol mata uang dan tanda koma, dan mengonversi ke tipe data float
data['revenues'] = data['revenues'].str.replace('[$,]', '', regex=True).astype(float)

# Menghitung statistik deskriptif untuk kolom-kolom yang relevan
summary_stats = data.describe()

# Menampilkan statistik deskriptif
print("\nStatistik Deskriptif:")
print(summary_stats)

# Menampilkan modus (mode) dari beberapa kolom
mode_name = data['name'].mode()
mode_rank = data['rank'].mode()
print("\nModus (Mode) Nama:")
print(mode_name)
print("\nModus (Mode) Rank:")
print(mode_rank)

# rata2 mean dan revenues 
mean_employees = data['employees'].mean()
mean_revenues = data['revenues'].mean()
print("\nRata-rata (Mean) Jumlah Employees:")
print(mean_employees)
print("\nRata-rata (Mean) Revenues:")
print(mean_revenues)

# Menampilkan histogram dari kolom 'employees' dan 'revenues'
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data['employees'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Jumlah Employees')
plt.ylabel('Frekuensi')
plt.title('Distribusi Jumlah Employees')

plt.subplot(1, 2, 2)
plt.hist(data['revenues'], bins=20, color='green', alpha=0.7)
plt.xlabel('Revenues')
plt.ylabel('Frekuensi')
plt.title('Distribusi Revenues')

plt.tight_layout()
plt.show()



# # # =======Soal 2========
# import pandas as pd
# import matplotlib.pyplot as plt

# # Data untuk Toko A
# toko_a = {
#     'Merk': ['Nokia', 'Samsung', 'Black Berry', 'Cross', 'Motorola', 'Siemens', 'Taxco', 'Nexian', 'Mito', 'Vitel', 'Smartfren', 'LG', 'Flexi', 'Esia', 'Iphone', 'Android', 'Advan', 'Apple', 'HTC'],
#     'StockA': [44, 24, 59, 23, 44, 90, 79, 45, 36, 78, 55, 67, 77, 78, 98, 35, 35, 67, 79],
#     'HargaA': ['Rp. 500.000', 'Rp. 450.000', 'Rp. 2.000.000', 'Rp. 400.000', 'Rp. 600.000', 'Rp. 550.000', 'Rp. 400.000', 'Rp. 650.000', 'Rp. 500.000', 'Rp. 450.000', 'Rp. 300.000', 'Rp. 500.000', 'Rp. 250.000', 'Rp. 300.000', 'Rp. 2.500.000', 'Rp. 3.000.000', 'Rp. 450.000', 'Rp. 4.000.000', 'Rp. 500.000']
# }

# # Data untuk Toko B
# toko_b = {
#     'Merk': ['Nokia', 'Samsung', 'Black Berry', 'Cross', 'Motorola', 'Siemens', 'Taxco', 'Nexian', 'Mito', 'Vitel', 'Smartfren', 'LG', 'Flexi', 'Esia', 'Iphone', 'Android', 'Advan', 'Apple', 'HTC'],
#     'StockB': [56, 75, 99, 98, 76, 56, 76, 87, 67, 43, 23, 43, 54, 65, 76, 78, 99, 54, 40],
#     'HargaB': ['Rp. 550.000', 'Rp. 500.000', 'Rp. 2.050.000', 'Rp. 450.000', 'Rp. 650.000', 'Rp. 650.000', 'Rp. 450.000', 'Rp. 700.000', 'Rp. 550.000', 'Rp. 500.000', 'Rp. 400.000', 'Rp. 600.000', 'Rp. 300.000', 'Rp. 350.000', 'Rp. 2.550.000', 'Rp. 3.050.000', 'Rp. 500.000', 'Rp. 4.050.000', 'Rp. 550.000']
# }

# # Membuat DataFrame untuk Toko A dan Toko B
# df_toko_a = pd.DataFrame(toko_a)
# df_toko_b = pd.DataFrame(toko_b)

# # Menghapus simbol mata uang dan mengonversi harga menjadi tipe data numerik
# df_toko_a['HargaA'] = df_toko_a['HargaA'].str.replace('[^\d]', '', regex=True).astype(int)
# df_toko_b['HargaB'] = df_toko_b['HargaB'].str.replace('[^\d]', '', regex=True).astype(int)

# # Statistik Deskriptif untuk StockA dan StockB
# statistik_stock_a = df_toko_a['StockA'].describe()
# statistik_stock_b = df_toko_b['StockB'].describe()

# # Menampilkan deskripsi statistik
# print("Statistik Deskriptif untuk StockA (Toko A):")
# print(statistik_stock_a)

# print("\nStatistik Deskriptif untuk StockB (Toko B):")
# print(statistik_stock_b)

# # Membuat grafik perbandingan stok di Toko A dan Toko B
# plt.figure(figsize=(10, 6))
# plt.bar(df_toko_a['Merk'], df_toko_a['StockA'], label='Toko A', alpha=0.7)
# plt.bar(df_toko_b['Merk'], df_toko_b['StockB'], label='Toko B', alpha=0.7)
# plt.xlabel('Merk Handphone')
# plt.ylabel('Stok')
# plt.title('Perbandingan Stok Handphone di Toko A dan Toko B')
# plt.xticks(rotation=90)
# plt.legend()
# plt.tight_layout()

# # Menampilkan grafik
# plt.show()


