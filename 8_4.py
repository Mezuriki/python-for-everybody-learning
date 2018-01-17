fh = open("romeo.txt")
lst = list()
for line in fh:
    spl = line.rstrip().split( )
    for x in spl:
        if x in lst: continue
        else:
            lst.append(x)
lst.sort()
print(lst)
