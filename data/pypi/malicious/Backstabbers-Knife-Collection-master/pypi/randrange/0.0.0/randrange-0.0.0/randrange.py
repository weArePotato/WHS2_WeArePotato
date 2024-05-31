import random

def randrange(step = 1):
    MAX_STOP = 32
    start = random.randint(0, MAX_STOP)
    stop = random.randint(start, MAX_STOP)
    return range(start, stop, step)
