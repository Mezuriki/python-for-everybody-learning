"""
Exercise 2: This program counts the distribution of the hour of the day for each of the
messages. You can pull the hour from the "From" line by finding the time string
and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts,
one per line, sorted by hour as shown below.

Sample Execution:

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
counts = dict()
mails = list()
hourslist = {}
tuple_list = []
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        mail = line[5]
        mail = mail.split(':')
        mail = mail[0]
        hourslist[mail] = hourslist.get(mail,0) + 1
for mail, count in hourslist.items():
    tuple_list.append((mail, count))
tuple_list.sort()
for mail, counts in tuple_list:
    print (mail,count)
