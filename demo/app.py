from .common.fibonacci import Fibonacci


def run():
    fibonacci = Fibonacci()
    print('Hello from python!')
    print(fibonacci.get_random_fibonacci())
    print(fibonacci.get_multiple_random_fibonacci())
    return fibonacci.get_fibonacci(8)
