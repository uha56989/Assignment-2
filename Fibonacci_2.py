import matplotlib.pyplot as plt

def fibonacci_recursive_count(n, count):
    if n == 4:
        count[0] += 1
    if n <= 1:
        return n
    else:
        return fibonacci_recursive_count(n-1, count) + fibonacci_recursive_count(n-2, count)

count_f4 = []

for i in range(5, 51):
    count = [0]
    fibonacci_recursive_count(i, count)
    count_f4.append(count[0])
    print(f"For n = {i}, the count of F(4) computations is {count[0]}")
    if i == 40 or i == 45 or i == 50:
        plt.figure(figsize=(12, 6))
        plt.plot(list(range(5, i+1)), count_f4, label='Count of F(4) Computations', color='blue')
        plt.xlabel('n')
        plt.ylabel('Count of F(4) Computations')
        plt.title('Number of Times F(4) is Computed for F(n) (n=5 to 40)')
        plt.legend()
        plt.grid(True)
        plt.show()

n_value = list(range(5, 51))

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(n_value, count_f4, label='Count of F(4) Computations', color='blue')
plt.xlabel('n')
plt.ylabel('Count of F(4) Computations')
plt.title('Number of Times F(4) is Computed for F(n) (n=5 to 50)')
plt.legend()
plt.grid(True)
plt.show()