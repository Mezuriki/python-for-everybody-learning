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

print(counts)

tmp = list()
for k,v in counts.items():
    newt = (v,k)
    tmp.append(newt)

#print('Flipped', tmp)
tmp = sorted(tmp, reverse =True)
#print('Sorted', tmp[:5])

for v,k in tmp[:5]:
    print(k,v)