$(function () {
	var gaugeOptions = {

		chart: {
			type: 'solidgauge'
		},

		title: null,

		pane: {
			center: ['50%', '85%'],
			size: '140%',
			startAngle: -90,
			endAngle: 90,
			background: {
				backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
				innerRadius: '60%',
				outerRadius: '100%',
				shape: 'arc'
			}
		},

		tooltip: {
			enabled: false
		},

		// the value axis
		yAxis: {
			stops: [
				[0.1, '#55BF3B'], // green
				[0.5, '#DDDF0D'], // yellow
				[0.9, '#DF5353'] // red
			],
			lineWidth: 0,
			minorTickInterval: null,
			tickAmount: 2,
			title: {
				y: -70
			},
			labels: {
				y: 16
			}
		},

		plotOptions: {
			solidgauge: {
				dataLabels: {
					y: 5,
					borderWidth: 0,
					useHTML: true
				}
			}
		}
	};

	// The speed gauge
	$('#container1').highcharts(Highcharts.merge(gaugeOptions, {
		yAxis: {
			min: 0,
			max: 100,
			title: {
				text: 'some var'
			}
		},

		credits: {
			enabled: false
		},

		series: [{
			name: 'Speed',
			data: [0],
			dataLabels: {
				format: '<div style="text-align:center"><span style="font-size:25px;color:' +
					((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
					   '<span style="font-size:12px;color:silver">unit</span></div>'
			},
			tooltip: {
				valueSuffix: ' unit'
			}
		}]

	}));

	function setgauge(v) {
		//console.log("setgauge(" + v + ")");
		var chart = $('#container1').highcharts();

		if (chart) {
			var point = chart.series[0].points[0];
			point.update(v);
		}
	}

	var url = "ws://localhost:9000/";
	//var url = "ws://192.168.0.10:9000/";
	ws = new ReconnectingWebSocket(url);
	ws.onopen = function(evt) {
		console.log(evt)
		//ws.send("128");
	};
	ws.onclose = function(evt) { console.log("closed") };
	ws.onmessage = function(evt) {
		//console.log("Got: ");
		console.log(evt.data);
		setgauge(Number(evt.data));
	};
	ws.onerror = function(evt) { console.log("error?") };
});