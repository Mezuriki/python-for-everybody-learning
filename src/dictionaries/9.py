handle = open("mbox-short.txt")
counts = dict()
bigcount = None
bigword = None
words = list()
for line in handle:
    #line = line.rstrip()
    if not line.startswith('From '): continue
    word = line.split()
    words.append(word[1])
for x in words:
    counts[x] = counts.get(x, 0) + 1

for y, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = y
        bigcount = count

print(bigword,bigcount)



