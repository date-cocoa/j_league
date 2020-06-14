## scrape.py
from bs4 import BeautifulSoup
import requests

import re

def get_hometeams_awayteams_results(year):
    """その年の試合結果のホームチーム、スコア、アウェイチームを取得し、それぞれをリストで返す
    Args:
        year（数値）
    
    Returns:
        home_teams(リスト), 
        results(リスト), 
        away_teams(リスト), 
    """

    URL_FRONT = 'https://data.j-league.or.jp/SFMS01/search?competition_years='
    URL_BACK = '&competition_frame_ids=1&tv_relay_station_name='
    url = URL_FRONT + str(year) + URL_BACK

    html_result = BeautifulSoup(requests.get(url).text).find_all('td')

    home_teams = []
    results = []
    away_teams = []
    years = []
    home_scores = []
    away_scores = []
    switch = True

    idx_1 = 5 # 5番目が最初のホームチーム
    idx_2 = 6 # 6番目が最初の試合結果
    idx_3 = 7 # 7番目が最初のアウェイチーム

    while switch:
        if (idx_3 == len(html_result) - 13): # 最後のtext以降13のtextが存在するのでここで終了
            switch = False
        
        home_team = html_result[idx_1].text
        result = html_result[idx_2].text
        away_team = html_result[idx_3].text
        home_score = result.split('-')[0].replace('\n', '').replace('\t', '').replace('\r', '')
        away_score = result.split('-')[1].replace('\n', '').replace('\t', '').replace('\r', '')

        home_teams.append(home_team.replace('\n', '').replace('\t', '').replace('\r', '')) # 最初と最後の\nを取り除くために[1:-1]
        results.append(result.replace('\n', '').replace('\t', '').replace('\r', ''))
        away_teams.append(away_team.replace('\n', '').replace('\t', '').replace('\r', ''))
        home_scores.append(home_score)
        away_scores.append(away_score)
        years.append(year)

        idx_1 += 11 # 11ずつホームチームが存在
        idx_2 += 11 # 11ずつ試合結果が存在
        idx_3 += 11 # 11ずつアウエイチームが存在

    return home_teams, results, away_teams, home_scores, away_scores, years