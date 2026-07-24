def infinite_tea():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_tea()
user2 = infinite_tea()
print(refill)
# print(next(refill))
# print(next(refill))
# print(next(refill))

for _ in range(1,4):
    print(next(refill))

for _ in range(6):
    print(next(user2))