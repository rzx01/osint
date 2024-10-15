const API_BASE_URL = 'http://localhost:5000/api'; 

const getUserId = () => {
  return localStorage.getItem('userId'); 
};

export const fetchActivities = async () => {
  const userId = getUserId() || "taha";
  
  try {
    const response = await fetch(`${API_BASE_URL}/activities/${userId}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.activities; // Return the activities directly
  } catch (error) {
    console.error('Error fetching activities:', error);
    throw error; 
  }
};

export const fetchApplicationUsage = async () => {
  const userId = getUserId() || "taha"; 

  try {
    const response = await fetch(`${API_BASE_URL}/application-usage/${userId}`); // Match the route
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.activities; 
  } catch (error) {
    console.error('Error fetching application usage:', error);
    throw error; 
  }
};

export const fetchUserData = async () => {
  const userId = getUserId() || "taha"; 

  try {
    const response = await fetch(`${API_BASE_URL}/users/${userId}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data; 
  } catch (error) {
    console.error('Error fetching application usage:', error);
    throw error; 
  }
};
