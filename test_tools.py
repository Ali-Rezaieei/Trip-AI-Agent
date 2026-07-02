import urllib.parse
import httpx
import hashlib
import random

def get_weather(location: str) -> str:
    try:
        encoded_location = urllib.parse.quote(location)
        url = f"https://wttr.in/{encoded_location}?format=j1"
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        current = data.get("current_condition", [])[0]
        temp_c = current.get("temp_C", "Unknown")
        desc = current.get("weatherDesc", [{}])[0].get("value", "Unknown")
        return f"Current weather in {location}: {temp_c}°C, {desc}."
    except Exception as e:
        return f"Error fetching weather for {location}: {str(e)}"

def get_transit_prices(origin: str, destination: str, travel_date: str = "") -> str:
    route_str = f"{origin.lower().strip()}-{destination.lower().strip()}"
    hash_val = int(hashlib.md5(route_str.encode()).hexdigest(), 16)
    random.seed(hash_val)
    distance_factor = random.randint(30, 200)
    flight_price = distance_factor * 1.5 + random.randint(20, 80)
    train_price = distance_factor * 0.8 + random.randint(10, 40)
    bus_price = distance_factor * 0.3 + random.randint(5, 20)
    return (f"Transit prices from {origin} to {destination}:\n"
            f"- Economy Flight: €{flight_price:.2f}\n"
            f"- Train / High-speed rail: €{train_price:.2f}\n"
            f"- Intercity Bus: €{bus_price:.2f}")

print("Wroclaw:")
print(get_transit_prices("Bonn", "Wroclaw"))
print(get_weather("Wroclaw"))
