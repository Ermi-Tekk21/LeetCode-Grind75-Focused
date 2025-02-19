class ProductOfNumbers:
    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.products = []
        else:
            self.products.append(num * (self.products[-1] if self.products else 1))

    def getProduct(self, k: int) -> int:
        n = len(self.products)
        if n == 0 or k > n:
            return 0
        if k == n:
            return self.products[-1]
        return self.products[-1] // self.products[n - k - 1]