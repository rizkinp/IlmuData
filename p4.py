# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import stats as st

# # n = np.array([2, 3, 5, 9, 10, 11, 12, 13, 14, 15 ])
# # print(n)
# # rata = sum(n)/len(n)
# # print(rata)
# # median = np.median(rata)
# # print(median)

# # # modes, counts = np.unique(n, return_counts=True)
# # # max_count = np.max(counts)
# # # mode = modes[counts == max_count]
# # # print("Modus:", mode)
# np.random.seed(10)
# nilai = np.random.randint(70, 100, 30)
# print("Nilai:", nilai)

# print("================================================================")
# mean = np.mean(nilai)
# print("Mean (Rata-rata):", mean)

# print("================================================================")
# median = np.median(nilai)
# print("Median:", median)

# print("================================================================")
# try:
#     mode = st.mode(nilai)
#     print("Modus:", mode)
# except st.StatisticsError:
#     print("Tidak ada modus tunggal dalam data ini.")

# plt.hist(nilai)
# plt.show()

# print("================================================================")
# y = np.random.uniform(1.0, 90.0, 20)
# print(y)

# print("================================================================")

# mean = np.mean(y)
# print("Mean (Rata-rata):", mean)

# print("================================================================")
# median = np.median(y)
# print("Median:", median)

# print("================================================================")
# try:
#     mode = st.mode(y)
#     print("Modus:", mode)
# except st.StatisticsError:
#     print("Tidak ada modus tunggal dalam data ini.")

# plt.hist(y)
# plt.show()


# import warnings
# warnings.filterwarnings('ignore')
# import pandas as pd

# d = {'Nama' : pd.Series(['Rina', 'Rizki', 'Amel', 'Retha', 'Nadine']), 'Age' : pd.Series([18, 19, 20, 21, 22]), 'Nilai' : pd.Series([99, 98, 97, 96, 95])}
# df = pd.DataFrame(d)
# print(df)
# print(df.sum())
# print(df.mean())

# import warnings
# warnings.filterwarnings('ignore')
# import pandas as pd
# import numpy as np

# d = {'Nama' : pd.Series(['Rina', 'Rizki', 'Amel', 'Retha', 'Nadine']), 'Age' : pd.Series([18, 19, 20, 21, 22]), 'Nilai' : pd.Series([99, 98, 97, 96, 95])}

# df = pd.DataFrame(d)

# # Memilih kolom numerik
# numeric_cols = df.select_dtypes(include=[np.number])

# # Melakukan pengurangan pada kolom numerik
# print(numeric_cols.sum())
# print("Mean: ", numeric_cols.mean())
# print("Maksimal: ", numeric_cols.max())
# print("Minimal: ",numeric_cols.min())
# print("================================================================")
# print(numeric_cols.describe())


# import seaborn as sns
# import pandas as pd
# df=pd.read_csv('tekanandarah.csv')
# print(df)
# print(df.shape)
# print(df.head(10))
# print(df.info)
# print(df.isnull().sum())
# print(df.describe())
# print(df.describe(include=['object']))
# print(df.describe(include='all'))
# print(df['bp_before'].describe())
# print(df['bp_after'].describe())
# print(df['bp_before'].mean())
# print(df['bp_after'].mean())
# print(df['sex'].describe())
# print(df['sex'].value_counts())
# e = df['bp_before'].kurtosis()
# print(e)
# f = df['bp_after'].skew()
# print(f)
# mean = df['bp_before'].mean()
# print(mean)
# median = df['bp_after'].median()
# print(median)
# mode = df['bp_before'].mode()
# print(mode)
# data = df['bp_before']
# sns.distplot(data, bins=10, hist=True, kde=True, label = 'bp_before')




import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tekanandarah.csv')

print(df)
print(df.shape)
print(df.head(10))
print(df.info()) 
print(df.isnull().sum())
print(df.describe())
print(df.describe(include=['object']))
print(df.describe(include='all'))
print(df['bp_before'].describe())
print(df['bp_after'].describe())
print(df['bp_before'].mean())
print(df['bp_after'].mean())
print(df['sex'].describe())
print(df['sex'].value_counts())
e = df['bp_before'].kurtosis()
print("Kurtosis bp_before:", e)
f = df['bp_after'].skew()
print("Skew bp_after:", f)
mean = df['bp_before'].mean()
print("Mean bp_before:", mean)
median = df['bp_after'].median()
print("Median bp_after:", median)
mode = df['bp_before'].mode()
print("Mode bp_before:", mode)
data = df['bp_before']
sns.distplot(data, bins=10, hist=True, kde=True, label='bp_before')
plt.show()




















