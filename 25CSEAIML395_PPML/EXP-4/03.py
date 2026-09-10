def fib(curr, next):
    for i in range(15):
        prev = curr
        curr = next
        next = prev + curr
        print(prev, end=" ") 

fib(1, 1)