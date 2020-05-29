import os
import urllib.request
import json
import cv2
import pandas as pd
from pyagender import PyAgender


path_raw_data = "../../data/Raw/tweets.jsonl"
path_img_data = "../../data/Raw/profile_imgs/"
path_out_data = "../../data/Raw/train_test_compact_2.json"

beliver_hashtag=["#climatechangeisreal","#actonclimate","#extinctionrebellion",
                 "#climateemergency","#climateactionnow"]
denier_hashtag=["#climatechangeisfalse","#climatechangenotreal","#climatechangehoax",
                "#globalwarminghoax","#tcot","#ccot","#tlot","#pjnet","#rednationrising",
                "#votered","#libtard","#libtards", "#climatehoax", "#climatealarmism", 
                "#climatechangealarmism", "#climatechangehysteria", "#globalwarminghysteria", 
                "#climatechangefraud", "#climateemergencyhoax", "#climatechangescam", 
                "#globalwarmingalarmism", "#globalwarmingcult", "#climatechangefrenzy", 
                "#globalwarmingfraud", "#globalwarmingscam", "#globalwarmingnonsense", 
                "#globalwarmingbullshit", "#climatefraud", "#climatescam", "#climatecult", 
                "#climatenonsense", "#climatebullshit", "#climatechangebullshit", 
                "#climatechangenonsense", "#climatechangecult", "#climatehysteria"]

#raw_data = [json.loads(line) for line in open(path_raw_data, 'r')]
#raw_data = []
_d = 0
_b = 0

r = []

agender = PyAgender()

#with open(path_out_data, 'w') as fp:
#    json.dump(r, fp)

#for i, tweet in enumerate(raw_data):
tweets = []
with open(path_raw_data, 'r') as infile:
    with open(path_out_data, 'w') as outfile:
        for i, line in enumerate(infile):
            tweet_in = json.loads(line)
            if i % 1000 == 0:
                print( f"{i}/?")
            #if i >= 100:
            #    break
            tweet = {}
            tweet["tweet_class"] = "unknown"
            for hashtag in tweet_in["entities"]["hashtags"]:
                v = "#" + hashtag['text'].lower().strip()
                if v in denier_hashtag:
                    tweet["tweet_class"] = "denier"
                    _d += 1
                    break
                elif v in beliver_hashtag:
                    tweet["tweet_class"] = "beliver"
                    _b += 1
                    break
            tweet["tweet_id"] = str(tweet_in["id"])
            tweet["tweet_full_text"] = str(tweet_in["full_text"])
            tweet["user_id"] = str(tweet_in["user"]["id"])
            tweet["user_location"] = str(tweet_in["user"]["location"])
            tweet["usert_description"] = str(tweet_in["user"]["description"])
            tweet["user_image_url"] = str(tweet_in["user"]["profile_image_url"])

            if tweet["tweet_class"] != "unknown":
                tweet["faces_predicted"] = "True"
                # Classifie Gender and Age

                # Download and save image as a temp file
                tweet_in["user"]["profile_image_url"] = tweet_in["user"]["profile_image_url"].replace("_normal", "")
                filename, file_extension = os.path.splitext(tweet_in["user"]["profile_image_url"])
                _my_img_path = path_img_data + tweet_in["user"]["id_str"] + file_extension

                if file_extension in ["", ".gif"]:
                    # The face predict tool doesn't work with some type of imgs.
                    face_predict = []
                else:
                    # Predict age and gender
                    try:
                        urllib.request.urlretrieve(tweet_in["user"]["profile_image_url"], _my_img_path)
                        face_predict = agender.detect_genders_ages(cv2.imread(_my_img_path))
                    except:
                        face_predict = []
                        #print(f"EXCEPT: {_my_img_path}    {tweet_in['user']['profile_image_url']}")
                for f in face_predict:
                    f["gender"] = float(round(f["gender"], 2))
                    f["age"] = float(round(f["age"], 2))
                tweet["faces_predict"] = face_predict
            else:
                tweet["faces_predicted"] = "False"
                tweet["faces_predict"] = []
            #json.dump(tweet, outfile)
            tweets.append(tweet)
        json.dump(tweets, outfile)
        #raw_data.append(tweet)
        
#print(f"Deniers: {_d}\nBelievers: {_b}\nUnknown: {len(raw_data)-_d-_b}")
print(f"Deniers: {_d}\nBelievers: {_b}\nUnknown: ?")



