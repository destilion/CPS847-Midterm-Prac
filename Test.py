import unittest
from random import randint
from Sorter import RadixSorter

class TestHelperMethods(unittest.TestCase):

    def setUp(self):
        self.sorter = RadixSorter(10)

    def tearDown(self):
        del self.sorter

    def test_FloorLog_NormalInput_ReturnsNormal(self):
        self.assertEqual(self.sorter.floorLog(100), 2)

    def test_FloorLog_NegativeInput_RaisesError(self):
        with self.assertRaises(ValueError):
            self.sorter.floorLog(-78)

    def test_DigitLen_NormalInput_ReturnsNormal(self):
        self.assertEqual(self.sorter.floorLog(100), 2)

class TestMainMethods(unittest.TestCase):

    def setUp(self):
        self.sorter = RadixSorter(10)

    def tearDown(self):
        del self.sorter

    def test_RadixSort_NormalValues_ReturnsNormal(self):
        vals = []
        for i in range(10):
            vals.append(randint(-50000, 50000))
        self.assertEqual(len(vals), 10)
        result = self.sorter.radixSort(vals)
        self.assertTrue(all(result[i] <= result[i + 1] for i in range(len(result) - 1)))

    def test_RadixSort_NonIntegerValues_RaisesError(self):
        with self.assertRaises(TypeError):
            self.sorter.radixSort([2.5, 1.2, 3.7, 6.9, 3.2])

if __name__ == '__main__':
    unittest.main(verbosity=2)
