from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):

    def testAddTwoNums(self):

        result = calc.add(5, 2)

        self.assertEqual(result, 7)
