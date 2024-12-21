'''
Систематизация и пропуск тестов
Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи
встроенных в unittest декораторов.
'''
import unittest
import RunnerTest, TournamentTest

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
