def fibonacci(n):
    fib_sequence = [0, 1]  # İlk iki Fibonacci sayısını tanımla

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence

n = int(input("Fibonacci dizisinin kaç terimini görmek istersiniz?  "))
fib_result = fibonacci(n)
print(fib_result)
