    const xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
    const yValues = [55, 49, 44, 24, 15];
    const barColors = ["red", "green","blue","orange","brown"];

    const ctx = document.getElementById('wineChart').getContext('2d');

    new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor: barColors,
          data: yValues
        }]
      },
      options: {
        plugins: {
          legend: {display: true},
          title: {
            display: true,
            text: "World Wine Production 2018",
            font: {size: 16}
          }
        }
      }
    });
