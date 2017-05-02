import json
import csv

filename='''Original JSON file name here'''
outfilename='''File output name'''


with open(outfilename,'w') as csvFile:
    fieldnames=["edited","id","parent_id","distinguished","created_utc","subreddit_id","retrieved_on","author_flair_css_class","author_flair_text","controversiality","link_id","score","author","subreddit","body","stickied","gilded"]
    writer=csv.DictWriter(csvFile,quotechar='"', fieldnames=fieldnames,quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    with open(filename, 'r') as f:
        for line in f:
            x=json.loads(line)
            text = [word.strip("\n\",") for word in x["body"].lower().split()]
            finaltext=''
            for thing in text:
                if(thing != '"'):
                    finaltext=finaltext+thing+' '
            finaltext=finaltext+''
            print(finaltext)
            writer.writerow({"edited": x["edited"],
                        "id":x["id"],
                        "parent_id":x["parent_id"],
                        "distinguished":x["distinguished"],
                        "created_utc":x["created_utc"],
                        "subreddit_id":x["subreddit_id"],
                        "retrieved_on":x["retrieved_on"],
                        "author_flair_css_class":x["author_flair_css_class"],
                        "author_flair_text":x["author_flair_text"],
                        "controversiality":x["controversiality"],
                        "link_id":x["link_id"],
                        "score":x["score"],
                        "author":x["author"],
                        "subreddit":x["subreddit"],
                        "body":finaltext,
                        "stickied":x["stickied"],
                        "gilded":x["gilded"]})
