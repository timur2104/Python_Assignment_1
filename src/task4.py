import datetime
import time
import contextlib
import io
import traceback


class ProtectedClassDecorator1:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.count += 1

        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            with open('exceptions.log', 'a') as log:
                contextlib.redirect_stderr(log)
                try:
                    output = self.func(*args, **kwargs)
                except:
                    log.write(f'Dropped exception at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}:\n"{traceback.format_exc().strip()}"\n')
                else:
                    end = time.perf_counter()
                    print(f"{self.func.__name__} call {self.count} executed in {end - start} sec")

                    return output


def protected_decorator_1(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()):
            with open('exceptions.log', 'a') as log:
                contextlib.redirect_stderr(log)
                try:
                    func(*args, **kwargs)
                except:
                    log.write(f'Dropped exception at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}:\n"{traceback.format_exc().strip()}"\n')
                else:
                    end = time.perf_counter()
                    print(f"{func.__name__} call {wrapper.count} executed in {end - start} sec")

    wrapper.count = 0
    return wrapper