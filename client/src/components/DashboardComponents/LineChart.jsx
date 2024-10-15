// src/components/DashboardComponents/LineChart.jsx
import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables); // Register all necessary components

const LineChart = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Line Chart</h2>
      <Line data={data} options={options} />
    </div>
  );
};

export default LineChart;
