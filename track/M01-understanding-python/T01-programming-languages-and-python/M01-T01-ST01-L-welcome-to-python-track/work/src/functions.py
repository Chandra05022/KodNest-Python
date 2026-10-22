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