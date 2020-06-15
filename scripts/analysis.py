import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

PATH = os.getcwd() # ./scripts
PARENT_PATH = '/'.join(PATH.split('/')[:-1]) # .
DATA_SAVE_PATH = PARENT_PATH  + '/result' # ./result

def make_directory(data_save_path):
    """親pathにディレクトリを作成。既に作成されている場合はskip
    args:
        data_save_path: ディレクトリを作成するpath
    """
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
    fig.savefig(DATA_SAVE_PATH + '/' + 'effect_home.png')
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
    fig.savefig(DATA_SAVE_PATH + '/' + 'time_series.png')
    print('結果ファイルを出力しました！(time_series.png)')

def main():
    make_directory(data_save_path=DATA_SAVE_PATH)
    data = pd.read_csv(PARENT_PATH + '/' + 'data/' + 'data.csv')
    data = data[data['year'] > 1998] # pk戦が廃止以降
    visualize_home_effect(data=data)
    visualize_home_effect(data=data)

if __name__ == '__main__':
    main()