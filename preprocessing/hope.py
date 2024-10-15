import random
from datetime import datetime, timedelta
import json
from pymongo import MongoClient

# Function to generate a random query text related to comedy, technology, or sports
def generate_query_text1():
    comedy_queries = [
        "best comedy movies to watch",
        "funniest stand-up comedians",
        "how to write a comedy sketch",
        "comedy shows on Netflix",
        "most popular sitcoms",
        "top comedy podcasts",
        "best pranks of all time",
        "funniest memes of the year",
        "how to improve your stand-up routine",
        "best comedy books to read",
        "hilarious TV commercials",
        "how to make people laugh",
        "worst jokes ever told",
        "greatest comedy moments in film history",
        "funniest YouTube channels"
    ]

    technology_queries = [
        "latest tech trends in 2024",
        "how to build a mobile app",
        "best programming languages to learn",
        "top 10 gadgets of the year",
        "AI advancements in 2024",
        "how to secure your online data",
        "latest innovations in renewable energy",
        "top 5 programming frameworks",
        "how to get started with machine learning",
        "the future of virtual reality",
        "best tech conferences to attend",
        "understanding blockchain technology",
        "how to improve your computer's performance",
        "emerging technologies in healthcare",
        "future of artificial intelligence",
        "top programming languages for data science",
        "latest advancements in quantum computing",
        "best cybersecurity practices for individuals",
        "how to build a personal website",
        "trends in artificial intelligence for 2024",
        "how to optimize website performance",
        "impact of 5G technology on everyday life",
        "top open-source software to use in 2024",
        "how to start a career in tech",
        "best tools for remote team collaboration",
        "understanding the Internet of Things (IoT)",
        "latest developments in cloud computing",
        "how to protect your privacy online",
        "top programming frameworks for web development",
        "the future of autonomous vehicles",
        "how to get started with ethical hacking",
        "impact of technology on education",
        "best practices for user interface design",
        "latest trends in digital marketing technology"
    ]

    sports_queries = [
        "best football players of all time",
        "how to improve your basketball skills",
        "latest cricket world cup news",
        "top sports documentaries to watch",
        "greatest moments in Olympic history",
        "how to become a professional athlete",
        "best workout routines for athletes",
        "sports psychology techniques",
        "how to coach a youth sports team",
        "top 10 sports movies",
        "greatest rivalries in sports history",
        "how to stay motivated in sports training",
        "best sports nutrition tips",
        "history of the Olympic games",
        "how to analyze sports performance",
        "F1 vs NASCAR: what's the difference?",
        "best documentaries about Formula 1 racing",
        "how to analyze driver performance in F1",
        "impact of weather on cricket matches",
        "best cricket documentaries to watch",
        "how to strategize for a cricket tournament",
        "famous cricket rivalries to follow",
        "role of captains in cricket team dynamics",
        "best documentaries about football legends",
        "how to prepare for a football match mentally",
    ]

    politics_queries = [
        "latest political news in India",
        "how to vote in the upcoming elections",
        "impact of social media on politics",
        "top political leaders in the world",
        "best political documentaries to watch",
        "how government policies affect the economy",
        "current state of democracy in the world",
        "major political parties in the USA",
        "political protests around the globe",
        "how to get involved in local politics",
        "effects of political corruption on society",
        "most influential political figures of the decade",
        "importance of civic engagement",
        "how to analyze political speeches",
        "top political podcasts to follow"
    ]

    news_queries = [
        "latest headlines from around the world",
        "how to stay updated with breaking news",
        "impact of climate change on global news",
        "most significant news events of the year",
        "how to fact-check news articles",
        "top news sources for reliable information",
        "how technology is changing journalism",
        "latest developments in international relations",
        "importance of media literacy in today's world",
        "how to write a news article",
        "current events in business and finance",
        "latest scientific discoveries making headlines",
        "top news stories of the month",
        "impact of fake news on public opinion",
        "how to report a news story ethically"
    ]

    all_queries = comedy_queries + technology_queries + sports_queries + politics_queries + news_queries
    return random.choice(all_queries)


def generate_query_text2():
    entertainment_queries = [
        "what are the top movies of 2024",
        "how to start a movie review blog",
        "most anticipated TV shows of the year",
        "how to write a screenplay",
        "best streaming platforms for movies",
        "top documentaries to watch in 2024",
        "how to get into acting",
        "latest celebrity news and gossip",
        "how to plan a film festival",
        "top animated movies of all time",
        "how to become a film critic",
        "impact of streaming on the film industry",
        "best movie soundtracks of the decade",
        "how to create a YouTube channel for reviews",
        "famous directors and their signature styles",
        "how to organize a movie night with friends",
        "top film festivals around the world",
        "how to analyze a film's cinematography",
        "impact of social media on movie marketing",
        "best books about filmmaking",
        "how to pitch a movie idea",
        "most influential films of the past decade",
        "how to get started in voice acting",
        "best documentaries about social issues",
        "top romantic comedies to watch",
        "how to create a successful film blog",
        "latest trends in reality TV",
        "how to analyze character development in films",
        "best animated TV shows for adults",
        "how to promote an indie film",
        "most iconic movie quotes of all time"
    ]
    music_queries = [
        "what are the top songs of 2024",
        "how to start a music blog",
        "most influential albums of the year",
        "how to write a song",
        "best streaming services for music",
        "top music festivals to attend in 2024",
        "how to promote your music online",
        "latest trends in music genres",
        "how to get started in music production",
        "famous musicians and their influences",
        "how to create a playlist for any occasion",
        "impact of technology on the music industry",
        "best music documentaries to watch",
        "how to analyze song lyrics",
        "top collaborations in music history",
        "how to learn an instrument as an adult",
        "most popular music videos of all time",
        "how to organize a local concert",
        "best ways to support independent artists",
        "latest news in the music industry",
        "how to create a successful music channel",
        "most memorable live performances",
        "how to understand music theory",
        "best songs for motivation",
        "how to make a music video",
        "top underground artists to watch",
        "how to get a record deal",
        "impact of streaming on music sales",
        "best cover songs of all time",
        "how to write a music review",
        "latest innovations in musical instruments"
    ]
    food_queries = [
        "what are the top food trends of 2024",
        "how to start a food blog",
        "best recipes for quick meals",
        "how to cook a perfect steak",
        "top food documentaries to watch",
        "how to meal prep for the week",
        "latest innovations in cooking technology",
        "best street foods around the world",
        "how to pair wine with food",
        "top vegan recipes for beginners",
        "how to bake the perfect cake",
        "impact of food delivery services on dining",
        "best kitchen gadgets for home cooks",
        "how to create a balanced diet",
        "top cuisines to try in 2024",
        "how to host a dinner party",
        "most popular food blogs to follow",
        "how to make homemade pasta",
        "best food festivals to attend",
        "how to understand food labels",
        "top restaurants in your city",
        "how to grow your own herbs",
        "most popular cooking shows",
        "how to make healthy snacks",
        "best recipes for entertaining guests",
        "how to cook with seasonal ingredients",
        "top tips for food photography",
        "how to create a food diary",
        "latest trends in sustainable eating",
        "best international dishes to try",
        "how to reduce food waste at home"
    ]
    gaming_queries = [
        "what are the top video games of 2024",
        "how to start a gaming YouTube channel",
        "most anticipated game releases this year",
        "how to improve your gaming skills",
        "best gaming consoles to buy in 2024",
        "how to analyze video game mechanics",
        "top esports tournaments to watch",
        "how to create a successful gaming blog",
        "impact of gaming on mental health",
        "best gaming accessories for serious gamers",
        "how to stream games on Twitch",
        "latest trends in mobile gaming",
        "top indie games to play in 2024",
        "how to get involved in game development",
        "best gaming communities to join",
        "how to create your own game",
        "top gaming podcasts to listen to",
        "how to organize a gaming tournament",
        "most memorable moments in gaming history",
        "how to write a game review",
        "best multiplayer games to play with friends",
        "how to balance gaming and daily life",
        "top gaming merchandise to collect",
        "how to set up a gaming PC",
        "best virtual reality games of the year",
        "how to create engaging content for gamers",
        "latest news in the gaming industry",
        "how to build a gaming community",
        "impact of loot boxes on gaming",
        "best gaming platforms for casual gamers",
        "how to stay safe while gaming online"
    ]
    travel_queries = [
        "what are the top travel destinations in 2024",
        "how to start a travel blog",
        "best tips for solo travel",
        "how to pack efficiently for a trip",
        "top travel apps to use",
        "how to save money while traveling",
        "latest travel trends to watch",
        "best travel documentaries to inspire wanderlust",
        "how to plan a road trip",
        "top travel experiences to have in your lifetime",
        "how to choose the right travel insurance",
        "impact of travel on local cultures",
        "best ways to travel sustainably",
        "how to create a travel itinerary",
        "most beautiful places to visit in the world",
        "how to deal with jet lag",
        "top travel blogs to follow",
        "how to make friends while traveling",
        "best tips for traveling with kids",
        "how to navigate airports like a pro",
        "latest travel safety tips",
        "how to find hidden gems while traveling",
        "top travel photography tips",
        "how to enjoy a staycation",
        "best foods to try while traveling",
        "how to use public transport in a new city",
        "impact of COVID-19 on travel plans",
        "how to travel on a budget",
        "best travel guides for first-time travelers",
        "how to experience local culture while traveling",
        "top travel myths debunked"
    ]

    all_queries = music_queries + travel_queries + food_queries + gaming_queries + entertainment_queries
    return random.choice(all_queries)

def generate_query_text3():
    fitness_queries = [
        "HIIT workouts",
        "best cardio",
        "home workouts",
        "calisthenics guide",
        "stretching benefits",
        "daily steps goal",
        "yoga poses",
        "core exercises",
        "mobility drills",
        "workout recovery",
        "hydration tips",
        "fitness apps",
        "morning routine",
        "workout music",
        "outdoor exercises",
        "aerobics guide",
        "running techniques",
        "fitness trackers",
        "interval training",
        "active lifestyle",
        "workout challenges",
        "weight loss tips",
        "fitness motivation",
        "muscle toning",
        "cross-training",
        "kettlebell workout",
        "cool-down stretches",
        "step aerobics",
        "flexibility training",
        "fitness myths"
    ]
    gym_queries = [
        "gym schedule",
        "morning vs evening workout",
        "strength vs cardio",
        "warm-up sets",
        "circuit training",
        "free weights vs machines",
        "gym etiquette",
        "personal trainers",
        "group classes",
        "gym bag essentials",
        "weightlifting tips",
        "treadmill workouts",
        "squat variations",
        "gym membership deals",
        "core machines",
        "gym motivation",
        "workout buddies",
        "post-gym meals",
        "sauna benefits",
        "gym routines",
        "cable machine guide",
        "barbell exercises",
        "gym stretching",
        "lifting straps",
        "safety tips",
        "reps vs sets",
        "foam rolling",
        "gym supplements",
        "gym wear",
        "gym playlists"
    ]
    f1_queries = [
        "latest F1 news",
        "driver standings",
        "race calendar",
        "F1 rules",
        "car specifications",
        "team strategies",
        "pole position",
        "pit stop timing",
        "F1 circuits",
        "lap records",
        "driver transfers",
        "tire strategy",
        "engine regulations",
        "F1 safety",
        "track conditions",
        "qualifying results",
        "aerodynamics",
        "wet race handling",
        "F1 history",
        "legendary drivers",
        "team budget caps",
        "F1 esports",
        "pre-race setup",
        "technical upgrades",
        "DRS zones",
        "power unit",
        "fuel management",
        "F1 documentaries",
        "race penalties",
        "overtaking tips"
    ]
    waterpolo_queries = [
        "basic rules",
        "water polo positions",
        "goalkeeper techniques",
        "ball handling",
        "treading water",
        "defensive drills",
        "offensive plays",
        "water polo history",
        "training routines",
        "match strategies",
        "tournament formats",
        "foul types",
        "shot clock rules",
        "water polo tactics",
        "strength training",
        "water polo events",
        "youth leagues",
        "Olympic history",
        "goal-scoring techniques",
        "team formations",
        "passing drills",
        "condition training",
        "hydration tips",
        "match preparation",
        "swim speed drills",
        "player substitutions",
        "ball control",
        "injury prevention",
        "game analysis",
        "water polo legends"
    ]
    food_queries = [
        "vegan recipes",
        "keto diet",
        "meal prep ideas",
        "food trends",
        "healthy snacks",
        "street food",
        "cooking techniques",
        "comfort foods",
        "spice guide",
        "regional cuisine",
        "superfoods",
        "fermented foods",
        "food safety",
        "gourmet dishes",
        "baking tips",
        "gluten-free meals",
        "sustainable eating",
        "seasonal produce",
        "food pairings",
        "ethnic dishes",
        "plant-based diets",
        "cheese varieties",
        "dessert recipes",
        "food festivals",
        "fusion cuisine",
        "BBQ tips",
        "seafood dishes",
        "breakfast ideas",
        "food storage tips",
        "herbs and spices"
    ]
    movie_queries = [
        "top movies 2024",
        "film reviews",
        "Oscar winners",
        "new releases",
        "movie trailers",
        "classic films",
        "cult favorites",
        "animated movies",
        "movie streaming",
        "director's cut",
        "film festivals",
        "action films",
        "romantic comedies",
        "sci-fi classics",
        "horror movies",
        "thriller films",
        "biopics",
        "movie soundtracks",
        "cinematography tips",
        "indie films",
        "documentaries",
        "movie sequels",
        "film adaptations",
        "superhero movies",
        "box office hits",
        "movie franchises",
        "movie ratings",
        "cinematic universes",
        "foreign films",
        "film industry news"
    ]

    all_queries = fitness_queries + movie_queries + waterpolo_queries + food_queries + gym_queries
    return random.choice(all_queries)
# Function to generate a random timestamp between two dates
def generate_random_timestamp(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_time = timedelta(seconds=random.randint(2000, 84399))  # random time of the day
    return start_date + timedelta(days=random_days) + random_time

# MongoDB connection
def insert_queries_to_mongo(db, user_id, num_queries=100):
    # Define the date range
    start_date = datetime(2024, 9, 15)
    end_date = datetime(2024, 10, 15)

    # Prepare the data to be inserted
    data_list = []
    for _ in range(num_queries):
        data = {
            "query_id": f"query_{random.randint(1000000000000, 9999999999999)}",
            "user_id": user_id,
            "timestamp": {"$date": generate_random_timestamp(start_date, end_date).isoformat() + "Z"},
            "search_engine": "www.opera.com",
            "query_text": generate_query_text3(),
            "result_clicks": [],
            "__v": 0,
            "r": True
        }
        data_list.append(data)

    # Insert the data into the MongoDB collection
    db.searchqueries.insert_many(data_list)
    print(f"Inserted {num_queries} queries into MongoDB.")

if __name__ == "__main__":
    # MongoDB connection details
    client = MongoClient('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/')
    db = client['cybercrime']  # Replace with your database name

    # Insert 100 random queries for user_id "rachit"
    insert_queries_to_mongo(db, user_id="taha", num_queries=100)

    # Close the MongoDB connection
    mongo_client.close()
