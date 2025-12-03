import unittest
from main import Student  # Assuming 'Student' is defined in the 'main' module.

class TestStudent(unittest.TestCase):
    def test_gpa_range(self):
        s = Student("Алиса", 19, "IS-23", 3.7)  # Creating an instance of the Student class.
        self.assertTrue(0 <= s.gpa <= 4.0)  # Checking if GPA is within a valid range (0.0 to 4.0).

if __name__ == "__main__":
    unittest.main()  # Running the tests if this file is executed directly.
