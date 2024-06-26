import threading
import time
from functools import wraps

# Limits from RIOT: 100 per 2min, 20 per seconds. Giving some buffer to avoid errors.
CALLS_LONG = 95
PERIOD_LONG = 120
CALLS_SHORT = 18
PERIOD_SHORT = 1

def rate_limiter(calls, period):
    """Retrieved from chatgpt, have no idea how it works, but it does work."""
    def decorator(func):
        lock = threading.Lock()
        times = []

        @wraps(func)
        def wrapped(*args, **kwargs):
            nonlocal times
            with lock:
                current_time = time.time()
                # Remove timestamps older than 'period'
                times = [t for t in times if current_time - t < period]
                
                # If rate limit is exceeded, wait
                if len(times) >= calls:
                    sleep_time = period - (current_time - times[0])
                    time.sleep(sleep_time)
                    current_time = time.time()
                    times = [t for t in times if current_time - t < period]

                times.append(current_time)
            return func(*args, **kwargs)
        
        return wrapped
    return decorator