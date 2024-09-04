def fibonacci(num):
    fib1 = 0
    fib2 = 1

    if num == fib1 or num == fib2:
        return f"O número {num} pertence a sequência de Fibonacci."
    
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
        
    if fib2 == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."
    

search_num = int(input("Informe um número: "))
print(fibonacci(search_num))
 