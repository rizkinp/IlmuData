import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2. read data
df = pd.read_csv('german_credit_data.csv')
df.head(10)

#3. preprocesing menghapus kolom unnamed
df.drop('Unnamed: 0', axis=1, inplace=True)

#4. menampilkan 5 data mengecek kolom yang dihapus
df.head()

#5. data kategori pada kolom purpose
df['Purpose'].value_counts()

#6. data kategori pada kolom saving account
df['Saving accounts'].value_counts()

#7. data kategori pada kolom checking account
df['Checking account'].value_counts()

#8. data kategori pada kolom housing
df['Housing'].value_counts()

#9. Menampilkan histogram untuk umur, credit amount dan duration
fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(16,5))

ax0 = fig.add_subplot(ax[0])
ax1 = fig.add_subplot(ax[1])
ax2 = fig.add_subplot(ax[2])

df.hist(column='Age', bins=50, ax=ax0)

df.hist(column='Credit amount', bins=50, ax=ax1)

df.hist(column='Duration', bins=50, ax=ax2)

plt.subplots_adjust(wspace=0.2)
plt.show()

#10. perbandingan berdasarkan jenis kelamin
sns.countplot(x='Sex', data=df)

#11. jumlah data housing berdasarkan jenis kelamin
sns.countplot(x='Housing', hue='Sex', data=df)

#12. jumlah data purpose berdasarkan jenis kelamin
plt.figure(figsize=(13, 7))
sns.countplot(x='Purpose', hue='Sex', data=df, palette='Set2')

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
df['Saving accounts'].fillna('little', inplace=True)
df['Checking account'].fillna('little', inplace=True)

#18. mendefinisikan fitur dan target
df_features = df.drop('Purpose', axis=1)
df_target = df['Purpose']

#19. menampilkan kolom fitur
df_features

#20. mengubah tipe data dari data yang memiliki kategori
df_features[['Sex', 'Housing', 'Saving accounts', 'Checking account']] = df_features[['Sex', 'Housing', 'Saving accounts', 'Checking account']].astype('category')

#cek hasil perubahan
df_features[['Sex', 'Housing', 'Saving accounts', 'Checking account']].info()

#21. encoding data dengan .cat.codes
df_features['Sex'] = df_features['Sex'].cat.codes
df_features['Housing'] = df_features['Housing'].cat.codes
df_features['Saving accounts'] = df_features['Saving accounts'].cat.codes
df_features['Checking account'] = df_features['Checking account'].cat.codes

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