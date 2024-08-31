import mongoose from 'mongoose';

const applicationUsageSchema = new mongoose.Schema({
  user_id: {
    type: String,
    required: true
  },
  app_id: {
    type: String,
    required: true
  },
  last_visited: {
    type: Date,
  },
  application_name: {
    type: String,
    required: true
  },
  total_duration: Number,
  avg_duration: Number,
  activities: [String],
  engagement_metrics: {
    likes: Number,
    shares: Number,
    comments: Number
  },
  device: {
    type: String,
    enum: ['Mobile', 'Desktop', 'Tablet'],
  }
});

export default mongoose.model('application_usage', applicationUsageSchema);
