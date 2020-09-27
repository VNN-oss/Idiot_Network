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
class Nerual_Network():
    def __init__(self, data_amount,t_size,y_test,pred):
        self.data_amount = data_amount
        self.t_size = t_size
        self.y_test = y_test
        self.pred = pred
    def create(self,data):
        print("Creating dataframe...")
        data = pd.DataFrame(data)
        X = data.drop("Distance", axis = 1) 
        y = data['Distance']#Actual answer
        
        print("Spliting data")
        #Split data
        X_train, X_Test, y_train,y_test = train_test_split(X,y, test_size = self.t_size, random_state = 50)
        
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
        #plot = sns.jointplot(x = "Correct", y = "Incorrect", data = self.y_test,kind = "reg", truncate = False, xlim = (0, self.data_amount), ylim = (0, self.t_size), color = 'r', height = 7)
        return self.pred
