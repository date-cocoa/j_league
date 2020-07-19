## scrape.py
from bs4 import BeautifulSoup
import requests
import time

import re


def get_detail_results(year):
    URL_FRONT = 'https://data.j-league.or.jp/SFMS01/search?competition_years='
    URL_BACK = '&competition_frame_ids=1&tv_relay_station_name='
    url = URL_FRONT + str(year) + URL_BACK

    html_result = BeautifulSoup(requests.get(url).text).find_all('a')
    root_html = 'https://data.j-league.or.jp'

    date_list = []
    start_list = []
    place_list = []
    numbers_list = []
    crowds_list = []
    whether_list = []
    temperature_list = []
    humidity_list = []

    switch = True
    idx = 21
    while switch:
        print(str(idx), '/', str(len(html_result)))
        detail_url = root_html + html_result[idx].get('href') # change number here first is 21, +3

        html_result_detail = BeautifulSoup(requests.get(detail_url).text).find_all('table')

        date = html_result_detail[-1].find_all('td')[0].text
        start = html_result_detail[-1].find_all('td')[1].text.split('\t')[-1]
        place = html_result_detail[-1].find_all('td')[2].text.split('\t')[-1]
        numbers = re.findall('[0-9]', html_result_detail[-1].find_all('td')[3].text) # 数字が個々に取得できる（例；[2, 3, 3, 4]）
        crowds =''
        for num in numbers:
            crowds += num
        whether = html_result_detail[-1].find_all('td')[4].text.split('\t')[-1]
        temperature = html_result_detail[-1].find_all('td')[5].text.split('\t')[-1].split('\n')[0]
        humidity = html_result_detail[-1].find_all('td')[6].text.split('\t')[-1]

        date_list.append(date)
        start_list.append(start)
        place_list.append(place)
        numbers_list.append(numbers)
        crowds_list.append(crowds)
        whether_list.append(whether)
        temperature_list.append(temperature)
        humidity_list.append(humidity)

        idx += 3
        if '-' not in html_result[idx].text:
            switch = False

        time.sleep(1)

    return date_list, start_list, place_list, numbers_list, crowds_list, whether_list, temperature_list, humidity_list


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