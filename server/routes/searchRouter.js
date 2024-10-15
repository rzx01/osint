import express from 'express';
import SearchQuery from '../models/Search.js'; 
import User from '../models/User.js';

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
router.get('/searchdata/:user_id', async (req, res) => {
  const { user_id } = req.params;

  try {
      // Fetch the search data for the specified user_id
      const searchData = await SearchQuery.find({ user_id: user_id }).lean();

      // Check if searchData is not empty
      if (!searchData.length) {
          return res.status(404).json({ message: 'No search data found for this user.' });
      }
      // Send the data back in the response
      res.json(searchData);

  } catch (error) {
      console.error('Error fetching search data:', error);
      res.status(500).json({ message: 'Internal Server Error' });
  }
});


router.get('/userdata/:user_id', async (req, res) => {
  const { user_id } = req.params;

  try {
      const userData = await User.findOne({ user_id: user_id }).lean();

      if (!userData) {
          return res.status(404).json({ message: 'No search data found for this user.' });
      }
      res.json(userData);

  } catch (error) {
      console.error('Error fetching search data:', error);
      res.status(500).json({ message: 'Internal Server Error' });
  }
});


export default router;
