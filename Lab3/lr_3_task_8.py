# -*- coding: utf-8 -*-
"""lr_3_task_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12wMtP4NpKeKNzUehGvwYNIYb_8R4uuu-
"""

from sklearn.metrics.cluster import silhouette_samples
# Імпортуємо необхідні бібліотеки
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import pairwise_distances_argmin
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Завантажуємо датасет iris
iris = load_iris()
X = iris.data  # Ознаки
y = iris.target  # Мітки класів

# Ініціалізуємо модель k-середніх з 5 кластерами
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)  # Навчання моделі

# Передбачаємо кластери для вхідних даних
y_kmeans = kmeans.predict(X)

# Візуалізація результатів
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

# Функція для знаходження кластерів, використовуючи pair-wise_distances_argmin
def find_clusters(X, n_clusters, rseed=2):
    rng = np.random.RandomState(rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    while True:
        labels = pairwise_distances_argmin(X, centers)
        new_centers = np.array([X[labels == i].mean(0) for i in range(n_clusters)])
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels

# відображення кластерів
centers, labels = find_clusters(X, 3, rseed=0)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.show()
score = silhouette_score(X,y_kmeans)
print("Силуетний коефіцієнт", score)