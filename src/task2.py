import time
import contextlib
import io
import inspect

indent = 12


def decorator_2(func):
	def wrapper(*args, **kwargs):
		# Writing start time
		start = time.perf_counter()

		# Redirecting output
		with contextlib.redirect_stdout(io.StringIO()) as f:
			func(*args, **kwargs)

		# Writing end time
		end = time.perf_counter()
		# Incrementing function execution counter
		wrapper.count += 1

		# Printing number of executions
		print(f"{func.__name__} call {wrapper.count} executed in {end - start} sec")

		# Printing function name
		print(f'Name:'.ljust(indent), func.__name__)

		# Printing function object type
		print(f'Type:'.ljust(indent), type(func))

		# Creating function object signature (object too)
		sig = inspect.signature(func)

		# Printing signature
		print(f'Sign:'.ljust(indent), sig)

		# Printing positional and key-worded arguments
		print('Args:'.ljust(indent), 'positional', sig.bind_partial(*args, **kwargs).args)
		print(''.ljust(indent), 'key-worded', sig.bind_partial(*args, **kwargs).kwargs)

		# Splitting doc string and printing it
		doc_rows = func.__doc__.strip().split('\n')
		print('Doc:'.ljust(indent), doc_rows[0])
		for i in range(1, len(doc_rows)):
			print(''.ljust(indent), doc_rows[i].strip())

		# Printing function source
		source_rows = inspect.getsource(func).split('\n')
		print('Source:'.ljust(indent), source_rows[0])
		for i in range(1, len(source_rows)):
			print(''.ljust(indent), source_rows[i].strip())

		# Printing function output
		output = f.getvalue().split('\n')
		print('Output:'.ljust(indent), output[0])
		for i in range(1, len(output)):
			print(''.ljust(indent), output[i].strip())
	wrapper.count = 0
	return wrapper

