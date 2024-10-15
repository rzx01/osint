// src/components/DashboardComponents/StackedBarChart.jsx
import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const StackedBarChart = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Activity Type per Application</h2>
      <Bar data={data} options={{ ...options, scales: { x: { stacked: true }, y: { stacked: true } } }} />
    </div>
  );
};

export default StackedBarChart;
