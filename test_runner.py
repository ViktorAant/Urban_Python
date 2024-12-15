import unittest
import test_12_1

calcST = unittest.TestSuite()
# calcST.addTest(unittest.makeSuite(test_12_1.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
