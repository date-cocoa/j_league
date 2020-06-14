import pandas as pd
import time
import numpy as np
import scrape
import os

path = os.getcwd()
parent_path = '/'.join(path.split('/')[:-1])

years = np.arange(1993, 2020, 1)
data = pd.DataFrame()
for year in years:
    data = pd.concat([data, pd.DataFrame(scrape.get_hometeams_awayteams_results(year)).T], axis=0) # yearの結果をdataframeにconcat
    print(str(year) + ' ' + 'Finish!!')
    time.sleep(5)

data.columns = ['home', 'score', 'away', 'home_scores', 'away_scores', 'year']

data_save_path = parent_path + '/data/'

try:
    os.mkdir(data_save_path)
except FileExistsError as e:
    print(e)
    print('既にファイルは存在しているので、os.mkdirの処理はスキップします')

data.to_csv(data_save_path + 'data.csv', index=False)
print('ファイルを出力しました！')
