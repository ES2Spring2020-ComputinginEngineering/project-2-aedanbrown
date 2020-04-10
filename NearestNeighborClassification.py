#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def normalizeData(glucose, hemoglobin, classification):

    #normalizeData normalizes the data to be on a 0 to 1 unitless scale
    #It takes in two arguments
        #glucose is an array of the original glucose values
        #hemoglobin is an array of the original hemoglobin values
        #classification is an array of the original classification values
    #It returns an three arrays: 
        #normal_glucose is an array of the the normalized glucose 
        #normal_hemoglobin is an array of the normalized hemoglobin values
        #normal_class is an array of the normalized classification values
    
    normal_glucose = (glucose-glucose.min())/(glucose.max()-glucose.min())
    normal_hemoglobin = ((hemoglobin-hemoglobin.min())/
                                    (hemoglobin.max() - hemoglobin.min()))
    normal_class = ((classification - classification.min())/
                                (classification.max() - classification.min()))
    return normal_glucose, normal_hemoglobin, normal_class


def graphData(glucose, hemoglobin, classification):
    
    #graphData graphs the normalized data; each classification has a different color
    #It takes in three arguments:
        #glucose is an array of the normalized glucose values
        #hemoglobin is an array of the normalied hemoglobin values
        #classification is an array that represents each data point's classification
    #It doesn't return anything
    
    plt.figure()
    plt.suptitle("Normalized Glucose vs Normalized Hemoglobin")
    plt.plot(hemoglobin[classification==1],glucose[classification==1], 
                                                 "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], 
                                                 "r.", label = "Class 0")
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalized Glucose")
    plt.legend()
    plt.show()
 
    
def createTestCase():
    
    #createTestCase creates a new test case
    #It doesn't take any arguments
    #It returns two integers:
        #new_hemoglobin represents the hemoglobin value of the test case
        #new_glucose represents the glucose value of the test case
    
    new_hemoglobin = random.randrange(0,10000)/10000
    new_glucose = random.randrange(0,10000)/10000

    return new_hemoglobin, new_glucose


def calculateDistanceArray(glucose_test, hemoglobin_test, glucose, hemoglobin):
    
    #calculateDistanceArray calculates the distance between each data point and the test case
    #It takes in four arguments:
        #glucose_test is the glucose value of the test case
        #hemoglobin_test is the hemoglobin value of the test case
        #glucose is the array of the normalized glucose values
        #hemoglobin is the array of the normalized hemoglobin values
    #It returns an array of the distance from the test case to each data point
    
    distance = np.sqrt((glucose-glucose_test)**2 + (hemoglobin-hemoglobin_test)**2)
    #Calculate the distance between the test point and each data point
    
    return distance


def nearestNeighborClassifier(glucose_test,hemoglobin_test, glucose, hemoglobin, classification):
    
    #nearestNeighborClassifier classifies a test case using the nearest neighbor method
    #It takes five arguments:
        #glucose_test is the glucose value of the test case
        #hemoglobin_test is the hemoglobin value of the test case
        #glucose is the array of the normalized glucose values
        #hemoglobin is the array of the normalized hemoglobin values
        #classification is an array that represents each data point's classification
    #It returns an interger representing the classification of the nearest neighbor
    
    distance = calculateDistanceArray(glucose_test, hemoglobin_test, glucose, hemoglobin)

    min_index = np.argmin(distance) #Find index of the minimum distance
    
    return classification[min_index] #Find the classification at that index


def graphTestCase(glucose_test, hemoglobin_test, glucose, hemoglobin, classification):
    
    #graphData graphs the normalized data and the test case
    #It takes in five arguments:
        #glucose_test is the glucose value of the test case
        #hemoglobin_test is the hemoglobin value of the test case      
        #glucose is an array of the normalized glucose values
        #hemoglobin is an array of the normalied hemoglobin values
        #classification is an array that represents each data point's classification
    #It doesn't return anything
    
    
    classification_num = nearestNeighborClassifier(new_glucose, new_hemoglobin, 
                                                  glucose, hemoglobin, 
                                                  classification)
    #Find the classification
    
    
    
    plt.figure()
    plt.suptitle("Normalized Glucose vs Normalized Hemoglobin")
    plt.plot(hemoglobin[classification==1],glucose[classification==1],
                                                     "k.", label = "Class 1", 
                                                     alpha = 0.3)
    plt.plot(hemoglobin[classification==0],glucose[classification==0], 
                                                     "r.", label = "Class 0", 
                                                     alpha = 0.3)
    if classification_num == 1:
        plt.plot(hemoglobin_test, glucose_test, "kx", label = "Test Case", 
                                                             markersize = 10)
    else:
        plt.plot(hemoglobin_test, glucose_test, "rx", label = "Test Case", 
                                                             markersize = 10)
    
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalized Glucose")
    plt.legend()
    plt.show()
    



def kNearestNeighborClassifier(k,glucose_test,hemoglobin_test,glucose,hemoglobin,classification):
    
    #kNearestNeighborClassifier classifies a test case using the k-nearest neighbor method
    #It takes six arguments:
        #k is the number of neighbors that should be looked at; it should be odd
        #glucose_test is the glucose value of the test case
        #hemoglobin_test is the hemoglobin value of the test case
        #glucose is the array of the normalized glucose values
        #hemoglobin is the array of the normalized hemoglobin values
        #classification is an array that represents each data point's classification
    #It returns an interger representing the classification of the nearest neighbor
   
    
    distance = calculateDistanceArray(glucose_test, hemoglobin_test, glucose, hemoglobin)
    
    sorted_dist = np.argsort(distance) #Get the array of the sorted indices
    
    classification_list = []
    
    for i in range(k):
        classification_list.append(classification[sorted_dist[i]])
        #Add the classification at the index of ith value in the array of
        #sorted indices
    
    if classification_list.count(1) > classification_list.count(0):
        return 1.0
    else:
        return 0.0
    
# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

norm_glucose, norm_hemoglobin, norm_classification = normalizeData(glucose,hemoglobin,classification)
#Normalize the data

graphData(norm_glucose, norm_hemoglobin, classification)
#Graph the normalized data

new_hemoglobin, new_glucose = createTestCase()
#Create a new test case

classification_number = nearestNeighborClassifier(new_glucose, new_hemoglobin, 
                                                  norm_glucose, norm_hemoglobin, 
                                                  norm_classification)
#Find the classification of the test case using the single closest neighbor

classification_number_k = kNearestNeighborClassifier(5, new_glucose, 
                                                     new_hemoglobin, norm_glucose, 
                                                     norm_hemoglobin, norm_classification)
#Find the classification of the test case using the k closest neighbors 

graphTestCase(new_glucose, new_hemoglobin,
                                      norm_glucose, norm_hemoglobin, norm_classification)
#Graph the data and test case

print("Nearest Neighbor: ", classification_number)
print("K-nearest Neighbor: ", classification_number_k)
