# K-MAENS
<h2>Clustering </h2>
Clustering is one of the most common exploratory data analysis technique used to get an intuition about the structure of the data. It can be defined as the task of identifying subgroups in the data such that data points in the same subgroup (cluster) are very similar while data points in different clusters are very different. In other words, we try to find homogeneous subgroups within the data such that data points in each cluster are as similar as possible according to a similarity measure such as euclidean-based distance or correlation-based distance. The decision of which similarity measure to use is application-specific.

<h2>K-means</h2>
Kmeans algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups (clusters) where each data point belongs to only one group. It tries to make the inter-cluster data points as similar as possible while also keeping the clusters as different (far) as possible. It assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s centroid (arithmetic mean of all the data points that belong to that cluster) is at the minimum. The less variation we have within clusters, the more homogeneous (similar) the data points are within the same cluster.<br>

The way kmeans algorithm works is as follows:<br><br>
1.Specify number of clusters K.<br>
2.Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.<br>
3.Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.<br>
4.Compute the sum of the squared distance between data points and all centroids.<br>
5.Assign each data point to the closest cluster (centroid).<br>
6.Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster.<br>
