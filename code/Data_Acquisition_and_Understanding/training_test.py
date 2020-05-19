import os
import urllib.request
import json
import cv2



path_raw_data = "../../data/Raw/tweets.jsonl"
path_out_data = "../../data/Raw/train_test.json"

beliver_hashtag=["#climatechangeisreal","#actonclimate","#extinctionrebellion","#climateemergency","#climateactionnow"]
denier_hashtag=["#climatechangeisfalse","#climatechangenotreal","#climatechangehoax","#globalwarminghoax","#tcot","#ccot","#tlot","#pjnet","#rednationrising","#votered","#libtard","#libtards"]

#raw_data = [json.loads(line) for line in open(path_raw_data, 'r')]
#raw_data = []
_d = 0
_b = 0

r = []

with open(path_out_data, 'w') as fp:
    json.dump(r, fp)

#for i, tweet in enumerate(raw_data):
with open(path_raw_data) as infile:
    with open(path_out_data, 'a') as outfile:
        for i, line in enumerate(infile):
            tweet = json.loads(line)
            if i % 100 == 0:
                print( f"{i}/?")
            tweet["class"] = "unknown"
            for hashtag in tweet["entities"]["hashtags"]:
                v = "#" + hashtag['text'].lower().strip()
                if v in denier_hashtag:
                    tweet["class"] = "denier"
                    _d += 1
                    break
                elif v in beliver_hashtag:
                    tweet["class"] = "beliver"
                    _b += 1
                    break
            json.dump(tweet, outfile, indent=4)
        #raw_data.append(tweet)
        
#print(f"Deniers: {_d}\nBelievers: {_b}\nUnknown: {len(raw_data)-_d-_b}")
print(f"Deniers: {_d}\nBelievers: {_b}\nUnknown: ?")



