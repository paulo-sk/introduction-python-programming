# swimming pool: 12 X 7 X 2 = 168m³
# flow = 17m³/60s = 0,283 m³ / s
# 168 / 0.28333
time_seconds = 168 / 0.28333

minuts = time_seconds // 60
hours = minuts // 60
remaining_minuts = minuts % 60 
remaining_seconds = time_seconds % 60 % 60

print(f"Horas:{hours} Minutos:{remaining_minuts} Segundos:{remaining_seconds} ")