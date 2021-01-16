class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        self.cases = ('string',  1.5)
        for c in self.cases:
            with self.subTest(x = c):
                self.assertRaises(TypeError, factorize, c)

    def test_negative(self):

        self.cases = (-1, -10, -100)
        for c in self.cases:
            with self.subTest(x = c):
                self.assertRaises(ValueError, factorize, c)

    def test_zero_and_one_cases(self):

        self.cases = (0, 1)

        for case in (self.cases):
            with self.subTest(x = case):
                self.assertEqual(factorize(case),(case,))

    def test_simple_numbers(self):
        self.cases = (3, 13,29)
        for case in (self.cases):
            with self.subTest(x = case):
                self.assertEqual(factorize(case),(case,))

    def test_two_simple_multipliers(self):

        self.cases = (6, 26,121)
        exp = ((2,3), (2,13), (11,11))
        for i, case in enumerate(self.cases):
            with self.subTest(x = case):
                self.assertEqual(factorize(case),exp[i])

    def test_many_multipliers(self):
        self.cases = (1001, 9699690)
        exp = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for i, case in enumerate(self.cases):
            with self.subTest(x = case):
                self.assertEqual(factorize(case),exp[i])
