import requests
import re

API_KEY = 'AIzaSyBVWcgD2n_AeAQK0M7kRmHa0S7f1mezzV8'

grouped_categories = {
    "Music & Podcasts": [10, 43, 44, 46],
    "Gaming & Online Content": [20, 45, 48],
    "Comedy & Fun": [23, 24],
    "Education & Information": [27, 25, 29, 49, 34, 47],
    "Science and Technology": [28],
    "Lifestyle": [22, 19, 15, 21, 26, 37],
    "Movies & Drama": [30, 32, 33, 35, 36, 38, 39, 40, 42],
    "Shorts": [41],
    "Sports": [17],
    "Film & Animation": [1, 18, 31],
    "Autos & Vehicles": [2]
}


def extract_video_id(url):
    video_id_match = re.search(r'v=([^&]+)', url)
    return video_id_match.group(1) if video_id_match else None


def find_category_name(category_id):
    for category_name, ids in grouped_categories.items():
        if int(category_id) in ids:
            return category_name
    return "Category ID not found."


def convert_duration_to_seconds(duration):
    match = re.match(r'^PT((\d+)H)?((\d+)M)?((\d+)S)?$', duration)
    if match:
        hours = int(match.group(2) or 0)
        minutes = int(match.group(4) or 0)
        seconds = int(match.group(6) or 0)
        return hours * 3600 + minutes * 60 + seconds
    return 0


def get_video_details(video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails&id={video_id}&key={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            snippet = data['items'][0]['snippet']
            category_id = snippet['categoryId']
            title = snippet['title']
            return {'categoryId': category_id, 'title': title}
        else:
            print("No video details found.")
    except requests.RequestException as e:
        print(f"Error fetching video details: {e}")

    return None


def get_category(video_url):
    video_id = extract_video_id(video_url)
    if video_id:
        video_details = get_video_details(video_id)
        if video_details:
            category_id = video_details['categoryId']
            title = video_details['title']
            category_name = find_category_name(category_id)
            return category_name, title
    return "Invalid YouTube URL or no category found."
