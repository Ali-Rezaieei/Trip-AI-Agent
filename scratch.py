from mcp_server import get_weather, get_transit_prices, search_web
print("--- WEATHER ---")
print(get_weather("Szczecin, Poland"))
print("--- TRANSIT ---")
print(get_transit_prices("Bonn, Germany", "Szczecin, Poland"))
print("--- ACTIVITIES ---")
print(search_web("top cheap activities in Szczecin Poland"))
