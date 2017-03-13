try:

    print('try...')
    r = 10 / 0
    print('result',r)
except ZeroDivisionError as e:
	print(e)
finally:
	print("finlly")
print("End")

try:
    print("try..")
    r = 10 / int("a")
    print("try...")
except ValueError as e:
	print()
except ZeroDivisionError as e:
	print()
finally:
	print("finally")
print("END")


try:
	print("try...")
	r = 10 /(int)a
	print('result':r)
except ValueError as e:
	print("ZeroDivisionError ",e)
except ZeroDivisionError as e
    print("ValueError":e)
else:
	print("no error")
finally:
	print('finally...')
print("ENd")

try:
	foo()
except ValueError as e:
	print("ValueError")
except UnicodeError as e:
	print("UnicodeError")




def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar("0")
	except Exception as e :
		print("Error",e)
	finally:
	print("finally")


class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n = 0:
		raise FooError("this is a error")
	return 10/ n		


foo("0")




def foo(s):
	n = int(s)
	if n==0;
		raise ValueError('this is a error')
	return 10/n
	
def bar():
	try:
		foo('0')
	except ValueError as e:
		print("Valueerror")
		raise			

bar()











