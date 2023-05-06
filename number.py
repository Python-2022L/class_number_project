class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return True if self.value%2 == 1 else False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return True if self.value%2 == 0 else False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        n = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                n += 1
        return False if n != 2 else True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        n = []
        for i in range(1, self.value + 1):
            if self.value%i == 0:
                n.append(i)
        return n

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        n = 0
        while self.value:
            self.value //= 10
            n += 1
        return n

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        n = 0
        while self.value:
            n += self.value % 10
            self.value //= 10
        return n

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.value == int(str(self.value)[::-1])

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return [int(i) for i in str(self.value)]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max([int(i) for i in str(self.value)])

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min([int(i) for i in str(self.value)])

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        n = [int(i) for i in str(self.value)]
        return sum(n)/len(n)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(1233748879237582379)
print(number.is_prime())