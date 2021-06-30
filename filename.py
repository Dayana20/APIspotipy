import spotipy
import requests
import json
import pandas as pd
from pandas import DataFrame
import sqlalchemy
from sqlalchemy import create_engine
'''
url = 'https://api.spotify.com/v1/audio-analysis/4JpKVNYnVcJ8tuMKjAj50A'
headers = {'Authorization': 'Bearer TOKEN-HERE'}
r = requests.get(url, headers=headers)
print( r.json())

'''
CLIENT_ID = ''
CLIENT_SECRET = ''

AUTH_URL = 'https://accounts.spotify.com/api/token'
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# print(auth_response.status_code)

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

engine = create_engine('mysql://root:codio@localhost/spot')

data.to_sql('table_name', con=engine, if_exists='replace', index=False)

print(data)