import unittest
import runner
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.run_1 = runner.Runner('Misha')
        for i in range(10):
            self.run_1.walk()
        self.assertEqual(self.run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.run_2 = runner.Runner('Dave')
        for i in range(10):
            self.run_2.run()
        self.assertEqual(self.run_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_cellenge(self):
        self.run_3 = runner.Runner('Vlad')
        self.run_4 = runner.Runner('Dan')
        for i in range(10):
            self.run_3.walk()
            self.run_4.run()
        self.assertNotEqual(self.run_3.distance, self.run_4.distance)


import runner_and_tournament as rt

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run_1 = rt.Runner('Усэйн', 10)
        self.run_2 = rt.Runner('Адрей', 9)
        self.run_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_result.values():
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tour = rt.Tournament(90, self.run_1, self.run_3)
        self.all_result[1] = tour.start()
        a = self.all_result[1]
        self.assertTrue(a[len(a)] == self.run_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tour = rt.Tournament(90, self.run_2, self.run_3)
        self.all_result[2] = tour.start()
        a = self.all_result[2]
        self.assertTrue(a[len(a)] == self.run_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tour = rt.Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_result[3] = tour.start()
        a = self.all_result[3]
        self.assertTrue(a[len(a)] == self.run_3.name)
