// src/components/DashboardComponents/AreaChart.jsx
import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const AreaChart = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Cumulative Activity Duration</h2>
      <Line data={data} options={{ ...options, elements: { line: { fill: true } } }} />
    </div>
  );
};

export default AreaChart;
