#1.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#2. read data
df = pd.read_csv('data_penduduk.csv')
df.head(10)

print(df.columns)
# Langkah 3: Preprocessing - menghapus kolom 'Unnamed: 0' jika diperlukan
# Jika 'Unnamed: 0' tidak ada dalam kolom, Anda dapat melewatkan langkah ini.
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# Lanjutkan dengan langkah-langkah selanjutnya seperti yang telah Anda berikan sebelumnya.


#4. menampilkan 5 data mengecek kolom yang dihapus
df.head()

#5. data kategori pada kolom purpose
df['Jenis Kelamin'].value_counts()

#6. data kategori pada kolom saving account
# df['Saving accounts'].value_counts()

#7. data kategori pada kolom checking account
# df['Checking account'].value_counts()

#8. data kategori pada kolom housing
df['Pekerjaan'].value_counts()

#9. Menampilkan histogram untuk umur, credit amount dan duration
fig, ax = plt.subplots(figsize=(16, 5))

df['Uang'] = df['Uang'].replace('[\$,]', '', regex=True).astype(float)  # Menghapus simbol mata uang dan mengubah ke tipe data float
df.hist(column='Uang', bins=50, ax=ax)

plt.show()


#10. perbandingan berdasarkan jenis kelamin
sns.countplot(x='Jenis Kelamin', data=df)

#11. jumlah data housing berdasarkan jenis kelamin
sns.countplot(x='Uang', hue='Jenis Kelamin', data=df)

#12. jumlah data purpose berdasarkan jenis kelamin
plt.figure(figsize=(13, 7))
sns.countplot(x='Uang', hue='Jenis Kelamin', data=df, palette='Set2')

#13. jumlah housing berdasarkan purpose

plt.figure(figsize=(13, 7))
sns.countplot(x='Housing', hue='Purpose', data=df, palette='coolwarm')

#14. menampilkan korelasi antar kolom/antar atribut
plt.figure(figsize=(12, 7))
corr = df.corr()
sns.heatmap(corr, annot=True, fmt='.2f')

#15. visualisasi data
sns.pairplot(df)

#16. melihat data pada masing masing atribut
df.info()

#17. menangani missing value
df['Jenis Kelamin'].fillna('little', inplace=True)
df['Uang'].fillna('little', inplace=True)
df['Pekerjaan'].fillna('little', inplace=True)

#18. mendefinisikan fitur dan target
df_features = df.drop('Uang', axis=1)
df_target = df['Uang']

#19. menampilkan kolom fitur
df_features

#20. mengubah tipe data dari data yang memiliki kategori
df_features[['Nama', 'Email', 'Jenis Kelamin', 'Pekerjaan']] = df_features[['Nama', 'Email', 'Jenis Kelamin', 'Pekerjaan']].astype('category')

#cek hasil perubahan
df_features[['Nama', 'Email', 'Jenis Kelamin', 'Pekerjaan']].info()

#21. encoding data dengan .cat.codes
df_features['Nama'] = df_features['Nama'].cat.codes
df_features['Email'] = df_features['Email'].cat.codes
df_features['Jenis Kelamin'] = df_features['Jenis Kelamin'].cat.codes
df_features['Pekerjaan'] = df_features['Pekerjaan'].cat.codes

#22. menampilkan hasil encoding
df_features.tail()

#23. normalisasi data
from sklearn.preprocessing import StandardScaler

x = StandardScaler().fit(df_features).transform(df_features.astype(float))
x[0:5]

#24. definisi target
y = df_target
y[0:5]

#25. bagi data jadi data training dan data test

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

print ('Train set:', x_train.shape, y_train.shape)
print ('Test set:', x_test.shape, y_test.shape)

#26. memodelkan data dg KNN
from sklearn.neighbors import KNeighborsClassifier
k = 5
#train Model
model_knn = KNeighborsClassifier(n_neighbors = k).fit(x_train, y_train)
model_knn

#27. menguji model dg data testing

y_pred = model_knn.predict(x_test)
y_pred[0:5]

#28. menampilkan data testing
y_test[0:5]

#29. mengukur akurasi kinerja machine learning
from sklearn.metrics import accuracy_score

print('Akurasi Train set: ', accuracy_score(y_train, model_knn.predict(x_train)))
print('Akurasi Test set: ', accuracy_score(y_test, y_pred))

#30. mencari nilai K terbaik
Ks = 15
mean_acc = np.zeros((Ks-1))
for n in range(1, Ks):
  #Train model and Predict
  model_knn = KNeighborsClassifier(n_neighbors = n).fit(x_train, y_train)
  y_pred = model_knn.predict(x_test)

  mean_acc[n-1] = accuracy_score(y_test, y_pred)

mean_acc

#31. menvisualisasikan hasil K
plt.plot(range(1, Ks), mean_acc, 'r')
plt.ylabel('Akurasi')
plt.xlabel('Jumlah Tetangga (K)')
plt.tight_layout()
plt.show()

#32. cetak hasil K dengan akurasi terbaik
print('Akurasi terbaik adalah ', mean_acc.max(), 'dengan nilai k =', mean_acc.argmax()+1)