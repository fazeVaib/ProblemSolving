n = int(input())
width = len(list(bin(n))[2:])
for i in range(1, n+1):
    print(str(i).rjust(width, ' '), str(oct(i))[2:].rjust(width, ' '),
          str(hex(i))[2:].rjust(width, ' ').upper(),
          str(bin(i))[2:].rjust(width, ' '), sep=' ')
