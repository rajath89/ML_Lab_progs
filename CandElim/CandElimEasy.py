#Candidate elimination
import  csv
with open('/content/finds.csv') as file2:#get the locatio from file in desktop
    reader2 = csv.reader(file2)
    data2 = list(reader2)
    can = []
    gh = []
    h = [0,0,0,0,0,0]#number of attribues=number of 0's
    for row in data2[1:]:
        if row[-1] == 'Yes':#check whether yes is in capital or small in the dataset
            j=0
            for col in row:
                if col != 'Yes':#because yes column need not be compared
                    if h[j] != col and h[j] == 0:
                        h[j] = col
                    elif h[j] != col and h[j] != 0:
                        h[j] = '?'
                    j = j+1
        elif row[-1] != 'Yes':#for the No value
            i=0
            for col in row:
                if col != 'No':
                    if h[i] != col and h[i] != '?' and h[i] != 0:#checking whether it's oppostie exists
                        g = ['?','?','?','?','?','?']
                        g[i] = h[i]
                        gh.append(g)
                    i = i+1
    print("Generic Boundry :",gh)
    print("Specific Boundry :",h)