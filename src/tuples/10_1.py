"""
Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses
from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email)
tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""
counts = dict()
mails = list()
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From: "): continue
    line = line.split()
    mails.append(line[1])
for mail in mails:
    if mail not in counts:
       counts[mail] = 1
    else:
       counts[mail] += 1
tmp = list()
for c,m in counts.items():
    new=(m,c)
    tmp.append(new)
tmp = sorted(tmp, reverse =True)
for m,c in tmp[:1]:
    print (c,m)