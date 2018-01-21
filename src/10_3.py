"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z. Your program
should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples
from several different languages and see how letter frequency varies between languages.
Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.
"""
import string
fhand = open("mbox-short.txt")
words = fhand.read()
words = words.lower()
twords = tuple(words)
letters = list()
for x in twords:
    if x.isalpha() == True:
        letters.append(x)

letter = dict()
for w in letters:
    letter[w]=letter.get(w,0)+1

result = list()
for k,v in letter.items():
    result.append((v,k))

result.sort(reverse=True)

for f,l in result[:]:
    print(l,f)