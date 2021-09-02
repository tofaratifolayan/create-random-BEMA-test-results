import random
import pandas as pd
import secrets

def getAnswer(options):
    randnum = random.randint(0, options)
    if randnum == 0:
        answer = "A"
    elif randnum == 1:
        answer = "B"
    elif randnum == 2:
        answer = "C"
    elif randnum == 3:
        answer = "D"
    elif randnum == 4:
        answer = "E"
    elif randnum == 5:
        answer = "F"
    elif randnum == 6:
        answer = "G"
    elif randnum == 7:
        answer = "H"
    elif randnum == 8:
        answer = "I"
    elif randnum == 9:
        answer = "J"
    return answer
current_question_list = []
csvtable = []
csvtable2 = []


numstudents = int(input("How many students do you want"))
starting_number = 1

tracker = []
answerdict = {}

while True:
    print("Enter -1 to break out of loop.")
    questions = int(input("how many questions in this set?"))
    options = int(input("how many options in this set?"))

    if questions == -1 or options == -1:
        break
    tracker.append((questions,options))
    for question in range(starting_number, len(current_question_list) + questions+1):
        questionnumber = "Q"+str(question)
        answerdict[questionnumber] = getAnswer(options-1)
    current_question_list += ([x for x in range(starting_number, len(current_question_list) + questions+1)])
    starting_number = current_question_list[-1]+1
answerdict
print(answerdict)
#

def newDict(ogdict):
    new = {}
    count = 1
    for rng in tracker:
        qsleft = rng[0]
        while qsleft != 0:
            new['Q'+str(count)] = getAnswer(rng[1]-1)
            qsleft -= 1
            count+=1
    return new



idlist = []
for student in range(numstudents):
    id = random.randint(100000, 999999)
    idlist += [id]

for student in range(numstudents):
    csvtable.append(newDict(answerdict))

for student in range(numstudents):
    csvtable2.append(newDict(answerdict))

df = pd.DataFrame(csvtable)
df.insert(len(current_question_list),"ID", idlist)

#df2 = pd.DataFrame(csvtable2)
#df2.insert(len(current_question_list),"ID", idlist)
#randomkey = str(secrets.randbelow(1000))

df.to_csv("RandomTest2_67BEMA.csv", index=False)
#df2.to_csv("ConceptualTestGenerator2"+ str(numstudents)+ "__" + randomkey + ".csv", index=False)

#print("The First File Name is ConceptualTestGenerator"+ str(numstudents)+ "s__" + randomkey + ".csv")
#print("The Second File Name is ConceptualTestGenerator2"+ str(numstudents)+ "s__" + randomkey + ".csv")
# import random
# numqs = 20
# randomkey = "testkey <- c("
#
# for i in range(numqs):
#     if len(randomkey) % 41 == 0:
#         randomkey += "\n"
#     randnum = random.randint(0, 4)
#     if randnum == 0:
#         randnum = "'A'"
#     elif randnum == 1:
#         randnum = "'B'"
#     elif randnum == 2:
#         randnum = "'C'"
#     elif randnum == 3:
#         randnum = "'D'"
#     elif randnum == 4:
#         randnum = "'E'"
#     randomkey += randnum
#     if i != numqs-1:
#         randomkey += ","
#     else:
#         randomkey += ")"
# print(randomkey, len(randomkey))