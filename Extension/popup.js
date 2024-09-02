document.getElementById('toggleTracking').addEventListener('click', () => {
    chrome.storage.local.get(['trackingEnabled'], (result) => {
        const newStatus = !result.trackingEnabled;
        chrome.storage.local.set({ trackingEnabled: newStatus });
        document.getElementById('toggleTracking').textContent = newStatus ? 'Disable Tracking' : 'Enable Tracking';
    });
});
