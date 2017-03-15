tel = {'jack':1020,'sape':4139}
tel['guido'] = 1233
tel

del tel['sape']
tel['irv'] = 4127
tel
list(tel.keys())
['jack','sape','irv']

sorted(tel.keys())

'jack' in tel 
'jack' not in tel

循环技巧。

 在字典中循环时，关键字和对应的值可以使用 items() 方法同时释放出来：
 knights = {'gallahad':'the pure','robin':'the brave'}
 for k,c in knights.items():
 	print(k,v)

在 序列中循环时，索引位置和对应值可以使用 enumerate() 函数同时得到。

for i, v in enumerate(['tic','tac','toe']):
	print(i,v)


questtions = ['name','quest','favortive']
answers = ['lancellot','the holy grail','blue']

for q,a in zip(questtions,answers):
	print('whats is your {0}? it is {1}'.format(q,a))

	
需要逆向循环序列的话，先正向定位序列，然后调用 reversed() 函数:

>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1




要按排序后的顺序循环序列的话，使用 sorted() 函数，它不改动原序列，而是生成一个新的已排序的序列:

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear


若要在循环内部修改正在遍历的序列（例如复制某些元素），建议您首先制作副本。在序列上循环不会隐式地创建副本。切片表示法使这尤其方便:

>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']











