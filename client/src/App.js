// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar.jsx';
import ActivityDashboard from "./pages/Activity.jsx"
import Search from "./pages/Search.jsx"
import Login from "./pages/Login.jsx"

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/activity" element={<ActivityDashboard />} />
        <Route path="/search" element={<Search />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
