
squares = []
for x in range(10):
	squares.append(x**2)

squares


squares = list(map(lambda x : x ** 2,range(10)))

squares = [x**2 for x in range(10)]


[(x,y) for x in [1,2,3] for y in [3,1,4] if x ! =y]

combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x x != y:
			combs.append((x,y))

combs


vec = [-4,-2,0,2,4]
[x * 2 for x in vec]

[x for x in vec if x >= 0]

[abs[x] for x in vec]


freshfruit = ['banaba','loganberry','passion fruit']
[weapon.strip() for weapon in freshfruit]


[(x,x**2) for x in range(6)]

vec = [[1,2,3],[4,5,6],[7,8,9]]
[num for elem in vec for num in elem]


form math import pi 
[str[round[pi,i] for i in range(1,6)]]


a = [-1,1,66.25,333,333,1234.5]
del a[0]
a

del a[2:4]
a

del a [:]
a

del a 


列表和字符串有很多通用的属性，它们都是 序列类型。

元组是另一种标准序列类型。

t = 123345,54321,'hello'
t[0]
t
u = t,(1,2,3,4,5)
u
((12345,544321,'hello'),(1,2,3,4,5))
v = ([1,2,3],[3,2,1])

元组总是在输出时有括号的，以便于正确表达嵌套结构。
在输入时可以有或没有括号，不过经常括号都是必须的
（如果元组是一个更大的表达式的一部分）。不能给元组的一个独立的元素赋值
（尽管你可以通过联接和切割来模拟）。还可以创建包含可变对象的元组，
例如列表。
元组是不可变的，


元组就像字符串， 不可变的。通常包含不同种类的元素并通过分拆
（参阅本节后面的内容) 或索引访问（如果是 namedtuples，甚至可以通过属性）。列表是 可变的 ，它们的元素通常是相同类型的并通过迭代访问。


empty = ()
singeton = 'hello',
len(empty)
0
len(singeton)
1
>>>singeton
('hello',)


basket = {'apple','organ','apple','pear','orange','banana'} 
print(basket)
'orange' in basket
'crabgrass' in basket
a = set('abracadabra')
b = set('alaczaam')
a
{'a','r','b','c','d'}
a - b
a | b
a & b
a ^ b








