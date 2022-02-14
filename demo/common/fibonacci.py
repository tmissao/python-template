def get_fibonacci(num: int) -> int:
    if num in (1, 2):
        return 1
    return get_fibonacci(num-1) + get_fibonacci(num-2)
