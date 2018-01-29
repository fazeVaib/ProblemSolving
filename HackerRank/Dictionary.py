if __name__ == '__main__':
    dic = {}
    for _ in range(int(input())):
        s = input().split()
        dic[s[0]] = list(map(float, s[1:]))
    query = input()
    print('%.2f' % (sum(dic[query]) / 3))
