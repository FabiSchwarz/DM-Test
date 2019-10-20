import pandas as pd
import os
folderpath=str(os.path.dirname(os.path.abspath(__file__)))

usedData = pd.read_csv(folderpath+'/data.csv', sep=',', usecols=['id', 'host_id', 'price', 'number_of_reviews', 'last_review'])

usedData.to_csv(folderpath+'/outputData.csv', index=False, sep=',')