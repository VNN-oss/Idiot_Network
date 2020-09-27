def Generate(runtime):
    #Initailze varibles
    math = {"Questions":[], "Answer": [], "Distance": []}
    clock = r.randint(0,1)
    
    #Create questions
    for i in range(0, runtime):
        #print(clock)
        add1 = r.randint(1, r.randint(1, 100))
        add2 = r.randint(1, r.randint(1, 100))
        equ = r.randint(0, 2)
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
        math["Questions"].append(que)
        
        #Decide if question is right or wrong.
        if (clock == 0):
            clock = clock + 1
            math["Answer"].append(ans)
            math["Distance"].append(1)
        else:
            clock = clock -1
            math["Answer"].append(r.randint(0, r.randint(1, 100)))
            math["Distance"].append(0)
    sns.countplot(math['Distance'])
    return math
