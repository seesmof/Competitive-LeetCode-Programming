class Factorial:
    def __init__(self, n) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a positive integer")
        self.n: int = n

    @staticmethod
    def recursive(n: int) -> int:
        if n < 2:
            return 1
        return n * Factorial.recursive(n - 1)

    def linear(self) -> int:
        product: int = 1
        for i in range(1, self.n + 1):
            product *= i
        return product
