import spotipy
import requests
import json
import pandas as pd
from pandas import DataFrame
import sqlalchemy
from sqlalchemy import create_engine
import os


# use client_id,client_secret
def setting_up(CLIENT_ID, CLIENT_SECRET):
    if(CLIENT_ID is None):
        return 1
    else:
        CLIENT_ID = CLIENT_ID
        CLIENT_SECRET = CLIENT_SECRET
        AUTH_URL = 'https://accounts.spotify.com/api/token'
        auth_response = requests.post(AUTH_URL, {
          'grant_type': 'client_credentials',
          'client_id': CLIENT_ID,
          'client_secret': CLIENT_SECRET,
        })
        if(auth_response.status_code == 200):
            # calling(auth_response)
            return 0, auth_response
        else:
            return 1


# need to use appropiate auth_response
# only called if setting_up works
def calling(auth_response):
    if(auth_response is not None):
        auth_response_data = auth_response.json()
        access_token = auth_response_data['access_token']
        headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        BASE_URL = 'https://api.spotify.com/v1/'
        track_id = '6mFkJmJqdDVQ1REhVfGgd1'
        r = requests.get(BASE_URL + 'audio-features/'
                         + track_id, headers=headers)
        r = r.json()
        dance = r["danceability"]
        data = pd.DataFrame.from_dict(r, orient='index')
        engine = create_engine('mysql://root:codio@localhost/mysql')
        os.system("mysqldump -u root -pcodio mysql > spot.sql")
        data.to_sql('SPOT', con=engine, if_exists='replace', index=False)
        return 0
    else:
        return 1


def main():
    CLIENT_ID = '74a90350ed1d4c1dbc80fe0dc996ce2d'
    CLIENT_SECRET = '9f31a864b9f14ceab01376dcfdb8c730'
    status, auth_response = setting_up(CLIENT_ID, CLIENT_SECRET)
    if(status == 0):
        print(calling(auth_response))
