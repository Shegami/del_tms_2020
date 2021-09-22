"""
Пользователь вводит время в минутах и расстояние в километрах. Найдите
скорость в м/c.
"""

time_min = float(input('time (minutes): '))
distance_km = float(input('distance (km): '))

speed_meter_sec = (distance_km * 1000) / (time_min * 60)

print(f'speed: {speed_meter_sec} (m/s)')
