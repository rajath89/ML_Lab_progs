import csv
with open("/home/xfce/Desktop/DATA SET/finds.csv") as find:
        reader = csv.reader(find)
        data = list(reader)
len(data)
h = ['0','0','0','0','0','0']
for row in data:
    if row[-1] == 'Yes':
        j=0
        for col in row:
            if col !='Yes':
                if col!=h[j] and h[j] == '0':
                    h[j]=col
                elif col!=h[j] and h[j] !='0':
                    print(col)
                    h[j]='?'
            j=j+1
print(h)
