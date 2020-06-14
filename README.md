# j_league
jリーグのデータを取得して分析するファイル

## スクリプトファイル(.py)
- scrape.py: jリーグのデータをスクレイプする関数
- get＿data.py: scrape.pyを実行し、/data にdata.csvを出力
- analysis.py: data.csvを分析し、結果を /result に結果ファイルを出力

## 実行方法
```zsh
# conda activate j_league (if you already created environment)

conda create -n j_league -y python=3.
conda activate j_league
pip install -r requirements.txt
cd scripts
python3 get_data.py
python3 analysis.py
```

## ファイル構成
```zsh
.
├── README.md
├── data
│   └── data.csv
├── requirements.txt
├── result
│   ├── effect_home.png
│   └── time_series.png
└── scripts
    ├── __pycache__
    │   └── scrape.cpython-38.pyc
    ├── analysis.py
    ├── get_data.py
    └── scrape.py
 ```