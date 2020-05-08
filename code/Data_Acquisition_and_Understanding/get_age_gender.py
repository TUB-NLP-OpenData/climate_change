import os
import urllib.request
import json
import cv2
import pandas as pd
from pyagender import PyAgender


path_raw_data = "../../data/Processed/tweets.jsonl"
path_img_data = "../../data/Raw/profile_imgs/"
path_out_csv = "../../data/Processed/age_gender.csv"

agender = PyAgender()

raw_data = [json.loads(line) for line in open(path_raw_data, 'r')]

columns = ["id", "age", "gender", "gender_predicted_value", "location", "profile_img_url"]


df = pd.DataFrame(columns=columns)


for user in raw_data:
    data = {}
    data["id"] = user["id_str"]
    data["profile_img_url"] = user["user"]["profile_image_url"].replace("_normal", "")
    data["location"] = user["user"]["location"]
    print(data)
    # Download and save image as a temp file
    filename, file_extension = os.path.splitext(data["profile_img_url"])
    _my_img_path = path_img_data + data["id"] + file_extension
    urllib.request.urlretrieve(data["profile_img_url"], _my_img_path)

    if file_extension in ["", ".gif"]:
        # The face predict tool doesn't work with some type of imgs.
        face_predict = []
    else:
        # Predict age and gender
        face_predict = agender.detect_genders_ages(cv2.imread(_my_img_path))
    
    if face_predict:
        data["age"] = face_predict[0]["age"]
        data["gender_predicted_value"] = face_predict[0]["gender"]  # male < 0.5, female > 0.5
        data["gender"] = "m" if face_predict[0]["gender"] < 0.5 else "f"
    else:
        # Face not found
        data["age"] = -1.0
        data["gender_predicted_value"] = -1.0
        data["gender"] = "no_face"

    df = df.append(data, ignore_index=True)

df.to_csv(path_out_csv)