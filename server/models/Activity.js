import mongoose from 'mongoose';

const activitySchema = new mongoose.Schema({
  activity_id: {
    type: String,
    required: true,
    unique: true
  },
  user_id: {
    type: String,
    required: true
  },
  app_usage_id: {
    type: String,
    required: true
  },
  begin: {
    type: Date,
    required: true
  },
  end: {
    type: Date,
  },
  duration: Number,
  activity_type: {
    type: String,
  },
  details: {
    url: String,
    user_feedback: String
  }
});

export default mongoose.model('activities', activitySchema);
