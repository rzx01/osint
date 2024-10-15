import express from 'express';
import Activity from '../models/Activity.js';
import Application from '../models/Application.js';
import User from "../models/User.js";
const activitiesRouter = express.Router();

activitiesRouter.post('/activities', async (req, res) => {
    try {
        console.log("backend activities");
        const activityData = req.body;
        const activity = new Activity(activityData);
        await activity.save();
        res.status(201).json({ message: 'Activity saved successfully', activity });
    } catch (error) {

        console.error(error);
        res.status(500).json({ message: 'Failed to save activity', error });
    }
});

const allowedAppIds = [
    "www.youtube.com",
    "www.reddit.com",
    "www.x.com",
    "www.amazon.in",
    "www.netflix.com",
    "www.primevideo.com"
];

activitiesRouter.get('/activities/:userId', async (req, res) => {
    try {
        const userId = req.params.userId;
        console.log(`Fetching activities for user ID: ${userId}`);

        const activities = await Activity.find({ 
            user_id: userId,
            app_usage_id: { $in: allowedAppIds }
        });

        if (activities.length === 0) {
            return res.status(404).json({ message: 'No activities found for this user' });
        }

        res.status(200).json({ activities });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to fetch activities', error });
    }
});

activitiesRouter.get('/application-usage/:userId', async (req, res) => {
    try {
        const userId = req.params.userId;
        console.log(`Fetching apps for user ID: ${userId}`);

        const applications = await Application.find({ 
            user_id: userId,
            app_id: { $in: allowedAppIds } 
        });

        if (applications.length === 0) {
            return res.status(404).json({ message: 'No applications found for this user' });
        }

        res.status(200).json({ activities: applications }); 
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to fetch applications', error });
    }
});

activitiesRouter.get('/users/:user_id', async (req, res) => {
    const { user_id } = req.params;
    console.log('Received user_id:', user_id); 

  
    try {
        const user = await User.findOne({ user_id: user_id.trim() });
      if (!user) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.json(user);
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });


export default activitiesRouter;
