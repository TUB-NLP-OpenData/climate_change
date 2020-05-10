import GetOldTweets3 as got
import pandas as pd

LIMIT=1000
FROM="2015-05-01"
TO="2019-09-30"
keywords='"climate change" OR "climatechange" OR "global warming" OR "globalwarming"'
out="../../Sample_Data/raw/ids.txt"

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keywords).setSince(FROM).setUntil(TO).setMaxTweets(LIMIT)
docs=[t.id for t in got.manager.TweetManager.getTweets(tweetCriteria)]
pdf=pd.DataFrame(docs).to_csv(out, header=None, index=None, sep=' ')
