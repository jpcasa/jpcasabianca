from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class SubMenuItem(models.Model):
    """This class represents the Submenu Item model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='submenuitems',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    url = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    action = models.CharField(
        blank=False,
        max_length=100,
        default="push"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.title)


class MenuItem(models.Model):
    """This class represents the Menu Item model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='menuitems',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    url = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    action = models.CharField(
        max_length=100,
        default="push"
    )
    sub_menu_items = models.ManyToManyField(
        SubMenuItem,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.title)


class Menu(models.Model):
    """This class represents the Menu model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='menus',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        blank=False,
        max_length=100,
        unique=True
    )
    menu_items = models.ManyToManyField(
        MenuItem,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return readable representation of the model instance."""
        return "{}".format(self.name)


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

        
