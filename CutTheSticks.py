n = int(input())

arr = list(map(int, input().strip().split(' ')))

while arr:
    print(len(arr))
    arr = [x for x in arr if x != min(arr)]
