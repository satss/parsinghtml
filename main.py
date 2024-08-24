import pandas as pd
import os
import re
import math

from bs4 import BeautifulSoup

your_path = 'docs'
files = os.listdir('.')
masterlis = list()
li = list()
di =dict()
for file in files:

    if file.endswith(".html"):
        names =file.split('-')
        year = names[1].split(".")[2]
        html_file = open(file, 'r', encoding='utf-8')
        source_code = html_file.read() 
        #print(source_code)
        soup = BeautifulSoup(source_code, 'html.parser')
        tables = soup.findAll("table", class_="std_table")
        print(len(tables))
        d = dict()
        for table in tables:
            dfs = pd.read_html(str(table), thousands='.', decimal=',')
            dfs[0].drop([col for col in ['Euro','Euro.1'] if col in dfs[0]],
            axis=1, inplace=True)
            dfCleaner = dfs[0].drop('Euro.1', axis=1,errors='ignore')
            #print (df.columns.nlevels)
            #print (dfCleaner.columns)

            

            if type(dfCleaner.columns)==pd.MultiIndex:
                print("multi")
                rows =dfCleaner.shape[0]
                for row in dfCleaner.itertuples(index=False):
                    d[row[0]] = row[1:]
                    li.append(d)

            else :
                rows =dfCleaner.shape[0]
                for row in dfCleaner.itertuples(index=False):
                    d[row[0]] = row[1:]
                    li.append(di)
        di[year] =li    
    print(di)
 
    
        
        




