# Multiprocessing example for brewing tea
from multiprocessing import Process
import time

def brew_tea(name):
    print(f"Start of {name} tea brewing")
    time.sleep(3)
    print(f"End of {name} tea brewing")

if __name__ == "__main__":
    tea_makers = [
        Process(target=brew_tea, args=(f"Tea Maker #{i + 1}", ))
        for i in range(3)
    ]

    #start all process
    for p in tea_makers:
        p.start()

    #wait for all to complete
    for p in tea_makers:
        p.join()

    print("All tea served")