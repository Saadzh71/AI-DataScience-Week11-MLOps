import os
import sys
import unittest

# Set the path to include the top-level directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Automatically discover and run tests
if __name__ == '__main__':
    tests = unittest.defaultTestLoader.discover('.', pattern='test_*.py')
    unittest.TextTestRunner().run(tests)
