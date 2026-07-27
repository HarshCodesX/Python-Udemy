def serve_tea(flavor):
    try:
        print(f"Preparing {flavor} tea")
        if flavor == "unknown":
            raise ValueError("We dont know that flavor")
        else:
            print(f"{flavor} tea is served")
    except ValueError as e:
        print("Error: ", e)
    finally:
        print(f"Next customer please")

serve_tea("Cardamom")
serve_tea("unknown")