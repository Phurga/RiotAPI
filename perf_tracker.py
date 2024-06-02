import time

def track_perf(func):
    """Decorator to track performance of functions"""
    def wrapper(*args, **kwargs):
        print(func.__name__ + ' started.')
        t1 = time.time()
        func(*args, **kwargs)
        t = time.time() - t1
        print(f"{func.__name__} finished in {t:9.3f}s.")
    return wrapper