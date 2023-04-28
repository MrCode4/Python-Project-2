import math

x = int(input())

result1 = math.ceil(math.pow(x, 5/3) + math.tan(math.radians(x)))
result2 = math.floor(math.pow(math.pi, 2 + math.atan(pow(math.sin(math.radians(x)),2))))

result = math.gcd(result1, result2)

print(result)