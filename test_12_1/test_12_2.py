import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}


    def setUp(self):
        self.run_1 = rt.Runner('Усэйн', 10)
        self.run_2 = rt.Runner('Адрей', 9)
        self.run_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_result.values():
            print(i)

    def test_1(self):
        tour = rt.Tournament(90, self.run_1, self.run_3)
        self.all_result[1] = tour.start()
        a = self.all_result[1]
        self.assertTrue(a[len(a)] == self.run_3.name)

    def test_2(self):
        tour = rt.Tournament(90, self.run_2, self.run_3)
        self.all_result[2] = tour.start()
        a = self.all_result[2]
        self.assertTrue(a[len(a)] == self.run_3.name)


    def test_3(self):
        tour = rt.Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_result[3] = tour.start()
        a = self.all_result[3]
        self.assertTrue(a[len(a)] == self.run_3.name)
