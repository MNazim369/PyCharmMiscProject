#4. Fibonacci Series
#✅ Easy Logic (looping)
def fabonacci(n):
    a,b= 0,1
    for _ in range(n):
        print(a,end= " ")
        a,b = b,a+b
fabonacci(5)

#✅ Alternative (Recursion)
def fib(n):
    if n<=1 :
        return n
    return fib(n-1) + fib(n-2)
print([fib(i) for i in range(5)])

#3rd EASY Mehthod:
def fabonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,n):
        c = a + b
        a=b
        b=c
        print(c)
print(fabonacci(6))

