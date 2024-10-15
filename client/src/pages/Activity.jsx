import React, { useEffect, useState } from 'react';
import LineChart from '../components/DashboardComponents/LineChart.jsx';
import BarChart from '../components/DashboardComponents/BarChart.jsx';
import PieChart from '../components/DashboardComponents/PieChart.jsx';
import Histogram from '../components/DashboardComponents/Histogram.jsx';
import ScatterPlot from '../components/DashboardComponents/ScatterPlot.jsx';
import AreaChart from '../components/DashboardComponents/AreaChart.jsx';
import DoughnutChart from '../components/DashboardComponents/DoughnutChart.jsx';
import StackedBarChart from '../components/DashboardComponents/StackedBarChart.jsx';
import RadarChart from '../components/DashboardComponents/RadarChart.jsx';
import SummaryBox from '../components/DashboardComponents/SummaryBox.jsx';
import UserBehaviorChart from '../components/DashboardComponents/UserBehaviourChart.jsx'; // Import your new UserBehaviorChart component
import { fetchActivities, fetchApplicationUsage, fetchUserData } from '../api.js';

const ActivityDashboard = () => {
  const [activityData, setActivityData] = useState([]);
  const [appUsageData, setAppUsageData] = useState([]);
  const [userData, setUserData] = useState(null); // State for user data

  useEffect(() => {
    const getData = async () => {
      try {
        const activities = await fetchActivities();
        const applicationUsage = await fetchApplicationUsage();
        const userDataResponse = await fetchUserData(); // Fetch user data

        setActivityData(activities);
        setAppUsageData(applicationUsage);
        setUserData(userDataResponse); // Set user data
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    getData();
  }, []);


  const averageSessionDurationData = {
    labels: userData?.sessionDurations?.map(session => new Date(session.date).toLocaleDateString()) || [],
    datasets: [
      {
        label: 'Average Session Duration (seconds)',
        data: userData?.sessionDurations?.map(session => session.duration) || [],
        borderColor: 'rgba(255, 159, 64, 1)',
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
        fill: true,
      },
    ],
  };

  const frequentDomainsData = {
    labels: userData?.frequent_domains || [],
    datasets: [
      {
        label: 'Domain Access Count',
        data: userData?.domainAccessCounts || [],
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
      },
    ],
  };

  // Prepare data for visualizations
  const lineChartData = {
    labels: activityData.map(activity => new Date(activity.begin).toLocaleDateString()),
    datasets: [
      {
        label: 'Activity Duration (seconds)',
        data: activityData.map(activity => activity.duration),
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
      },
    ],
  };

  const barChartData = {
    labels: appUsageData.map(app => app.application_name),
    datasets: [
      {
        label: 'Total Duration (seconds)',
        data: appUsageData.map(app => app.total_duration),
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
      },
    ],
  };

  // 3. Pie Chart Data (Activity Category Distribution)
  const categoryCounts = activityData.reduce((acc, activity) => {
    const category = activity.details.additional_info?.category || 'Uncategorized';
    acc[category] = (acc[category] || 0) + 1;
    return acc;
  }, {});

  const pieChartData = {
    labels: Object.keys(categoryCounts),
    datasets: [
      {
        label: 'Activity Category',
        data: Object.values(categoryCounts),
        backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)'],
      },
    ],
  };

  // 4. Histogram Data (Activity Type Distribution)
  const histogramData = {
    labels: [...new Set(activityData.map(activity => activity.activity_type))],
    datasets: [
      {
        label: 'Activity Count',
        data: [...new Array([...new Set(activityData.map(activity => activity.activity_type))].length)].map((_, index) => 
          activityData.filter(activity => activity.activity_type === [...new Set(activityData.map(activity => activity.activity_type))][index]).length
        ),
        backgroundColor: 'rgba(255, 159, 64, 0.6)',
      },
    ],
  };

  // 5. Scatter Plot Data (Activity Duration vs. Time of Day)
  const scatterPlotData = {
    datasets: [
      {
        label: 'Activity Duration vs. Time',
        data: activityData.map(activity => ({
          x: new Date(activity.begin).getHours(), // Hour of the day
          y: activity.duration,
        })),
        backgroundColor: 'rgba(255, 205, 86, 0.6)',
      },
    ],
  };

  // 6. Area Chart Data (Cumulative Activity Duration)
  const areaChartData = {
    labels: activityData.map(activity => new Date(activity.begin).toLocaleDateString()),
    datasets: [
      {
        label: 'Cumulative Activity Duration',
        data: activityData.map(activity => activity.duration),
        fill: true,
        backgroundColor: 'rgba(153, 102, 255, 0.6)',
        borderColor: 'rgba(153, 102, 255, 1)',
      },
    ],
  };

  // 7. Doughnut Chart Data (Proportion of Application Usage)
  const doughnutChartData = {
    labels: appUsageData.map(app => app.application_name),
    datasets: [
        {
            label: 'Application Usage Proportion',
            data: appUsageData.map(app => app.total_duration),
            backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)'],
        },
    ],
  };

  // 8. Stacked Bar Chart Data (Activity Type per Application)
  const stackedBarData = {
    labels: appUsageData.map(app => app.application_name),
    datasets: [
      ...[...new Set(activityData.map(activity => activity.activity_type))].map(type => ({
        label: type,
        data: appUsageData.map(app => 
          activityData.filter(activity => 
            activity.activity_type === type && activity.app_usage_id === app.app_id
          ).length
        ),
        backgroundColor: `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 0.6)`,
      })),
    ],
  };

  // 9. Radar Chart Data (Engagement Metrics for Applications)
  const radarChartData = {
    labels: appUsageData.map(app => app.application_name),
    datasets: [
      {
        label: 'Engagement Metrics',
        data: appUsageData.map(app => app.total_duration), // or any other engagement metric
        backgroundColor: 'rgba(255, 159, 64, 0.6)',
      },
    ],
  };

  const totalActivities = activityData.length;
  const totalAppUsageDuration = appUsageData.reduce((acc, app) => acc + app.total_duration, 0);
  const userName = userData?.user_id || "User"; // Use optional chaining to safely access user_id

  return (
    <div className="p-4 px-24">
      <h1 className="text-2xl font-bold mb-4 text-gray-900 dark:text-gray-100">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <SummaryBox 
          title="Total Activities" 
          value={totalActivities} 
          icon="📅" 
        />
        <SummaryBox 
          title="Total Application Usage Duration" 
          value={`${totalAppUsageDuration} seconds`} 
          icon="⏳" 
        />
        <SummaryBox 
          title={`Welcome, ${userName}`} 
          value="Your Dashboard" 
          icon="👤" // Use an appropriate icon
        />
        <SummaryBox 
          title="Average Session Duration" 
          value={`${userData?.average_session_duration.toFixed(2)} seconds`} 
          icon="⏱️" // Use an appropriate icon
        />
        <SummaryBox 
          title="Frequent Domains" 
          value={userData?.frequent_domains.join(', ') || 'None'} 
          icon="🌐" // Use an appropriate icon
        />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <LineChart data={lineChartData} options={{ responsive: true }} />
        {/* <BarChart data={frequentDomainsData} options={{ responsive: true }} title="Domain Access Count" /> */}
        {/* <LineChart data={averageSessionDurationData} options={{ responsive: true }} title="Average Session Duration" /> */}
        <BarChart data={barChartData} options={{ responsive: true }} />
        <PieChart data={pieChartData} options={{ responsive: true }} />
        {/* <Histogram data={histogramData} options={{ responsive: true }} /> */}
        <ScatterPlot data={scatterPlotData} options={{ responsive: true }} />
        <AreaChart data={areaChartData} options={{ responsive: true }} />
        <DoughnutChart data={doughnutChartData} options={{ responsive: true }} />
        <StackedBarChart data={stackedBarData} options={{ responsive: true }} />
        <RadarChart data={radarChartData} options={{ responsive: true }} />
      </div>
    </div>
  );
};

export default ActivityDashboard;
