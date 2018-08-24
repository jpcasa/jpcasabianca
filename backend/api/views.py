from django.shortcuts import render
from rest_framework import generics, permissions

from . import serializers
from . import models
from .permissions import IsOwner


class ListCreateMenuView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new menu."""
        serializer.save(owner=self.request.user)


class MenuDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )


class ListCreateMenuItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new menu item."""
        serializer.save()


class MenuItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListCreateSubMenuItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = models.SubMenuItem.objects.all()
    serializer_class = serializers.SubMenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new menu item."""
        serializer.save()


class SubMenuItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = models.SubMenuItem.objects.all()
    serializer_class = serializers.SubMenuItemSerializer
    permission_classes = (permissions.IsAuthenticated,)
