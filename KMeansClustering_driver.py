#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions



glucoseData, hemoglobinData, classificationData = kmc.openckdfile()

kCentroids = kmc.createKCentroids(3)



normGlucose, normHemoglobin = kmc.normalizeData(glucoseData,hemoglobinData)

centroid_assign, distance = kmc.assignKCentroid(kCentroids,normGlucose,normHemoglobin)

mean_array = kmc.updateKCentroid(centroid_assign, normGlucose, normHemoglobin)