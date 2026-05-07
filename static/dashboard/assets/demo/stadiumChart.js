//async function loadChart() {
//    const response = await fetch('api/fifa/');
//    const chartData = await response.json();
//
//    const ctx = document.getElementById('stadiumChart').getContext('2d');
//    new Chart(ctx, {
//        type: 'line', // You can change this to 'line', 'pie', etc.
//        data: {
//            labels: chartData.labels,
//            datasets: [{
//                label: 'Stadium Capacity',
//                data: chartData.values,
//                backgroundColor: 'rgba(54, 162, 235, 0.5)',
//                borderColor: 'rgba(54, 162, 235, 1)',
//                borderWidth: 1
//            }]
//        },
//        options: {
//            responsive: true,
//            scales: {
//                y: { beginAtZero: true }
//            }
//        }
//    });
//}
//
//loadChart();


document.addEventListener('DOMContentLoaded', function() {
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
    });