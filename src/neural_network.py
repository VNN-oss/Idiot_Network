#Full nerual_network class
import pandas as pd
import random as r
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
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
    print("Returning data...")
    return pack
class Neural_Network():
    def __init__(self, data_amount,t_size,pred):
        self.data_amount = data_amount
        self.t_size = t_size
        self.pred = pred
    def create(self,pack):
        if (pack == None):
            raise ("No datapack detected.")
        print("Data Fetched !!")
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
        pred = confusion_matrix(y_test, pred)
        return self.pred
    
def plot(*args):
    to_graph = {"set":[],"label":[]}
    j = args[-1]
    print(j)
    for i in range(0, j):
        to_graph["label"].append("Net{}".format(i))
    for i in range (0, j):
        to_graph["set"].append(round(args[0][i][0,0]/args[0][i][1,1]))
       # print(to_graph["set"])
    sns.countplot(x= "label",data = to_graph)
    print(to_graph)
