#Please place your DRIVER code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

num_centroids = 2

glucose_data, hemoglobin_data, classification_data = kmc.openckdfile()

norm_glucose, norm_hemoglobin = kmc.normalizeData(glucose_data,hemoglobin_data)

centroids = kmc.createCentroids(num_centroids) #Select random centroids

while True: #This will interate the process
    
    
    centroid_assign = kmc.assignCentroid(centroids,norm_glucose,norm_hemoglobin)
    #Assign each data point to a centroid
    
    mean_array = kmc.calculateMean(centroid_assign, norm_glucose, norm_hemoglobin)
    #Create an array of the means of each cluster of data points
    
    if np.array_equal(centroids,mean_array): #Check to see if the centroids
                                             #will change
        break                                #If it doesn't, leave the loop

    centroids = mean_array
    #Reassign the means of each cluster to be the new centroids



    
kmc.plotClusters(centroids, centroid_assign, norm_glucose, norm_hemoglobin)
print(centroids)
print(centroid_assign)
