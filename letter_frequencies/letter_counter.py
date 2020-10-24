import json
import urllib.request
import time
from threading import Thread, Lock

finished_count = 0


def count_letters(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    for l in txt:
        letter = l.lower()
        mutex.acquire()
        if letter in frequency:
            frequency[letter] += 1
        mutex.release()
    mutex.acquire()
    global finished_count
    finished_count += 1
    mutex.release()


def main():
    frequency = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    for i in range(1000,1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()
    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        time.sleep(0.5)
    end = time.time()
    print("Done, time taken", end - start)
    print(json.dumps(frequency, indent=4))


main()
