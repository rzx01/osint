import express from 'express';
import SearchQuery from '../models/Search.js'; 

const router = express.Router();


router.post('/search_queries', async (req, res) => {
  try {
    console.log("backend search");
    const queryData = req.body;
    const newQuery = new SearchQuery(queryData);
    await newQuery.save();
    res.status(201).json({ message: 'Search query data saved successfully', data: newQuery });
  } catch (error) {
    console.error('Error saving search query data:', error);
    res.status(500).json({ message: 'Error saving search query data', error: error.message });
  }
});

export default router;
