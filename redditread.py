#! /usr/bin/env python

import json
from pprint import pprint


count = 0
with open('redditComments.json') as f:
    for line in f: #line is simply a string type?
        #stores each line as individual dictionary?  
        x = json.loads(line)
        #test to store just one attribute of x (stores as unicode)
        subreddit = x['subreddit']
        #prints only the comments from the politics subreddit
        if (subreddit == 'politics'):
            #print "post to politics subreddit found
            print x
        #tests the code with a sample size so it doesn't run for an hour each time
        #count = count + 1  
        #if (count == 100000):
           # break


