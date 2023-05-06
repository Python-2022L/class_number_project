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
        if self.value%2==1:
            return True
        else:
            return False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value%2==0:
            return True
        else:
            return False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        s = 2
        a = self.value
        for i in range(2,a):
            if a%i==0:
                s+=1
            elif s>2:
                break
        if s==2:
            return True
        else:
            return False
            
            
                    

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        s = []
        a = self.value
        for i in range(1,a+1):
            if a%i==0:
                s.append(i)
        return s
    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        a = []
        for i in str(self.value):
            if int(i) not in a:
                a.append(i)
        return len(a)
    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        s = 0
        for i in str(self.value):
            s+=int(i)
        return s

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        c = 0
        d = 1
        a = self.value
        while a>0:
            b = a%10
            a = (a-a%10)/10
            c = (c+b)*10
        return (c/10)

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        pass

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        pass

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        pass

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        pass

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

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
number = Number(3)
number = Number(455555555584)
print(number.get_reverse())