import requests
# import spotipy
# import json
# import pandas as pd
# from pandas import DataFrame
# import sqlalchemy
# from sqlalchemy import create_engine
# import os
# import matplotlib.pyplot as plt


def piechart(dataframe):
    # Pie chart, where the slices will be ordered
    # and plotted counter-clockwise:
    sizes = []
    labels = []
    count = 0
    for key, values in dataframe.items():
        count += 1
        if(count == 5):
            break
        if(isinstance(values, int) is True or
           isinstance(values, float) is True):
            sizes.append(abs(values))
            labels.append(key)
    blank = ['']*len(labels)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=None, labels=blank, shadow=False, startangle=90)
    ax1.axis('equal')
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.xlabel("")
    ax1.legend(labels)
    plt.show()


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
            return auth_response
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
        return r
    else:
        return 1


CLIENT_ID = '74a90350ed1d4c1dbc80fe0dc996ce2d'
CLIENT_SECRET = '9f31a864b9f14ceab01376dcfdb8c730'
auth_response = setting_up(CLIENT_ID, CLIENT_SECRET)
print(auth_response)
if(auth_response != 1):
    data = calling(auth_response)
print(data)
# piechart(data)
