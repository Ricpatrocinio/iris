document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const sepalLength = document.getElementById('sepal-length').value;
    const sepalWidth = document.getElementById('sepal-width').value;
    const petalLength = document.getElementById('petal-length').value;
    const petalWidth = document.getElementById('petal-width').value;

    const data = {
        sepal_length: sepalLength,
        sepal_width: sepalWidth,
        petal_length: petalLength,
        petal_width: petalWidth
    };

    fetch('http://127.0.0.1:5000/predict', {  // Adjust the URL if your Flask app runs on a different host/port
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error making prediction';
    });
});
