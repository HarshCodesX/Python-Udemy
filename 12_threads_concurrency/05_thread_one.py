# This is a simple example of using threads in Python to perform two tasks concurrently: boiling milk and toasting a bun. The `boil_milk` function simulates the process of boiling milk, while the `toast_bun` function simulates toasting a bun. Each function includes a sleep period to represent the time taken for each task.
import threading
import time

def boil_milk():
    print("Boiling milk")
    time.sleep(2)
    print("Milk boiled")


def toast_bun():
    print("Toasting bun")
    time.sleep(3)
    print("Done with the bun toasting")

start = time.time()
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")