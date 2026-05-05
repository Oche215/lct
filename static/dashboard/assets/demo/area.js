// Ensure you have Chart.js loaded in your project

// Set default font family and color for all charts globally
Chart.defaults.gl.font.family = `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`;
Chart.defaults.gl.font.color = '#212529'; // Bootstrap's default body text color

// Optional: You can also adjust other default font options if needed
Chart.defaults.gl.font.size = 12;       // default font size
Chart.defaults.gl.font.weight = 'normal'; // normal font weight
Chart.defaults.gl.font.style = 'normal';  // normal font style
Chart.defaults.gl.color = '#212529';       // fallback for color in some cases

// Example Geo chart using the new defaults
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'choropleth', // Example geo chart type
    data: {
        labels: ['Nigeria', 'Ghana', 'Kenya'],
        datasets: [{
            label: 'Population',
            data: [
                { feature: 'NGA', value: 214000000 },
                { feature: 'GHA', value: 32000000 },
                { feature: 'KEN', value: 54000000 }
            ]
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: {
                    font: Chart.defaults.gl.font,
                    color: Chart.defaults.gl.color
                }
            }
        }
    }
});