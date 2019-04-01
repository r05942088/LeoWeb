console.log('??????')
console.log('XDD')
// http://api.jquery.com/html/
const host = 'http://192.168.152.129:8000/api/datarate/';
console.log('XDD')
$.ajax({
    type: "GET",
    url: host,
    contentType: "application/json",
    success: function(data) {
        let len = data.length;
        let dr = data[len - 1].dr;
        var svg = d3.select("#speedometer")
                .append("svg:svg")
                .attr("width", 400)
                .attr("height", 400);
        var gauge = iopctrl.arcslider()
                .radius(120)
                .events(false)
                .indicator(iopctrl.defaultGaugeIndicator);
        gauge.axis().orient("in")
                .normalize(true)
                .ticks(6)
                .tickSubdivide(3)
                .tickSize(10, 8, 10)
                .tickPadding(5)
                .scale(d3.scale.linear()
                        .domain([0, 300])
                        .range([-3*Math.PI/4, 3*Math.PI/4]));
        var segDisplay = iopctrl.segdisplay()
                .width(80)
                .digitCount(6)
                .negative(false)
                .decimals(0);
        svg.append("g")
                .attr("class", "segdisplay")
                .attr("transform", "translate(130, 200)")
                .call(segDisplay);
        svg.append("g")
                .attr("class", "gauge")
                .call(gauge);
        segDisplay.value(dr);
        gauge.value(dr);
            }
});

console.log('???')