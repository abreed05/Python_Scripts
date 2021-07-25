with open('c:\\Users\\path\\to\\list1.txt') as f1:
    lines1 = [line.rstrip() for line in f1]

with open('c:\\Users\\path\\to\\list2.txt') as f2:
    lines2 = [line.rstrip() for line in f2]

difference = list(set(lines1) - set(lines2))
for line in difference:
    print(line)