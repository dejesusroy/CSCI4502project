# Tutorial code found at: "http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/"
# Run using Python 3

# If Python 2 is the only option, uncomment the following:
#from __future__ import division, unicode_literals

# If we want to remove stop words, we will have to implement NLKT lib which has 2.4k stop words listed
# We can do this by hand
# Or we can supply various "documents"
# Textblob will remove words that are frequent in across all documents according to the instructions


import math
from textblob import TextBlob as tb

def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return (float)(sum(1 for blob in bloblist if word in blob))

def idf(word, bloblist):
    return (float)(math.log(len(bloblist)) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return (float)((float)(tf(word, blob)) * (float)(idf(word, bloblist)))

# As a giant string
document1 = tb("""Enter Text Here""")

# As a document
with open("words2.txt") as inFile:
    document2 = tb(inFile.read().lower())

# More documents or words will push the ranking of stop words lower.
with open("words.txt") as f:
	document3 = tb(f.read().lower())


bloblist = [document1, document2, document3]


for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("Word: {}, TF-IDF Score: {}".format(word, round(score, 5)))