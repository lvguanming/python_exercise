# -- coding:utf-8 --
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
print('----------------------------')

def parrot(voltage, state='a stiff', action='voom'):
	"""Do nothing ,but document it.

	This is a Function of Test
	but this will be do nothing. 
	Sorted it can bu lake from yet.
	"""
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)  #-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

print(parrot.__doc__)

print('----------------------------')


def f(ham:43,eggs: int = 'spam') -> "nothing to see there":
	print("Annotations:",f.__annotations__)
	print("Arguments:",ham,eggs)
	return lambda x:x+ham

f1 = f(12,'wonderful')
a = f1(10)
print(a)

from collections import deque
list0 = [11.2,'xxxxx',43.2,332,3,20,44]
list1 = deque(list0)

while len(list0)>0:
	v = list0.pop();
	print(v)


while len(list1)>0:
	v = list1.popleft();
	print(v)

from math import pi
pis = [str(round(pi,i)) for i in range(1,15)]
print(pis)

matrix=[
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
]
transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)

print(transposed)

print(list(zip(*matrix)))