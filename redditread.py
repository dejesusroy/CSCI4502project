#! /usr/bin/env python

import json


count = 0
comments = {}
comments['nodes'] = []
#the first method--encode each object individually as a json object, and individually append to file
#outfile = io.open('test1.json', 'w', encoding='utf8')

#second method -- 
#outfile = open('test6.json', 'w')
with open('redditComments.json') as f, open('politics2.json','w') as outfile:
    for line in f: #line is simply a string type?
        #stores each line as individual dictionary?  
        x = json.loads(line)
        #print type(x)
        #break;
        #test to store just one attribute of x (stores as unicode)
        subreddit = x['subreddit']
        #prints only the comments from the politics subreddit
        if (subreddit == 'politics'):
            #print "post to politics subreddit found
            #with io.open('testdoc.json', 'w', encoding='utf8') as outfile:
                #METHOD1
                #json.dumps(x,outfile)
                #str_ = json.dumps(x)
                #outfile.write((unicode(str_))+'/n')
                #METHOD2
                #json.dump(x, outfile)
                #outfile.write('/n')
                
                #METHOD3
                comments['nodes'].append(x)
        #tests the code with a sample size so it doesn't run for an hour each time
        count = count + 1 
        print "line", count, "processed" 
        if (count == 10000000):
        #    json.dump(comments,outfile)
             break 
    print "adding to .json file...." 
    json.dump(comments,outfile)

