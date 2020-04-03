#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

num_centroids = 2

glucoseData, hemoglobinData, classificationData = kmc.openckdfile()

kCentroids = kmc.createKCentroids(num_centroids)

normGlucose, normHemoglobin = kmc.normalizeData(glucoseData,hemoglobinData)


while True:
    

    centroid_assign = kmc.assignKCentroid(kCentroids,normGlucose,normHemoglobin)
   
    kmc.plot(kCentroids,centroid_assign,normGlucose,normHemoglobin)
    
    mean_array = kmc.updateKCentroid(centroid_assign, normGlucose, normHemoglobin)
    
    if np.array_equal(kCentroids,mean_array):
        break

    kCentroids = mean_array
#    print(kCentroids)
    



    
kmc.plot(kCentroids, centroid_assign, normGlucose, normHemoglobin)

print(kCentroids, "\n", centroid_assign)