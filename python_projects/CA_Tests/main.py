# Write your code below:
import surfshop
import unittest
import datetime


class Test(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                self.assertEqual(self.cart.add_surfboards(i), f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    #    def test_add_surfboards(self):
#        self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')

    @unittest.skip
    def test_too_many_boards_raised(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    def test_apply_locals_discount(self):
        self.assertTrue(self.cart.apply_locals_discount())


unittest.main()
