from sklearn.cluster import DBSCAN
from matplotlib.backends.backend_pgf import PdfPages
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import heapq as hq
import matplotlib
folder_path = 'plots/'


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted {filename}")

data = [] 
dat = []

with open('scores.txt', 'r') as file:
    for line in file:
        if line.startswith("#"):
            data.append(dat)
            dat=[]
        else:
            dat.append(float(line.split(" ")[1]))
    # data.append(hq.nlargest(50,dat))
    data.append(dat)

fig, axes = plt.subplots(nrows=2, ncols=5, figsize =(8,4))

data=data[1:]
for i, ax in enumerate(axes.flat):
    if i < 10:
        X = np.array(data[i]).reshape(-1, 1)

        # Fit the DBSCAN model to the data
        dbscan = DBSCAN(eps=5, min_samples=5)
        dbscan.fit(X)

        # Get the labels assigned to each sample
        labels = dbscan.labels_
        # print(labels)

        # Get the indices of the outlier samples
        outlier_indices = np.where(labels == -1)[0]

        # Create a scatter plot of the data points
        plt.scatter(data[i],np.zeros(len(data[i])),)

        ax.set_yticklabels([])
        ax.set_xticklabels([])
        # Highlight the outliers in red
        ax.scatter(data[i], np.zeros(len(data[i])), color='blue')
        ax.scatter([data[i][j] for j in outlier_indices], np.zeros(len(outlier_indices)), color='red')

        # Add axis labels and a title
    else:
        ax.axis('off')

   
  # Show the plot
plt.show()
# plt.savefig("cluster-plots/dbscan.pgf")

