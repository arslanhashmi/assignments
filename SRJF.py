import os
import string
import time	


def SRTF (dlist):
	i=0
	t=0
	timings={}
	dlist2=dlist
	while (len(dlist)):
		
		if (dlist and t<dlist[0]['at']):
				while (t!=dlist[0]['at']):
					print("Idle time...")
					t+=1
		print ("Program "+ dlist[0]['pNo'] + " starts \n")
		print("sleep...")
		#time.sleep(1)
		t+=1
		dlist[0]['bt']=dlist[i]['bt']-1
		if (dlist[0]['bt']==0):
			timings[dlist[0]['pNo']]=t	
			dlist.pop(0)
		dlist=sorted(dlist,key=lambda user:user['bt'])
		
	i=0
	while(i<3):		
		print ("Progsram "+ dlist2[i]['pNo'] + " ends and took ");print (timings[dlist2[i]['pNo']]-dlist2[i]['at']-dlist2[i]['bt']);print( "sec in wait and turnaround time is");print (timings[dlist2[i]['pNo']]-dlist2[i]['at']); print("\n" )
		i=i+1
	print ("Through put is" ); print (t/3)



	
if __name__=="__main__":
	file=open("input","r")
	content= file.read()
	lines=content.splitlines()
	
	d={};
	dlist=[]
	for i in xrange(0,3):
		p=lines[i].split()
		d['pNo']=p[0]
		d['bt']=int(p[1])
		d['at']=int(p[2])
		dlist.append(d.copy())
	dlist=sorted(dlist,key=lambda user:user['at'])
	SJF(dlist)
	print (dlist)
	








