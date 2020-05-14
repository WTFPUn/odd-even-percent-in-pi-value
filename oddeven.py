import numpy as np
xpiread = open('pi.txt','r')
piread = xpiread.read()
#print(len(piread))
piread = str(piread[:100000])
pireadarray =[]
for i  in range(len(piread)):
    pireadarray.append(int(piread[i]))
pireadarray = np.array(pireadarray)
print(len(pireadarray))
sett = []
percent = []
for i in range(1):
    rngstart  = np.random.randint(1,len(pireadarray),1)
    rngend = np.random.randint(rngstart-1000,rngstart+1000,1)
    nrange = np.absolute(rngend-rngstart)
    sett.append(nrange)
    #print(sett)
    even = []
    odd = []
    truerng = pireadarray[rngstart[0]:rngend[0]]
    for j in range(len(truerng)):
        if truerng[j] % 2 == 0 :
                even.append(truerng[j])
        elif truerng[j] % 2 == 1 :
                odd.append(truerng[j])
    #print(odd)
    #print(even)
    print(len(odd))
    print(len(even))
    try :
        per = len(odd)/(len(odd)+len(even))
        percent.append(per)
    except ZeroDivisionError :
        i = i - 1
print(percent)
print(sum(percent)/len(percent))