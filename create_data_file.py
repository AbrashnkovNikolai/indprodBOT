import csv
import requests as req
from bs4 import BeautifulSoup
response = req.get('http://www.psu.ru/files/docs/priem-2023/prikazy/bkl/index.html') #data for analyze
soup = BeautifulSoup(response.content, 'html.parser')


def DOGOODCSV():
    item={}
    step=0
    napravo=[]
    bali=[]
    specs=[]
    slov={}
    for s in soup.find_all('p'):
        if 'Направление/специальность' in s.text: #ищем специальность и форматируем их , убирая ненужную часть строки
            spec=s.text[s.text.index('\n'):]
            spec=spec[3:]
            napravo.append([])
            bali.append([])
            specs.append(spec)

        
        if (len(s.text)==14 and s.text[0].isdigit()) or len(s.text)==11 : #ищем снилсы 
            napravo[len(napravo)-1].append(s.text)

            step=0
        step+=1
        if step==6 and len(specs)>0:
            bali[len(bali)-1].append(s.text)
            
    #print(len(specs))
    #print(len(napravo)) #проверка что все всему равно и можжно делать ксв словарь
    #print(len(bali))

    #print(specs[1],napravo[1],bali[1])
    
    
        
    with open('data.csv', 'w+', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in range(len(specs)):
            item = [specs[i], napravo[i]]  
            writer.writerow(item) 
DOGOODCSV()





























