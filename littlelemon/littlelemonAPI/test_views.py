from django.test import TestCase
from .views import MenuItem
from .serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.item1 = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title='Pizza', price=100, inventory=50)
    def test_getall(self):
        all_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(all_items, many=True)
        json_items = "[OrderedDict([('id', 2), ('title', 'IceCream'), ('price', '80.00'), ('inventory', 100)]), OrderedDict([('id', 3), ('title', 'Pizza'), ('price', '100.00'), ('inventory', 50)])]"
        self.assertEqual(str(serializer.data), json_items)