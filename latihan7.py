import pandas as pd
import warnings
import numpy as np

# Mengabaikan semua peringatan (warning)
warnings.filterwarnings("ignore")

# Membaca file CSV
df = pd.read_csv('data.csv')


rata_nilai_alamat = df.groupby('alamat')['nilai'].mean()
rata_nilai_jk = df.groupby('jenis kelamin')['nilai'].mean()

total_nilai_alamat = df.groupby('alamat')['nilai'].sum()
total_nilai_jk = df.groupby('jenis kelamin')['nilai'].sum()

jumlah_nilai_alamat = df.groupby('alamat')['nilai'].count()
jumlah_nilai_jk = df.groupby('jenis kelamin')['nilai'].count()

maksimal_nilai_alamat = df.groupby('alamat')['nilai'].max()
maksimal_nilai_jk = df.groupby('jenis kelamin')['nilai'].max()

minimal_nilai_alamat = df.groupby('alamat')['nilai'].min()
minimal_nilai_jk = df.groupby('jenis kelamin')['nilai'].min()

print("Rata-rata berdasarkan alamat:")
print(rata_nilai_alamat.to_string())
print("Rata-rata berdasarkan jenis kelamin:")
print(rata_nilai_jk.to_string())
print("============================================================")
print("Total berdasarkan alamat:")
print(total_nilai_alamat.to_string())
print("Total berdasarkan jenis kelamin:")
print(total_nilai_jk.to_string())
print("================================================")
print("jumlah berdasarkan alamat:")
print(jumlah_nilai_alamat.to_string())
print("jumlah berdasarkan jenis kelamin:")
print(jumlah_nilai_jk.to_string())
print("=========================")
print("minimal berdasarkan alamat:")
print(minimal_nilai_alamat.to_string())
print("minimal berdasarkan jenis kelamin:")
print(minimal_nilai_jk.to_string())
print("================================================================")
print("maksimal berdasarkan alamat:")
print(maksimal_nilai_alamat.to_string())
print("maksimal berdasarkan jenis kelamin:")
print(maksimal_nilai_jk.to_string())

df_grouped = df.groupby(['jenis kelamin'])
jenis_kelamin = df_grouped['nilai'].agg([np.mean, np.sum])


print(jenis_kelamin)