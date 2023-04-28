import random

def is_aval(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

a, b = input().split()

a = int(a)
b = int(b)

for i in range(a,b+1):
    if( is_aval(i) ):
        x = i
        while(True):
            if x < 100:
                if is_aval(x):
                    print(i)
                break
            else:
                if not is_aval(x%100):
                    break
                else: x = x // 10


            