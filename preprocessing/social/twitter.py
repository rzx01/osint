import requests
import json


def twitter_category(url):

    def extract_username_from_url(url):
        return url.rstrip('/').split('/')[-1]

    def fetch_profile_tweets(username):
        url = f"https://syndication.twitter.com/srv/timeline-profile/screen-name/{username}"
        r = requests.get(url)
        if r.status_code == 200:
            html = r.text

            start_str = '<script id="__NEXT_DATA__" type="application/json">'
            end_str = '</script></body></html>'

            try:
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

                return {"tweets": top_5_tweets}

            except (ValueError, KeyError) as e:
                print(f"Error parsing HTML for Twitter profile: {e}")
                return {"error": "Failed to parse Twitter profile data"}

        else:
            print(f"Failed to retrieve Twitter profile. Status code: {r.status_code}")
            return {"error": f"Failed to retrieve Twitter profile. Status code: {r.status_code}"}

    def fetch_tweet_content(tweet_id):

        url = f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&token=a"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return {"tweet": data.get("text", "No text available")}
        else:
            print("Failed to retrieve tweet data. Status code:", response.status_code)
            return {"error": f"Failed to retrieve tweet data. Status code: {response.status_code}"}

    if "/status/" in url:
        tweet_id = url.split('/')[-1]
        return fetch_tweet_content(tweet_id)
    else:
        username = extract_username_from_url(url)
        return fetch_profile_tweets(username)
