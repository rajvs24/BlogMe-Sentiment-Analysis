# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:14:58 2023

@author: Raj Shrivastava
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Reading Excel file
data=pd.read_excel('articles.xlsx')

#Summary of the data

data.describe()

#summary of columns
data.info()

#counting the number of articles per source
#format of groupy df.groupby(['column_to_group])['coulumn_to_count].count()

data.groupby(['source_id'])['article_id'].count()


#Number of reaction by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()
#dropping a column

data=data.drop('engagement_comment_plugin_count' , axis=1)



    
#creating a function

def keywordflag(keyword):
    length=len(data)
    
    keyword_flag=[]
    for x in range (0,length):
        heading=data['title'][x]
        try:
            if keyword in heading :
                flag=1
            else :
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag
k=keywordflag("murder")

#Creating a new column in dataframe

data['keyword_flag']=pd.Series(k)


#SentimentIntensityAnalyzer

sent_int=SentimentIntensityAnalyzer()
text = data['title'][16]
sent=sent_int.polarity_scores(text)

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']


#adding a for loop to extract sentiments per title

length=len(data)
title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]
for x in range (0,length):
    try:
        text=data['title'][x]
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment=pd.Series(title_neg_sentiment)
title_pos_sentiment=pd.Series(title_pos_sentiment)
title_neu_sentiment=pd.Series(title_neu_sentiment)

data['title_neg_sentiment']=title_neg_sentiment
data['title_pos_sentiment']=title_pos_sentiment
data['title_neu_sentiment']=title_neu_sentiment

#writing the data 

data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata',index=False)