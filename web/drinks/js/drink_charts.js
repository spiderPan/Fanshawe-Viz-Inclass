//Rada Chart

fetch("/data/json/drinks_by_countries.json")
  .then(resp => resp.json())
  .then(function(data) {
    var drinks_type = ["beer", "spirit", "wine"];
    var pickedCountry = [];

    while (pickedCountry.length < 4) {
      let index = Math.floor(Math.random() * data.length);
      pickedCountry.push(data[index]);
    }

    var bar_country_data = pickedCountry.map(function(x) {
      return {
        label: x["country"],
        fill: false,
        backgroundColor: random_rgba(),
        borderColor: random_rgba(),
        pointBorderColor: random_rgba(),
        pointBackgroundColor: random_rgba(),
        data: [x["beer_servings"], x["spirit_servings"], x["wine_servings"]]
      };
    });

    new Chart(document.getElementById("radar-chart"), {
      type: "radar",
      data: {
        labels: drinks_type,
        datasets: bar_country_data
      },
      options: {
        title: {
          display: true,
          text: "Drinks Consumption by Countries"
        }
      }
    });

    var bubble_country_data = pickedCountry.map(function(c) {
      return {
        label: c["country"],
        backgroundColor: random_rgba(),
        borderColor: random_rgba(),
        data: [
          {
            x: c["wine_servings"],
            y: c["spirit_servings"],
            r: c["beer_servings"]
          }
        ]
      };
    });
    //Bubble
    new Chart(document.getElementById("bubble-chart"), {
      type: "bubble",
      data: {
        datasets: bubble_country_data
      },
      options: {
        title: {
          display: true,
          text: "Beer Serving"
        },
        scales: {
          yAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: "Spirit"
              }
            }
          ],
          xAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: "Wine"
              }
            }
          ]
        }
      }
    });
  });

function getRandomColor() {
  var letters = "0123456789ABCDEF".split("");
  var color = "#";
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function random_rgba() {
  var o = Math.round,
    r = Math.random,
    s = 255;
  return (
    "rgba(" +
    o(r() * s) +
    "," +
    o(r() * s) +
    "," +
    o(r() * s) +
    "," +
    r().toFixed(1) +
    ")"
  );
}

fetch("/data/json/drinks_by_continent.json")
  .then(resp => resp.json())
  .then(function(data) {
    console.log(data);
    var continents = data.map(function(x){
      return x['continent'];
    });
    var wines = [],
        beers = [],
        spirit = [];
    
    data.forEach(function(x){
      beers.push(x['beer_servings']);
      wines.push(x['wine_servings']);
      spirit.push(x['spirit_servings']);
    });

    console.log(continents);

    //Grouped Bar Chart
    new Chart(document.getElementById("bar-chart-grouped"), {
      type: "bar",
      data: {
        labels: continents,
        datasets: [
          {
            label: "Beer",
            backgroundColor: "#3e95cd",
            data: beers
          },
          {
            label: "Spirit",
            backgroundColor: "#8e5ea2",
            data: spirit
          },
          {
            label: "Wine",
            backgroundColor: "#000",
            data: wines
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: "Population growth (millions)"
        }
      }
    });
  });
