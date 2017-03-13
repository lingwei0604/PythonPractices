
class Student(object)
	def __init__(self,name,score)
		self.name = name
		self.score = score

	def print_score(self):
			print(self.name,self.score)
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


bart = Student

给它自由的绑定一个那么属性
bart.name = "lingwei"

bart = Student('Bart Simpson', 59)
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))




class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score():
		print('%s:%s'%(self.__name,self.__core))

	def get_name(self):
		return self.__name

	def get_score():
		return self.__score

	def set_score(self,score):
		if 0 <= socre <= 100:
			self.__score = socre
		else:
			raise ValueError('bad socre')

class Animal(object):
	def run(self):
		print('Animal is running')




calss Dog(Animal):
	def run(self):
		print("Dog is running")

	def run(self):
		print("Eating meat...")



class Dgo(Animal):
	def run(self):
		print("Dog is running")
class Cat(Animal):
    def run(self):
    	print("Cat is running")


a = list()
b = Animal()
c = Dog()


isinstance(a,list)
isinstance(b,Animal)
isinstance(c,Dog)
isinstance(c.Animal)


file-like-object
动态语言：则不一定需要传入Animal类型
我们只需要保证传入的对象有一个run方法就OK。


判断对象类型
基本类型可以用type（）函数
type(123)
type(abs)

对于继承关系的，我们可以使用 isinstance()

a = Animal()
d = Dog()
h = Hucky()
isinstance(h,Hucky)

isinstance(d,Dog) and isinstance(d,Animal)

能用type（） 判断的也能使用 isinstance()判断

使用dir 获得一个对象的所有属性和方法，
返回一个包含字符串的list。

配合 gatatter(),setattr(),hasattr() women可以直接操作一个
对象的状态。


实例属性和类属性。













