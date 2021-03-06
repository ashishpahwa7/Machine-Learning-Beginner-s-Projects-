from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# loading data from file and Preparing for machine learning

def file2matrix(filename):

	fr = open(filename)
	numberofLines = len(fr.readlines())
	returnMat = zeros((numberofLines,3))
	classLabelVector = []
	fr = open(filename)
	
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(listFromLine[-1])
		index += 1
	return returnMat,classLabelVector

#Data Normalization code
def autonorm(FeatureMatrix):

	scaler = MinMaxScaler()
	rescaled_DataSet = scaler.fit_transform(FeatureMatrix)
	return rescaled_DataSet


# Spliting into training and test sets (80-20 split)
def SplitData(FeatureMatrix, classLabelVector):

	no_of_samples = len(FeatureMatrix)

	train_size = int (80.0/100 * no_of_samples)
	test_size = no_of_samples - train_size

	features_train = FeatureMatrix[0:train_size]
	labels_train = classLabelVector[0:train_size]
	
	features_test = FeatureMatrix[train_size:]
	labels_test = classLabelVector[train_size:]

	return features_train, labels_train, features_test, labels_test


# Visualizing data 
def drawPlot(features_train, labels_train):
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(features_train[:,0], features_train[:,1],15.0*array(labels_train).astype(float), 15.0*array(labels_train).astype(float))
	plt.show()


#K- Nearest neighbours
def classify(features_train, labels_train):
	
	clf = neighbors.KNeighborsClassifier(n_neighbors = 3)
	clf = clf.fit(features_train, labels_train)

	return clf
	
# Testing classifier and printing accuracy score 
def TestClassifier(clf, features_test, labels_test):
	pred = clf.predict(features_test)	
	
	acc = accuracy_score(pred,labels_test)
	print "Accuracy Score  : ",acc

def classifyPerson(clf):

	resultList = ['not at all','in small doses', 'in large doses']
	percentTats = float(raw_input(" \tPercentage of time playing video games? \t"))
	ffMiles = float(raw_input("frequent flier miles earned per year? \t"))
	iceCream = float(raw_input("liters of ice cream consumed per year? \t"))
	inArr = array([[ffMiles, percentTats, iceCream]])
	result = clf.predict(inArr)
	result = (result[0]).astype(int)
	print "you'll probably like the person : ",resultList[result]



FeatureMatrix,classLabelVector = file2matrix('datingTestSet2.txt')
FeatureMatrix = autonorm(FeatureMatrix)
features_train, labels_train, features_test, labels_test = SplitData(FeatureMatrix, classLabelVector)
clf = classify(features_train, labels_train)

import pickle
pickle.dump(clf,open("classifier.p","wb"))









