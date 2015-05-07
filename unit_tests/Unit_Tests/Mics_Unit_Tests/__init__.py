from unittest.suite import TestSuite
import unittest


def load_tests(loader, tests, pattern):
    
    
    suite = TestSuite()
    for test_suites in unittest.defaultTestLoader.discover('.', 
                                                           pattern='test_*'):
        for test_suite in test_suites:
            suite.addTest(test_suite)
    return suite


if __name__ == "__main__":
    unittest.main()
    