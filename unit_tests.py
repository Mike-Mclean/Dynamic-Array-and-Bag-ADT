import unittest
from dynamic_array import *
from bag_da import Bag

class Test_Bag_and_DA(unittest.TestCase):

    def setUp(self):
        self.da = DynamicArray()
        return super().setUp()


    def test_1(self):
        """Test for the resize function"""
        self.da.resize(8)
        self.assertEqual(self.da.get_capacity(), 8)
        self.da.resize(2)
        self.assertEqual(self.da.get_capacity(), 2)

    def test_2(self):
        """Test for the resize function"""
        for i in range(1, 9):
            self.da.append(i)
        self.da.resize(20)
        self.assertEqual(self.da.get_capacity(), 20)
        self.da.resize(8)
        self.assertEqual(self.da.get_capacity(), 8)
        self.da.resize(4)
        self.assertEqual(self.da.get_capacity(), 8)

    def test_3(self):
        """Test for insert at index function"""
        self.da.append(100)
        self.da.insert_at_index(0, 200)
        self.assertEqual(self.da.get_at_index(0), 200)
        self.da.insert_at_index(0, 300)
        self.assertEqual(self.da.get_at_index(0), 300)
        self.da.insert_at_index(0, 400)
        self.assertEqual(self.da.get_at_index(0), 400)
        self.da.insert_at_index(3, 500)
        self.assertEqual(self.da.get_at_index(3), 500)
        self.da.insert_at_index(1, 600)
        self.assertEqual(self.da.get_at_index(1), 600)

    def test_4(self):
        """Test for insert at index"""
        with self.assertRaises(DynamicArrayException):
            self.da.insert_at_index(-1, 100)

    def test_5(self):
        """Test for remove at index"""
        for i in range(10, 90, 10):
            self.da.append(i)
        self.da.remove_at_index(0)
        self.assertNotEqual(self.da.get_at_index(0), 10)
        self.da.remove_at_index(6)
        with self.assertRaises(DynamicArrayException):
            self.da.get_at_index(6)

    def test_6(self):
        """Test for remove at index"""
        for i in range(1, 6):
            self.da.append(i)

        for _ in range(1, 5):
            self.da.remove_at_index(0)
            self.assertNotEqual(self.da.get_at_index(0), _)

        self.da.remove_at_index(0)
        with self.assertRaises(DynamicArrayException):
            self.da.get_at_index(0)

    def test_7(self):
        """Test for slice"""
        for i in range(1, 10):
            self.da.append(i)
        new_da = self.da.slice(1 ,3)
        for x in range(3):
            self.assertEqual(new_da.get_at_index(x), self.da.get_at_index(x + 1))

    def test_8(self):
        """Test for merge"""
        for i in range(1, 6):
            self.da.append(i)
        da2 = DynamicArray([10, 11, 12, 13])
        self.da.merge(da2)
        final_da = DynamicArray([1, 2, 3, 4, 5, 10, 11, 12, 13])
        for x in range(9):
            self.assertEqual(self.da.get_at_index(x), final_da.get_at_index(x))


    def test_9(self):
        """Test for reduce"""
        values = [100, 5, 10, 15, 20, 25]
        for value in values:
            self.da.append(value)
        self.assertEqual(self.da.reduce(lambda x, y: (x // 5 + y ** 2)), 714)
        self.assertEqual(self.da.reduce(lambda x, y: (x + y ** 2), -1), 11374)

    def test_10(self):
        """Test for bag.equal"""
        bag1 = Bag([10, 20, 30, 40, 50, 60])
        bag2 = Bag([60, 50, 40, 30, 20, 10])
        bag3 = Bag([10, 20, 30, 40, 50])

        self.assertTrue(bag1.equal(bag2))
        self.assertTrue(bag2.equal(bag1))
        self.assertFalse(bag1.equal(bag3))
        self.assertFalse(bag3.equal(bag1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
