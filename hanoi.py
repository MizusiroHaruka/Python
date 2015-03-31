# -*- coding: utf-8 -*-
global num
num=0
def p(start,end):
	print('move from '+str(start)+' to '+str(end))
def t(n,start,end,free):
        global num
	if n==1:
		p(start,end)
		num+=1
	else:
		t(n-1,start,free,end)
		t(1,start,end,free)
		t(n-1,free,end,start)
t(10,1,2,3)
print(str(num))
#完成汉诺塔所需的最少步数是2**n（层数）-1
