#!/usr/bin/python3
# Copyright 2023 Sam Steele
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests, sys, html
from config import *

if not STEAM_API_KEY:
    logging.error("STEAM_API_KEY not set in config.py")
    sys.exit(1)

def fetch_owned_games():
    try:
        response = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/',
            params={'key': STEAM_API_KEY, 'steamid': STEAM_ID, 'include_appinfo': '1'})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logging.error("HTTP request failed: %s", err)
        sys.exit(1)
    json = response.json()
    if 'response' in json and 'games' in json['response']:
        logging.info("Got %s games from Steam library", json['response']['game_count'])
        return json['response']['games']
    else:
        return []

print('<?xml version="1.0" encoding="utf-8"?><opml version="1.0"><head><title>Steam Feeds</title></head><body><outline text="Steam Library News" title="Steam Library News">')

for game in fetch_owned_games():
    print(f'<outline text="{html.escape(game["name"])}" title="{html.escape(game["name"])}" type="rss" xmlUrl="https://store.steampowered.com/feeds/news/app/{game["appid"]}/" htmlUrl="https://store.steampowered.com/news/app/{game["appid"]}"/>')

print('</outline></body></opml>')