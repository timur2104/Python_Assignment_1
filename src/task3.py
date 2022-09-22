import time
import contextlib
import io
import inspect

indent = 12

ranking = {}


class ClassDecorator1:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.count += 1

        start = time.perf_counter()

        with contextlib.redirect_stdout(io.StringIO()) as f:
            ret_val = self.func(*args, **kwargs)

        end = time.perf_counter()

        with open("output.txt", "a") as output_file:
            with contextlib.redirect_stdout(output_file):
                print(f"{self.func.__name__} call {self.count} executed in {end - start} sec")

        return ret_val


# Here inheritance from ClassDecorator1 would be convenient to avoid duplications of code.
class ClassDecorator2:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        # Writing start time
        start = time.perf_counter()

        # Redirecting output
        with contextlib.redirect_stdout(io.StringIO()) as f:
            ret_val = self.func(*args, **kwargs)

        with open("output.txt", "a") as output_file:
            with contextlib.redirect_stdout(output_file):
                # Writing end time
                end = time.perf_counter()
                # Incrementing function execution counter
                self.count += 1

                # Printing number of executions
                print(f"{self.func.__name__} call {self.count} executed in {end - start} sec")

                # Printing function name
                print(f'Name:'.ljust(indent), self.func.__name__)

                # Printing function object type
                print(f'Type:'.ljust(indent), type(self.func))

                # Creating function object signature (object too)
                sig = inspect.signature(self.func)

                # Printing signature
                print(f'Sign:'.ljust(indent), sig)

                # Printing positional and key-worded arguments
                print('Args:'.ljust(indent), 'positional', args)
                print(''.ljust(indent), 'key-worded', kwargs)

                # Splitting doc string and printing it
                doc_rows = self.func.__doc__.strip().split('\n')
                print('Doc:'.ljust(indent), doc_rows[0])
                for i in range(1, len(doc_rows)):
                    print(''.ljust(indent), doc_rows[i].strip())

                # Printing function source
                source_rows = inspect.getsource(self.func).split('\n')
                print('Source:'.ljust(indent), source_rows[0])
                for i in range(1, len(source_rows)):
                    print(''.ljust(indent), source_rows[i].strip())

                # Printing function output
                out = f.getvalue().split('\n')
                print('Output:'.ljust(indent), out[0])
                for i in range(1, len(out)):
                    print(''.ljust(indent), out[i].strip())

        return ret_val


class Ranker:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()

        with contextlib.redirect_stdout(io.StringIO()) as f:
            output = self.func(*args, **kwargs)

        end_time = time.perf_counter()

        ranking[self.func.__name__] = end_time - start_time

        return output

    def print_ranking():
        print('FUNCTION | RANK | TIME_ELAPSED')
        for index, (key, value) in enumerate(sorted(ranking.items(), key=lambda item: item[1])):
            print(f'{key:.9}'.ljust(12), f'{index + 1}'.ljust(6), f'{value:.6f}')
