import threading
import time

def prepare_tea(type_, wait_time):
    print(f"{type_} tea: brewing...")
    time.sleep(wait_time)
    print(f"{type_} tea: Ready")

t1 = threading.Thread(target=prepare_tea, args=("Lemon", 2))
t2 = threading.Thread(target=prepare_tea, args=("Ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()