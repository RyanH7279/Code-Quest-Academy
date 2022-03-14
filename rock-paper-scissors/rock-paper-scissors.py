cases = int(input())
for case in range(cases):
    inf = input().split(" ")

    if "R" in inf and "P" in inf and "S" in inf: #blocks all three
        print("NO WINNER")
        continue

    if "R" in inf and "P" in inf and inf.count("P") == 1:
        print("PAPER")
        continue
    if "P" in inf and "S" in inf and inf.count("S") == 1:
        print("SCISSORS")
        continue
    if "S" in inf and "R" in inf and inf.count("R") == 1:
        print("ROCK")
        continue

    print("NO WINNER")
    