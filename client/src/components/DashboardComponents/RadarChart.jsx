// src/components/DashboardComponents/RadarChart.jsx
import React from 'react';
import { Radar } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const RadarChart = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Engagement Metrics Comparison</h2>
      <Radar data={data} options={options} />
    </div>
  );
};

export default RadarChart;
