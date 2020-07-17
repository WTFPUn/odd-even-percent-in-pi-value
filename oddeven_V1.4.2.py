import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import datetime
conn = sqlite3.connect('oddevendatabase.db')
c = conn.cursor()
c.execute("DELETE FROM rngtime")

xpiread = open('pi.txt','r')
piread = xpiread.read()
#print(len(piread))

piread = str(piread[:100000])
pireadarray =[]
random = np.random

counti = []

for i  in range(len(piread)):
    pireadarray.append(int(piread[i]))
pireadarray = np.array(pireadarray)
print(len(pireadarray))
sett = []
percent = []
irange = np.arange(len(pireadarray))[1000:len(pireadarray)-1000]
rirange = irange * -1
ichoose = np.asscalar(np.random.choice(np.concatenate((irange,rirange),axis =None)))
i = 1
while i != 1000 :
    
    rngstart  = random.randint(1,len(pireadarray),1)
    rngend = ichoose
    nrange = np.absolute(rngend-rngstart)
    sett.append(nrange)
    #print(sett)
    even = []
    odd = []
    truerng = pireadarray[rngstart[0]:rngend]
    for j in range(len(truerng)):
        if truerng[j] % 2 == 0 :
                even.append(truerng[j])
        elif truerng[j] % 2 == 1 :
                odd.append(truerng[j])


    #print(odd)
    #print(even)
    #print(len(odd))
    #print(len(even))


    try :
        per = len(odd)/(len(odd)+len(even))
        percent.append(per) 
        tf_check = True
        
    except ZeroDivisionError :
        i = i - 1
        tf_check = False
    if tf_check == True :
        insert = [datetime.datetime.now(),i,per,1-per,np.asscalar(nrange)]
        c.execute("INSERT INTO rngtime VALUES(?,?,?,?,?)",insert)
        i = i + 1

    
#print(percent)
print(sum(percent)/len(percent))
conn.commit()
conn.close()
plt.scatter(np.arange(len(percent))+1,percent,alpha=.5)
plt.show()

#แก้บัคบางส่วน และบัคบางส่วนเพิ่มขึ้นมา :)