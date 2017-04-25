#! /usr/bin/env python

import json


count = 0
comments = {}
comments['nodes'] = []
#the first method--encode each object individually as a json object, and individually append to file
#outfile = io.open('test1.json', 'w', encoding='utf8')

#second method -- 
#outfile = open('test6.json', 'w')
index = 0
with open('redditComments.json') as infile, open('LeMotJuste.json','w') as outfile:
    for line in infile: #line is simply a string type?
        #stores each line as individual dictionary?
        if count > index:
            x = json.loads(line)
            subreddit = x['subreddit']
            author = x['author']
            if (subreddit != 'politics' and author == 'LeMot-Juste'):
                comments['nodes'].append(x)
        count = count + 1
        print "line", count, "processed"
        #if (count == 40000000):
            #json.dump(comments,outfile)
        #    break
    print "adding to .json file...."
    json.dump(comments,outfile)



                                   
