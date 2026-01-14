def add(a,b):
    print(a+b)

def sub(a,b):
    return a-b,a

add(10,20)
print(sub(30,20))


def multi(a,b):
    return(a*b),a
print(multi(10,20))

def hello(greeting = "hello", name = "world"):
    print('%s,%s'%(greeting,name))
hello()
hello('greetings','mahi')
def print_param(*params):
    print(params)
print_param('testing')
print_param(1,2,3,4)
def print_param1(**params):
    print(params)

print_param1(x=1,y=2,z=3)
