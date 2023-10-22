from .models import Item
from django.test import TestCase


class TestVModels(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)


def test_item_method_returns_name(self):
    item = Item.objects.create(name='Test Todo Item')
    self.assertEqual(str(item), 'Test Todo Item')
