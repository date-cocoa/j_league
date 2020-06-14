import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# home効果を可視化
path = os.getcwd()
data = pd.read_csv(path + '/' + 'data.csv')
data = data[data['year'] > 1998] # pk戦が廃止以降
home_sum = sum(data['home_scores'].astype('int'))
away_sum = sum(data['away_scores'].astype('int'))

plot_data = pd.DataFrame({'Score': [home_sum, away_sum], 'Kind': ['Home Team', 'Away Team']})
sns.set()
fig = plt.figure()
sns.barplot(x=plot_data['Kind'], y=plot_data['Score'])
plt.xlabel('')
fig.savefig(path + '/' + 'effect_home.png')
