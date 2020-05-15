# Climate Change
There is an increasing politicization of climate science in an effort to delegitimize the scientific consensus about climate change; this is carried out mostly by vested-interest groups through organized disinformation campaigns and fake news. On a macro scale, this is an important issue because legislators tend to act according to what they perceive to be the concerns of their electoral base. Thus, public knowledge about climate change can push legislation towards policies that will tackle the issue and counteract the commercial lobbying from industries.
In short, the student will dive deep into DS in order to understand the people's perception about Climate Change with a view of designing strategies and education tools to help mitigate the dissemination of false news on the internet.

It is commonly assumed that convincing deniers that climate change is real is necessary for them to act pro-environmentally. In order to to that, it's very important to understand who are the deniers and what are their arguments.



## Potential Research Questions:

* Do people believe in climate change?
* Who are the “deniers” / “warmists”?
* What are the perceptions of different social groups (in terms of age, gender and social class, local) about the situation related to Climate Change?
* What are the criteria used for the acceptance of information among the population, regarding trust in origin, source, transmission on social networks?
* What are the psycho-emotional reactions, for example fear, stigma and anxiety, in the face of rumors related to global warming?
* What is the role of non-textual media (images, videos, audio, etc.) on the effectiveness of and people’s engagement with misinformation?
* How much harm is global warming believed to cause?
  * Alarmed, Concerned, Cautious,Disengaged, Doubtful, Dismissive
* Attitudes to science and risk?
  * Sceptics, Mainstream, Radicals

## Project: Kanban board [here](https://github.com/TUB-NLP-OpenData/climate_change/projects/2) 

  
## References
* Representativeness of Abortion Legislation Debate on Twitter: A Case Study in Argentina and Chile. https://dl.acm.org/doi/fullHtml/10.1145/3366424.3383561
* Who Tweets? Deriving the Demographic Characteristics of Age, Occupation and Social Class from Twitter User Meta-Data - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115545
* Beyond ‘deniers’ and ‘believers’: Towards a map of the politics of climate change.
* Detecting Climate Change Deniers on Twitter Using a Deep Neural Network
* Promoting pro-environmental action in climate change deniers.

* https://github.com/gravesa333/Classifying_Climate_Change_Tweets
* https://towardsdatascience.com/classifying-climate-change-tweets-8245450a5e96



## How to process the Harvard Dataset
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5QCCUU

### 1. download partially the data e.g. 50K tweet ids
```
python3 get_ids_from_harvard_dataset.py
```

### 2. Hydrate tweet ids
Twarc's hydrate command will read a file of tweet identifiers and write out the tweet JSON for them using Twitter's status/lookup API.

```
twarc hydrate Raw/ids.txt > Processed/tweets.jsonl
```

### 3. label the data: deniers/believers
```
python3 training_test.py
```

### 4. predict demographics (age, gender)
```
python3 get_age_gender.py
```

### 5. more
```
???????
```




