n, k = map(int, input().strip().split(' '))

cloud = list(map(int, input().strip().split(' ')))

print(100 - sum(1 + 2*cloud[i] for i in range(0, n, k)))