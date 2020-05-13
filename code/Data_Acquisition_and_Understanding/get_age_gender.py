import os
import urllib.request
import json
import cv2
import pandas as pd
from pyagender import PyAgender


path_raw_data = "../../data/Raw/train_test.json"
path_img_data = "../../data/Raw/profile_imgs/"
path_out = "../../data/Raw/data_age_gender.json"

agender = PyAgender()
raw_data = [json.loads(line) for line in open(path_raw_data, 'r')]
#df = pd.DataFrame(columns=["id", "age", "gender", "gender_predicted_value", "location", "profile_img_url"])

df=[]
#for user in pd.read_json(path_raw_data,  lines=True).iterrows():
for i, user in enumerate(raw_data):
    print(f"{i+1}/{len(raw_data)}")

    user["user"]["profile_img_url"] = user["user"]["profile_image_url"].replace("_normal", "")
    
    # Download and save image as a temp file
    filename, file_extension = os.path.splitext(user["user"]["profile_img_url"])
    _my_img_path = path_img_data + user["user"]["id_str"] + file_extension
    urllib.request.urlretrieve(user["user"]["profile_img_url"], _my_img_path)

    if file_extension in ["", ".gif"]:
        # The face predict tool doesn't work with some type of imgs.
        face_predict = []
    else:
        # Predict age and gender
        try:
            face_predict = agender.detect_genders_ages(cv2.imread(_my_img_path))
        except:
            face_predict = []
            print(f"EXCEPT: {_my_img_path}")
    for f in face_predict:
        f["gender"] = float(round(f["gender"], 2))
        f["age"] = float(round(f["age"], 2))
    user["faces_predict"] = face_predict

with open(path_out, 'w') as fp:
    json.dump(raw_data, fp)
print("Complete.")
#pd.DataFrame(df).reset_index().to_json(path_out_csv)

#df.to_csv(path_out_csv)
