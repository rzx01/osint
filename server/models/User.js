
import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
    user_id: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    behavior_profile: {
        preferred_content: [{ type: String }],
    },
    average_session_duration: { type: Number, required: true },
    frequent_domains: [{ type: String }],
    total_duration: { type: Number, required: true },
    top_15_terms: {
        type: Map,
        of: Number,
    },
    top_15_entities: {
        type: Map,
        of: Number,
    },
    average_sentiment: { type: Number, required: true },
    topics: [{ type: Number }],
    cluster: { type: Number },
    top_keywords: {
        type: Map,
        of: Number,
    },
    similar_users: [{ type: String }],
}, { collection: 'user' });

const User = mongoose.model('user', UserSchema);

export default User;
