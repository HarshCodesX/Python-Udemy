seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()
match seat_type:
    case "sleeper":
        print("Price is 500 rupees")
    case "ac":
        print("Price is 1000 rupees")
    case "general":
        print("Price is 300 rupees")
    case "luxury":
        print("Price is 2000 rupees")
    case _:
        print("Invalid seat type. Please choose sleeper, AC, general, or luxury.")