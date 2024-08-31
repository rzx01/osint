import express from "express";
import Session from "../models/Session.js";
const browserRouter = express.Router()

browserRouter.post('/browser_sessions', async (req, res) => {
    try {
      console.log("browser session");
      const sessionData = req.body;
      const newSession = new Session(sessionData);
      await newSession.save();
      res.status(201).json({ message: 'Session data saved successfully', data: newSession });
    } catch (error) {
      console.error('Error saving session data:', error);
      res.status(500).json({ message: 'Error saving session data', error: error.message });
    }
  });
  

  export default browserRouter;