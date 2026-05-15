    function drawChart() {

// Set Data
const data = google.visualization.arrayToDataTable([
  ['Country', 'Mhl'],
  ['Italy', 55],
  ['France', 49],
  ['Spain', 44],
  ['USA', 24],
  ['Argentina', 15]
]);

// Set Options
const options = {
  title: 'World Wide Wine Production'
};

// Draw
const chart = new google.visualization.BarChart(document.getElementById('wineChart'));
chart.draw(data, options);

}






//    const xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
//    const yValues = [55, 49, 44, 24, 15];
//    const barColors = ["red", "green","blue","orange","brown"];
//
//    const ctx = document.getElementById('wineChart').getContext('2d');
//
//    new Chart(ctx, {
//      type: "doughnut",
//      data: {
//        labels: xValues,
//        datasets: [{
//          backgroundColor: barColors,
//          data: yValues
//        }]
//      },
//      options: {
//        plugins: {
//          legend: {display: true},
//          title: {
//            display: true,
//            text: "World Wine Production 2018",
//            font: {size: 16}
//          }
//        }
//      }
//    });
