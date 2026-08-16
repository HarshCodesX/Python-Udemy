from multiprocessing import Process, Queue

def prepare_tea(queue):
    queue.put("Ginger Tea is ready")


if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_tea, args=(queue,))
    p.start()
    p.join()
    print(queue.get())