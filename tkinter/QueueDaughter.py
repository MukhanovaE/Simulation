import time
import random

def func(q):
    while True:
        q.put([random.randint(0, 100), random.randint(0, 100)])
        time.sleep(0.2)
