from youtube import get_category

video_url = 'https://www.youtube.com/watch?v=N1M8jq6ix3U'

category_name, video_title = get_category(video_url)
print(f"Category Name: {category_name}")
print(f"Title:{video_title}")
