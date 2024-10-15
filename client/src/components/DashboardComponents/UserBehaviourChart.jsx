import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Pie } from 'react-chartjs-2';

const UserBehaviorChart = ({ userData }) => {
  // Data for average session duration
  const avgSessionDurationData = {
    labels: ['Average Session Duration'],
    datasets: [
      {
        label: 'Duration (seconds)',
        data: [userData.average_session_duration],
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  // Data for frequent domains
  const frequentDomainsData = {
    labels: userData.frequent_domains,
    datasets: [
      {
        label: 'Frequent Domains',
        data: Array(userData.frequent_domains.length).fill(1), // Just for visualization, using count of 1 for each domain
        backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(255, 205, 86, 0.6)', 'rgba(153, 102, 255, 0.6)'],
      },
    ],
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">User Behavior Analysis</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <h3 className="text-lg font-semibold mb-2">Average Session Duration</h3>
          <Bar data={avgSessionDurationData} options={{ responsive: true }} />
        </div>
        <div>
          <h3 className="text-lg font-semibold mb-2">Frequent Domains</h3>
          <Pie data={frequentDomainsData} options={{ responsive: true }} />
        </div>
      </div>
    </div>
  );
};

export default UserBehaviorChart;
