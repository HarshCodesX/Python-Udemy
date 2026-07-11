masala_spices = ("cardamom", "cloves", "cinnamon")
(spice1, spice2, spice3) = masala_spices
print(spice1)
print(spice2)
print(spice3)

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio of ginger to cardamom: {ginger_ratio}:{cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio of ginger to cardamom after interchange: {ginger_ratio}:{cardamom_ratio}")

# membership

print(f"Is ginger present in masala spices? {"ginger" in masala_spices}")
print(f"Is ginger present in masala spices? {"cloves" in masala_spices}")