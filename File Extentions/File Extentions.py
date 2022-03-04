cases = int(input())
total = []
for case in range(cases):total.append(input().split(".")[1])
p = {}
for type in total: p[type] = total.count(type)
for key, value in p.items(): print(key + " " + str(value))