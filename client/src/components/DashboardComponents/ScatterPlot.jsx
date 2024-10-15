// src/components/DashboardComponents/ScatterPlot.jsx
import React from 'react';
import { Scatter } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const ScatterPlot = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Activity Duration vs. Time</h2>
      <Scatter data={data} options={options} />
    </div>
  );
};

export default ScatterPlot;
