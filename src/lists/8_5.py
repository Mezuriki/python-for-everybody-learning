fh = open("mbox-short.txt")
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From:"): continue
    word = line.split()
    print(word[1])
    count +=1

print("There were", count, "lines in the file with From as the first word")
