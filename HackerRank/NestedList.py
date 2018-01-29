if __name__ == '__main__':
    myList = []
    for _ in range(int(input())):
        myList.append([input(), float(input())])
    secHigh = sorted(list(set(marks for name, marks in myList)))[1]
    print('\n'.join([a for a, b in sorted(myList) if b == secHigh]))
common = 'string'
for c in common:
    if c.isupper():
        c = c.lower()
