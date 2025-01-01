'''
Простые Юнит-Тесты
Цель: приобрести навык создания простейших Юнит-тестов
'''
import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.runner = Runner('somename')
        for i in range(10):
            self.runner.walk()
        self.assertEqual(50, self.runner.distance)

    def test_run(self):
        self.runner = Runner('somename')
        for i in range(10):
            self.runner.run()
        self.assertEqual(100, self.runner.distance)

    def test_challenge(self):
        self.first_runner = Runner('first_runner')
        self.second_runner = Runner('second_runner')
        for i in range(10):
            self.first_runner.run()
            self.second_runner.walk()
        self.assertNotEqual(self.second_runner.distance, self.first_runner.distance)


if __name__ == "__main__":
    unittest.main()
