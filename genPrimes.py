def genPrimes():
    flag=True
    primes=[2]
    i = 3
    while True:
        if flag:
            primes.append(i-1)
            yield primes[-1]
        for j in primes:
            if i%j == 0:
                flag = False
                break
            else:
                flag = True
        i += 1