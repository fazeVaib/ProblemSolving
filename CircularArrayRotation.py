n, p, q = input().strip().split(' ')
n, p, q = [int(n), int(p), int(q)]

arr = []
ele = input().split(' ')
for i in ele:
    arr.append(int(i))

for i in range(p):
    value = arr.pop()
    arr.insert(0, value)

for i in range(q):
    s = int(input())
    print(arr[s-1])


