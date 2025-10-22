// API endpoint - update this with your Azure Function URL when deployed
const API_URL = 'http://localhost:8000/api/counter';

// Function to fetch and display visitor count
async function updateVisitorCount() {
    try {
        // Increment the counter
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error('Failed to fetch visitor count');
        }

        const data = await response.json();
        document.getElementById('counter').textContent = data.count;
    } catch (error) {
        console.error('Error updating visitor count:', error);
        document.getElementById('counter').textContent = 'Error';
    }
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', updateVisitorCount);
