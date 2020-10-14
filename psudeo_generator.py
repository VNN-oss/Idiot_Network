import random as r
import seaborn as sns
import pandas as pd
class Set():
    math = {"Questions":[], "Answer": [], "Distance":[]}
    def generate(self,runtime):
        #Initailze local varibles
        clock = r.randint(0,1)
        que = 0
        #Create questions
        for i in range(0, runtime):
            #print(clock)
            add1 = r.randint(1, r.randint(1, 1000))
            add2 = r.randint(1, r.randint(1, 1000))
            equ = r.randint(0, 3)
            if (equ == 0):
                ans = add1 + add2
                que = str(add1) + str(add2) + '.1'
                que = float(que)
            elif(equ == 1):
                ans = add1 * add2
                que = str(add1) + str(add2) + '.2'
                que = float(que)
            elif(equ == 2):
                ans = add1 - add2
                que = str(add1) + str(add2) + '.3'
                que = float(que)
            else:
                if (add1 < add2):
                    add1 = add2
                    add2 = add1
                ans = add1/add2
            self.math["Questions"].append(que)
        
            #Decide if question is right or wrong.
            if (clock == 0):
                clock = clock + 1
                self.math["Answer"].append(ans)
                self.math["Distance"].append(1)
            else:
                clock = clock -1
                self.math["Answer"].append(r.randint(0, r.randint(1, 1000)))
                self.math["Distance"].append(0)
        sns.countplot(self.math["Distance"])
        print("Qlen: {a}".format(a = len(self.math["Questions"])))
        print("Alen: {a}".format(a = len(self.math["Answer"])))
        print("Dlen: {a}".format(a = len(self.math["Distance"])))
        return self.math
    def Cut (self,amount):
        del self.math["Questions"][amount:]
        del self.math["Answer"][amount:]
        del self.math["Distance"][amount:]
        print("Data succesfully cut by {a}".f(a= amount))
        return self.math
