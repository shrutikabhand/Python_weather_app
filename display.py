def show_current(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"].capitalize()

    print(f"\n{'='*45}")
    print(f"  {city}, {country}")
    print(f"  {desc}")
    print(f"  Temp     : {temp}°C  (feels like {feels}°C)")
    print(f"  Humidity : {humidity}%")
    print(f"{'='*45}\n")

def show_forecast(data):
    print("  5-step forecast:")
    for item in data["list"]:
        time = item["dt_txt"]
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        print(f"  {time}  →  {temp}°C, {desc}")
    print()