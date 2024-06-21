import requests 
import  bs4 
import pandas as pd 
url="http://china.nba.com/statistics/"

url1="""http://china.nba.com/static/data/league/playerstats_All_All_All_0_All_false_2017_4_All_Team_points_All_perGame.json"""

r=requests.get(url)

players=r.json()['payload']['players']

data=[ dict(w['playerProfile'],**w['statTotal']) for w in  players]

df=pd.DataFrame(data=data)
