chai_type = "Ginger Chai"
customer_name = "Alex"

print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"
# print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[:8]}") #This will also print the same as above line

print(f"Last word: {chai_description[12:]}") #This will print the last word of the string
print(f"Last word: {chai_description[::-1]}") #This will reverse the string

label_text = "Chai Latté"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")

print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
print(f"Decoded label: {decoded_label}")