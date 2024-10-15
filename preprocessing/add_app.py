from pymongo import MongoClient

client = MongoClient('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/')
db = client['cybercrime']
app_collection = db['applications']
activity_collection = db['activities']


def generate_app_db():
    grouped_activities = activity_collection.aggregate([
        {
            "$group": {
                "_id": {
                    "user_id": "$user_id",
                    "app_usage_id": "$app_usage_id"
                },
                "total_duration": {"$sum": "$duration"},
                "activities": {"$push": "$activity_id"},
                "last_visited": {"$max": "$end"},
                "count": {"$sum": 1}
            }
        }
    ])

    for entry in grouped_activities:
        user_id = entry['_id']['user_id']
        app_id = entry['_id']['app_usage_id']
        total_duration = entry['total_duration']
        last_visited = entry['last_visited']
        activities = entry['activities']
        count = entry['count']

        avg_duration = total_duration / count if count > 0 else 0

        application_name = app_id

        app_document = {
            "user_id": user_id,
            "app_id": app_id,
            "last_visited": last_visited,
            "application_name": application_name,
            "total_duration": total_duration,
            "avg_duration": avg_duration,
            "activities": activities
        }

        existing_doc = app_collection.find_one({"user_id": user_id, "app_id": app_id})
        if existing_doc:
            app_collection.update_one({"_id": existing_doc["_id"]}, {"$set": app_document})
            print(f"Updated app: {app_id} for user: {user_id}")
        else:
            app_collection.insert_one(app_document)
            print(f"Inserted app: {app_id} for user: {user_id}")


if __name__ == "__main__":
    generate_app_db()
