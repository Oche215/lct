const xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
const yValues = [55, 49, 44, 24, 15];
const barColors = ["red", "green","blue","orange","brown"];

const ctx = document.getElementById('wineChart').getContext('2d');

new Chart(ctx, {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    plugins: {
      legend: {display: false},
      title: {
        display: true,
        text: "World Wine Production 2018",
        font: {size: 16}
      }
    }
  }
});



//// Set new default font family and font color to mimic Bootstrap's default styling
//Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
//Chart.defaults.global.defaultFontColor = '#292b2c';
//
//// Bar Chart Example
//var ctx = document.getElementById("wineChart");
//var myLineChart = new Chart(ctx, {
//  type: 'bar',
//  data: {
//    labels: ["Italy", "France", "Spain", "USA", "Argentina"];
//    datasets: [{
//      label: "World Wine Production 2018",
//      barColors: ["red", "green","blue","orange","brown"];
////      backgroundColor: "rgba(2,117,216,1)",
////      borderColor: "rgba(2,117,216,1)",
//      data: [55, 49, 44, 24, 15];
//    }],
//  },
//  options: {
//    scales: {
//      xAxes: [{
//        time: {
//          unit: 'month'
//        },
//        gridLines: {
//          display: false
//        },
//        ticks: {
//          maxTicksLimit: 6
//        }
//      }],
//      yAxes: [{
//        ticks: {
//          min: 0,
//          max: 15000,
//          maxTicksLimit: 5
//        },
//        gridLines: {
//          display: true
//        }
//      }],
//    },
//    legend: {
//      display: false
//    }
//  }
//});
