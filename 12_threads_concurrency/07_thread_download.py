# this example shows how to download files concurrently using threads
import requests
import threading
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download,args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    t.join()

end = time.time()
print(f"All downloads done in {end - start:.2f} seconds")