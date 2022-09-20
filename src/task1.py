import contextlib
import io
import time


def decorator_1(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        with contextlib.redirect_stdout(io.StringIO()):
            start = time.perf_counter()
            ret_val = func(*args, **kwargs)
            end = time.perf_counter()

        print(f"{func.__name__} call {wrapper.count} executed in {end - start} sec")

        return ret_val

    wrapper.count = 0

    return wrapper
