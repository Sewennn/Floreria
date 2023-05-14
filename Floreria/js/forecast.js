/* no logre que funcionara xd */

function api(){
    fetch('https://api.openweathermap.org/data/2.5/weather?lat=-33.457&lon=-70.648&appid=10ecded2d32cca671bc8da70a87d0f63')
    .then(response => response.json())
    .then(data =>{
        console.log(data);
        let temperatura = document.getElementById("weather.id");
        temperatura.innerHTML += data.temperatura.valor;
    })

}