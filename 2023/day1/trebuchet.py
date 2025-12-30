import re

ans = 0
for l in open('day1/input'):
    print("---")
    print(l)
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        l = l.replace(n, n + str(i+1) + n)

    x = re.findall(r'(\d)', l)
    xx = int(x[0] + x[-1])
    ans += xx
    print(l, x, xx, ans)

print(ans)