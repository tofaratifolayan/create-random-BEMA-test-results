import random
import pandas as pd
answerkey = ["A","A","B","E","A","D","E","B","B","F","E","E","D","B","G","B","D","B","B","G","A","E","E","A","D","D","C","B","C","F","D"]

students = 1000
samedict = {}
sametable = []
for j in range(1, students+1):
    for i in range(1, len(answerkey)+1):
        samedict['Q'+str(i)] = answerkey[i-1]
        #print(samedict)
        #id = random.randint(100000, 999999)
        #samedict['ID'] = id
    sametable.append(samedict)

df = pd.DataFrame(sametable)
df.to_csv('AllRightBEMA.csv', index=False)