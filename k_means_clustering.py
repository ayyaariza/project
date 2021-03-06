# -*- coding: utf-8 -*-
"""K-Means Clustering

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EeS5f9UM85DS2qfASUbH6CmGIax-ue7S
"""

#Kelompok 7:

#Anggit Daneswara Purbaningrum (M0118009)
#Ayya Agustina Riza (M0118020)
#Yuriska Christina A. S (M0118072)
#Bayu Purboutomo (M0119016)
#Jasmine Laksmi Maharani (M0119047)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('DATA DBD JATENG_.xlsx')
data

data = data.drop(['No'], axis = 1)
data

data.info()

data_k = data.drop(['Kabupaten/ Kodya'], axis = 1)
data_k

x_array=np.array(data_k)
print(x_array)

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)
x_scaled

Kmeans = KMeans(n_clusters = 5, random_state=123)

Kmeans.fit(x_scaled)

print(Kmeans.cluster_centers_)

data['cluster'] = Kmeans.labels_

import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

reduced_data = PCA(n_components=2).fit_transform(x_scaled)
results = pd.DataFrame(reduced_data,columns=['PCA 1','PCA 2'])
results

output = plt.scatter(results['PCA 1'], results['PCA 2'], s = 100, c = data.cluster, marker = 'o', alpha = 1)
centers =Kmeans.cluster_centers_

plt.scatter(centers[:,0], centers[:,1], c='red', s=200, alpha=1 , marker='o');

plt.title('Hasil K-Means Clustering')
plt.colorbar(output)
plt.show()

y_Kmeans = Kmeans.fit_predict(data_k)
y_Kmeans

data

#K-Means Clustering dengan jumlah custer 5 diperoleh hasil sebagai berikut
#Cluster 0: Wonosobo, Wonogiri, Kota Magelang, Kota Salatiga, Kota Pekalongan, dan Kota Tegal
#Cluster 1: Cilacap, Banyumas, Klaten, Sragen, Kudus, Jepara, Semarang, Batang, Pemalang, dan Brebes
#Cluster 2: Karanganyar, Grobogan, Pati, Demak, Temanggung, Kota Semarang
#Cluster 3: Blora dan Rembang
#Cluster 4: Purbalingga, Banjarnegara, Kebumen, Purworejo, Magelang, Boyolali, Sukoharjo, Kendal, Pekalongan, Tegal,dan Kota Surakarta