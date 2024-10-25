import logging
import unittest
import rt_with_exceptions as runner
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.run_1 = runner.Runner('Misha', -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                self.run_1.walk()
            self.assertEqual(self.run_1.distance, 50)

        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)



    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.run_2 = runner.Runner(5)
            for i in range(10):
                self.run_2.run()
            self.assertEqual(self.run_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_cellenge(self):
        self.run_3 = runner.Runner('Vlad')
        self.run_4 = runner.Runner('Dan')
        for i in range(10):
            self.run_3.walk()
            self.run_4.run()
        self.assertNotEqual(self.run_3.distance, self.run_4.distance)




logging.basicConfig(level=logging.INFO, filemode='w', filename='runner tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')


