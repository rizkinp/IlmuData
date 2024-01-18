# from cProfile import label
# import pandas as pd
# import numpy as np

# np.random.seed(100)
# age = pd.DataFrame({'Age' : np.random.randint(0, 100, 100)})
# #2
# print(age)

# # #3
# # Menampilkan 10 data teratas
# print(age.head(10))

# # # Menampilkan 10 data terbawah
# print(age.tail(10))


# # 4 kategorikan pada data frame diatas dengan perintah
import pandas as pd
import numpy as np

np.random.seed(100)
age = pd.DataFrame({'Age' : np.random.randint(0, 100, 100)})

# Memotong data menjadi kategori
a = pd.cut(age['Age'], [0, 2, 11, 20, 61, 101])
print (age.head(10))

# Menampilkan 10 data pertama setelah dipotong menjadi kategori
print(a.head(10))


# np.random.seed(100)
# age = pd.DataFrame({'Age' : np.random.randint(0, 100, 100)})
# b = pd.cut(age['Age'], [0, 2, 11, 20, 61, 101], labels = [
#     'Bayi', 'Anak-anak', 'Remaja', 'Dewasa', 'Manula'])
# print(b.head(10))

# # 6. buatlah grafik kategori umur dengan perintah
# import matplotlib.pyplot as plt
# age.plot(kind = 'hist', bins = [0, 2, 11, 20, 61, 101], figsize = (8,5))
# plt.grid()
# plt.show()

# # 7. buat 1 kolom untuk menaruh data kategori
# import pandas as pd
# import numpy as np

# np.random.seed(100)
# age = pd.DataFrame({'Age' : np.random.randint(0, 100, 100)})

# # Membuat kolom 'range' dengan interval
# age['range'] = pd.cut(age['Age'], [0, 2, 11, 20, 61, 101])

# # Membuat kolom 'group' dengan label
# age['group'] = pd.cut(age['Age'], [0, 2, 11, 20, 61, 101],
#         labels=['bayi', 'anal-anak', 'Remaja', 'Dewasa', 'Lanjut Usia'])

# # Menampilkan DataFrame dengan kedua kolom baru
# print(age.head(10))

# #8.
# print(age.head(10))

# #9.
# category_counts = age['group'].value_counts()
# print(category_counts)