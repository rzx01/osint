import React from 'react';

const SummaryBox = ({ title, value, icon }) => {
  return (
    <div className="flex items-center justify-between p-4 border rounded-lg shadow-md bg-white dark:bg-gray-800 dark:border-gray-700">
      <div className="flex items-center">
        <div className="text-2xl">{icon}</div>
        <div className="ml-4">
          <h2 className="text-lg font-bold text-gray-800 dark:text-white">{title}</h2>
          <p className="text-xl font-semibold text-gray-600 dark:text-gray-400">{value}</p>
        </div>
      </div>
    </div>
  );
};

export default SummaryBox;
