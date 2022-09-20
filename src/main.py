import math

import task3
from task1 import decorator_1
from task2 import decorator_2
from task4 import ProtectedClassDecorator1, protected_decorator_1


def pascal_triangle_printer(n=2):
    """
    Function prints n first lines of Pascal's triangle.
    :param n: height of Pascal's triangle
    :return: None
    """
    if n <= 0:
        raise ValueError

    length = 0
    rows = [[1]]

    while len(rows) != n:
        rows.append(
            [a + b for a, b in zip([0] + rows[length - 1], rows[length - 1] + [0])]
        )
        length = len(rows)

    print(rows)


def quadratic_equation_solver(a, b, c):
    """
    No description:(
    :param a:
    :param b:
    :param c:
    :return:
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        raise ValueError

    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print(f"'x_1' = {x_1}, 'x_2' = {x_2}.")
    return x_1, x_2


def fn():
    for i in range(1000):
        print(lambda: i ** 2)


useless_lambda = lambda a: print(a * a + a / a)


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


print("Checking task 1")
d1_pascal = decorator_1(pascal_triangle_printer)
d1_quadratic = decorator_1(quadratic_equation_solver)

d1_pascal(20)
d1_quadratic(1, 3, 1)
d1_pascal(2)
d1_quadratic(1, 5, 3)
d1_pascal(30)

print("_" * 75)


print("Checking task 2")
d2_pascal = decorator_2(pascal_triangle_printer)
d2_quadratic = decorator_2(quadratic_equation_solver)

d2_pascal(20)
d2_quadratic(1, 3, 1)
d2_pascal(2)
d2_quadratic(1, 5, 3)
d2_pascal(30)
funh(None, bar2="lol")

print("_" * 75)


print("Checking task 3\n(Look for outputs in output.txt file)")
d31_pascal = task3.ClassDecorator1(pascal_triangle_printer)
d31_quadratic = task3.ClassDecorator1(quadratic_equation_solver)

d31_pascal(20)
d31_quadratic(1, 3, 1)
d31_pascal(2)
d31_quadratic(1, 5, 3)
d31_pascal(30)

d32_pascal = task3.ClassDecorator2(pascal_triangle_printer)
d32_quadratic = task3.ClassDecorator2(quadratic_equation_solver)

d32_pascal(20)
d32_quadratic(1, 3, 1)
d32_pascal(2)
d32_quadratic(1, 5, 3)
d32_pascal(30)

ranking_pascal = task3.Ranker(pascal_triangle_printer)
ranking_quadratic = task3.Ranker(quadratic_equation_solver)
ranking_funh = task3.Ranker(funh)
ranking_fn = task3.Ranker(fn)
ranking_lambda = task3.Ranker(useless_lambda)

ranking_pascal(100)
ranking_quadratic(1, 5, 3)
ranking_funh(None, bar2="lol")
ranking_fn()
ranking_lambda(3)
task3.Ranker.print_ranking()

print("_" * 75)

print(
    "Checking task 4\n(Look for outputs in output.txt file, for logs in cases of exceptions - in exception.log file)"
)
protected_pascal = ProtectedClassDecorator1(pascal_triangle_printer)
protected_funh = ProtectedClassDecorator1(funh)
protected_quadratic = protected_decorator_1(quadratic_equation_solver)

protected_pascal("lol")
protected_pascal(4)
protected_funh()
protected_quadratic()
protected_quadratic(1, 5, 3)
