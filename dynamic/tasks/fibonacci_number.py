
class FibonacciNumber:

    @staticmethod
    def calc_fibonacci_number(n):
        prev_fibonacci_numbers = {0:0, 1:1}
        for i in range(2,n+1):
            prev_fibonacci_numbers[i] = prev_fibonacci_numbers[i-1] + prev_fibonacci_numbers[i-2]
        return prev_fibonacci_numbers[n]

