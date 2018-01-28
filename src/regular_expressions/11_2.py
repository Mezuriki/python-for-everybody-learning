"""
Exercise 2: Write a program to look for lines of the form
`New Revision: 39772`
and extract the number from each of the lines using a regular
expression and the findall() method. Compute the average of the numbers and print out the average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259
"""
import re
count = 0
sum_=0
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: (.*)', line)
    if len(x) > 0:
        count +=1
        sum_ = sum_+ float(x[0])
print(round(sum_/count, 7))
