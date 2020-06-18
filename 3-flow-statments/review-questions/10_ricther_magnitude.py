magnitude = float(input("Enter the Ritcher magnitude: "))

if magnitude >= 1.0 and magnitude <= 2.0:
    print("Microearthquakes not felt or rarely felt")
elif magnitude > 2.0 and magnitude <= 4.0:
    print("Very rarely causes damage")
elif magnitude > 4.0 and magnitude <= 5.0:
    print("Damage done to weak buildings")
elif magnitude > 5.0 and magnitude <= 6.0:
    print("Cause damage to the poorly constructed building")
elif magnitude > 6.0 and magnitude <= 7.0:
    print("Causes damage to well-built structures")
elif magnitude > 7.0 and magnitude <= 8.0:
    print("Causes damage to most buildings")
elif magnitude > 8.0 and magnitude <= 9.0:
    print("Causes major destruction")
elif magnitude > 9.0:
    print("Causes unbelievable damage")
else:
    print("Nothing at all")