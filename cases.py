import requests
from bs4 import BeautifulSoup
from tabulate import tabulate 
import os
import numpy as np
import matplotlib.pyplot as plt

extract_contents =lambda  row:[x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS =['SNo','State','India-Confirmed','Cured','Death']

response =requests.get(URL).content
soup =BeautifulSoup(response,'html.parser')
header =extract_contents(soup.tr.find_all('th'))

stats =[]
all_rows =soup.find_all('tr')

for row in all_rows:
	stat =extract_contents(row.find_all('td'))
	if stat:
		if len(stat) == 4:
			stat =['',*stat]
			stats.append(stat)
		elif len(stat) ==5:
			stats.append(stat)

stats[-1][1] ="Total Cases"

stats.remove(stats[-1])

objects =[]

for row  in stats:
	objects.append(row[1])

y_pos =np.arange(len(objects))
performance =[]
s=0
s1=0
s2=0

for row in stats:
	performance.append(int(row[2]))
	s=s+int(row[2])
	if row[3]=='':
		s1=s1+0
	else:	
		s1 = s1+ int(row[3])
	if row[4]=='':
		s2=s2+0
	else:	
		s2 = s2+int(row[4])
	

table = tabulate(stats ,headers =SHORT_HEADERS)
print (table)
print()
print("Total Number of positive cases =",s)
print("Total Number of cured =",s1)
print("Total Number of deaths =",s2)


plt.barh(y_pos, (performance), align='center', alpha=0.5, 
                 color=(234/256.0, 128/256.0, 252/256.0), 
                 edgecolor=(106/256.0, 27/256.0, 154/256.0)) 
  
plt.yticks(y_pos, objects) 
plt.xlim(1,max(performance)+1000) 
plt.xlabel('Number of Cases') 
plt.title('Corona Virus Cases') 
plt.show() 
