from kNN import classifyPerson
import pickle

clf = pickle.load(open("classifier.p","rb"))

classifyPerson(clf)

# TODO: If user is satisfied with date, add the instance to training set for further imporovement in accuracy score for future :)





