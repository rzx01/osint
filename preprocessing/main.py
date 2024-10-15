from social.youtube import youtube_category
from social.reddit import reddit_category
from social.twitter import twitter_category
from ecom.amazon import amazon_category
from stream.netflix import netflix_category
from stream.prime import prime_category

from pymongo import MongoClient

client = MongoClient('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/')
db = client['cybercrime']
activity_collection = db['activities']


def fetch_unprocessed_activities():
    return activity_collection.find({"details.preprocessed": {"$exists": False}})


def update_activity(activity_id, additional_info):
    activity_collection.update_one(
        {"activity_id": activity_id},
        {"$set": {
            "details.additional_info": additional_info,
            "details.preprocessed": True
        }}
    )


def main():
    unprocessed_activities = fetch_unprocessed_activities()
    for activity in unprocessed_activities:
        url = activity["details"]["url"]
        app_usage_id = activity["app_usage_id"]

        if app_usage_id == "www.youtube.com":
            additional_info = youtube_category(url)
        elif app_usage_id == "www.reddit.com":
            additional_info = reddit_category(url)
        elif app_usage_id == "www.x.com":
            additional_info = twitter_category(url)
        elif app_usage_id == "www.amazon.in":
            additional_info = amazon_category(url)
        elif app_usage_id == "www.netflix.com":
            additional_info = netflix_category(url)
        elif app_usage_id == "www.primevideo.com":
            additional_info = prime_category(url)
        else:
            additional_info = {"error": "Unsupported app usage"}

        update_activity(activity["activity_id"], additional_info)


if __name__ == "__main__":
    main()
