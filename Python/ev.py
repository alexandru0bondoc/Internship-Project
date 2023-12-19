def estimate_range(battery_level_percent):
    # Estimate the available range of an EV based on the battery level.
    # Args: battery_level_percent(float)
    # Returns: The estimated available range in kilometers(float).
    total_battery_capacity = 62  # kWh
    energy_consumption_per_100km = 15.6  # kWh/100km

    # Available energy in battery
    available_energy = (battery_level_percent / 100) * total_battery_capacity

    # Estimated range
    es_Range = (available_energy / energy_consumption_per_100km) * 100

    return es_Range


# Example usage
battery_level = 50  # 50% battery level
estimated_range = estimate_range(battery_level)
print(f"Estimated Range: {estimated_range} km")
