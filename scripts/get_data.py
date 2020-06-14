import pandas as pd
import time
import numpy as np
import scrape

years = np.arange(1993, 2020, 1)
data = pd.DataFrame()
for year in years:
    data = pd.concat([data, pd.DataFrame(scrape.get_hometeams_awayteams_results(year)).T], axis=0) # yearの結果をdataframeにconcat
    print(str(year) + ' ' + 'Finish!!')
    time.sleep(5)

data.columns = ['home', 'score', 'away', 'home_scores', 'away_scores', 'year']
data.to_csv('data.csv', index=False)
print('ファイルを出力しました！')