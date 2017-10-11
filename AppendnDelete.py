s = input().strip()
t = input().strip()
k = int(input().strip())

commonLength = 0

for i in range(min(len(s), len(t))):
    if s[i] == t[i]:
        commonLength = commonLength + 1
    else:
        break

if ((len(s) + len(t) - 2 * commonLength) < k and k % 2 == 0) \
        or (len(s) + len(t) - 2 * commonLength) == k:
    print("Yes")

elif (len(s) + len(t) - 2 * commonLength) < k \
        and (k - (len(s) + len(t) - 2 * commonLength)) > 2 * commonLength:
    print("Yes")

elif len(s) + len(t) < k:
    print("Yes")

else:
    print("No")
