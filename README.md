# 🌦️ Weather App

A Python command-line weather application that fetches real-time weather and forecast data using the OpenWeatherMap API.

## Features

* Current weather information
* Temperature and "feels like" temperature
* Humidity information
* 5-step weather forecast
* Error handling for invalid cities
* Secure API key management using environment variables

## Project Structure

```text
weather-app/
│
├── api.py          # Handles API requests
├── display.py      # Formats and displays weather data
├── main.py         # Main application flow
├── .gitignore
├── .env.example
└── README.md
```

---

## Technologies Used

- Python
- Requests Library
- Python Dotenv
- OpenWeatherMap API

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shrutikabhand/weather-app.git
cd weather-app
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Create a `.env` file

```env
API_KEY=your_openweathermap_api_key
```

### 4. Run the application

```bash
python main.py
```

---

## Sample Output

```text
Enter city name: Pune

===================================
  Pune, IN
  Clear sky
  Temp     : 30°C (feels like 32°C)
  Humidity : 65%
===================================

See 5-step forecast? (y/n): y

  5-step forecast:
  2026-06-06 12:00:00 → 31°C, clear sky
  2026-06-06 15:00:00 → 30°C, scattered clouds
  2026-06-06 18:00:00 → 28°C, light rain
  2026-06-06 21:00:00 → 26°C, broken clouds
  2026-06-07 00:00:00 → 25°C, clear sky
```


## What I Learned

* Working with REST APIs
* Sending HTTP requests using Python Requests
* Parsing JSON data
* Exception handling and error management
* Environment variables and API key security
* Organizing Python projects using multiple modules

## Future Improvements

* Weather icons
* Wind speed and pressure
* Sunrise and sunset information

* Streamlit web application
* CSV export of weather reports

## Author

**Shrutika Bhand**
