let activityStartTime = null;
let currentUrl = null;

function getAppIdFromUrl(url) {
    const domain = new URL(url).hostname;
    return domain;
}

function sendActivityData(activity) {
    fetch('http://localhost:5000/api/activities', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(activity)
    })
    .then(response => response.json())
    .then(data => console.log('Activity data sent:', data))
    .catch(error => console.error('Error sending activity data:', error));
}

function sendSearchQueryData(queryData) {
    fetch('http://localhost:5000/api/search_queries', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(queryData)
    })
    .then(response => response.json())
    .then(data => console.log('Search query data sent:', data))
    .catch(error => console.error('Error sending search query data:', error));
}

function startActivity(url) {
    console.log("Activity started for URL:", url);
    activityStartTime = new Date();
    currentUrl = url;
}

function endActivity(url) {
    console.log("Activity ended for URL:", url);
    if (activityStartTime) {
        const appId = getAppIdFromUrl(url);
        const searchQuery = getSearchQuery(url);

        if (searchQuery) {
            const queryData = {
                query_id: 'query_' + Date.now(),
                user_id: userId,
                timestamp: new Date().toISOString(),
                search_engine: appId,
                query_text: searchQuery,
                result_clicks: []
            };

            sendSearchQueryData(queryData);
        } else {
            const activity = {
                activity_id: 'activity_' + Date.now(),
                user_id: userId,
                app_usage_id: appId,
                begin: activityStartTime,
                end: new Date(),
                duration: Math.floor((new Date() - activityStartTime) / 1000),
                activity_type: 'page_visit',
                details: {
                    url: url,
                    user_feedback: 'URL changed'
                }
            };

            sendActivityData(activity);
        }

        activityStartTime = null;
        currentUrl = null;
    }
}

function getSearchQuery(url) {
    const searchEngines = [
        { host: "google.com", param: "q" },
        { host: "bing.com", param: "q" },
        { host: "yahoo.com", param: "p" },
        { host: "duckduckgo.com", param: "q" },
        { host: "baidu.com", param: "wd" },
        { host: "yandex.com", param: "text" },
    ];

    const urlObj = new URL(url);
    for (let engine of searchEngines) {
        if (urlObj.hostname.includes(engine.host)) {
            return urlObj.searchParams.get(engine.param);
        }
    }
    return null;
}

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
        if (currentUrl && currentUrl !== tab.url) {
            endActivity(currentUrl);
        }
        startActivity(tab.url);
    }
});

chrome.tabs.onCreated.addListener((tab) => {
    startActivity(tab.url);
});

chrome.tabs.onRemoved.addListener((tabId, removeInfo) => {
    if (currentUrl) {
        endActivity(currentUrl);
    }
});

let sessionStartTime = null;
let currentSessionId = null;
let appUsage = {};
const userId = 'rachit'; 

function generateSessionId() {
    return 'session_' + Date.now();
}

function startSession() {
    sessionStartTime = new Date();
    currentSessionId = generateSessionId();
    appUsage = {}; 
    console.log('Session started:', currentSessionId);
}

function endSession() {
    if (!sessionStartTime || !currentSessionId) return;

    const sessionEndTime = new Date();
    const totalDuration = Math.floor((sessionEndTime - sessionStartTime) / 1000); 
    
    const sessionData = {
        session_id: currentSessionId,
        user_id: userId,
        start_time: sessionStartTime.toISOString(),
        end_time: sessionEndTime.toISOString(),
        total_duration: totalDuration,
        session_type: 'Leisure',
        activities: [], 
        application_usage: Object.keys(appUsage).map(key => ({
            key: key,
            value: appUsage[key]
        }))
    };
    
    fetch('http://localhost:5000/api/browser_sessions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(sessionData)
    })
    .then(response => response.json())
    .then(data => console.log('Session data sent:', data))
    .catch(error => console.error('Error sending session data:', error));

    sessionStartTime = null;
    currentSessionId = null;
    appUsage = {};
}

function updateAppUsage(url) {
    if (!url) return;
    const domain = new URL(url).hostname;
    if (appUsage[domain]) {
        appUsage[domain] += 1;
    } else {
        appUsage[domain] = 1;
    }
}

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url) {
        updateAppUsage(tab.url);
    }
});

chrome.windows.onRemoved.addListener((windowId) => {
    endSession();
});

chrome.runtime.onStartup.addListener(startSession);
chrome.runtime.onInstalled.addListener(startSession);
