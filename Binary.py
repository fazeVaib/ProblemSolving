import itertools

n = int(input())
a = list(map(int, input().strip().split(' ')))


def fsub(s, m):
    return set(itertools.combinations(s, m))


max = 0
currmax = 0
1
list = fsub(a, 3)
curr_list = []

for i in list:
    if i[0]< i[1] < i[2]:
        currmax = i[0]*i[1]*i[2]
        if currmax > max:
            max = currmax
            curr_list = i
        elif currmax == max:
            if curr_list[0] > i[0]:
                curr_list = i
            elif curr_list[0] == i[0] and curr_list[1] > i[1]:
                curr_list = i

print(max)
print(curr_list[0], curr_list[1], curr_list[2])







































