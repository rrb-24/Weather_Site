var input = document.querySelector('.input_text');
var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var desc = document.querySelector('.desc');
var humidity = document.querySelector('.humidity');
var speed = document.querySelector('.speed');
var clouds = document.querySelector('.clouds');
var button = document.querySelector('.submit');
var temp_c = document.querySelector('.temp_c');



fetch('https://api.openweathermap.org/data/2.5/weather?q=bengaluru&appid=50a7aa80fa492fa92e874d23ad061374')
    .then(response => response.json())
    .then(data => {
        var tempValue = data['main']['temp'];
        var nameValue = data['name'];
        var descValue = data['weather'][0]['description'];
        var humidityvalue = data['main']['humidity'];
        var speedvalue = data['wind']['speed'];

        main.innerHTML = nameValue;
        desc.innerHTML = "Desc - " + descValue;
        temp.innerHTML = "Temp - " + tempValue + "K";
        temp_c.innerHTML = tempValue - 273.15 + "&deg;C";
        humidity.innerHTML = "Humidity - " + humidityvalue;
        speed.innerHTML = "Wind speed - " + speedvalue + "Km/h";
        input.value = "";

    })
