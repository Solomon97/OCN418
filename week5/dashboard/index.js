$(function() {
	var window_size = 1000;

	var chart;
	
	function addpoint(d) {
		if (!(chart == null)) {
			var shift = chart.series[0].length > window_size;
			var ts = Date.now() - 10*60*60*1000;
			chart.series[0].addPoint([ts,Number(d[0])],true,shift);
			chart.series[1].addPoint([ts,Number(d[1])],true,shift);
			chart.series[2].addPoint([ts,Number(d[2])],true,shift);
		}
	}

	var color1 = 'blue';
	var color2 = 'purple';
	var color3 = 'red';

	chart = new Highcharts.Chart({
		chart: {
			type: 'line',
			renderTo: 'container',
			defaultSeriesType: 'spline',
			events: {
				//load: addpoint
			},
			animation: false
		},
		title: {
			text: 'OCN418 Live Plot Demo'
		},
		subtitle: {
			text: 'Data from an Aanderaa 4531D Oxygen Optode',
			style: {
				fontSize: '1em'
			}
		},
		xAxis: {
			type: 'datetime',
			tickPixelInterval: 150,
			minRange: 1000,
			title: {
				text: 'HST',
				style: {
					fontSize: '2em',
				}
			}
		},
		yAxis: [{
			minPadding: 0.2,
			maxPadding: 0.2,
			labels: {
				format: '{value}uM',
				style: {
					color: color1,
					fontSize: '1.5em',
				},
				x: -30,
			},
			title: {
				text: 'Oxygen',
				margin: 30,
				style: {
					fontSize: '2em',
					color: color1
				}
			}
		},{
			gridLineWidth: 0,
			labels: {
				format: '{value}%',
				style: {
					color: color2,
					fontSize: '1.5em',
				}
			},
			title: {
				text: 'Air Saturation',
				style: {
					fontSize: '2em',
					color: color2
				}
			},
			opposite: true
		},{
			gridLineWidth: 0,
			labels: {
				format: '{value}°C',
				style: {
					color: color3,
					fontSize: '1.5em',
				}
			},
			title: {
				text: 'Temperature',
				style: {
					fontSize: '2em',
					color: color3
				}
			},
			opposite: true
		}],
		tooltip: {
			shared: true
		},
		series: [{
			name: 'O2',
			data: [],
			yAxis: 0,
			color: color1,
			lineWidth: 3,
			tooltip: {
				valueSuffix: ' uM'
			},
			marker: {
				enabled: false
			}
		},{
			name: 'Air Sat.',
			data: [],
			yAxis: 1,
			color: color2,
			lineWidth: 3,
			dashStyle: 'shortdash',
			tooltip: {
				valueSuffix: ' %'
			},
			marker: {
				enabled: false
			}
		},{
			name: 'Temperature',
			data: [],
			yAxis: 2,
			color: color3,
			lineWidth: 3,
			dashStyle: 'shortdot',
			tooltip: {
				valueSuffix: ' °C'
			},
			marker: {
				enabled: false
			}
		}],
		tooltip: {
			enabled: true
		},
		legend: {
			enabled: true,
			layout: 'vertical',
			floating: true,
			align: 'left',
			verticalAlign: 'top',
			y: 60,
			x: 100,
			backgroundColor: '#ffffff',
			itemStyle: {
				fontSize: '1em'
			}
		},
		credits: {
			enabled: false
		},
	});
	
	//var url = "ws://localhost:9000/";
	var url = "ws://" + String(window.location.host) + ":9000";
	//ws = new WebSocket(url);
	ws = new ReconnectingWebSocket(url);
	ws.onopen = function(evt) {
		//console.log(evt)
	};
	ws.onclose = function(evt) {
		//console.log("closed")
	};
	ws.onmessage = function(evt) {
		console.log(evt.data);
		addpoint(evt.data.split(','));
	};
	ws.onerror = function(evt) {
		console.log("error?")
	};

	//setInterval(function() { check_liveliness(chart,120); },10*1000);
});