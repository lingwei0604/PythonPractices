
变量可以指向函数
函数名也是变量
传入函数

def add (x,y,f):
	return f(x) + f(y)

x = -5
y = 6
f =abs

函数作为返回值
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		reurn ax
	reurn sum 		

当我们调用 lazy_sum（）返回的是求和函数。
调用 f 时，才真正的计算求和的结果。
f = lazy_sum(1,3,5,7,9)

f()

在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
f1()和f2()的调用结果互不影响。


返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

匿名函数

list(map(lamda x : x * x,[1,2,3,4,5,6,7,8,9]))

关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数 lambda x : x * x
def f(x):
	reurn x * x

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

f = lambda x : x  * x

def build(x,y):
	reurn lambda: x * x + y * y 

由于函数也是一个对象，而且函数对象可以被赋值给变量，通过变量也能调用该变量。
def now():
	print("2017")
f = now
f()

now.__name__
f.__name__	
















