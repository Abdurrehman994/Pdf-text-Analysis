

from tika import parser
import pprint
import numpy as np
import os
import pandas as pd
breaking_condition = 0
path = "/content/drive/MyDrive/pdfs"
files = os.listdir(path)
n = 1
Result = []

for file in files:
  print('<-----------for pdf',file,'------------->')
  Result.append(['','PDF Name',file])
  n=n+1
  # print(file)
  file = path +'/'+file
  rawText = parser.from_file(file)
# rawText = parser.from_file('/content/sample_data/3M 203779 20MSDS.Image.Marked.pdf')
  if rawText['content']:
    rawList = rawText['content'].splitlines()
  # pprint.pprint(rawText)
  data = []
  for i in range(len(rawList)):
    if rawList[i] is not None and rawList[i] != '':
      # print(rawList[i])
      d = rawList[i]
      data.append(d)
    # print('Line ',i,rawList[i])
  # for i in range(len(data)):
  #   print('Line',i,data[i])
  import difflib
  # fname1 = 'orderd list of strings that occurs in SDS.txt'
  fname2 = '/content/drive/MyDrive/orderd list of strings that occurs in SDS.txt'

  # f1 = open(fname1)
  f2 = open(fname2)

  # lines1 = data.readlines()
  lines2 = f2.readlines()

  text_line=[]
  pdf_line_no=[]
  percentage_similarity_1=[]

  # f1.seek(0)
  f2.seek(0)
  complete_average = 0
  previous_index = 0
  order_score = 0
  previous_max_index = 0
  for line1 in lines2:
    # print(line1)
    max_similarity=0
    index=0
    max_string=''
    max_index=0
    # max_index = 0
    percentage_similarity = 0
    for line2 in data:
        index = index + 1
        similarity = difflib.SequenceMatcher(None, line1,line2).ratio()
        
        if similarity > max_similarity:
            max_similarity=similarity
            max_string=line2
            max_index=index
            
            percentage_similarity=max_similarity
    if max_index > previous_max_index:
      order_score +=1
    else:
      previous_max_index = max_index
    complete_average = complete_average + percentage_similarity
    Result.append([line1.replace('\n',''),max_index,percentage_similarity])
  Result.append(['','Average Similarity',complete_average/len(Result)*100])
  Result.append(['','Order Score',(order_score/len(Result))*100])
  # print(Result)

  # f1.close()

  f2.close()
  print()
  # avg_value =np.mean(Result[2,:])
import pandas as pd	 
df = pd.DataFrame(Result,columns=['String in Text','Line No in PDF','Similarity Score']) 
df.to_csv('Test.csv',index=False)

import pandas as pd
cities = pd.DataFrame([['Sacramento', 'California','ew'], ['Miami', 'Florida','fds'],['1','2','3']], columns=['City', 'State','similarity'])
cities.to_csv('cities.csv')