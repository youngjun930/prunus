
import pandas as pd


target_file_all = 'C:/python_result/tumblbug_crawling_all_21_02_24.csv'
target_file_game = 'C:/python_result/tumblbug_crawling_game.csv'

with open(target_file_all, 'r', encoding='utf-8') as all_file:
    all_file_data = pd.read_csv(all_file)
with open(target_file_game, 'r', encoding='utf-8') as game_file:
    game_file_data = pd.read_csv(game_file)

game_data = {}

game_file_data['year'] = game_file_data['런칭날짜'].apply(lambda x: x.split('-')[0])
game_file_data['creator-year'] = game_file_data[['창작자', 'year']].apply(lambda row: row.values.astype(list).tolist(), axis=1)
for creator, year in game_file_data['creator-year']:
    year_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if creator in game_data:
        game_data[creator][int(year)-2011] += 1
    elif creator not in game_data:
        year_list[int(year)-2011] += 1
        game_data[creator] = year_list

df = pd.DataFrame(game_data)
df.to_csv("C:/python_result/tumblbug_creator_game.csv", mode='w', encoding='utf-8')

all_data = {}

all_file_data['year'] = all_file_data['런칭날짜'].apply(lambda x: x.split('-')[0])
all_file_data['creator-year'] = all_file_data[['창작자', 'year']].apply(lambda row: row.values.astype(list).tolist(), axis=1)
for creator, year in all_file_data['creator-year']:
    year_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if creator in all_data:
        all_data[creator][int(year)-2011] += 1
    elif creator not in all_data:
        year_list[int(year)-2011] += 1
        all_data[creator] = year_list

df = pd.DataFrame(all_data)
df.to_csv("C:/python_result/tumblbug_creator_all.csv", mode='w', encoding='utf-8')



