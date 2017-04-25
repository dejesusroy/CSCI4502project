#! /usr/bin/env python

import json
from collections import Counter
subreddits = []

print "opening le files..."
with open('LeMotJuste.json') as f :
    x = json.load(f)
    for i in x['nodes']:
        subreddits.append(str(i['subreddit']))


commentcount = 0;
for i in range (0, len(subreddits)):
    commentcount = commentcount+1
#    print authors[i]

    #print "Author:",line[0],", Comments:",line[1]
#cleanly prints the 10 most common author names

sr = Counter(subreddits).most_common()
print "Number of comments: ", commentcount
print "Other subreddits: "
for line in sr:
    print line
                      
