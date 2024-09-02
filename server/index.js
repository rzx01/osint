import express from 'express';
import cors from 'cors';
import activitiesRoutes from './routes/activitiesRoutes.js';
import connectDB from './db.js'; 
import browserRouter from './routes/browserRouter.js';
import searchQueryRouter from './routes/searchRouter.js';
connectDB();

const app = express();
const PORT = 5000;

app.use(express.json());
app.use(cors());

app.get('/', (req, res) => {
    res.send('running');
});


app.use('/api', activitiesRoutes);
app.use('/api', browserRouter);
app.use('/api', searchQueryRouter);


app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});



