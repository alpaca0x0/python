# -*- coding: utf-8 -*

import sys

mySteps=0

def hanoi(n, A, B, C):
	global mySteps

	if n == 0:
		return
	else:
		hanoi(n-1, A, C, B)
		mySteps=mySteps+1
		print(str(mySteps)+") Moved "+str(n)+" From " + A + " To " + C)
		hanoi(n-1, B, A, C)

if(len(sys.argv)>1):
	n=int(sys.argv[1])
if(n<1):
	n = int(input("請輸入環數："))

hanoi(n, "A", "B", "C")
print('最佳解：'+str(pow(2,n)-1)+"\n"+'運算解：'+str(mySteps))