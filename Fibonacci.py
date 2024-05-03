import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dynamic(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

n_values = list(range(1, 101))
execution_times_recursive = []
execution_times_dynamic = []
plot_needed = True

for n in n_values:
    start_time = time.time()
    result = fibonacci_recursive(n)
    execution_time = time.time() - start_time
    print(f"F({n}) is {result}, calculated in {execution_time:.6f} seconds using top-down (recursive) approach.")
    execution_times_recursive.append(execution_time)

    start_time = time.time()
    result = fibonacci_dynamic(n)
    execution_time = time.time() - start_time
    print(f"F({n}) is {result}, calculated in {execution_time:.6f} seconds using bottom-up (dynamic programming) approach.")
    execution_times_dynamic.append(execution_time)

    if max(execution_times_recursive[-1], execution_times_dynamic[-1]) > 100 and plot_needed:
        plt.plot(n_values[:n], execution_times_recursive, label='Top-down (Recursive)')
        plt.plot(n_values[:n], execution_times_dynamic, label='Bottom-up (Dynamic Programming)')
        plt.xlabel('n')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Time of Fibonacci Calculation')
        plt.legend()
        plt.show()
        plot_needed = False