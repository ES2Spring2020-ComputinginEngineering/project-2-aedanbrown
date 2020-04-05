#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def createCentroids(k):
    
    #createCentroids makes random centroids to start the algorithm
    #It takes in one argument:
        #k is an integer representing the number of centroids to be created
    #It returns an array representing the centroids
    
    return np.random.random((2,k)) #2 comes from the number of features

    #The array of centroids is structured as follows:
    
                        # Centroid 1    Centroid 2   ....
                        #____________ _____________ 
    #Glucose Value      |____________|_____________| ....
    #Hemoglobin Value   |____________|_____________|
    

    
def normalizeData(glucose, hemoglobin):
    
    #normalizeData normalizes the data to be on a 0 to 1 unitless scale
    #It takes in two arguments
        #glucose is an array of the original glucose values
        #hemoglobin is an array of the original hemoglobin values
    #It returns an two arrays: the normalized glucose and hemoglobin values

    normal_glucose = (glucose-glucose.min())/(glucose.max()-glucose.min())
    normal_hemoglobin = (hemoglobin-hemoglobin.min())/(hemoglobin.max() - hemoglobin.min())
    
    return normal_glucose, normal_hemoglobin


def assignCentroid(centroids, glucose, hemoglobin):
        
        #assignCentroids assigns a centroid to each data point
        #It takes in three arguments
            #centroids is an array representing the location of the centroids
            #glucose is an array of the normalized glucose values
            #hemoglobin is an array of the normalized hemoglobin values
        #It returns an array that shows which centroid each data point is assigned to

        
        distance = np.zeros((len(centroids[0]),len(glucose))) 
        #Creates an 2D array of zeros with rows equal to the number of centroids 
        #and columns equal to the number of observations 
        #(Glucose is an arbitraty choice)
        #Will store the distances between each observation and each centroid
        
        for i in range(len(centroids[0])): 
            
            distance[i] = np.sqrt((glucose-centroids[:,i][0])**2+(hemoglobin-centroids[:,i][1])**2)
            #Calculate the distance between the centroid and each observation
            
            
            
        centroid_assign = np.zeros(len(glucose)) 
        #Creates an array of zeros with number of entries equal to the number of observations
        #Will store which centroid each observation is assigned to
        
        for i in range(len(centroid_assign)):
    
            centroid_assign[i] = np.argmin(distance[:,i])
            #Store the index of the min value (This is the centroid number)


        all_values = np.zeros(len(centroids[0]))
        #Create an array of zeros with a number of entries 
        #equal to the number of centroids
        #This array will store a 0 or 1 depending on 
        #if a observation has been assigned to a centroid
            #1 if any oberservations have been assigned to the centroid
            #0 if no observations have been assigned to the centroid
            
        #Checking if every centroid has an observation assigned
        #to is is important because other functions assume
        #that every centroid has some observations assigned
        
        #Examples of where issues could arise 
        #if this check isn't performed are noted below
            
        for i in range(len(centroids[0])):
            
            if list(centroid_assign).count(i) == 0:
                all_values[i] = 0
            else:
                all_values[i] = 1
        
        #Check if the number of 1s does not equal the number of centroids
        #(A centroid doesn't have a observation)
        if list(all_values).count(1) != len(centroids[0]):
            centroid_assign = assignCentroid(createCentroids(len(centroids[0]))
                                                           ,glucose,hemoglobin)
            #Assign to centroid_assign the result of calling 
            #this function again, with new centroids.
            
            #This technically could reach the maximum recursion depth, 
            #but that is very unlikely as every time, 
            #there would have to be a centroid that 
            #doesn't have an observation assigned to it every time.
            
            #The chances increase as the number of centroids increase,
            #so if a large number of centroids is used, 
            #a different method may be needed
            
        return centroid_assign
    
def calculateMean(centroid_assign, glucose, hemoglobin):
    
    #calculateMean calculates the mean of the data associated to each centroid
    #It takes in three arguments:
        #centroid_assign is an array that shows which centroid each data point is assigned to
        #glucose is an array of the normalized glucose values
        #hemoglobin is an array of the normalized hemoglobin values
    #It returns an array representing the mean values of each cluster
    
    
    mean_array = np.zeros((2,int(np.max(centroid_assign)) + 1)) 
    #Creates an array of zeros with a number of rows equal to the features (2)
    #and a number of columns equal to the number of centroids
    
    #This assumes the max value was achieved,
    #which is okay because of the check in assignCentroids
        #All values are achieved because of the check,
        #so the max one must be achieved


    for i in range(int(np.max(centroid_assign)) + 1):

        ave_glucose = glucose[centroid_assign==i].mean() #Can potentially 
                                                         #get an empty slice 
                                                         #if none are assigned 
                                                         #to the centroid, 
                                                         #which causes an error,
                                                         #but this is fixed by
                                                         #the check in 
                                                         #assignCentroids
        ave_hemoglobin = hemoglobin[centroid_assign==i].mean()

        mean_array[:,i] = [ave_glucose,ave_hemoglobin]
        #The ith column becomes the average glucose and average hemoglobin
        #of the observations assigned to the centroid
        
    return mean_array
 
def plotClusters(centroids,centroid_assignment, glucose, hemoglobin):
    
    #plotClusters plots the data with different colors and symbols to represent each cluster
    #It takes in four arguments:
        #centroids is an array representing the location of the centroids
        #centroid_assignment is an array that shows which centroid each data point is assigned to
        #glucose is an array of the normalized glucose values
        #hemoglobin is an array of the normalized hemoglobin values
    #It doesn't return anything
    
    plt.figure()
    plt.suptitle("Normalized Glucose vs Normalized Hemoglobin")
    
    for i in range(len(centroids[0])):
        
        plt.plot(hemoglobin[centroid_assignment==i],glucose[centroid_assignment==i], str(i+1), label = "Class " + str(i))
        #Each cluster is assigned its own marker and color
            #Using this method, only four clusters can be graphed
            #so a graph where more than four is needed will need to
            #graph differently
            
        plt.plot(centroids[:,i][1],centroids[:,i][0], "ko")
        #Each centroid is a large black dot
        
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalized Glucose")
    plt.legend()
    plt.show()
        
        
        
        