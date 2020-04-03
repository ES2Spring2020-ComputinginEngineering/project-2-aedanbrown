#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt


features = 2
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def createKCentroids(k):
    
    return np.random.random((features,k))

    #The array of centroids is structured as follows:
    
                        # Centroid 1    Centroid 2   ....
                        #____________ _____________ 
    #Glucose Value      |____________|_____________| ....
    #Hemoglobin Value   |____________|_____________|
    
    
def normalizeData(glucose, hemoglobin):

    normalGlucose = (glucose-glucose.min())/(glucose.max()-glucose.min())
    normalHemoglobin = (hemoglobin-hemoglobin.min())/(hemoglobin.max() - hemoglobin.min())
    
    return normalGlucose, normalHemoglobin


def assignKCentroid(k_points, glucose, hemoglobin):
    

        
        distance = np.zeros((len(k_points[0]),len(glucose))) 
        #Creates an 2D array of zeros with rows equal to the number of centroids 
        #and columns equal to the number of observations 
        #(Glucose is an arbitraty choice)
        #Will store the distances between each observation and each centroid
        
        for i in range(len(k_points[0])): 
            
            distance[i] = np.sqrt((glucose-k_points[:,i][0])**2+(hemoglobin-k_points[:,i][1])**2)
            #Calculate the distance between the centroid and each observation
            
            
            
        centroid_assign = np.zeros(len(glucose)) 
        #Creates an array of zeros with number of entries equal to the number of observations
        #Will store which centroid each observation is assigned to
        
        for i in range(len(centroid_assign)):
    
            centroid_assign[i] = np.argmin(distance[:,i])
            #Store the index of the min value (This is the centroid number)


        allValues = np.zeros(len(k_points[0]))
        #Create an array of zeros with a number of entries equal to the number of centroids
        #This array will store a 0 or 1 depending on if a observation has been assigned to a centroid
            #1 if any oberservations have been assigned to the centroid
            #0 if no observations have been assigned to the centroid
            
        #Checking if every centroid has an observation assigned
        #to is is important because other functions assume
        #that every centroid has some observations assigned
        
        #Examples of where issues could arise 
        #if this check isn't performed are noted below
            
        for i in range(len(k_points[0])):
            
            if list(centroid_assign).count(i) == 0:
                allValues[i] = 0
            else:
                allValues[i] = 1
        
        #Check if the number of 1s does not equal the number of centroids
        #(A centroid doesn't have a observation)
        if list(allValues).count(1) != len(k_points[0]):
            centroid_assign = assignKCentroid(createKCentroids(len(k_points[0])),glucose,hemoglobin)
            #Assign to centroid_assign the result of calling this function again,
            #with new centroids.
            
            #This technically could reach the maximum recursion depth, 
            #but that is very unlikely as every time, 
            #there would have to be a centroid that 
            #doesn't have an observation assigned to it.
            
            #The chances increase as the number of centroids increase,
            #so if a large number of centroids is used, 
            #a different method may be needed
            
        return centroid_assign
    
def updateKCentroid(centroid_assign, glucose, hemoglobin):
    
    mean_array = np.zeros((features,int(np.max(centroid_assign)) + 1)) 
    #Creates an array of zeros with a number of rows equal to the features
    #and a number of columns equal to the number of centroids
    
    #This assumes the max value was achieved,
    #which is okay because of the check in assignKCentroids
        #All values are achieved because of the check,
        #so the max one must be achieved


    for i in range(int(np.max(centroid_assign)) + 1):

        ave_glucose = glucose[centroid_assign==i].mean() #Can potentially 
                                                         #get an empty slice 
                                                         #if none are assigned 
                                                         #to the centroid, 
                                                         #which causes an error
        ave_hemoglobin = hemoglobin[centroid_assign==i].mean()

        mean_array[:,i] = [ave_glucose,ave_hemoglobin]
        #The ith column becomes the average glucose and average hemoglobin
        #of the observations assigned to the centroid
        
    return mean_array
 
def plot(kCentroids,centroid_assignment, glucose, hemoglobin):
    
    plt.figure()
    plt.suptitle("Normalized Glucose vs Normalized Hemoglobin")
    
    for i in range(len(kCentroids[0])):
        
        plt.plot(hemoglobin[centroid_assignment==i],glucose[centroid_assignment==i], str(i+1), label = "Class " + str(i))
        #Each cluster is assigned its own marker and color
            #Using this method, only four clusters can be graphed
            #so a graph where more than four is needed will need to
            #graph differently
            
        plt.plot(kCentroids[:,i][1],kCentroids[:,i][0], "ko")
        #Each centroid is a large black dot
        
    plt.xlabel("Normalized Hemoglobin")
    plt.ylabel("Normalized Glucose")
    plt.legend()
    plt.show()
        
        
        
        