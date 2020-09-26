
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
    def __init__(self, data_amount,t_size):
        self.data_amount = data_amount
        self.t_size = t_size
    def create(self,math_problems):

        print("Creating dataframe...")
        math_problems = pd.DataFrame(math_problems)
        sns.countplot(math_problems['Distance'])
        X = math_problems.drop("Distance", axis = 1) 
        y = math_problems['Distance']#Actual answer
        
        print("Spliting data")
        #Split data
        X_train, X_Test, y_train,y_test = train_test_split(X,y, test_size = self.t_size, random_state = 50)
        print("Creating network")
        #Create Neural Network
        mlpc = MLPClassifier(hidden_layer_sizes = (11,11,11), max_iter = 500)
        print("Training network")
        mlpc.fit(X_train,y_train)
        pred = mlpc.predict(X_Test)
        print("Network complete!")
        
        #Return and plot accuracy
        print(classification_report(y_test,pred))
        plot = sns.jointplot(x = "Correct", y = "Incorrect", data = y_test,kind = "reg", truncate = False, xlim = (0, self.data_amount), ylim = (0, self.t_size), color = 'r', height = 7)
