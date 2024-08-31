import mongoose from 'mongoose';

const browserSessionSchema = new mongoose.Schema({
  session_id: {
    type: String,
    required: true,
    unique: true
  },
  user_id: {
    type: String,
    required: true
  },
  start_time: {
    type: Date,
    required: true
  },
  end_time: {
    type: Date,
    required: true
  },
  total_duration: Number,
  session_type: {
    type: String,
    enum: ['Leisure', 'Work', 'Study'],
  },
  activities: [String],
  application_usage: [
    {
      key: String,
      value: Number
    }
  ]
});

export default mongoose.model('browser_session', browserSessionSchema);
