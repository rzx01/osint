import requests


def reddit_category(reddit_url):
    json_url = reddit_url + ".json"

    try:
        response = requests.get(json_url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        data = response.json()
        post_data = data[0]['data']['children'][0]['data']

        title = post_data.get('title', 'No title')
        selftext = post_data.get('selftext', 'No content')

        return {"title": title, "content": selftext}

    except requests.RequestException as e:
        print(f"Error fetching Reddit post: {e}")
        return {"error": "Failed to fetch Reddit post data"}

    except (IndexError, KeyError):
        print("Unexpected data format from Reddit response.")
        return {"error": "Invalid Reddit URL or no post data found"}
