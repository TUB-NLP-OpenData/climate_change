import GetOldTweets3 as got
import pandas as pd
import urllib
import re

"""https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5QCCUU"""

data_files=["https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/5QCCUU/QPYP8G"]
LIMIT=50000
out="../../data/raw/50k_ids.txt"



import urllib.request  # the lib that handles the url stuff
count=0
docs=[]
for f in data_files:
    for line in urllib.request.urlopen(f):
        count+=1
        print (count)
        if count >LIMIT:
            break
        docs.append(line.decode("utf-8").replace('\n', '').replace('\t','').replace('\r',''))
pdf=pd.DataFrame(docs).to_csv(out, header=None, index=None, sep=' ')
