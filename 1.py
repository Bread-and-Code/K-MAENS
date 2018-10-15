from sklearn import cluster
from nltk  import cluster
# from nltk import 
import sklearn
import numpy
import nltk


NUM_CLUSTER = 7
hhhhhh =   nltk.cluster.kmeans.KMeansClusterer(NUM_CLUSTER,distance=nltk.cluster.util.cosine_distance,repeats=100)
print(hhhhhh)