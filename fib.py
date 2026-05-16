def fibonacci(n):
    
    if n <= 0:
        return 1
    a = 0
    b = 1
    for _ in range(n):
        print(a , end= " ")
        
        c = a + b
        a = b
        b = c    
n = int(input("Enter the number of Fibonacci numbers: "))
fibonacci(n)
