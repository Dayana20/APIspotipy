import spotipy
import requests
import json
import pandas as pd
from pandas import DataFrame
'''
url = 'https://api.spotify.com/v1/audio-analysis/4JpKVNYnVcJ8tuMKjAj50A'
headers = {'Authorization': 'Bearer TOKEN-HERE'}
r = requests.get(url, headers=headers)
print( r.json())

'''
CLIENT_ID = '74a90350ed1d4c1dbc80fe0dc996ce2d'
CLIENT_SECRET = '9f31a864b9f14ceab01376dcfdb8c730'

AUTH_URL = 'https://accounts.spotify.com/api/token'
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

#print(auth_response.status_code)

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
track_id = '6mFkJmJqdDVQ1REhVfGgd1'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

r = r.json()

dance = r["danceability"]
data = pd.DataFrame.from_dict(r, orient='index')
print(data) ##prints formatted data

import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('mysql://root:codio@localhost/spot')


data.to_sql('table_name', con=engine, if_exists='replace', index=False)

'''
print("Danceability", r["danceability"])
print("instrumentalness", r["instrumentalness"])
print("liveness", r["liveness"])
'''