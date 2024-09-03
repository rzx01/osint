import requests
import json

url = "https://x.com/BBCBreaking/status/1829875342246363161" 

def extract_username_from_url(url):
    return url.rstrip('/').split('/')[-1]

#this doesnt have scraping of some types of account like private ones but ive tested many types like verified business accounts, non verified youtubers, news channels, education channels etc and those work
def fetch_profile_tweets(username):
    url = f"https://syndication.twitter.com/srv/timeline-profile/screen-name/{username}"
    r = requests.get(url)
    html = r.text

    start_str = '<script id="__NEXT_DATA__" type="application/json">'
    end_str = '</script></body></html>'

    start_index = html.index(start_str) + len(start_str)
    end_index = html.index(end_str, start_index)

    json_str = html[start_index: end_index]
    data = json.loads(json_str)

    entries = data["props"]["pageProps"]["timeline"]["entries"]

    top_5_tweets = []
    for entry in entries:
        if "content" in entry and "tweet" in entry["content"]:
            tweet_text = entry["content"]["tweet"].get("full_text", "")
            top_5_tweets.append(tweet_text)
            if len(top_5_tweets) == 5:
                break

    print("Latest 5 Tweets:\n")
    for i, tweet in enumerate(top_5_tweets, 1):
        print(f"Tweet {i}: {tweet}\n")

def fetch_tweet_content(tweet_id):
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&token=a"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Tweet Content:", data["text"])
    else:
        print("Failed to retrieve tweet data. Status code:", response.status_code)

        #checking if the URL is of a profile or a specific tweet
if "/status/" in url:
    #specific tweet url
    tweet_id = url.split('/')[-1]
    fetch_tweet_content(tweet_id)
else:
    #profile url
    username = extract_username_from_url(url)
    fetch_profile_tweets(username)