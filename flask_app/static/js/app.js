const weatherContainer = document.getElementById("weather-container");

function fetchWeatherData() {
    fetch("/api/live-weather")
        .then(response => response.json())
        .then(data => {
            weatherContainer.innerHTML = ""; // Clear existing data
            data.forEach(item => {
                const card = document.createElement("div");
                card.className = "weather-card";
                card.innerHTML = `
                    <h3>${item.weather_data.city}</h3>
                    <p>Temperature: ${item.weather_data.temperature}°C</p>
                    <p>Humidity: ${item.weather_data.humidity}%</p>
                    <p>Condition: ${item.weather_data.condition}</p>
                `;
                weatherContainer.appendChild(card);
            });
        })
        .catch(error => console.error("Error fetching weather data:", error));
}

// Fetch weather data every 5 seconds
setInterval(fetchWeatherData, 5000);
fetchWeatherData();
