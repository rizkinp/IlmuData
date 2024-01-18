# try :
#     import matplotlib.pyplot as plt
#     print ("import matplotlib successfully")
# except ModuleNotFoundError:
#     print ("import matplotlib failed")
    

# import matplotlib as plt

# print(" Versi matplotlab: " + plt.__version__)


# import matplotlib.pyplot as plt

# x = [2, 4, 6, 8, 10]
# y = [3, 5, 1, 2, 9]

# plt.plot(x, y)
# plt.show()


# import matplotlib.pyplot as plt
# x = [2, 4, 5]
# y = [5, 1, 9]

# plt.plot(x, y, 'o')
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 3, 6 ])
# ypoints = np.array([0, 100, 250])

# print('x points: ', xpoints )

# print('y points: ', ypoints )

# plt.plot(xpoints, ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 50, 150])
# ypoints = np.array([1, 3, 6])

# plt.plot(xpoints, ypoints, linestyle='dotted', label='Dotted Line')
# plt.plot(xpoints, ypoints, linestyle='dashed', label='Dashed Line')
# plt.plot(xpoints, ypoints, linestyle='dashdot', label='Dashdot Line')

# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([1, 3, 6, 5])
# xpoints = np.array([0, 1, 2, 3])

# plt.subplot(1, 2, 1)
# plt.plot(xpoints, ypoints, linestyle='dotted')
# plt.title('Dotted Line')

# plt.subplot(1, 2, 2)
# plt.plot(xpoints, ypoints)
# plt.title('Default Line')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Data untuk grafik pertama
# x1 = np.array([1, 2, 3, 4, 5])
# y1 = np.array([1, 4, 9, 16, 25])

# # Data untuk grafik kedua
# x2 = np.array([1, 2, 3, 4, 5])
# y2 = np.array([9, 3, 5, 1, 4])

# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)
# plt.title('Grafik 1: y = x^2')

# plt.subplot(2, 1, 2)
# plt.plot(x2, y2)
# plt.title('Grafik 2: y = 6 - x')

# plt.tight_layout() 
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([1, 2, 3, 4, 5])
# y1 = np.array([1, 4, 9, 16, 25])

# x2 = np.array([1, 2, 3, 4, 5])
# y2 = np.array([5, 4, 3, 2, 1])

# x3 = np.array([0, 1, 2, 3, 4])
# y3 = np.array([0, 2, 4, 6, 8])

# x4 = np.array([0, 1, 2, 3, 4])
# y4 = np.array([3, 1, 4, 2, 5])

# plt.subplot(2, 2, 1)
# plt.plot(x1, y1)
# plt.title('Grafik 1')

# plt.subplot(2, 2, 2)
# plt.plot(x2, y2)
# plt.title('Grafik 2')

# plt.subplot(2, 2, 3)
# plt.plot(x3, y3)
# plt.title('Grafik 3')

# plt.subplot(2, 2, 4)
# plt.plot(x4, y4)
# plt.title('Grafik 4')

# plt.tight_layout()
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 30, 100)
# y1 = np.cos(x)
# y2 = np.sin(x)
# y3 = np.cos(x*2)
# fig, ax = plt.subplots(figsize=(10, 6))

# ax.plot(x, y1, color = 'red')
# ax.plot(x, y2, color = 'blue')
# ax.plot(x, y3, color = 'yellow')
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 3, 5, 7, 9])
# y1 = np.array([2, 1, 5 , 0, 9 ])
# y2 = np.array([1, 2, 3, 4, 5])
# y3 = np.array([2, 6 , 10, 14, 18 ])

# fig, ax = plt.subplots(figsize=(10, 20))
# ax.plot(x, y1, color = 'red', marker='o')
# ax.plot(x, y2, color = 'blue', marker='*')
# ax.plot(x, y3, color = 'green', marker='+')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-v0_8-pastel')
# x = np.linspace(0, 30, 100)
# y1 = np.cos(x)
# y2 = np.sin(x)
# y3 = np.cos(x*2)
# fig, ax = plt.subplots(figsize=(10, 6))

# ax.plot(x, y1)
# ax.plot(x, y2)
# ax.plot(x, y3)

# plt.show()
# fig.savefig('contohvisualisasi.png')

# from PIL import Image
# img = Image.open('contoh_visualisasi.png')
# img.show()

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [32, 76, 30, 57, 28, 90, 66, 34, 45, 26]

# plt.figure(figsize=(12, 6)) #merubah ukuran grafik
# plt.plot(x, y)
# plt.xlabel("Sumbu X") #memberikan nama pada label x
# plt.ylabel("Sumbu Y") #memberikan nama pada label y
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["2005", "2010", "2015", "2020"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
# y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
# plt.scatter(x, y)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([25, 30, 35, 10])

# plt.pie(y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([25, 30, 35, 10])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([25, 30, 35, 10])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels, startangle = 45)
# plt.show()








# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([25, 30, 35, 10])
# nama = ["Apel", "Jeruk", "Mangga", "Melon"]
# pisah = [0.1, 0, 0, 0]
# plt.pie(y, labels = nama, explode = pisah, shadow = True)
# plt.legend(title = 'nama buah')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
X = np.linspace(0, 30, 100) #membuat 1 set angka dengan spasi merata dalam interval yang telah ditentukan
y1 = np.cos(X*2)
y2 = np.cos(X)
y3 = np.sin(X/3)
y4 = np.sin(X)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(X, y1)
ax.plot(X, y2)
ax.plot(X, y3)
ax.plot(X, y4)
plt.show()
