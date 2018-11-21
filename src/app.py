# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
import csv



parsed_data = []
csv.field_size_limit(sys.maxsize)

#played around with this to filter data from this link 
#https://github.com/mkearney/trumptweets

# with open('parsedtrumptweetsv6.csv', 'rU') as csvfile , open('parsedtrumptweetsv7.csv', 'wb') as csvfile2:
#     tweet_reader = csv.reader(csvfile, delimiter=' ', quotechar='|', dialect=csv.excel)
#     parsed_writer = csv.writer(csvfile2, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
#     for row in tweet_reader:
#         k = []
#         for i in row:
#             j = i.replace(' ','')
#             k.append(j)
#         parsed_writer.writerow([k])        

# store_words=[]
# with open('parsedtrumptweetsfinal.csv', 'rb') as csvfile:
#     tweet_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in tweet_reader:
#         row = row[0].strip('\"')
#         sentence = row.split(',')
#         for word in sentence:
#             word=word.lower()
#             store_words.append(word)
# 
# result_dict = dict( [ (i, store_words.count(i)) for i in set(store_words) ] )    

with open('dict_filtered.csv', 'wb') as csv_file,open('dict_sorted.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    mydict = dict(reader)
    writer = csv.writer(csv_file)  
    for key, value in mydict.items():
        if len(key) >=5:
            writer.writerow([key, value])   
 
  




