import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Gantilah 'nama_file.csv' dengan nama file yang sesuai
data_path = 'movies.csv'

# Membaca data dari file CSV
df = pd.read_csv(data_path)

#GRAFIK JUMLAH FILM TIAP GENRE
# Membuat bar plot untuk menampilkan jumlah film untuk setiap genre
plt.figure(figsize=(12, 6))
sns.countplot(x='genre', data=df, order=df['genre'].value_counts().index)
plt.title('Jumlah Film untuk Setiap Genre')
plt.xlabel('Genre')
plt.ylabel('Jumlah Film')
plt.xticks(rotation=45, ha='right')
plt.show()

#GRAFIK KEUNTUNGAN BERSIH 10 DATA TERATAS
# Menghitung selisih antara gross dan budget
df['profit'] = df['gross'] - df['budget']
# Mengurutkan data berdasarkan profit secara descending
top_profit_movies = df.sort_values(by='profit', ascending=False).head(10)
# Membuat bar plot untuk menampilkan selisih terbesar dari 10 data pertama
plt.figure(figsize=(12, 6))
sns.barplot(x='name', y='profit', data=top_profit_movies)
plt.title('Selisih Gross dan Budget Terbesar (10 Data Pertama)')
plt.xlabel('Nama Film')
plt.ylabel('Selisih Gross dan Budget(PROFIT)')
plt.xticks(rotation=45, ha='right')
plt.show()


#GRAFIK MENAMPILKAN 20 DATA PERTAMA UNTUK NAME DAN SCOREATAU RATING
top_score_movies = df[['name', 'score']].head(20)
# Membuat bar plot untuk menampilkan 10 data pertama
plt.figure(figsize=(12, 6))
sns.barplot(x='name', y='score', data=top_score_movies)
plt.title('20 Data Pertama: Nama Film dan Skor')
plt.xlabel('Nama Film')
plt.ylabel('Skor')
plt.xticks(rotation=45, ha='right')
plt.show()

#GRAFIK COMPANY
# Hitung jumlah film untuk setiap perusahaan
company_counts = df['company'].value_counts()

# Ambil 10 perusahaan dengan jumlah film terbanyak
top_companies = company_counts.head(10).index

# Filter data untuk perusahaan-perusahaan tersebut
top_movies_by_company = df[df['company'].isin(top_companies)]

plt.figure(figsize=(12, 6))
sns.countplot(x='company', data=top_movies_by_company, order=top_companies)
plt.title('Jumlah Film per Perusahaan (Top 10)')
plt.xlabel('Perusahaan Produksi')
plt.ylabel('Jumlah Film')
plt.xticks(rotation=45, ha='right')
plt.show()
#pisah
print("Dataset information")
df_info = df.info()
print(df_info)
#pisah
print("=== Cek missing value semua kolom true/false ===")
missing_value = df.isnull().any()
print(missing_value)  
#pisah
print("=== Cek jumlah missing value pwe kolom ===")
missing_value_count = df.isnull().sum()
print(missing_value_count)
#pisah
print("=== Jumlah missing value dari semua kolom ===")
missing_value_count_all = df.isnull().sum().sum()
print(missing_value_count_all)
#pisah
print("=== missing value dari kolom budget ===")
data_budget = df['budget'].unique()
print(data_budget)

plt.boxplot(df['budget']) 

# Menampilkan 10 data pertama dengan nilai missing value pada kolom budget sebelum penanganan
print("10 Data pertama sebelum penanganan nilai missing value KOLOM BUDGET:")
print(df[df['budget'].isnull()].head(10)[['name', 'budget']])

# Mengganti nilai missing value pada kolom budget dengan 0
df['budget'].fillna(0, inplace=True)

# Menampilkan 10 data pertama setelah penanganan nilai missing value
print("\n10 Data pertama setelah penanganan nilai missing value:")
print(df[['name', 'budget']].head(30))

#PENANGANAN KOLOM GROSS
print("10 Data pertama sebelum penanganan nilai missing value KOLOM GROSS:")
print(df[df['gross'].isnull()].head(50)[['name', 'gross']])

# Mengganti nilai missing value pada kolom budget dengan 0
df['gross'].fillna(0, inplace=True)

# Menampilkan 10 data pertama setelah penanganan nilai missing value
print("\n50 Data pertama setelah penanganan nilai missing value:")
print(df[['name', 'gross']].head(50))

