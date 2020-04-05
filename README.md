This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

## Nearest Neighbor and K-Nearest Neighbor


Related Files: NearestNeighborClassification.py

NearestNeighborClassification.py contains functions to classify a unknown observation using the nearest neighbor or k-nearest neighbor methods.

The main body currently contains code to open ckd.csv (also in this repository), normalize the data, graph the normalized data, create a random test case, 
classify the test case with both nearest neighbor and k-nearest neighbor, and then recreate the graph with the test case added.
If you want to classify your own unknown observation, replacing new_glucose and new_hemoglobin in the function calls in lines 183 and 188 to your own 
normalized values will cause the code to print out the classification using both methods.


Functions in NearestNeighborClassification.py:

normalizeData(glucose, hemoglobin, classification)
- normalizeData normalizes the data to be on a 0 to 1 unitless scale
- It takes in two arguments
        - glucose is an array of the original glucose values
        - hemoglobin is an array of the original hemoglobin values
        - classification is an array of the original classification values
- It returns an three arrays: 
        - normal_glucose is an array of the the normalized glucose 
        - normal_hemoglobin is an array of the normalized hemoglobin values
        - normal_class is an array of the normalized classification values

graphData(glucose, hemoglobin, classification)    
-graphData graphs the normalized data; each classification has a different color
-It takes in three arguments:
        -glucose is an array of the normalized glucose values
        -hemoglobin is an array of the normalied hemoglobin values
        -classification is an array that represents each data point's classification
-It doesn't return anything
   

createTestCase()
-createTestCase creates a new test case
-It doesn't take any arguments
-It returns two integers:
        -new_hemoglobin represents the hemoglobin value of the test case
        -new_glucose represents the glucose value of the test case


calculateDistanceArray(glucose_test, hemoglobin_test, glucose, hemoglobin)
-calculateDistanceArray calculates the distance between each data point and the test case
-It takes in four arguments:
        -glucose_test is the glucose value of the test case
        -hemoglobin_test is the hemoglobin value of the test case
        -glucose is the array of the normalized glucose values
        -hemoglobin is the array of the normalized hemoglobin values
-It returns an array of the distance from the test case to each data point


nearestNeighborClassifier(glucose_test,hemoglobin_test, glucose, hemoglobin, classification)
-nearestNeighborClassifier classifies a test case using the nearest neighbor method
-It takes five arguments:
        -glucose_test is the glucose value of the test case
        -hemoglobin_test is the hemoglobin value of the test case
        -glucose is the array of the normalized glucose values
        -hemoglobin is the array of the normalized hemoglobin values
        -classification is an array that represents each data point's classification
-It returns an interger representing the classification of the nearest neighbor


graphTestCase(glucose_test, hemoglobin_test, glucose, hemoglobin, classification)
-graphData graphs the normalized data and the test case
-It takes in five arguments:
        -glucose_test is the glucose value of the test case
        -hemoglobin_test is the hemoglobin value of the test case      
        -glucose is an array of the normalized glucose values
        -hemoglobin is an array of the normalied hemoglobin values
        -classification is an array that represents each data point's classification
-It doesn't return anything


kNearestNeighborClassifier(k,glucose_test,hemoglobin_test,glucose,hemoglobin,classification)
-kNearestNeighborClassifier classifies a test case using the k-nearest neighbor method
-It takes six arguments:
	-k is the number of neighbors that should be looked at; it should be odd
        -glucose_test is the glucose value of the test case
        -hemoglobin_test is the hemoglobin value of the test case
        -glucose is the array of the normalized glucose values
        -hemoglobin is the array of the normalized hemoglobin values
        -classification is an array that represents each data point's classification
-It returns an interger representing the classification of the nearest neighbor





## K-Means Clustering


Related Files: KMeansClustering_driver.py, KMeansClustering_functions.py

KMeansClustering_driver.py contains the main body of the code for the k-means clustering algorithm
KMeansClustering_functions.py contains the functions that KMeansClustering_driver.py calls

KMeansClustering_driver.py currently contains code to open ckd.csv (also in this repository) and then use the data contained to perform the k-means
clustering algorithm with 2 clusters. A graph is then generated, showing the clusters and the centroids. The arrays representing the centroids and  All of the functions currently operate 
under the assumption that only two feature were recorded about each observation. To change the number of clusters, change the num_centroids variable in
line 5 of KMeansClustering_driver.py. The general algorithm should work for up to ~15 clusters. However, plotClusters in KMeansClustering_functions.py 
can only support four clusters currently. Changing the number of features of an observation would require new variables to be introduced and the functions
would need new parameters and some would need to be reworked (e.g. the 2-D distance formula would need to be changed to 3-D)


Functions in KMeansClustering_functions.py:

createCentroids(k)   
    -createCentroids makes random centroids to start the algorithm
    -It takes in one argument:
        -k is an integer representing the number of centroids to be created
-It returns an array representing the centroids


normalizeData(glucose, hemoglobin)   
-normalizeData normalizes the data to be on a 0 to 1 unitless scale
-It takes in two arguments
        -glucose is an array of the original glucose values
        -hemoglobin is an array of the original hemoglobin values
-It returns an two arrays: the normalized glucose and hemoglobin values


assignCentroid(centroids, glucose, hemoglobin)
-assignCentroids assigns a centroid to each data point
-It takes in three arguments
            -centroids is an array representing the location of the centroids
            -glucose is an array of the normalized glucose values
            -hemoglobin is an array of the normalized hemoglobin values
-It returns an array that shows which centroid each data point is assigned to


calculateMean(centroid_assign, glucose, hemoglobin)
-calculateMean calculates the mean of the data associated to each centroid
-It takes in three arguments:
        -centroid_assign is an array that shows which centroid each data point is assigned to
        -glucose is an array of the normalized glucose values
        -hemoglobin is an array of the normalized hemoglobin values
-It returns an array representing the mean values of each cluster


plotClusters(centroids,centroid_assignment, glucose, hemoglobin)    
-plotClusters plots the data with different colors and symbols to represent each cluster
-It takes in four arguments:
        -centroids is an array representing the location of the centroids
        -centroid_assignment is an array that shows which centroid each data point is assigned to
        -glucose is an array of the normalized glucose values
        -hemoglobin is an array of the normalized hemoglobin values
-It doesn't return anything


















