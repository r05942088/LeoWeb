var ctxBc = document.getElementById('bubbleChart').getContext('2d');

    var bubbleChart = new Chart(ctxBc, {
    type: 'bubble',
    data: {
      datasets: [{
        label: 'Anchor',
        data: [{
          x: 0,
          y: 0,
          r: 10
        },{
          x: 10,
          y: 10,
          r: 10
        },{
          x: 10,
          y: 0,
          r: 10
        },{
          x: 0,
          y: 10,
          r: 10
        }],
        backgroundColor: "#62088A",
        hoverBackgroundColor: "#62088A"
      }, {
        label: 'Tag',
        data: [{
      x: 5,
      y: 5,
      r: 10
    }],
        
        backgroundColor: "#ff6384",
        hoverBackgroundColor: "#ff6384"
      }]
    }
    })