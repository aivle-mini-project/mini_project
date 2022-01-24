// Set new default font family and font color to mimic Bootstrap's default styling
// Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
// Chart.defaults.global.defaultFontColor = '#292b2c';

const DATA_COUNT = 5;
const NUMBER_CFG = { count: DATA_COUNT, min: 0, max: 100 };

var ctx = document.getElementById('myPieChart');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [
            '긍정',
            '중립',
            '부정'
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [
                s_data[0].positive,
                s_data[0].neutral,
                s_data[0].negative,
            ],
            backgroundColor: [
                '#9FE2FA',
                '#9CA393',
                '#FA786A'
            ],
            hoverOffset: 4
        }]
    },
    options: {
        animation: {
            animateScale: true,
            animateRotate: true
        },
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Doughnut Chart'
            }
        }
    }
});