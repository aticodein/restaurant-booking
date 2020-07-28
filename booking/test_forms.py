from django.test import TestCase
from .forms import bookingItemForm

# Create your tests here.


class TestbookingItemForm(TestCase):

    def test_bookingItem_name_is_required(self):
        form = bookingItemForm({'name': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_bookingItem_date_is_required(self):
        form = bookingItemForm({'date': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')
