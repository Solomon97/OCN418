$(function () {
	// check out the official example for the Highcharts.merge() function
	//.highcharts(Highcharts.merge(gaugeOptions, { blah... }

	var gaugeOptions = {
		chart: {
			type: 'solidgauge',
			backgroundColor: '#e6f2ff',
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
				y: -70,
				text: '',//'some variable',
				style: {
					fontSize: "1.5em",
				}
			},
			labels: {
				y: 16
			},
			min: 0,
			max: 100,
		},
		series: [{
			name: 'Speed',
			data: [0],
			dataLabels: {
				format: '<div style="text-align:center"><span style="font-size:25px;color:' +
					((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
					   '<span style="font-size:10px;color:silver">[unit]</span></div>'
			},
			/*tooltip: {
				valueSuffix: ' unit'
			}*/
		}],
		plotOptions: {
			solidgauge: {
				dataLabels: {
					y: 5,
					borderWidth: 0,
					useHTML: true
				}
			}
		},
		tooltip: {
			enabled: false
		},
		credits: {
			enabled: false
		},
	};
	
// !
	_.times(20,function(k) {
		$('#container' + (k+1)).highcharts(gaugeOptions);
	});

	function setgauge(k,v) {
		var chart = $('#container' + k).highcharts();
		if (chart) {
			var point = chart.series[0].points[0];
			point.update(v);
		}
	}

	var url = "ws://" + String(window.location.host) + ":9000";
	//var url = "ws://192.168.0.108:9000";
	ws = new ReconnectingWebSocket(url);
	ws.onopen = function(evt) {
		console.log(evt)
		//ws.send("128");
	};
	ws.onclose = function(evt) { console.log("closed") };
	ws.onmessage = function(evt) {
		var m = evt.data;
		console.log(m);
		m = m.split(',');
		var k = m[0];
		var v = Math.round(m[1],2);
		if (2 == m.length && k >= 1 && k <= 20) {
			if ((0 <= v) && (v <= 100)) {
				setgauge(k,v);
			}
		}
	};
	ws.onerror = function(evt) { console.log("error?") };
});