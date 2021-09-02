
def expectedvalues(x):
    RW= (1 / x) * ((x - 1) / x)
    WR = (1 / x) * ((x - 1) / x)
    RR  = (1 / x) * (1 / x)
    WSW = (1 / x)
    WDW = ((x - 2) / x) * ((x - 1) / x)

    #xQ = (RW + WR + WDW) / (RR + WSW + RW + WR + WDW)
    #xP = (WR) / (RW + WR + WDW)
    #xC = (RW) / (RW + WR + WDW)
    #xS = (WDW) / (RW + WR + WDW)
    #xK = (RR) / (RR + RW)
    #xM = (WSW) / (WDW + WSW + WR)

    return RW, WR, WDW, WSW, RR

questionlist = []
startingnumber = 0

totalRW = 0
totalWR = 0
totalWDW = 0
totalWSW = 0
totalRR = 0

RWdict= {}
WRdict= {}
WDWdict= {}
WSWdict = {}
RRdict = {}

testcreate = {}


while True:
    questions = int(input("What does this next set go up to? (ie 4 means from 1 to 4: [1, 2, 3, 4]), enter 0 to quit loop)"))
    if questions == 0:
        break
    numquestions = int(input("How many options for this set? \n All of these include j, ie a-g(7) + j(1) = 8  \n a-d has 5 options \n a-e has 6 options \n a-e has 7 options \n a-g has 8 options \n a-h has 9 options \n "  ))

    totalRW += expectedvalues(numquestions)[0] * questions
    totalWR += expectedvalues(numquestions)[1] * questions
    totalWDW += expectedvalues(numquestions)[2] * questions      
    totalWSW += expectedvalues(numquestions)[3] * questions
    totalRR += expectedvalues(numquestions)[4] * questions

    for i in range(startingnumber+1, questions+1):
        RWdict[i] = round(expectedvalues(numquestions)[0], 3)
        WRdict[i] = round(expectedvalues(numquestions)[1], 3)
        WDWdict[i] = round(expectedvalues(numquestions)[2], 3)
        WSWdict[i] = round(expectedvalues(numquestions)[3], 3)
        RRdict[i] = round(expectedvalues(numquestions)[4], 3)

    if len(questionlist) > 0:
        startingnumber = questionlist[-1]
    questionlist += [i for i in range(startingnumber+1,questions+1)]
    
    print("These are questions in your set", questionlist, "This is the length of your set: " + str(len(questionlist)), sep='\n')
    print("The expected RW value for each question in this set is "+str(round(expectedvalues(numquestions)[0], 3)),"The expected WR value for each question in this set is "+str(round(expectedvalues(numquestions)[1], 3)),"The expected WDW value for each question in this set is "+str(round(expectedvalues(numquestions)[2], 3)),"The expected WsW value for each question in this set is "+str(round(expectedvalues(numquestions)[3], 3)),"The expected RR value for each question in this set is "+str(round(expectedvalues(numquestions)[4], 3)), sep="\n")

print("These are dictionaries for each type of expectation value of the submetrics for each question",RWdict,WRdict,WDWdict,WSWdict,RRdict, sep='\n')

xQ = (totalRW + totalWR + totalWDW) / (totalRR + totalWSW + totalRW + totalWR + totalWDW)
xP = totalRW / (totalRW + totalWR + totalWDW)
xS = totalWDW / (totalRW + totalWR + totalWDW)
xC = totalWR / (totalRW + totalWR + totalWDW)

print("Your expected Q value is", round(xQ, 3))
print("Your expected P value is", round(xP, 3))
print("Your expected S value is", round(xS, 3))
print("Your expected C value is", round(xC, 3))
