tea_menu = {"masala": 30, "ginger": 40}
try:
    tea_menu["cardamom"]
except KeyError:
    print("The key that you are trying to access does not exist")
print("hello")