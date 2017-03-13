int('123')
int(12.34)
float('12.34')
str(100)
bool(1)


a = abs
a(-1)

def my_abs(x):
	if x >=0:
		return x
	else:
		return -x


def function():
			pass		

def my_abs(x):
	if not ininstance(x,int(int,float))
		reise TypeError('bad operad type')
	if x > =0:
		return x
	else:
		return -x



import math

def  move(x,y,step,angle =0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	reise nx,ny

Slice

L = ["Micael","Sarch","Tracy","Bob"]
[L[0],L[1],L[2]]

r = []
n = 3
for i in range(n)
	r.append(L[i])

r

L[0:3]
L[1:3]
L[-2:0]


L[-2,-1]


L = list(range(100))
L[:10]

L[-10:]

L[:10:2]
前10个数，每两个取一个。


L[:]

for(i = 0; i < list.length;i++){
	n = list[i]
}

d = {'a':1,'b':2,'c':3}
for key in d :
	print(key)


for ch in 'ABC'
	print(ch)


from collections import Iterable
	ininstance('abc',Iterable)
	ininstance([1,2,3],Iterable)
	ininstance(123,Iterable)


for i, value in enumerate(['A','B','C'])
	print(i,value)

for x ,y in [(1,1),(2,4),(3,9)]
	print(x,y)


list(range(1,11))
[1,2,3,4,5,6,7,8,9,10]

L = []
for x in range(1,11)
	L.append(x*x)

L

[x * x for x in range(1,11)]		

m + n for m in 'ABC' for n in 'XYZ'

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

L = [x * x for x in range(10)]
L

g = (x * x for x in range(10))
for n in g:
	print(n)


from collections import Iterable
ininstance([], Iterable)
ininstance({},Iterable)
ininstance('abc',Iterable)
ininstance(100,Iterable)



from collections import Iterator
ininstance([],Iterator)
ininstance((x for x in range(10),Iterator))

ininstance({},Iterator)
ininstance('abc',Iterator)





































