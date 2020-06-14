import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

path = os.getcwd()
parent_path = '/'.join(path.split('/')[:-1])

try:
    os.mkdir(data_save_path)
except FileExistsError as e:
    print(e)
    print('既にファイルは存在しているので、os.mkdirの処理はスキップします')
data_save_path = parent_path + '/result/'

# home効果を可視化
data = pd.read_csv(parent_path + '/' + 'data/' + 'data.csv')
data = data[data['year'] > 1998] # pk戦が廃止以降
home_sum = sum(data['home_scores'].astype('int'))
away_sum = sum(data['away_scores'].astype('int'))

plot_data = pd.DataFrame({'Score': [home_sum, away_sum], 'Kind': ['Home Team', 'Away Team']})
sns.set()
fig = plt.figure()
sns.barplot(x=plot_data['Kind'], y=plot_data['Score'])
plt.xlabel('')
fig.savefig(data_save_path + '/' + 'effect_home.png')
print('結果ファイルを出力しました！(effect_home.png)')

# 時系列で得点を可視化
data = pd.read_csv(parent_path + '/' + 'data/' + 'data.csv')
data = data[data['year'] > 1998] # pk戦が廃止以降
data['total_scores'] = data['home_scores'].astype(int) + data['away_scores'].astype(int)

sns.set()
fig = plt.figure()
sns.violinplot(x=data['year'].astype(str), y=data['total_scores'])
fig.savefig(data_save_path + '/' + 'time_series.png')
print('結果ファイルを出力しました！(time_series.png)')

