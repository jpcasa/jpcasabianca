from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from .. import models


class MenuViewTestCase(TestCase):
    """Test suite for the Menu api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="jpc")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.menu_data = {
            'owner': user.id,
            'name': 'Portfolio'
        }
        self.response_menu = self.client.post(
            reverse('ListCreateMenu'),
            self.menu_data,
            format="json"
        )

        self.menu_item_data = {
            'owner': user.id,
            'title': 'Design',
            'url': 'portfolio/design'
        }
        self.response_menu_item = self.client.post(
            reverse('ListCreateMenuItem'),
            self.menu_item_data,
            format="json"
        )

        self.sub_menu_item_data = {
            'owner': user.id,
            'title': 'ux',
            'url': 'portfolio/design/ux'
        }
        self.response_sub_menu_item = self.client.post(
            reverse('ListCreateSubMenuItem'),
            self.sub_menu_item_data,
            format="json"
        )


    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/menus/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_create_a_menu(self):
        """Test the api has menu creation capability."""
        self.assertEqual(
            self.response_menu.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_menu_item(self):
        """Test the api has menu item creation capability."""
        self.assertEqual(
            self.response_menu_item.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_create_a_sub_menu_item(self):
        """Test the api has sub menu item creation capability."""
        self.assertEqual(
            self.response_menu_item.status_code,
            status.HTTP_201_CREATED
        )


    def test_api_can_get_a_menu(self):
        """Test the api can get a given menu."""
        menu = models.Menu.objects.get()
        response = self.client.get(
            reverse(
                'MenuDetails',
                kwargs={'pk': menu.id}
            ), format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, menu)


    def test_api_can_update_menu(self):
        """Test the api can update a given menu."""
        menu = models.Menu.objects.get()
        change_menu = {
            'name': 'Resources'
        }
        response = self.client.put(
            reverse(
                'MenuDetails',
                kwargs={'pk': menu.id}
            ), change_menu, format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_menu(self):
        """Test the api can delete a menu."""
        menu = models.Menu.objects.get()
        response = self.client.delete(
            reverse(
                'MenuDetails',
                kwargs={'pk': menu.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_get_a_menu_item(self):
        """Test the api can get a given menu item."""
        menu_item = models.MenuItem.objects.get()
        response = self.client.get(
            reverse(
                'MenuItemDetails',
                kwargs={'pk': menu_item.id}
            ), format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, menu_item)


    def test_api_can_update_menu_item(self):
        """Test the api can update a given menu item."""
        menu_item = models.MenuItem.objects.get()
        change_menu_item = {
            'title': 'more',
            'url': 'more/stuff'
        }
        response = self.client.put(
            reverse(
                'MenuItemDetails',
                kwargs={'pk': menu_item.id}
            ), change_menu_item, format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_menu_item(self):
        """Test the api can delete a menu item."""
        menu_item = models.MenuItem.objects.get()
        response = self.client.delete(
            reverse(
                'MenuItemDetails',
                kwargs={'pk': menu_item.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_api_can_get_a_sub_menu_item(self):
        """Test the api can get a given sub menu item."""
        sub_menu_item = models.SubMenuItem.objects.get()
        response = self.client.get(
            reverse(
                'SubMenuItemDetails',
                kwargs={'pk': sub_menu_item.id}
            ), format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertContains(response, sub_menu_item)


    def test_api_can_update_sub_menu_item(self):
        """Test the api can update a given sub menu item."""
        sub_menu_item = models.SubMenuItem.objects.get()
        change_sub_menu_item = {
            'title': 'another',
            'url': 'more/another'
        }
        response = self.client.put(
            reverse(
                'SubMenuItemDetails',
                kwargs={'pk': sub_menu_item.id}
            ), change_sub_menu_item, format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_api_can_delete_sub_menu_item(self):
        """Test the api can delete a sub menu item."""
        sub_menu_item = models.SubMenuItem.objects.get()
        response = self.client.delete(
            reverse(
                'SubMenuItemDetails',
                kwargs={'pk': sub_menu_item.id}
            ), format='json', follow=True)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
