import mongoose from 'mongoose';

const connectDB = async () => {
    try {
        await mongoose.connect('mongodb+srv://rxchit01:KIet03Wzg9HiMg6g@main.c5s9m.mongodb.net/cybercrime');
        console.log('Connected to MongoDB');
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
        process.exit(1); 
    }
};

export default connectDB;
