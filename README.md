# j_league
jリーグのデータを取得して分析するファイル

## ファイル
- scrape.py: jリーグのデータをスクレイプする関数
- get＿data.py: scrape.pyを実行し、data.csvを出力
- analysis.py: data.csvを分析するファイル
- requirements.txt(準備中)

## 実行方法
```zsh
conda activate j_league # とりあえずこれ。最終的には最初から実行する
python3 get_data.py
python3 analysis.py
```