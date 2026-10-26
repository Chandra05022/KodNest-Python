def largest():
    a=20
    b=30
    c=40
    if(a>b and a>c):
        print("a is largest")
    elif(b>a and b>c):
        print("b is largest")
    else:
        print("c is largest")

largest()
def even():
    a=int(input("Enter the number:"))
    if(a%2==0):
        print("even")
    else:
        print("odd")
even()
def greet():
    a="chandu"
    print("Hello",a)

greet()
def square():
    n=5*5
    print("Square of 5 is",n)

square()
def square():
    n=5*5
    return n

print(square())
def square(n):
    res=n*n
    print(res)
square(10)
def square(n):
    res =n*n
    res=square(5)
    print(res)
c= 30
def add():
    global a
    a=10
    b=20
    print(a+b)
    print(c)
add()
print(a)
x=100
def display():
    print("local x:",x)
display()
print("global x:",x)

def add(a,b=0,c=0):
    return a+b+c
print(add(10,20))

def add(*args):
    total=0
    for i in args:
        total += i
    return total
print(add(10,20,30))

def stu_info(**kwargs):
    print(f"name is {kwargs['name']}",end =" " )
    print(f"age is {kwargs['age']}",end =" " )
    print(f"gender is {kwargs['gender']}",end =" " )
stu_info(name="chandu",age=21,gender="male")
def count(n):
    if n==0:
        return
    else:
        print(n)
        count(n-1)
count(5)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n -1)+fib(n-2)
print(fib(5))