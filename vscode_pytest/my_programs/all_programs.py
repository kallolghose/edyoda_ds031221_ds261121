def is_prime(num):
    prime_flag = True
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                prime_flag = False
                break
    return prime_flag
