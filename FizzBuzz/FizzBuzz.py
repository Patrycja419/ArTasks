class FizzBuzz:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def validate(self):
        if self.m < 1000 and self.n > 1 and self.n < self.m:
            return True
        else:
            raise ValueError('enter correct values')

    def fizzBuzzFunction(self):
        for num in range(self.n, self.m + 1):
            modulo = lambda numFunc: False if num % numFunc else True
            print('.'.join(
                ['Fizz' * modulo(3) or 'Buzz' * modulo(5) or 'FizzBuzz' * (modulo(3) and modulo(5)) or str(num)]))


assignClassVariable = FizzBuzz(5, 151)
if assignClassVariable.validate():
    print(assignClassVariable.fizzBuzzFunction())
