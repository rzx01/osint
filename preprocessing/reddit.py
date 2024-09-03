import requests
import json

reddit_url = "https://www.reddit.com/r/ChainedTogether/comments/1f5zuyd/jesus_christ_ive_played_like_1_hour_with_my/"

json_url = reddit_url + ".json"

response = requests.get(json_url, headers={'User-Agent': 'Mozilla/5.0'})
data = response.json()
post_data = data[0]['data']['children'][0]['data']

title = post_data.get('title', 'no title')
selftext = post_data.get('selftext', 'no content')

print(f"title: {title}")
print(f"content: {selftext}")