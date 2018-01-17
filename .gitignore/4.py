import random

articles = ["the", "a", "her", "his"]
nouns = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

for line in range(5):
    article = random.choice(articles)
    noun = random.choice(nouns)

    print (article, noun)