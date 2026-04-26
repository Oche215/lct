// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
const response = await fetch("{% url 'chart_data' %}");
                const chartData = await response.json();

                const ctx = document.getElementById("myPieChart").getContext("2d");

//var ctx = document.getElementById("myPieChart").getContext("2d");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: chartData.labels,
    datasets: [{
      data: chartData.data,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }],
  },
});
