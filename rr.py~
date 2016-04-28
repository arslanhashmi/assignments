import os
import string
import time	
import copy

class Program:
	totalP=0
	time=5
	def __init__ (self,name,bt,at,wt,inpt):
		self.name=int(name)
		self.bt=int(bt)
		self.wt=int(wt)
		self.at=int(at)
		self.inputAfter=int(inpt)
		self.block=0
		self.finishtime=0
		self.remainingTime=time
		self.maxInWaiting=0
		Program.totalP+=1
	
	def display(self):
		print self.name,self.bt,self.wt,self.at,self.inputAfter


def RR (dlist):
	time=0
	dlist2=copy.copy(dlist)
	rQueue=[]
	wQueue=[]
	j=0
	while (j<3):
		print j,dlist2[j].name
		j+=1
	while (len (dlist) or len (rQueue) or len(wQueue)):
		#updateQueues(dlist,rQueue,wQueue,time)
		
		i=0
		while ( i<len (wQueue)):
			#print"in wq"
			#input()
			wQueue[i].maxInWaiting-=1
			if (wQueue[i].maxInWaiting<=0):
				input()
				rQueue.append(wQueue[i])
				wQueue.pop(i)
			i+=1
		i=0
		while (i<len(dlist)):
			#print"in qq"
			#input()
			
			if (dlist[i].at<=time):
				rQueue.append(dlist[i])
				dlist.pop(i)
				
			i+=1
		
		if (len(rQueue)):
			mxTime=time+dlist[0].time
		
			while (rQueue[0].bt!=0 and time<=mxTime and time<rQueue[0].remainingTime):
				print "Program ",rQueue[0].name," is executing"
				time+=1
				rQueue[0].bt-=1;
			if (rQueue[0].bt==0):		
				j=0
				while (j<3):
					print j,dlist2[j].name,rQueue[0].name
					if (dlist2[j].name==rQueue[0].name):
						break
					j+=1
				dlist2[j].finishtime=time
				input()
				rQueue.pop(0)
			elif (mxTime==time or rQueue[0].remainingTime==0):
				rQueue[0].remainingTime=rQueue[0].time
				rQueue.append(rQueue.pop(0))
			else:
				rQueue[0].remainingTime=mxTime-time
				rQueue[0].maxInWaiting=rQueue[0].wt	
				wQueue.append(rQueue.pop(0))
		else:
			print "Idle"
			time+=1
	
if __name__=="__main__":
	file=open("input","r")
	content= file.read()
	lines=content.splitlines()
	dlist=[]
	for i in xrange(0,3):
		p=lines[i].split()
		p=Program(p[0],p[1],p[2],p[3],p[4])
		p.display()
		dlist.append(p)
	dlist=sorted(dlist,key=lambda user:user.at)
	
	RR(dlist)
	








