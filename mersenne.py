def isPrime(n):
    for i in range(2, (n//2)+1):
        if n%i == 0:
            return False
    return True
    
i=1
while True:
    i+=1
    if isPrime((2**i)-1):
        print((2**i)-1)

    