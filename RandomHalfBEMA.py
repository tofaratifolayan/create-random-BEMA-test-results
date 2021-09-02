import random
import pandas as pd
import secrets
from collections import OrderedDict



def getAnswer(options):
    randnum = random.randint(0, options - 1)
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

answerkey = ["A","A","B","E","A","D","E","B","B","F","E","E","D","B","G","B","D","B","B","G","A","E","E","A","D","D","C","B","C","F","D"]

numstudents = int(input("How many students do you want"))
starting_number = 1

tracker = []
answerdict = {}
c_q_l_keys = []
answerQs = []

while True:
    print("Enter -1 to break out of loop.", current_question_list, answerdict, (c_q_l_keys, len(c_q_l_keys)), sep='\n')
    questions = int(input("how many questions in this set?"))
    if questions == -1:
        last =questions
        break
    options = int(input("how many options in this set?"))
    if options == -1:break

    tracker.append((questions,options))

    for question in range(starting_number, len(current_question_list) + questions + 1):
        questionnumber = "Q"+str(question)
        answerdict[questionnumber] = getAnswer(options)
        c_q_l_keys +=[options]
    current_question_list += ([x for x in range(starting_number, len(current_question_list) + questions+1)])
    answerQs += (["Q"+str(x) for x in range(starting_number, len(current_question_list) + questions+1)])

    starting_number = current_question_list[-1]+1

#
def newDict(ogdict):
    new = {}
    count = 1
    for rng in tracker:
        qsleft = rng[0]
        while qsleft != 0:
            new['Q'+str(count)] = getAnswer(rng[1])
            qsleft -= 1
            count+=1
    return new



answerQs = []
for i in range(1, len(answerkey) +1):
    answerQs += ["Q"+str(i)]
answerkeydict = dict(zip(answerQs,answerkey))

optionsdict = dict(zip(answerQs, c_q_l_keys ))

def addSame(ogdict, randomquestion):
    new[randomquestion] = ogdict['Q'+str(randomquestion)]

#change while statement for fillcount to determine how much you want right.
#right now it's on 3/4 right, 1/4 random
#change the file name each time you change the fillcount
l = 0
while l < numstudents:
    bob = current_question_list[:]
    fillcount = 0
    new = {}
    while True:
        while fillcount < (3 *len(c_q_l_keys)//4) + 1:
            random_question = random.choice(bob)
            addSame(answerkeydict, random_question)
            bob.remove(random_question)
            fillcount += 1
        while len(bob) != 0:
            questions_left_over = random.choice(bob)
            new[questions_left_over] = getAnswer(optionsdict['Q' + str(questions_left_over)])
            bob.remove(questions_left_over)
            fillcount += 1
        break


    dict1 = OrderedDict(sorted(new.items()))
    sorteddict ={}
    for i in dict1:
        sorteddict["Q"+str(i)] =dict1[i]
    csvtable.append(sorteddict)
    bob = current_question_list
    l +=1

#change file name each time.
df = pd.DataFrame(csvtable)
df.to_csv("3QuarterRightBEMA.csv", index=False)

# idlist = []
# for student in range(numstudents-1):
#     id = random.randint(100000, 999999)
#     idlist += [id]
#
for student in range(numstudents - 1):
    csvtable.append(newDict(answerdict))

# for student in range(numstudents-1):
#     csvtable2.append(newDict(answerdict))
#
#df2 = pd.DataFrame(csvtable2)
#df2.to_csv("RandomPreTestBEMA.csv", index=False)
#
# df2 = pd.DataFrame(csvtable2)
# df2.insert(len(current_question_list),"ID", idlist)
# randomkey = str(secrets.randbelow(1000))
#
# df.to_csv("ConceptualTestGenerator"+ str(numstudents)+ "s__" + randomkey + ".csv", index=False)
# df2.to_csv("ConceptualTestGeneratorTwo"+ str(numstudents)+ "s__" + randomkey + ".csv", index=False)
#
# print("The First File Name is ConceptualTestGenerator"+ str(numstudents)+ "s__" + randomkey + ".csv")
# print("The Second File Name is ConceptualTestGeneratorTwo"+ str(numstudents)+ "s__" + randomkey + ".csv")

# import random
# import pandas as pd
# import secrets
#
# def getAnswer(options):
#     randnum = random.randint(-1, options)
#     if randnum == 0:
#         answer = "A"
#     elif randnum == 1:
#         answer = "B"
#     elif randnum == 2:
#         answer = "C"
#     elif randnum == 3:
#         answer = "D"
#     elif randnum == 4:
#         answer = "E"
#     elif randnum == 5:
#         answer = "F"
#     elif randnum == 6:
#         answer = "G"
#     elif randnum == 7:
#         answer = "H"
#     elif randnum == 8:
#         answer = "I"
#     elif randnum == -1:
#         answer = "J"
#     return answer
# current_question_list = []
# csvtable = []
#
# numstudents = int(input("How many students do you want"))
# starting_number = 1
#
# tracker = []
# answerdict = {}
# while True:
#     print("Enter -1 to break out of loop.")
#     questions = int(input("how many questions in this set?"))
#     options = int(input("how many options in this set?"))
#
#     if questions == -1 or options == -1:
#         break
#     tracker.append((questions,options))
#     for question in range(starting_number, len(current_question_list) + questions+1):
#         questionnumber = "Q"+str(question)
#         answerdict[questionnumber] = getAnswer(options-1)
#     current_question_list += ([x for x in range(starting_number, len(current_question_list) + questions+1)])
#     starting_number = current_question_list[-1]+1
# print(answerdict)
# #
#
# def newDict(ogdict):
#     new = {}
#     count = 1
#     for rng in tracker:
#         qsleft = rng[0]
#         while qsleft != 0:
#             new['Q'+str(count)] = getAnswer(rng[1]-1)
#             qsleft -= 1
#             count+=1
#     return new
#
# for student in range(numstudents-1):
#     csvtable.append(newDict(answerdict))
#
# print(csvtable)
# df = pd.DataFrame(csvtable)
# randomkey = str(secrets.randbelow(1000))
#
# df.to_csv("ConceptualTestGenerator"+ str(numstudents)+ "__" + randomkey + ".csv", index=False)
#
# print("The File Name is ConceptualTestGenerator"+ str(numstudents)+ "s__" + randomkey + ".csv")
