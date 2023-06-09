import time


def calculate_taxi_cost(distance_km):
    base_rate = 4.00
    price_per_140m = 0.25
    distance_m = distance_km * 1000
    num_140m_segments = distance_m // 140
    total_cost = base_rate + num_140m_segments * price_per_140m
    return total_cost


def print_calculation_time(func):
    def wrapper(distance_km):
        start_time = time.time()
        result = func(distance_km)
        end_time = time.time()
        print(f"Calculation time: {end_time - start_time:.6f} s")
        print(f"Input distance: {distance_km} km")
        print(f"Taxi cost: ${result:.2f}")
        return result

    return wrapper



@print_calculation_time
def calculate_taxi_cost(distance_km):
    base_rate = 4.00
    price_per_140m = 0.25
    distance_m = distance_km * 1000
    num_140m_segments = distance_m // 140
    total_cost = base_rate + num_140m_segments * price_per_140m
    return total_cost


distance = float(input("Введите расстояние поездки в километрах: "))

cost = calculate_taxi_cost(distance)
print(f"Стоимость поездки на такси: ${cost:.2f}")