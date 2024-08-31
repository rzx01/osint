import express from 'express';
import Activity from '../models/Activity.js';

const activitiesRouter = express.Router();

activitiesRouter.post('/activities', async (req, res) => {
    try {
        const activityData = req.body;
        const activity = new Activity(activityData);
        console.log("activity session");
        await activity.save();
        res.status(201).json({ message: 'Activity saved successfully', activity });
    } catch (error) {

        console.error(error);
        res.status(500).json({ message: 'Failed to save activity', error });
    }
});

export default activitiesRouter;
