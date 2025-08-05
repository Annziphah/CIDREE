""" 5. Decorators and Logging
You want to automatically log the execution time of multiple functions without repeating code.
Task: Write a decorator that logs the start time, end time, and duration of any function it's applied to. """
import time
def log_time(func):
    def wrapper():
        start = time.time()
        print("Started")
        func()
        end = time.time()
        print("Ended")
        print("Duration:", end - start, "seconds")
    return wrapper
@log_time
def declog_time():
    for _ in range(1000000):
        pass
declog_time()
