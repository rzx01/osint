import mongoose from 'mongoose';

const searchQuerySchema = new mongoose.Schema({
  query_id: {
    type: String,
    required: true,
    unique: true
  },
  user_id: {
    type: String,
    required: true
  },
  timestamp: {
    type: Date,
    required: true
  },
  search_engine: {
    type: String,
    required: true
  },
  query_text: {
    type: String,
    required: true
  },
  result_clicks: {
    type: [String], 
    default: []
  }
});

export default mongoose.model('SearchQuery', searchQuerySchema);
