// Set new default font family and font color to mimic Bootstrap's default styling
// Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
// Chart.defaults.global.defaultFontColor = '#292b2c';
//DATA 작업
let data_labels = [];
let dataset = [];
let colorset = [];

function pushData(data_labels, dataset, colorset, s_data) {
    if (s_data.length === 0)
        return 0;
    let data_length = s_data.length;
    for (let i = 0; i < data_length; i++) {
        if (s_data[i]['offset'] === undefined)
            return 0;
        let sub_length = s_data[i]['offset'].length
        for (let j = 0; j < sub_length; j++) {
            let [start_num, end_num, emotion] = [s_data[i]['offset'][j], s_data[i]['offset'][j] + s_data[i]['length'][j], s_data[i]['emotion'][j]]
            let temp = s_data[i]['sentence'].slice(start_num, end_num)
            const searchIndex = data_labels.indexOf(temp)
            if (searchIndex == -1) {
                data_labels.push(temp)
                dataset.push(1)
                let colorstring = "";
                if (emotion == 'negative')
                    colorstring += 'rgb(235,' + String(200 - 2 * i) + ',' + String(200 - 2 * i) + ',0.5)';
                else if (emotion == 'neutral')
                    colorstring += 'rgb(' + String(214 - 2 * i) + ',' + String(214 - 2 * i) + ',' + String(214 - 2 * i) + ',0.5)';
                else
                    colorstring += 'rgb(202,227,' + String(246 - 2 * i) + ',0.5)';
                colorset.push(colorstring);
            }
            else {
                dataset[searchIndex]++;
            }
        }
    }
}
pushData(data_labels, dataset, colorset, s_data);
// ㅡㅡㅡㅡㅡ


var ctx = document.getElementById('keyword_chart');
var keyWordChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: data_labels,
        datasets: [{
            label: 'My First Dataset',
            data: dataset,
            backgroundColor: colorset
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
                text: 'Chart.js PolarArea Chart'
            }
        }
    }
});