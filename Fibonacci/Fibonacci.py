cases = int(input())
for case in range(cases):
    n = int(input())
    l2 = []
    if n == 1:
        print("1 = 0")
    else:
        for i in range(n-1):
            t = 0
            for l in l2:
                t += l
            if t == 0: t += 1
            l2.append(t)
            if len(l2) > 2: l2.pop(0)
        print(str(n) + " = " + str(t))