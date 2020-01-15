function drawBarChart() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            console.log(Object.values(dataObj))
            var ctx = document.getElementById('bar').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: Object.keys(dataObj),
                    datasets: [{
                        label: 'Problems Solved',
                        data: Object.values(dataObj),
                        backgroundColor: '#11174b',
                        borderColor: '#b3ddcc',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        labels: {
                            fontColor: "white",
                        }
                    },
                    scales: {
                        yAxes: [{
                            gridLines: {
                                color: "white"
                            },
                            ticks: {
                                fontColor: "white",
                                beginAtZero: true
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                color: "white"
                            },
                            ticks: {
                                fontColor: "white",
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
    };
    xhttp.open("GET", "../data/ProgramCounts.json", true);
    xhttp.send();
}
drawBarChart();

function drawPieChart() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            console.log(Object.values(dataObj))
            var ctx = document.getElementById('pie').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: Object.values(dataObj),
                        backgroundColor: ["#b3ddcc", "#8acdce", "#62bed2", "#46aace", "#3d91be", "#3577ae", "#2d5e9e", "#24448e", "#1c2b7f", "#162065", "#11174b"]
                    }],
                    labels: Object.keys(dataObj)
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "white",
                        }
                    },
                    scales: {}
                }
            });
        }
    };
    xhttp.open("GET", "../data/ProgramLanguage.json", true);
    xhttp.send();
}
drawPieChart();

function code() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            console.log(dataObj)
            document.getElementById('loc').innerHTML = dataObj['loc']
            document.getElementById('num').innerHTML = dataObj['num']
            var ctx1 = document.getElementById('code').getContext('2d');
            var myChart1 = new Chart(ctx1, {
                type: 'horizontalBar',
                data: {
                    labels: ['Expressions', 'Decisions', 'Iterations'],
                    datasets: [{
                        label: '# occurences',
                        data: [dataObj['expressions'], dataObj['decisions'], dataObj['for'] + dataObj['while']],
                        backgroundColor: '#11174b',
                        borderColor: '#b3ddcc',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    legend: {
                        labels: {
                            fontColor: "white",
                        }
                    },
                    scales: {
                        yAxes: [{
                            gridLines: {
                                color: "white"
                            },
                            ticks: {
                                fontColor: "white",
                                beginAtZero: true
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                color: "white"
                            },
                            ticks: {
                                fontColor: "white",
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
            var ctx2 = document.getElementById('loops').getContext('2d');
            var myChart2 = new Chart(ctx2, {
                type: 'pie',
                data: {
                    datasets: [{
                        data: [dataObj['for'], dataObj['while']],
                        backgroundColor: ["#2d5e9e", "#162065"],
                    }],
                    labels: ['For', 'While']
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "white",
                        }
                    },
                    scales: {}
                }
            });


        }
    };
    xhttp.open("GET", "../data/ProgramAnalysis.json", true);
    xhttp.send();
}
code();