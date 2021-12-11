import unittest


def run_suite(path):
    loader = unittest.TestLoader()
    tests = loader.discover(path)
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    run_suite("tests")
