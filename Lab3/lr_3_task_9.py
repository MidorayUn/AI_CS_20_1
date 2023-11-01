# -*- coding: utf-8 -*-
"""lr_3_task_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rUbId2F4mgfNGimoJZFlMiBPKDANXqMd
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle
from sklearn.metrics import silhouette_score

# Завантаження вхідних даних
X = np.loadtxt('data_clustering.txt', delimiter=',')

# Оцінка ширини вікна для X
bandwidth_X = estimate_bandwidth(X, quantile=0.1, n_samples=len(X))

# Кластеризація даних методом зсуву середнього
meanshift_model = MeanShift(bandwidth=bandwidth_X, bin_seeding=True)
meanshift_model.fit(X)

# Витягнення центрів кластерів
cluster_centers = meanshift_model.cluster_centers_
print('\nЦентри кластерів:\n', cluster_centers)

# Оцінка кількості кластерів
labels = meanshift_model.labels_
num_clusters = len(np.unique(labels))
print("\nКількість кластерів у вхідних даних =", num_clusters)

# Створення кольорового циклу для побудови графіку
colors = cycle(plt.cm.tab20(np.linspace(0, 1, num_clusters)))

# Створення фігури та вісей для графіку
fig, ax = plt.subplots()

# Побудова кожного кластера
for i, col in zip(range(num_clusters), colors):
    cluster_points = X[labels == i]
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], c=[col], marker='o', label=f'Кластер {i}')

# Побудова центрів кластерів
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=100, label='Центри кластерів')

# Встановлення підписів та назви графіку
ax.set_xlabel('Ознака 1')
ax.set_ylabel('Ознака 2')
ax.set_title('Результати кластеризації')

# Додавання легенди
ax.legend()

# Відображення графіку
plt.show()

# Розрахунок та виведення на екран значення коефіцієнта силуету
silhouette_avg = silhouette_score(X, labels)
print("Значення коефіцієнта силуету:", silhouette_avg)