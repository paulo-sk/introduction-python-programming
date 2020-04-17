# A plane travels 395,000 meters in 9000 seconds. 
# Write a program to find the speed of the plane (Speed = Distance / Time).

d,t = [float(x) for x in input("Enter the distance in meters and the time in seconds, respectively: ").split(' ')]
speed = d / t
print(f"The speed is {speed:.2f} m/s")