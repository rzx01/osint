from pymongo import MongoClient

client = MongoClient('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/')
db = client['cybercrime']

activity_collection = db['activities']
pre_activity_collection = db['pre-activities']
user_collection = db['user']

def generate_user_db():
    unique_users = activity_collection.distinct("user_id")

    for user_id in unique_users:        
        # Filter activities with duration greater than 20 seconds
        user_activities = list(activity_collection.find({"user_id": user_id, "duration": {"$gt": 20}}))

        if not user_activities:
            continue

        # Copy filtered activities to the 'pre-activities' collection
        pre_activity_collection.insert_many(user_activities)

        total_duration = 0
        session_durations = []
        domain_count = {}

        for activity in user_activities:
            duration = activity['duration']
            total_duration += duration
            session_durations.append(duration)

            domain = activity['app_usage_id']
            if domain in domain_count:
                domain_count[domain] += 1
            else:
                domain_count[domain] = 1

        average_session_duration = total_duration / len(session_durations) if session_durations else 0
        frequent_domains = sorted(domain_count, key=domain_count.get, reverse=True)

        user_document = {
            "user_id": user_id,
            "email": f"{user_id}@example.com",
            "behavior_profile": {
                "preferred_content": [],
            },
            "average_session_duration": average_session_duration,
            "frequent_domains": frequent_domains[:5],
            "total_duration": total_duration,
        }

        # Insert user document if it doesn't already exist
        if not user_collection.find_one({"user_id": user_id}):
            user_collection.insert_one(user_document)
            print(f"Inserted user: {user_id}")

if __name__ == "__main__":
    generate_user_db()
