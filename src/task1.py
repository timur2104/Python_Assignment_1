import time
import contextlib
import io


def decorator_1(func):
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		with contextlib.redirect_stdout(io.StringIO()):
			func(*args, **kwargs)
		end = time.perf_counter()
		wrapper.count += 1
		print(f"{func.__name__} call {wrapper.count} executed in {end - start} sec")
	wrapper.count = 0
	return wrapper

