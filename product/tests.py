from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Category, Item

class CategoryModelTest(TestCase):
  def setUp(self):
    '''
    Test the creation of a new category
    '''
    Category.objects.create(name="Test Category")

  def test_category_str(self):
    category = Category.objects.get(name="Test Category")
    self.assertEqual(str(category), "Test Category")
