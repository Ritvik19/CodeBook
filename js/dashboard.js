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
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    legend: {
                        labels: {
                            fontColor: "white",
                        }
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                fontColor: "white",
                                beginAtZero: true
                            }
                        }],
                        xAxes: [{
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
drawPieChart()