import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
  user_id: {
    type: String,
    required: true,
    unique: true
  },
  email: {
    type: String,
    unique: true
  },
  behavior_profile: {
    preferred_content: [String],
    average_session_duration: Number
  },
  frequent_domains:  {
    type: Map,
    of: Number  
  },
  total_duration: Number
});

export default mongoose.model('user', userSchema);
