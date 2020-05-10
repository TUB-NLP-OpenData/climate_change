import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


input="../../data/processed/50k_tweets.jsonl"
out_dir="../../data/for_modeling"
beliver_hashtag=["#climatechangeisreal","#actonclimate","#extinctionrebellion","#climateemergency","#climateactionnow"]
denier_hashtag=["#climatechangeisfalse","#climatechangenotreal","#climatechangehoax","#globalwarminghoax","#tcot","#ccot","#tlot","#pjnet","#rednationrising","#votered","#libtard","#libtards"]


data=[]
for index, row in pd.read_json(input,  lines=True).iterrows():
    if len(row.keys())==len(df.columns):
        for h in beliver_hashtag:
            if h in row["full_text"].lower():
                row["class"]="believer"
                data.append(row)
                break
        for h in denier_hashtag:
            if h in row["full_text"].lower():
                row["class"]="denier"
                data.append(row)
                break


pd.DataFrame(data).reset_index().to_json(out_dir+"/data_with_label.json")
#train, test = train_test_split(data_df, test_size=0.2, stratify=data_df["class"], random_state=42)
#train.to_json(out_dir+"/train.json")
#test.to_json(out_dir+"/test.json")
# print (" train / test ",len(train),len(test) )

