import unittest
from tutorial import *
from mock import patch, Mock

class TestBasicCommands(unittest.TestCase):
    # Basic Assert Methods
    
    def test_assert_boolean(self):
        '''
        Evaluate boolean expressions
        '''
        # Can evaluate boolean expressions
        self.assertTrue(True)
        self.assertFalse(False)
        
    def test_assert_equality(self):
        '''
        Check that two expressions evaluate to the same value
        '''
        value1 = "workshop"
        value2 = "workshop"
        self.assertEqual(value1, value2)
        
    def test_assert_inequality(self):
        '''
        Check that two expressions evaluate to different values
        '''
        value1 = "workshop"
        value2 = "beginner"
        self.assertNotEqual(value1, value2)
    
    def test_assert_raises_exception(self):
        '''
        Check that an exception is raised
        '''
        with self.assertRaises(TypeError):
            a = "workshop" + 1
            
    # Other examples: assertIsInstance(), assertIs(), assertIsNone(), etc.
            
    # Marking tests as pending / skipping tests
    
    @unittest.skip("demonstrating skipping")
    def test_skipping(self):
        self.assertTrue(True)
        
class TestFixtures(unittest.TestCase):
    def setUp(self):
        print("Setting up the database")
        self.database = {
            1: "Jon Smith",
            2: "Katie Johnson",
            3: "Chris Armstrong"
        }
        
    def test_student_is_in_database(self):
        student_name = fetch_student(self.database, 1)
        self.assertEqual(student_name, "Jon Smith")
        
    def test_student_is_not_in_database(self):
        student_name = fetch_student(self.database, 4)
        self.assertEqual(student_name, None)
        
    def tearDown(self):
        print("Clearing the database")
        self.database = {}
        
class TestMocking(unittest.TestCase):
    # Patching
    
    @patch('tutorial.current_day_of_week')
    def test_saturday_is_weekend(self, today):
        today.return_value = "Saturday"
        self.assertTrue(today_is_weekend())
    
    @patch('tutorial.current_day_of_week')
    def test_tuesday_is_not_weekend(self, today):
        today.return_value = "Tuesday"
        self.assertFalse(today_is_weekend())
        
    # Mocking
    def test_student_has_enough_credits(self):
        student = Mock()
        student.total_credits = Mock(return_value=40)
        self.assertTrue(satisfied_requirements(student))
        
    def test_student_does_not_have_enough_credits(self):
        student = Mock()
        student.total_credits = Mock(return_value=14)
        self.assertFalse(satisfied_requirements(student))
        
if __name__ == '__main__':
    unittest.main()