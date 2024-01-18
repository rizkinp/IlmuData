import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]
y = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
kelas = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

plt.scatter(x, y, c=kelas, s=25, alpha=0.7)
plt.show()

from sklearn.neighbors import KNeighborsClassifier

data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, kelas)

new_x = 8
new_y = 21
new_point = [(new_x, new_y)]
prediction = knn.predict(new_point)

# plt.scatter(x + [new_x], y + [new_y], c=kelas + [prediction[0]])
# plt.text(x=new_x -1.7, y = new_y -0.7, s=f"new point, class: {prediction[0]}")
# plt.show()

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data, kelas)
predictions = knn.predict(new_point)
plt.scatter(x + [new_x], y + [new_y], c=kelas + [prediction[0]])
plt.text(x=new_x -1.7, y = new_y -0.7, s=f"new point, class: {prediction[0]}")
plt.show()

# X = np.array(list(zip(x, y)))
# y = np.array(kelas)

# k = 3
# knn = KNeighborsClassifier(n_neighbors=k)
# knn.fit(X, y)

# new_point = np.array([[5, 5]])
# print(f'Kelas prediksi: {knn.predict(new_point)}')