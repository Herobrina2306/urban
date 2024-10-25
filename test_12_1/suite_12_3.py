import unittest
import tests_12_3

ranST = unittest.TestSuite()
ranST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ranST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ranST)
