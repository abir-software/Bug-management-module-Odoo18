// This file contains JavaScript code for the bug management functionality, likely handling client-side interactions.

document.addEventListener('DOMContentLoaded', function() {
    // Initialize bug management functionality
    const bugList = document.getElementById('bug-list');
    
    if (bugList) {
        // Example: Fetch and display bugs
        fetch('/api/bugs')
            .then(response => response.json())
            .then(data => {
                data.forEach(bug => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${bug.id}: ${bug.title}`;
                    bugList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching bugs:', error));
    }

    // Example: Add event listener for bug submission
    const bugForm = document.getElementById('bug-form');
    if (bugForm) {
        bugForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(bugForm);
            fetch('/api/bugs', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log('Bug submitted:', data);
                // Optionally refresh the bug list or provide feedback
            })
            .catch(error => console.error('Error submitting bug:', error));
        });
    }
});