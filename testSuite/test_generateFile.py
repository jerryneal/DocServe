import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        #Clean up after tests
        pass

if __name__ == '__main__':
    unittest.main()
