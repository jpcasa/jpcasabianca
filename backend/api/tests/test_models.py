from django.test import TestCase
from django.contrib.auth.models import User

from .. import models


class MenuModelTestCase(TestCase):
    """This class defines the test suite for the Menu model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.name = "Main Menu"
        self.menu = models.Menu(
            name=self.name,
            owner=user
        )

        self.title = "About Me"
        self.menu_item = models.MenuItem(
            title=self.title,
            owner=user
        )

        self.sub_title = "Short Bio"
        self.sub_menu_item = models.SubMenuItem(
            title=self.sub_title,
            owner=user
        )


    def test_model_can_create_a_menu(self):
        """Test the Menu model can create a menu."""
        old_count = models.Menu.objects.count()
        self.menu.save()
        new_count = models.Menu.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_model_can_create_a_menu_item(self):
        """Test the MenuItem model can create a menu item."""
        old_count = models.MenuItem.objects.count()
        self.menu_item.save()
        new_count = models.MenuItem.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_model_can_create_a_sub_menu_item(self):
        """Test the SubMenuItem model can create a submenu item."""
        old_count = models.SubMenuItem.objects.count()
        self.sub_menu_item.save()
        new_count = models.SubMenuItem.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_menu_can_add_item(self):
        """Test the Menu model can add a menu item."""
        self.menu.save()
        self.menu_item.save()
        old_count = self.menu.menu_items.count()
        self.menu.menu_items.add(self.menu_item)
        new_count = self.menu.menu_items.count()
        self.assertNotEqual(old_count, new_count)


    def test_menu_item_can_add_a_sub_item(self):
        """Test the Menu model can add a sub menu item."""
        self.menu_item.save()
        self.sub_menu_item.save()
        old_count = self.menu_item.sub_menu_items.count()
        self.menu_item.sub_menu_items.add(self.sub_menu_item)
        new_count = self.menu_item.sub_menu_items.count()
        self.assertNotEqual(old_count, new_count)


class Test(TestCase):
    """Example Test."""

    def test_something(self):
        """Test Something."""
        self.assertEqual(0, 0, 'message')
