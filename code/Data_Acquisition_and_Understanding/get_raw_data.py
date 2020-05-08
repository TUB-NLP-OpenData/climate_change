import GetOldTweets3 as got
import pandas as pd

LIMIT=100
FROM="2015-05-01"
TO="2015-09-30"
keywords='"climate change" OR "climatechange" OR "global warming" OR "globalwarming"'
out="../../sample_Data/raw/ids.txt"

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords).setSince(FROM).setUntil(TO).setMaxTweets(LIMIT)
docs=[t.id for t in got.manager.TweetManager.getTweets(tweetCriteria)]
pdf=pd.DataFrame(docs).to_csv(out, header=None, index=None, sep=' ', mode='a')
