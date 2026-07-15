device_status = input("Enter device status (active/inactive): ").lower()
if device_status == "active":
    temperature = float(input("Enter the current temperature: "))
    if temperature > 35:
        print("High temperature")
    else:
        print("Temperature is normal")
else:
    print("Device is inactive.")