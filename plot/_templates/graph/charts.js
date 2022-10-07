// Graph values
labels = document.getElementById('labels').value
datas = document.getElementById('datas').value

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels  : JSON.parse(labels),
        datasets: [{
            data           : JSON.parse(datas),
            backgroundColor: ['rgba(30, 144, 255, 0.8)'],
            borderColor    : ['rgb(30, 144, 255)'],
            borderWidth    : 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});