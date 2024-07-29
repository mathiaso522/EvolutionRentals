document.addEventListener('DOMContentLoaded', function() {
    // Handle 'Learn More' button click if it exists
    const learnMoreBtn = document.getElementById('learnMoreBtn');
    if (learnMoreBtn) {
        learnMoreBtn.addEventListener('click', function() {
            alert('More information coming soon!');
        });
    }

    // Handle 'Rent Now' button clicks on any page where they exist
    document.querySelectorAll('.rentBtn').forEach(button => {
        button.addEventListener('click', function() {
            const vehicle = this.dataset.vehicle;

            // Send the data to the server using fetch
            fetch('/rent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ vehicle: vehicle })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Rental recorded successfully!');
                } else {
                    alert('Error recording rental.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error recording rental.');
            });
        });
    });
});

// Handle the reset database on the rentals page
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('resetBtn').addEventListener('click', function() {
        fetch('/reset-db', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Database reset successfully!');
                location.reload(); // Refresh the page to reflect the changes
            } else {
                alert('Error resetting the database.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error resetting the database.');
        });
    });
});

