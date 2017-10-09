n = int(input())

ele = input().split(' ')
arr = [int(i) for i in ele]

arr.insert(0, 999)
for i in range(1, n+1):
    print(arr.index(arr.index(i)))
