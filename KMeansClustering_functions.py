#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def createKCentroids(k):
    
    return np.random.random((2,k))

def normalizeData(glucose, hemoglobin):

    normalGlucose = (glucose-glucose.min())/(glucose.max()-glucose.min())
    normalHemoglobin = (hemoglobin-hemoglobin.min())/(hemoglobin.max() - hemoglobin.min())
    
    return normalGlucose, normalHemoglobin


def assignKCentroid(k_points, glucose, hemoglobin):
    
    distance = np.zeros((len(k_points[0]),len(glucose)))
    
    for i in range(len(k_points[0])):
        
        distance[i] = np.sqrt((glucose-k_points[:,i][0])**2+(hemoglobin-k_points[:,i][1])**2)
        
    centroid_assign = np.zeros(len(glucose))

    for i in range(len(centroid_assign)):

        centroid_assign[i] = np.argmin(distance[:,i])

    return centroid_assign, distance
    
def updateKCentroid(centroid_assign, glucose, hemoglobin):
    
    mean_array = np.zeros((2,int(np.max(centroid_assign))+1)) #This assumes the max value was achieved


    for i in range(int(np.max(centroid_assign)) + 1):

        ave_glucose = glucose[centroid_assign==i].mean() #Can potentially get an empty slice if none are assigned to this one
        ave_hemoglobin = hemoglobin[centroid_assign==i].mean()

        mean_array[:,i] = [ave_glucose,ave_hemoglobin]
        
    return mean_array
        
        
        
        