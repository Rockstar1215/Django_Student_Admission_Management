import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            student_number=random.randint(10000, 99999),
            first_name='Vikram',
            last_name='Poojary',
            email='vikram.21cs067@sode-edu.in',
            field_of_study='Computer Science',
            gpa=9322445891
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
