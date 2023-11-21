import pandas as pd
import numpy as np
import csv

# Function to read marks from CSV file
def get_marks():
    df = pd.read_csv('inputm.csv', header=None)
    return df[0].tolist()

# Function to generate random marks
def generate_random_marks(total_marks, mark_split, lower_bound, upper_bound):
    random_marks = np.random.randint(lower_bound, upper_bound, size=len(mark_split))
    while random_marks.sum() != total_marks:
        random_marks = np.random.randint(lower_bound, upper_bound, size=len(mark_split))
    return random_marks

# RandomSplitter Function
def ranCOS(reg, ass, assName, dep, co_lister, ms_lister):
    ms = []
    co = []

    # Configuration based on reg, ass, and dep values
    if reg == 13 or reg == 17:
        if ass == 1:
            ms = [2, 2, 2, 2, 2, 16, 16, 8]
            co = [1, 1, 1, 2, 2, 1, 2, 1]
        elif ass == 2:
            ms = [2, 2, 2, 2, 2, 16, 16, 8]
            co = [3, 3, 3, 4, 4, 3, 4, 3]
        elif ass == 3:
            if dep == 1:
                ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 16, 16, 16, 16]
                co = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5]
            elif dep == 2:
                ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 13, 13, 13, 13, 13, 15]
                co = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5, 5]
        elif ass == 4 or ass == 5:
            ms = [20, 20, 20, 20, 20]
            co = [1, 2, 3, 4, 5]
        elif ass == 6:
            for i in co_lister:
                co.append(int(i))
            for i in ms_lister:
                ms.append(int(i))

    elif reg == 21:
        if ass == 1:
            ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 16, 8]
            co = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 1, 2, 3]
        elif ass == 2:
            ms = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 16, 8]
            co = [4, 4, 4, 4, 5, 5, 5, 5, 3, 3, 4, 5, 3]
        elif ass == 4 or ass == 5:
            ms = [20, 20, 20, 20, 20]
            co = [1, 2, 3, 4, 5]
        elif ass == 6:
            for i in co_lister:
                co.append(int(i))
            for i in ms_lister:
                ms.append(int(i))

    wm = get_marks()

    rm = []
    for j in wm:
        if j == 0:
            ml = np.zeros(len(ms))
        elif j < 41:
            ml = generate_random_marks(j, ms, 0, 11)
        elif j < 61:
            ml = generate_random_marks(j, ms, 5, np.array(ms) + 1)
        elif j < 81:
            ml = generate_random_marks(j, ms, 7, np.array(ms) + 1)
        elif j < 100:
            ml = generate_random_marks(j, ms, 9, np.array(ms) + 1)
        else:
            ml = np.array(ms)
        rm.append(dict(enumerate(ml, 1)))

    # Write results to a new CSV file
    assName = assName + ".csv"
    with open(assName, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["KGiSL INSTITUTE of Technology"])
        writer.writerow([f"Assessment Name : {assName}"])
        co1spup = [sum([ms[v] for v in range(len(ms)) if co[v] == 1])]
        co2spup = [sum([ms[v] for v in range(len(ms)) if co[v] == 2])]
        co3spup = [sum([ms[v] for v in range(len(ms)) if co[v] == 3])]
        co4spup = [sum([ms[v] for v in range(len(ms)) if co[v] == 4])]
        co5spup = [sum([ms[v] for v in range(len(ms)) if co[v] == 5])]
        writer.writerow([*['QNO ->'], *[i+1 for i in range(len(ms))], *["Course Outcome SPUP"]])
        writer.writerow([*['CO ->'], *co, *['co1Tot'], *['co2Tot'], *['co3Tot'], *['co4Tot'], *['co5Tot']])
        writer.writerow([*['TM | MS -> '], *ms, *co1spup, *co2spup, *co3spup, *co4spup, *co5spup])
        
        for i in range(len(rm)):
            spup = list(rm[i].values())
            co1tot = [spup[v] for v in range(len(spup)) if co[v] == 1]
            co2tot = [spup[v] for v in range(len(spup)) if co[v] == 2]
            co3tot = [spup[v] for v in range(len(spup)) if co[v] == 3]
            co4tot = [spup[v] for v in range(len(spup)) if co[v] == 4]
            co5tot = [spup[v] for v in range(len(spup)) if co[v] == 5]
            writer.writerow([*[sum(spup)], *spup, *[sum(co1tot)], *[sum(co2tot)], *[sum(co3tot)], *[sum(co4tot)], *[sum(co5tot)]])
