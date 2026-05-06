
        // Fetch data from Django API
        fetch('https://lcttechnologies.com/api/sales-mon-total-data/')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error("Error fetching sales data:", data.error);
                    return;
                }

                const ctx = document.getElementById('salesChart').getContext('2d');

                new Chart(ctx, {
                    type: 'line', // Change to 'line' for line chart
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'Total Sales',
                            data: data.values,
                            backgroundColor: 'rgba(54, 162, 235, 0.5)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return '$' + value; // Format as currency
                                    }
                                }
                            }
                        }
                    }
                });
            })
            .catch(error => console.error("Fetch error:", error));
