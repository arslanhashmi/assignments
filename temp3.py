import string
import time    
import copy
global time
time = 0
class Program:
    totalP=0
    time=5
    def __init__ (self,name,bt,at,wt,inpt):
        self.name=int(name)
        self.bt=int(bt)
        self.wt=int(wt)
        self.at=int(at)
        self.inputAfter=int(inpt)
        self.inputAfterFinal = int(inpt)
        self.block=0
        self.finishtime=0
        self.remainingTime = Program.time
        self.maxInWaiting=0
        Program.totalP+=1
    
    def display(self):
        print (self.name,self.bt,self.wt,self.at,self.inputAfter)

def waitCheckDoNothing(wQueue,rQueue,aQueue):
    global time
    i = 0
    while ( i<len (wQueue)):
        if (wQueue[i].maxInWaiting <= 0):
            if (wQueue[i].maxInWaiting <= 0):
                if wQueue[i].remainingTime == 0:
                    rQueue.append(wQueue.pop(i))
                else:
                    aQueue.append(wQueue.pop(i))
            i -= 1
        i+=1

def waitCheck(wQueue,rQueue,aQueue):
    global time
    i=0
    while ( i<len (wQueue)):
        wQueue[i].maxInWaiting-=1
        if (wQueue[i].maxInWaiting <= 0):
            if wQueue[i].remainingTime == 0:
                rQueue.append(wQueue.pop(i))
            else:
                aQueue.append(wQueue.pop(i))
            i -= 1
        i+=1

def RR(dlist):
    global time
    time=0
    dlist2=copy.copy(dlist)
    rQueue=[]
    wQueue=[]
    aQueue = []
    check = False
    
    if time == 0:
        i = 0
        while (i<len(dlist)):            
            if (dlist[i].at<=time):
                rQueue.append(dlist.pop(i))
            i+=1

    while (len (dlist) or len (rQueue) or len(wQueue) or len(aQueue)):
        #updateQueues(dlist,rQueue,wQueue,time)
        if(len(aQueue)):
            while len(aQueue) != 0:
                rQueue.insert(0, aQueue.pop(0))
        if (len(rQueue)):
            check = False
            mxTime=time+rQueue[0].time
            
            while (rQueue[0].bt!=0 and time<=mxTime  and rQueue[0].inputAfter != 0):
                if time >= time + rQueue[0].remainingTime:
                    break
                waitCheck(wQueue, rQueue, aQueue)
                i=0
                while (i<len(dlist)):            
                    if (dlist[i].at<=time):
                        rQueue.append(dlist.pop(i))
                        
                    i+=1
                time+=1
                i=0
                rQueue[0].bt-=1;
                rQueue[0].inputAfter -= 1
            if (rQueue[0].bt==0):        
                j=0
                while (j<3):
                    if (dlist2[j].name==rQueue[0].name):
                        break
                    j+=1
                dlist2[j].finishtime=time
                print ("Program ",rQueue[0].name," has finished execution at time ",time)
                rQueue.pop(0)
            elif (mxTime==time or rQueue[0].remainingTime==0) and rQueue[0].inputAfter != 0:
                rQueue[0].remainingTime=rQueue[0].time
                print ("Program ",rQueue[0].name," is goint to reqady queue at time ",time)
                rQueue.append(rQueue.pop(0))
            else:
                rQueue[0].remainingTime=mxTime-time
                rQueue[0].maxInWaiting= rQueue[0].wt
                rQueue[0].inputAfter = rQueue[0].inputAfterFinal 
                print ("Program ",rQueue[0].name," is going to waiting queue at time ",time)   
                wQueue.append(rQueue.pop(0))
        else:
            check = True
            i=0
            while (i<len(dlist)):            
                if (dlist[i].at<=time):
                    rQueue.append(dlist.pop(i))
                    check = False
                i+=1
        i = 0
        while (i<len(dlist)):            
            if (dlist[i].at<=time):
                rQueue.append(dlist.pop(i))
                check = False
            i+=1
        waitCheckDoNothing(wQueue, rQueue,aQueue)
        if check == True:
            time += 1
            i = 0
            while (i<len(dlist)):            
                if (dlist[i].at<=time):
                    rQueue.append(dlist.pop(i))
                    check = False
                i+=1
            waitCheck(wQueue, rQueue, aQueue)
            check = False
    
if __name__=="__main__":
    file=open("inputtemp.txt","r")
    content = file.read()
    lines=content.splitlines()
    dlist=[]
    for i in range(0,3):
        p=lines[i].split()
        p=Program(p[0],p[1],p[2],p[3],p[4])
        p.display()
        dlist.append(p)
    dlist=sorted(dlist,key=lambda user:user.at)
    
    RR(dlist)