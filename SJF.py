import os
import string
import time	


def SJF (dlist):
	i=0
	t=0
	t2=0
	timings={}
	dlist2=dlist
	while (len(dlist)):
		t2=t
		while (dlist[0]['bt']):
			if (dlist and t<dlist[0]['at']):
				while (t!=dlist[0]['at']):
					print("Idle time...")
					t+=1
			print ("Program "+ dlist[0]['pNo'] + " starts \n")
			print("sleep...")
			#time.sleep(1)
			t+=1
			dlist[0]['bt']=dlist[i]['bt']-1
		print ("Program "+ dlist[0]['pNo'] + " ends and took ");print (t2-dlist[0]['at']);print("sec in wait and turnaround time is");print (t-dlist[0]['at']); print("\n" )
		dlist.pop(0)
		dlist=sorted(dlist,key=lambda user:user['bt'])
		
			
		
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
	








