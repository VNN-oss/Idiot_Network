#Full nerual_network class
import pandas as pd
import seaborn as sns
import random as r
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
#from pesudo_generator import generator
def frame_data(data, t_size):
    pack = []
    #Split data
    data = pd.DataFrame(data)
    print("Spliting data")
    X = data.drop("Distance", axis = 1) 
    y = data['Distance']#Actual answer
    X_train, X_Test, y_train,y_test = train_test_split(X,y, test_size = t_size, random_state = 0)
    print("Test_size: {a}".format(a=len(X_Test["Questions"])))
    print("Packaging data...")
    pack.append(X_train)
    pack.append(X_Test)
    pack.append(y_train)
    pack.append(y_test)
    return pack

class Neural_Network():
    def __init__(self, data_amount,t_size,pred):
        self.data_amount = data_amount
        self.t_size = t_size
        self.pred = pred
    def create(self,pack):
        print("Unpacking data...")
        X_train = pack[0]
        X_Test = pack[1]
        y_train = pack[2]
        y_test = pack[3]
        print("Creating dataframe...")

        print("Creating network")
        #Create Neural Network
        mlpc = MLPClassifier(hidden_layer_sizes = (12,12,12), max_iter = 520)
        
        print("Training network....")
        mlpc.fit(X_train,y_train)

        pred = mlpc.predict(X_Test)

        print("Creating report")
        #Return and plot accuracy
        print(classification_report(y_test,pred))
        print("Creating confusion matrix")
        print(confusion_matrix(y_test, pred))
        return self.pred
