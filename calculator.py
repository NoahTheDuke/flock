import unittest

from numbers import Number


class Calculator:
    """Simple calculator for the four basic arithmetic operations

    Technically, these could be static methods, but for the purposes of extensibility, I think it's better to leave them
    as instance methods so that when new functionality arises, an instance will already be available for use.
    """

    def add(self, *args, silent=False):
        """Return the sum of provided numbers.

        If silent, ignores any non-numeric elements.
        """
        if not silent:
            return sum(args)

        total = 0
        for num in args:
            try:
                total += num
            except TypeError as ex:
                pass
        return total

    def subtract(self, *args, silent=False):
        """Return the difference of provided numbers.

        Initial value is first element, and all following elements are subtracted from it.
        If silent, ignores any non-numeric elements.
        """
        it_args = iter(args)

        total = next(it_args)
        for num in it_args:
            try:
                total -= num
            except TypeError as ex:
                if not silent:
                    raise ex
        return total

    def multiply(self, *args, silent=False):
        """Return the product of provided numbers.

        If silent, ignores any non-numeric elements.
        """
        it_args = iter(args)

        total = next(it_args)
        for num in it_args:
            if isinstance(num, Number):
                total *= num
            else:
                if not silent:
                    raise TypeError
        return total

    def divide(self, *args, silent=False):
        """Return the quotient of provided numbers.

        If silent, ignores any non-numeric elements.
        """
        it_args = iter(args)

        total = next(it_args)
        for num in it_args:
            if isinstance(num, Number):
                total /= num
            else:
                if not silent:
                    raise TypeError
        return total


class TestCalculatorMethods(unittest.TestCase):
    """Simple test cases for Calculator class.

    Sets up a new instance of Calculator, and then tries most every combination. Current issues: subtraction,
    multiplication, and division can't handle initial strings.
    """

    def setUp(self):
        self.calc = Calculator()

    # add
    def test_add_positive_number_to_positive(self):
        test_case = [2, 2]
        result = self.calc.add(*test_case)
        self.assertEqual(4, result)

    def test_add_positive_number_to_negative(self):
        test_case = [2, -2]
        result = self.calc.add(*test_case)
        self.assertEqual(0, result)

    def test_add_negative_number_to_positive(self):
        test_case = [-2, 2]
        result = self.calc.add(*test_case)
        self.assertEqual(0, result)

    def test_add_negative_number_to_negative(self):
        test_case = [-2, -2]
        result = self.calc.add(*test_case)
        self.assertEqual(-4, result)

    def test_add_numbers_and_string_error(self):
        test_case = [2, 2, '2']
        with self.assertRaises(TypeError):
            self.calc.add(*test_case)

    def test_add_numbers_and_string_silent(self):
        test_case = [2, 2, '2']
        result = self.calc.add(*test_case, silent=True)
        self.assertEqual(4, result)

    # subtract
    def test_subtract_positive_number_from_positive(self):
        test_case = [10, 3]
        result = self.calc.subtract(*test_case)
        self.assertEqual(7, result)

    def test_subtract_negative_number_from_positive(self):
        test_case = [10, -3]
        result = self.calc.subtract(*test_case)
        self.assertEqual(13, result)

    def test_subtract_positive_number_from_negative(self):
        test_case = [10, -3]
        result = self.calc.subtract(*test_case)
        self.assertEqual(13, result)

    def test_subtract_negative_number_from_negative(self):
        test_case = [-10, -3]
        result = self.calc.subtract(*test_case)
        self.assertEqual(-7, result)

    def test_subtract_numbers_and_string_error(self):
        test_case = [10, 3, '3']
        with self.assertRaises(TypeError):
            self.calc.subtract(*test_case)

    def test_subtract_numbers_and_string_silent(self):
        test_case = [10, 3, '3']
        result = self.calc.subtract(*test_case, silent=True)
        self.assertEqual(7, result)

    # multipy
    def test_multiply_positive_number_with_positive(self):
        test_case = [2, 10]
        result = self.calc.multiply(*test_case)
        self.assertEqual(20, result)

    def test_multiply_positive_number_with_negative(self):
        test_case = [2, -10]
        result = self.calc.multiply(*test_case)
        self.assertEqual(-20, result)

    def test_multiply_negative_number_with_positive(self):
        test_case = [-2, 10]
        result = self.calc.multiply(*test_case)
        self.assertEqual(-20, result)

    def test_multiply_negative_number_with_negative(self):
        test_case = [-2, -10]
        result = self.calc.multiply(*test_case)
        self.assertEqual(20, result)

    def test_multiply_numbers_and_string_error(self):
        test_case = [2, 10, '10']
        with self.assertRaises(TypeError):
            self.calc.multiply(*test_case)

    def test_multiply_numbers_and_string_silent(self):
        test_case = [2, 10, '10']
        result = self.calc.multiply(*test_case, silent=True)
        self.assertEqual(20, result)

    # divide
    def test_divide_positive_number_with_positive(self):
        test_case = [20, 10]
        result = self.calc.divide(*test_case)
        self.assertEqual(2.0, result)

    def test_divide_positive_number_with_negative(self):
        test_case = [20, -10]
        result = self.calc.divide(*test_case)
        self.assertEqual(-2.0, result)

    def test_divide_negative_number_with_positive(self):
        test_case = [-20, 10]
        result = self.calc.divide(*test_case)
        self.assertEqual(-2.0, result)

    def test_divide_negative_number_with_negative(self):
        test_case = [-20, -10]
        result = self.calc.divide(*test_case)
        self.assertEqual(2.0, result)

    def test_divide_any_number_by_zero(self):
        test_case = [20, 0]
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(*test_case)

    def test_divide_numbers_and_string_error(self):
        test_case = [20, 10, '10']
        with self.assertRaises(TypeError):
            self.calc.divide(*test_case)

    def test_divide_numbers_and_string_silent(self):
        test_case = [20, 10, '10']
        result = self.calc.divide(*test_case, silent=True)
        self.assertEqual(2.0, result)


if __name__ == '__main__':
    unittest.main()
