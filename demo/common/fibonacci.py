import random
from typing import List


class Fibonacci:

    def get_fibonacci(self, num: int) -> int:
        if num < 0:
            raise ValueError('The Fibonacci Number cannot be negative')
        if num == 0:
            return 0
        if num in (1, 2):
            return 1
        return self.get_fibonacci(num-1) + self.get_fibonacci(num-2)

    def get_random_fibonacci(self) -> int:
        random_num = random.randrange(1, 20)
        return random_num, self.get_fibonacci(random_num)

    def get_multiple_random_fibonacci(self) -> List[int]:
        fibonacci_numbers = random.randrange(1, 5)
        result = []
        for _ in range(fibonacci_numbers):
            random_num = random.randrange(1, 20)
            result.append((random_num, self.get_fibonacci(random_num)))
        return result
