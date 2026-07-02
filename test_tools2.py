import urllib.parse
import urllib.request
import json
import hashlib
import random

def get_weather(location: str) -> str:
    try:
        encoded_location = urllib.parse.quote(location)
        url = f"https://wttr.in/{encoded_location}?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10.0) as response:
            data = json.loads(response.read().decode())
        current = data.get("current_condition", [])[0]
        temp_c = current.get("temp_C", "Unknown")
        desc = current.get("weatherDesc", [{}])[0].get("value", "Unknown")
        return f"Current weather in {location}: {temp_c}°C, {desc}."
    except Exception as e:
        return f"Error fetching weather for {location}: {str(e)}"

def get_transit_prices(origin: str, destination: str) -> str:
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

print("--- Wroclaw ---")
print(get_transit_prices("Bonn", "Wroclaw"))
print(get_weather("Wroclaw"))

print("\n--- Szczecin ---")
print(get_transit_prices("Bonn", "Szczecin"))
print(get_weather("Szczecin"))

print("\n--- Krakow ---")
print(get_transit_prices("Bonn", "Krakow"))
print(get_weather("Krakow"))
