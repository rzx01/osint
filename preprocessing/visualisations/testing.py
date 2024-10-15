import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/')
db = client['cybercrime']
activity_collection = db['activities']


excluded_app_usage_ids = ['newtab', 'history', 'prod-apnortheast-a.online.tableau.com']

pipeline = [
    {"$match": {"app_usage_id": {"$nin": excluded_app_usage_ids}}},
    {"$group": {"_id": "$app_usage_id", "total_duration": {"$sum": "$duration"}}},
    {"$sort": {"total_duration": -1}}
]

data = list(activity_collection.aggregate(pipeline))
df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
sns.barplot(x='_id', y='total_duration', data=df, palette='viridis')
plt.xlabel('Application/Website')
plt.ylabel('Total Duration (seconds)')
plt.title('Total Duration Spent on Each Application/Website')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
