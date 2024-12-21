'''
Методы Юнит-тестирования
Цель: освоить методы, которые содержит класс TestCase
'''
import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test in TournamentTest.all_results:
            print({k: v.name for k, v in test.items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first(self):
        tour = Tournament(90, self.runner1, self.runner3)
        results = tour.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == self.runner3.name,
                        f'Ожидали {self.runner3.name}, фактически имеем {results[2]}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second(self):
        tour = Tournament(90, self.runner2, self.runner3)
        results = tour.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == self.runner3.name,
                        f'Ожидали {self.runner3.name}, фактически имеем {results[2]}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tour.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3] == self.runner3.name,
                        f'Ожидали {self.runner3.name}, фактически имеем {results[3]}')

    # дополнительный тест
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_check_order_1_2(self):
        self.assertGreaterEqual(self.runner1.speed, self.runner2.speed,
                                f'Скорость первого бегуна должна быть не меньше скорости второго, фактически: {self.runner1.speed} и {self.runner2.speed}')

    # дополнительный тест
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_check_order_2_3(self):
        self.assertGreaterEqual(self.runner2.speed, self.runner3.speed,
                                f'Скорость второго бегуна должна быть не меньше скорости третьего, фактически: {self.runner2.speed} и {self.runner3.speed}')


if __name__ == '__main__':
    unittest.main()
