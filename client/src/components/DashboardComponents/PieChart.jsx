// src/components/DashboardComponents/PieChart.jsx
import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables); // Register all necessary components

const PieChart = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Pie Chart</h2>
      <Pie data={data} options={options} />
    </div>
  );
};

export default PieChart;
