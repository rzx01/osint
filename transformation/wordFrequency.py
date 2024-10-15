import spacy
from collections import Counter
from pymongo import MongoClient
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from textblob import TextBlob
from sentence_transformers import SentenceTransformer, util

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/cybercrime')
db = client['cybercrime']
search_queries_collection = db['searchqueries']
user_collection = db['user']

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Fetch search queries along with user identification
search_queries = search_queries_collection.find({}, {'user_id': 1, 'query_text': 1, '_id': 0})

# Initialize dictionaries to hold user data
user_nouns = {}
user_entities = {}
user_sentiments = {}
search_texts = []

# Process each search query with spaCy
for query in search_queries:
    user_id = query['user_id']
    query_text = query['query_text']

    doc = nlp(query_text)
    sentiment = TextBlob(query_text).sentiment.polarity

    if user_id not in user_nouns:
        user_nouns[user_id] = []
        user_entities[user_id] = []
        user_sentiments[user_id] = []

    user_nouns[user_id].extend([token.text for token in doc if token.pos_ == 'NOUN'])
    user_entities[user_id].extend([ent.text for ent in doc.ents])
    user_sentiments[user_id].append(sentiment)

    search_texts.append(' '.join([token.text for token in doc if token.pos_ == 'NOUN']))

# Update top 15 nouns for each user
for user_id, nouns in user_nouns.items():
    noun_frequencies = Counter(nouns)
    top_15_nouns = dict(noun_frequencies.most_common(15))

    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'top_15_terms': top_15_nouns}},
        upsert=True
    )

# Update top 15 entities for each user
for user_id, entities in user_entities.items():
    entity_frequencies = Counter(entities)
    top_15_entities = dict(entity_frequencies.most_common(15))

    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'top_15_entities': top_15_entities}},
        upsert=True
    )

# Average sentiment score per user
for user_id, sentiments in user_sentiments.items():
    avg_sentiment = sum(sentiments) / len(sentiments)

    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'average_sentiment': avg_sentiment}},
        upsert=True
    )

# Topic Modeling using LDA
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
term_matrix = vectorizer.fit_transform(search_texts)
lda = LatentDirichletAllocation(n_components=5, random_state=0)
lda.fit(term_matrix)
topics = lda.transform(term_matrix)

# Store topics for each user
for idx, user_id in enumerate(user_nouns.keys()):
    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'topics': topics[idx].tolist()}},
        upsert=True
    )

# Clustering using K-Means
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(term_matrix)
cluster_labels = kmeans.labels_

# Store cluster labels for each user
for idx, user_id in enumerate(user_nouns.keys()):
    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'cluster': int(cluster_labels[idx])}},
        upsert=True
    )

# Keyword Extraction using TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=15, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(search_texts)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Get top keywords for each user
for idx, user_id in enumerate(user_nouns.keys()):
    user_keywords = {feature_names[i]: tfidf_matrix[idx, i] for i in tfidf_matrix[idx].nonzero()[1]}
    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'top_keywords': user_keywords}},
        upsert=True
    )

# Semantic Similarity Matching using BERT
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = model.encode(search_texts, convert_to_tensor=True)
cosine_scores = util.pytorch_cos_sim(embeddings, embeddings)

# Process similarity results to find related users or common interests
similarity_threshold = 0.8  # Define a threshold for high similarity
similar_users = {}

for i, user_id in enumerate(user_nouns.keys()):
    similar_users[user_id] = []
    for j, other_user_id in enumerate(user_nouns.keys()):
        if i != j and cosine_scores[i][j] > similarity_threshold:
            similar_users[user_id].append(other_user_id)

    user_collection.update_one(
        {'user_id': user_id},
        {'$set': {'similar_users': similar_users[user_id]}},
        upsert=True
    )

print("NLP enhancements have been applied and data updated in the database.")
