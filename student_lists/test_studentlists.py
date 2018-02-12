'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase


class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_and_remove_student(self):
        student = "Ben Sisko"
        test_class = ClassList(2)
        test_class.add_student(student)
        test_class.remove_student(student)
        self.assertNotIn(student, test_class.class_list)

    def test_remove_student_not_in_list(self):
        student_a = "Ben Sisko"
        student_b = "Kira Nerys"
        student_c = "Gul Dukat"
        test_class = ClassList(2)
        test_class.add_student(student_a)
        test_class.add_student(student_b)
        with self.assertRaises(StudentError):
            test_class.remove_student(student_c)

    def test_remove_student_not_from_empty_list(self):
        student = "Aurthur Dent"
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student(student)

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_if_student_not_in_class_is_enrolled(self):
        student_a = "Ben Sisko"
        student_b = "Kira Nerys"
        student_c = "Gul Dukat"
        student_d = "Aurthur Dent"
        test_class = ClassList(2)
        test_class.add_student(student_a)
        test_class.add_student(student_b)
        test_class.add_student(student_c)
        self.assertFalse(test_class.is_enrolled(student_d))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_index_of_student_is_None_when_not_in_list_and_list_is_empty(self):
        test_class = ClassList(3)
        student = "John Doe"
        self.assertIsNone(test_class.index_of_student(student))

    def test_index_of_student_is_None_when_not_in_list(self):
        test_class = ClassList(3)
        student_a = "Jain Doe"
        student_b = "John Doe"
        test_class.add_student(student_a)
        self.assertIsNone(test_class.index_of_student(student_b))

    def test_is_class_full_returns_true_when_class_is_full(self):
        test_class = ClassList(3)
        student_a = "Michael Burnham"
        student_b = "Philippa Georgiou"
        student_c = "Gabriel Lorca"
        test_class.add_student(student_a)
        test_class.add_student(student_b)
        test_class.add_student(student_c)
        self.assertTrue(test_class.is_class_full())

    def test_is_class_full_returns_false_when_class_is_empty_or_not_full(self):
        test_class = ClassList(3)
        student_a = "Michael Burnham"
        student_b = "Philippa Georgiou"
        self.assertFalse(test_class.is_class_full())
        test_class.add_student(student_a)
        test_class.add_student(student_b)
        self.assertFalse(test_class.is_class_full())
