import os
import urllib.request
import json
import cv2



path_raw_data = "../../data/Raw/tweets.jsonl"
path_out_data = "../../data/Raw/train_test.json"

beliver_hashtag=["#climatechangeisreal","#actonclimate","#extinctionrebellion","#climateemergency","#climateactionnow"]
denier_hashtag=["#climatechangeisfalse","#climatechangenotreal","#climatechangehoax","#globalwarminghoax","#tcot","#ccot","#tlot","#pjnet","#rednationrising","#votered","#libtard","#libtards"]

raw_data = [json.loads(line) for line in open(path_raw_data, 'r')]

_d = 0
_b = 0
for tweet in raw_data:
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
with open(path_out_data, 'w') as fp:
    json.dump(raw_data, fp)


print(f"Deniers: {_d}\nBelievers: {_b}\nUnknow: {len(raw_data)-_d-_b}")