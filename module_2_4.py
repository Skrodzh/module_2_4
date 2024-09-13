numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i < 2:
        continue
    is_primes = True # по умолчанию принимаю число простым
    for div in range(2, i): # доступные делители для числа от 2 не включая сам элемент (i = i-1)
        if i % div == 0:
            is_primes =False
            break
    if is_primes:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)



