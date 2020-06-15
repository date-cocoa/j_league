import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

def make_directory(path):
    """親pathにディレクトリを作成。既に作成されている場合はskip
    args:
        path: 現在のpath
    """
    parent_path = '/'.join(PATH.split('/')[:-1])
    data_save_path = parent_path + '/result/'

    try:
        os.mkdir(data_save_path)
    except FileExistsError as e:
        print(e)
        print('既にファイルは存在しているので、os.mkdirの処理はスキップします')

def visualize_home_effect(data):
    """home効果を図示化したを出力（effect_home.png）
    args:
        data: dataを入力
    """
    home_sum = sum(data['home_scores'].astype('int'))
    away_sum = sum(data['away_scores'].astype('int'))
    plot_data = pd.DataFrame({'Score': [home_sum, away_sum], 'Kind': ['Home Team', 'Away Team']})

    sns.set()
    fig = plt.figure()
    sns.barplot(x=plot_data['Kind'], y=plot_data['Score'])
    plt.xlabel('')
    fig.savefig(data_save_path + '/' + 'effect_home.png')
    print('結果ファイルを出力しました！(effect_home.png)')

def visualize_timeseries_score(data):
    """試合の得点を年ごとにviolin plotで可視化（time_series.png）
    args:
        data: dataを入力
    """
    data['total_scores'] = data['home_scores'].astype(int) + data['away_scores'].astype(int)

    sns.set()
    fig = plt.figure(figsize=(10, 7))
    sns.violinplot(x=data['year'].astype(str), y=data['total_scores'])
    fig.savefig(data_save_path + '/' + 'time_series.png')
    print('結果ファイルを出力しました！(time_series.png)')

def main():
    PATH = os.getcwd()
    data = pd.read_csv(parent_path + '/' + 'data/' + 'data.csv')
    data = data[data['year'] > 1998] # pk戦が廃止以降

    make_directory(path=PATH)
    visualize_home_effect(data=data)
    visualize_home_effect(data=data)
    
if __name__ == '__main__':
    main()