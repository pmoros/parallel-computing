import threading
import unittest

from libs.increments import increment_shared_variable_race_condition
from libs.increments import increment_shared_variable


class TestRaceCondition(unittest.TestCase):
    def setUp(self) -> None:
        global lock
        lock = threading.Lock()
        return super().setUp()

    def test_race_condition(self):
        # Initialize a shared variable with value 0
        shared_variable = [0]

        # Define two threads that both call the increment function
        thread1 = threading.Thread(
            target=increment_shared_variable_race_condition, args=(shared_variable,))
        thread2 = threading.Thread(
            target=increment_shared_variable_race_condition, args=(shared_variable,))

        # Start the threads and wait for them to complete
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        # Check that the shared variable has the expected value
        self.assertEqual(shared_variable[0], 200000)

    def test_no_race_condition(self):
        shared_variable = [0]

        # Define two threads that both call the increment function
        thread1 = threading.Thread(
            target=increment_shared_variable, args=(shared_variable, lock))
        thread2 = threading.Thread(
            target=increment_shared_variable, args=(shared_variable, lock))

        # Start the threads and wait for them to complete
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        # Check that the shared variable has the expected value
        self.assertEqual(shared_variable[0], 200000)
