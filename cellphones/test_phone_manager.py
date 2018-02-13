import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError, EmployeeError


class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        test_phone1 = Phone(1, 'Apple', 'iPhone 6')
        test_phone2 = Phone(2, 'Apple', 'iPhone 5')

        test_phones = [ test_phone1, test_phone2 ]

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)
        test_assignment_mgr.add_phone(test_phone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(test_phones, test_assignment_mgr.phones)

    def test_create_and_add_phone_with_duplicate_id(self):
        test_phone1 = Phone(1, 'Apple', 'iPhone 6')
        test_phone2 = Phone(1, 'Apple', 'iPhone 5')

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)

        with self.assertRaises(PhoneError):
            test_assignment_mgr.add_phone(test_phone2)

    def test_create_and_add_new_employee(self):
        test_assignment_mgr = PhoneAssignments()

        emp_1 = Employee(1, "Enoch Root")
        emp_2 = Employee(2, "Goto Dengo")
        emp_3 = Employee(3, "Randy Waterhouse")
        emp_4 = Employee(4, "Avi Halaby")

        test_assignment_mgr.add_employee(emp_1)
        test_assignment_mgr.add_employee(emp_2)
        test_assignment_mgr.add_employee(emp_3)
        test_assignment_mgr.add_employee(emp_4)

        self.assertTrue(emp_1 in test_assignment_mgr.employees)
        self.assertTrue(emp_2 in test_assignment_mgr.employees)
        self.assertTrue(emp_3 in test_assignment_mgr.employees)
        self.assertTrue(emp_4 in test_assignment_mgr.employees)

    def test_create_and_add_employee_with_duplicate_id(self):
        test_assignment_mgr = PhoneAssignments()

        emp_1 = Employee(1, "John Locke")
        emp_2 = Employee(1, "Jack Sheppard")

        test_assignment_mgr.add_employee(emp_1)
        with self.assertRaises(EmployeeError):
            test_assignment_mgr.add_employee(emp_2)

    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments

        self.fail()

    def test_assign_phone_that_has_already_been_assigned_to_employee(self):

        test_phone1 = Phone(1, 'Apple', 'iPhone 6')

        test_employee1 = Employee(1, "Dirk Gently")
        test_employee2 = Employee(1, "Aurthur Dent")

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)
        test_assignment_mgr.add_employee(test_employee1)

        test_assignment_mgr.assign(test_phone1.id, test_employee1)
        with self.assertRaises(PhoneError):
            test_assignment_mgr.assign(test_phone1.id, test_employee2)

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        self.fail()

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        test_phone1 = Phone(1, 'Apple', 'iPhone 6')
        test_employee1 = Employee(1, "Frank Gallagher")

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)
        test_assignment_mgr.add_employee(test_employee1)

        test_assignment_mgr.assign(test_phone1.id, test_employee1)
        # with self.assertRaises(PhoneError):
        try:
            test_assignment_mgr.assign(test_phone1.id, test_employee1)
        except PhoneError:
            self.fail()

    def test_un_assign_phone(self):

        test_phone1 = Phone(1, 'Apple', 'iPhone 6')

        test_employee1 = Employee(1, "Dirk Gently")

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)
        test_assignment_mgr.add_employee(test_employee1)

        test_assignment_mgr.assign(test_phone1.id, test_employee1)
        test_assignment_mgr.un_assign(test_phone1.id)

        self.assertIsNone(test_assignment_mgr.phones[0].employee_id)

    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

        self.fail()
