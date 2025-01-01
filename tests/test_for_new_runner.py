'''
Простые Юнит-Тесты
Цель: приобрести навык создания простейших Юнит-тестов
'''
import unittest
from runner import Runner

class NewRunnerTest(unittest.TestCase):
    def test_pi(self):
        self.runner = Runner('somename')
        self.assertEqual(3.14, self.runner.pi())


if __name__ == "__main__":
    unittest.main()
