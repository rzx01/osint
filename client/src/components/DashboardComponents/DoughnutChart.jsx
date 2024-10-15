// src/components/DashboardComponents/DoughnutChart.jsx
import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const DoughnutChart = ({ data, options }) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">Application Usage Proportion</h2>
      <Doughnut data={data} options={options} />
    </div>
  );
};

export default DoughnutChart;
