from encodings import utf_8
import urllib.request
import random

file = urllib.request.urlopen("https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")
f = file.read()
text = f.decode(encoding = 'utf_8', errors = 'ignore')

lines = text.split("\n")

reviews = {}

for line in lines:
    l = line.strip().split("\t")
    
    score = l[0]
    id = l[1]
    title = l[2]
    review = [3]
    
    reviews[id] = {"score" : score, "title" : title, "review" : review}
    
print(reviews[random.choice(list(reviews.keys()))])
print(reviews)