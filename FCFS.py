import os
import string
import time	
def FCFO (dlist):
	i=0
	t=0
	while (i<3):
		if (i<3 and t<dlist[i]['at']):
			while (t!=dlist[i]['at']):
				print("Idle time...")
				t+=1
		print ("Program "+ dlist[i]['pNo'] + " starts \n")
		t2=t
		while (dlist[i]['bt']!=0):
			print("sleep...")
			#time.sleep(1)
			t+=1
			dlist[i]['bt']=dlist[i]['bt']-1
		print ("Program "+ dlist[i]['pNo'] + " ends and took ");print (t2-dlist[i]['at']);print("sec in wait and turnaround time is");print (t-dlist[i]['at']); print("\n" )
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
	FCFS(dlist)
	
	








