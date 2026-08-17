import threading

tea_stock = 0

def restock():
    global tea_stock
    for _ in range(100000):
        tea_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print("Tea Stock: ", tea_stock)