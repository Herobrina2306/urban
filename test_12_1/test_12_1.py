import unittest
import runner
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.run_1 = runner.Runner('Misha')
        for i in range(10):
            self.run_1.walk()
        self.assertEqual(self.run_1.distance, 50)

    def test_run(self):
        self.run_2 = runner.Runner('Dave')
        for i in range(10):
            self.run_2.run()
        self.assertEqual(self.run_2.distance, 100)

    def test_cellenge(self):
        self.run_3 = runner.Runner('Vlad')
        self.run_4 = runner.Runner('Dan')
        for i in range(10):
            self.run_3.walk()
            self.run_4.run()
        self.assertNotEqual(self.run_3.distance, self.run_4.distance)
