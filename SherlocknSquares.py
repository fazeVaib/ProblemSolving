import math

n = int(input().strip())

for i in range(n):
    a, b = map(int, input().strip().split(' '))
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) +1)






