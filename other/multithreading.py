import threading
import time
from collections import deque


def append_last(arr):
    arr = list(arr)
    first_part, last_part = arr[:5], arr[5:]
    first_part = deque(first_part)
    last_part = deque(last_part)
    last_part.appendleft(first_part.popleft())
    first_part.appendleft(last_part.pop())
    arr = first_part + last_part
    arr = list(arr)
    print(arr)
    time.sleep(1)


def append_first(arr):
    arr = list(arr)
    first_part, last_part = arr[5:], arr[:5]
    first_part = deque(first_part)
    last_part = deque(last_part)
    first_part.append(last_part.pop())
    last_part.append(first_part.popleft())
    arr = list(first_part) + list(last_part)
    print(arr)
    time.sleep(1)


arr = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr)
for i in range(10):
    thread1 = threading.Thread(target=append_first(arr))
    thread2 = threading.Thread(target=append_last(arr))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished!")
