#fibonecci function
def fib(n):
    a = 0
    b = 1
    if n == 1:   
       print (a)
    else:
        for i in range(2,n):
            c = a + b      
            a = b
            b = c
            print(c)
    return n

n = int(input(f"Enter the value of the number: "))   #user input
fib(n)
