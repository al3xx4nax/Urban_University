import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.walker = Runner("Alex")
        for _ in range(10):
            self.walker.walk()
        result = self.walker.distance
        self.assertEqual(result, 50)

    def test_run(self):
        self.runner = Runner("Denis")
        for _ in range(10):
            self.runner.run()
        result = self.runner.distance
        self.assertEqual(result,100)

    def test_challenge(self):
        self.runner = Runner("Denis")
        self.walker = Runner("Alex")
        self.runner.run(), self.walker.walk()
        result_1, result_2 = self.runner.distance, self.walker.distance
        self.assertNotEqual(result_1, result_2,)


if __name__ == "__main__":
    unittest.main()

