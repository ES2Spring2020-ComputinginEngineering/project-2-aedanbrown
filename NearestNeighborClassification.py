#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):

    normalGlucose = (glucose-glucose.min())/(glucose.max()-glucose.min())
    normalHemoglobin = (hemoglobin-hemoglobin.min())/(hemoglobin.max() - hemoglobin.min())
    normalClassification = (classification-classification.min())/(classification.max()-classification.min())
    
    return normalGlucose, normalHemoglobin, normalClassification

def graphData(glucose, hemoglobin, classification):
    
    plt.figure()
    plt.suptitle("Normalized Glucose vs Normalized Hemoglobin")
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalized Glucose")
    plt.legend()
    plt.show()
    
def createTestCase():
    
    newHemoglobin = random.randrange(0,10000)/10000
    newGlucose = random.randrange(0,10000)/10000

    return newHemoglobin, newGlucose

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    
    distance = np.sqrt((glucose-newglucose)**2 + (hemoglobin-newhemoglobin)**2)
    
    return distance

def nearestNeighborClassifier(newglucose,newhemoglobin, glucose, hemoglobin, classification):
    
    distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    
    min_index = np.argmin(distance)
    
    return classification[min_index]

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    
    classification_number = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
    
    
    plt.figure()
    plt.suptitle("Normalized Glucose vs Normalized Hemoglobin")
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(newhemoglobin, newglucose, "bo", label = "Test Case")
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalized Glucose")
    plt.legend()
    plt.show()
    
    return classification_number



def kNearestNeighborClassifier(k,newglucose,newhemoglobin,glucose,hemoglobin,classification):
    
    distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    
    sorted_dist = np.argsort(distance)
    
    classification_list = []
    
    for i in range(k):
        classification_list.append(classification[sorted_dist[i]])
    
    if classification_list.count(1) > classification_list.count(0):
        return 1
    else:
        return 0
    
# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

norm_glucose, norm_hemoglobin, norm_classification = normalizeData(glucose,hemoglobin, classification)

graphData(norm_glucose, norm_hemoglobin, norm_classification)

newHemoglobin, newGlucose = createTestCase()

classification_number = graphTestCase(newGlucose, newHemoglobin, norm_glucose, norm_hemoglobin, norm_classification)

classification_number_k = kNearestNeighborClassifier(5,newGlucose, newHemoglobin, norm_glucose, norm_hemoglobin, norm_classification)

#plt.figure()
#plt.suptitle("Glucose vs Hemoglobin")
#plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
#plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
#plt.xlabel("Hemoglobin")
#plt.ylabel("Glucose")
#plt.legend()
#plt.show()