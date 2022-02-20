# Recursion Approach
def factorial(n):
    # Base Case
    if n == 0:
        return 1
    fact = n * factorial(n-1)
    return fact


# TC = O(n^2)
def loop_in_loop(n):
    avg = 1
    for i in range(0, n):
        for j in range(5, n):
            avg = i * j

    for i in range(n, n*10):
        avg = avg * i

    return avg
















# Iterative Approach using loops
def factorial_itr(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Write a recursive function to find the
# sum of n positive integers
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)


if __name__ == "__main__":
    print(factorial(5))