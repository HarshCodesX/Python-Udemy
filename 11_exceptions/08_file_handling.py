# file = open("order.txt", "w")
# try:
#     file.write("Ginger tea - 2 cups")
# finally:
#     file.close()

# ANOTHER WAY
with open("order.txt", "w") as file:
    file.write("lemon tea - 1 cup")