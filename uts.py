import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file Excel (data_penumpang.csv)
data = pd.read_csv('data_penumpang.csv')

# Melakukan penyeragaman nama untuk kolom 'trayek'
data['trayek'] = data['trayek'].str.replace('.', '')

# Mengecek data yang hilang (missing value)
missing_values = data.isnull().sum()

# Mendeteksi outlier (misalnya dengan IQR)
Q1 = data['jumlah_penumpang'].quantile(0.25)
Q3 = data['jumlah_penumpang'].quantile(0.75)
IQR = Q3 - Q1
outliers = ((data['jumlah_penumpang'] < (Q1 - 1.5 * IQR)) | (data['jumlah_penumpang'] > (Q3 + 1.5 * IQR)))

# Melakukan data binning (misalnya dengan cut)
bins = [0, 25, 50, 75, 100]
labels = ['1st Quartile', '2nd Quartile', '3rd Quartile', '4th Quartile']
data['Quartile'] = pd.cut(data['jumlah_penumpang'], bins=bins, labels=labels)

# Grup data berdasarkan kolom tertentu
grouped_data = data.groupby('jenis')['jumlah_penumpang'].mean()

# Menampilkan hasil
print("Data yang Hilang:")
print(missing_values)
print("\nOutliers:")
print(outliers)
print("\nData Binning:")
print(data[['jumlah_penumpang', 'Quartile']])
print("\nData yang Sudah Dikelompokkan:")
print(grouped_data)

# Menampilkan seluruh data setelah penyeragaman nama 'trayek'
print("\nSeluruh Data Setelah Penyeragaman Nama 'trayek':")
print(data)

# Melakukan pengecekan untuk missing value per kolom
missing_per_column = data.isnull().sum()

# Melakukan pengecekan untuk missing value per baris
missing_per_row = data.isnull().any(axis=1)

# Melakukan pengecekan outlier pada kolom 'jumlah_penumpang' dengan boxplot
plt.boxplot(data['jumlah_penumpang'])
plt.ylim([-100, 300])

# Menampilkan hasil penanganan data
print("\nMissing Values per Kolom:")
print(missing_per_column)
print("\nMissing Values per Baris:")
print(missing_per_row)

# Menampilkan beberapa baris pertama dari data
print("\nBeberapa Baris Pertama dari Data:")
print(data.head())
