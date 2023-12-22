import csv
def readfile(a)->str:
    with open('data.csv', newline='',encoding='utf-8') as f:
        reader = csv.reader(f)
        s='lose'
        for row in reader:
            if a in row[1]:
                return row[0]
        
#c=input('dasd: ')
#print(readfile(c))
