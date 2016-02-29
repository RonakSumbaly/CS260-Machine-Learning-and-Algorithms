import numpy as np
from sklearn import preprocessing

def featureArray(featureCSV):
    data = np.genfromtxt(featureCSV,delimiter=',')
    data = np.delete(np.delete(data,0,1),0,0)  # remove the ID names and the feature names

    return (preprocessing.normalize(np.delete(data,0,1),norm='l2',axis=0),data[:,0])  # return data and labels
