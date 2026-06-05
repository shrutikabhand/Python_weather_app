from api import get_current_weather, get_forecast
from display import show_current, show_forecast

def main():
    city = input("Enter city name: ").strip()
    if not city:
        print("No city entered.")
        return
    
    try:
        current = get_current_weather(city)
        show_current(current)

        see_forecast = input("See 5-step forecast? (y/n)").strip().lower()
        if see_forecast == 'y':
            forecast = get_forecast(city)
            show_forecast(forecast)

    except ValueError as e:
        print(f"Error: {e}")
    
    except ConnectionError as e:
        print(f"Network error: {e}")
    

if __name__ == "__main__":
    main()


    