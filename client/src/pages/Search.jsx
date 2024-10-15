import React, { useEffect, useState } from 'react';
import PieChart from '../components/DashboardComponents/PieChart.jsx';
import BarChart from '../components/DashboardComponents/BarChart.jsx'; 
import SummaryBox from '../components/DashboardComponents/SummaryBox.jsx'; 
import { FaSearch, FaClock, FaUsers } from 'react-icons/fa'; 

const Search = () => {
    const [searchData, setSearchData] = useState([]);
    const [userData, setUserData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const user_id = localStorage.getItem('userId') ||"nia"; 

    useEffect(() => {
        const fetchData = async () => {
            try {
                const searchResponse = await fetch(`http://localhost:5000/api/searchdata/${user_id}`);
                if (!searchResponse.ok) {
                    throw new Error('Search data network response was not ok');
                }
                const searchResult = await searchResponse.json();
                setSearchData(searchResult); 

                const userResponse = await fetch(`http://localhost:5000/api/userData/${user_id}`);
                if (!userResponse.ok) {
                    throw new Error('User data network response was not ok');
                }
                const userResult = await userResponse.json();
                setUserData(userResult); 
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    const domainCounts = userData.frequent_domains ? userData.frequent_domains.reduce((acc, domain) => {
        acc[domain] = (acc[domain] || 0) + 1;
        return acc;
    }, {}) : {};

    const domainChartData = {
        labels: Object.keys(domainCounts),
        datasets: [{
            label: 'Frequent Domains',
            data: Object.values(domainCounts),
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
        }],
    };

    const terms = userData.top_15_terms || {};
    const termsChartData = {
        labels: Object.keys(terms),
        datasets: [{
            label: 'Top 15 Terms',
            data: Object.values(terms),
            backgroundColor: '#36A2EB',
        }],
    };

    const entities = userData.top_15_entities || {};
    const entitiesChartData = {
        labels: Object.keys(entities),
        datasets: [{
            label: 'Top 15 Entities',
            data: Object.values(entities),
            backgroundColor: '#FFCE56',
        }],
    };

    const searchQueriesPerDay = searchData.reduce((acc, query) => {
        const date = new Date(query.timestamp.$date).toLocaleDateString(); 
        acc[date] = (acc[date] || 0) + 1; 
        return acc;
    }, {});

    const lineChartData = {
        labels: Object.keys(searchQueriesPerDay),
        datasets: [
            {
                label: 'Search Queries Per Day',
                data: Object.values(searchQueriesPerDay),
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
            },
        ],
    };

    const chartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'User and Search Data Visualization',
            },
        },
    };

    const summaryData = [
        { title: 'Total Searches', value: searchData.length || 0, icon: <FaSearch /> },
        { title: 'Total Duration (seconds)', value: userData.total_duration || 0, icon: <FaClock /> },
        { title: 'Frequent Domains', value: userData.frequent_domains ? userData.frequent_domains.length : 0, icon: <FaUsers /> },
        { title: 'Average Sentiment', value: (userData.average_sentiment || 0).toFixed(2), icon: <FaSearch /> },
    ];

    return (
        <div className="p-4 px-24">
            <h1 className="text-2xl font-bold mb-4">User and Search Data Visualization</h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                {summaryData.map((item, index) => (
                    <SummaryBox key={index} title={item.title} value={item.value} icon={item.icon} />
                ))}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div>
                    <PieChart data={domainChartData} options={chartOptions} />
                </div>
                <div>
                    <BarChart data={termsChartData} options={chartOptions} />
                </div>
                <div className="col-span-2">
                    <BarChart data={entitiesChartData} options={chartOptions} />
                </div>
                <div className="col-span-2">
                    <BarChart data={lineChartData} options={chartOptions} />
                </div>
            </div>
        </div>
    );
};

export default Search;
