# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:47:16 2019

@author: Gulshan
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='fb1.xlsx'      #File loaded
xl=pd.ExcelFile(file) # Read From excel
dfs=xl.parse(xl.sheet_names[0]) #parsing  excel sheet to dataframe
dfs=list(dfs['Gulshan Baraik shared a link.']) #removes the blank rows from dataframe
print(dfs)
sid=ss()
month=":"
for data in dfs:
    a = data.find(month)
    if(a==-1):
        s=sid.polarity_scores(data)
        print(data)
        for k in s:
            print(k,s[k])
