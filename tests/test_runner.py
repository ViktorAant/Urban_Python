'''
Лекция. Систематизация тестов
'''
import unittest
import test_for_runner, test_for_new_runner

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_for_runner.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_for_new_runner.NewRunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
