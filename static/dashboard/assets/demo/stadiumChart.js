// Fetch data from your Django API endpoint
        fetch('/api/fifa/')
            .then(response => response.json())
            .then(data => {
                const ctx = document.getElementById('stadiumChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.labels, // Data from your JsonResponse
                        datasets: [{
                            label: 'Stadium Capacity',
                            data: data.values,
                            backgroundColor: 'rgba(54, 162, 235, 0.6)'
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: { title: { display: true, text: '2026 FIFA Stadiums' } }
                    }
                });
            });


//document.addEventListener('DOMContentLoaded', function() {
//        // Fetch data from your Django API endpoint
//        fetch('/api/fifa/')
//            .then(response => response.json())
//            .then(data => {
//                const ctx = document.getElementById('stadiumChart').getContext('2d');
//                new Chart(ctx, {
//                    type: 'line',
//                    data: {
//                        labels: data.labels, // Data from your JsonResponse
//                        datasets: [{
//                            label: 'Stadium Capacity',
//                            data: data.values,
//                            backgroundColor: 'rgba(54, 162, 235, 0.6)'
//                        }]
//                    },
//                    options: {
//                        responsive: true,
//                        plugins: { title: { display: true, text: '2026 FIFA Stadiums' } }
//                    }
//                });
//            });
//    });