from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuView

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="Rice", price=100, inventory=210)
        item1 = Menu.objects.create(title="Beans", price=10, inventory=310)

    def test_getall(self):
        all_item_test = Menu.objects.all()
        all_item = MenuView().queryset
        self.assertEqual(all_item, all_item_test)
