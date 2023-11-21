import random as ra
import csv
import pandas as pd

#Input
def getmarks():
    with open('inputm.csv', newline='') as f:
        reader = csv.reader(f)
        print(reader)
        ll = []
        totall = [list(map(int, rec)) for rec in csv.reader(f, delimiter=',')]
        for i in totall:
            ll.append(i[0])
    return ll

    #totall=[rec for rec in csv.reader(f, delimiter=',')]


#RandomSplitter
#initialize
def ranCOS(reg, ass, assName, dep, co_lister, ms_lister):
    print(reg,ass,assName)
    rm =[]  #randomMarks
    ms=[]
    co=[]
    #print(reg, ass, dep)
    if (reg == 13) or (reg == 17):
        #print(reg)
        if ass == 1:
            ms = [2, 2, 2, 2, 2, 16, 16, 8]  #markSplitup
            co = [1, 1, 1, 2, 2, 1, 2, 1]  #CO No
        elif ass == 2:
            ms = [2, 2, 2, 2, 2, 16, 16, 8]  #markSplitup
            co = [3, 3, 3, 4, 4, 3, 4, 3]  #CO No
        elif ass == 3 :
            # dep=int(input("\nDepartment\n1.S & H \n2.Other  \nchoose the department : "))
            if dep==1:
                ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 16, 16, 16,
                  16]  #markSplitup
                co = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5]  #CO No
            elif dep == 2:
                ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 13, 13, 13, 13, 13,
                  15]  #markSplitup
                co = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5, 5]  #CO No
        elif ass == 4:
            ms = [20, 20, 20, 20, 20]  #markSplitup
            co = [1, 2, 3, 4, 5]  #CO No
        elif ass == 5:
            ms = [20, 20, 20, 20, 20]  #markSplitup
            co = [1, 2, 3, 4, 5]  #CO No
        elif ass == 6:
            # que_count=int(input("PLease enter Question Count : "))
            for i in co_lister:
                co.append(int(i))
            for i in ms_lister:
                ms.append(int(i))
                # ms.append(int(input(f"Enter the question {i+1} mark : ")))
        
    elif reg == 21:
        if ass == 1:
            ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 16, 8]  #markSplitup
            co = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 1, 2, 3]  #CO No
        if ass == 2:
            ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 16, 8]  #markSplitup
            co = [4, 4, 4, 4, 5, 5, 5, 5, 3, 3, 4, 5, 3]  #CO No
        elif ass == 4:
            ms = [20, 20, 20, 20, 20]  #markSplitup
            co = [1, 2, 3, 4, 5]  #CO No
        elif ass == 5:
            ms = [20, 20, 20, 20, 20]  #markSplitup
            co = [1, 2, 3, 4, 5]  #CO No
        elif ass == 6:
            # que_count=int(input("PLease enter Question Count : "))
            # for i in range(que_count):
            #     co.append(int(input(f"Enter the question {i+1} co number : ")))
            # for i in range(que_count):
            #     ms.append(int(input(f"Enter the question {i+1} mark : ")))
            
            for i in co_lister:
                co.append(int(i))
            for i in ms_lister:
                ms.append(int(i))
    #print(ms,co)
    #que_count = qcount
    qno = [ i+1 for i in range(len(ms))]  
    wm = getmarks() # read the marks
    #print(wm)
    #splitter
    for j in wm:
        ml = {}
        summ = j
        while True:
            for i in range(len(ms)):
                #print(j)
                if j == 0:
                    ml[i + 1] = 0
                elif j < 41:
                    if j > 10:
                        ml[i + 1] = ra.randint(0, ms[i])
                    elif j < 6:
                        ml[i + 1] = ra.randint(0, 1)
                    else:
                        ml[i + 1] = ra.randint(0, 2)
                elif j > 40 and j < 61:
                    if ms[i] < 3:
                        ml[i + 1] = ra.randint(0, ms[i])
                    else:
                        ml[i + 1] = ra.randint(5, ms[i])
                elif j > 60 and j < 81:
                    if ms[i] < 3:
                        ml[i + 1] = ra.randint(1, ms[i])
                    else:
                        ml[i + 1] = ra.randint(7, ms[i])
                elif j > 80 and j < 100:
                    if ms[i] < 3:
                        ml[i + 1] = ra.randint(2, ms[i])
                    else:
                        ml[i + 1] = ra.randint(9, ms[i])
                else:
                    ml[i + 1] = ms[i]

            #print(ml)
            if sum(ml.values()) == summ:
                rm.append(ml)
                #print(rm)
                break
    #output
    assName = assName + ".csv"
    with open(assName, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["KGiSL INSTITUTE of Technology"])
        writer.writerow([f"Assessment Name : {assName}"])
        co1spup=[sum([ms[v] for v in range(len(ms)) if co[v] == 1])]
        co2spup=[sum([ms[v] for v in range(len(ms)) if co[v] == 2])]
        co3spup=[sum([ms[v] for v in range(len(ms)) if co[v] == 3])]
        co4spup=[sum([ms[v] for v in range(len(ms)) if co[v] == 4])]
        co5spup=[sum([ms[v] for v in range(len(ms)) if co[v] == 5])]
        writer.writerow([*['QNO ->'], *qno,*["Course Outcome SPUP"]])
        writer.writerow([*['CO ->'], *co,*['co1Tot'], *['co2Tot'], *['co3Tot'],
            *['co4Tot'], *['co5Tot']
                        #, *['co6Tot']
                        ])
        writer.writerow([
            *['TM | MS -> '], *ms,*co1spup,*co2spup,*co3spup,*co4spup,*co5spup])
        #writer.writerow(list(ml.keys()))
        for i in range(len(rm)):
            spup = list(rm[i].values())
            co1tot = [spup[v] for v in range(len(spup)) if co[v] == 1]
            co2tot = [spup[v] for v in range(len(spup)) if co[v] == 2]
            co3tot = [spup[v] for v in range(len(spup)) if co[v] == 3]
            co4tot = [spup[v] for v in range(len(spup)) if co[v] == 4]
            co5tot = [spup[v] for v in range(len(spup)) if co[v] == 5]
            #co6tot = [spup[v] for v in range(len(spup)) if co[v] == 6]
            #print(co1tot, co2tot, co3tot, co4tot, co5tot, co6tot)
            writer.writerow([
                *[sum(spup)], *spup, *[sum(co1tot)], *[sum(co2tot)],
                *[sum(co3tot)], *[sum(co4tot)], *[sum(co5tot)]
                #*[sum(co6tot)
            ])
            #writer.writerow(co1tot)

 
'''
# Reading the csv file
df_new = pd.read_csv('ghu.csv') 
# saving xlsx file
GFG = pd.ExcelWriter('Names.xlsx')
df_new.to_excel(GFG, index=False)
 
GFG.save()'''
