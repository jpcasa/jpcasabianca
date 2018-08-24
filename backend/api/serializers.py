from rest_framework import serializers

from . import models


class SubMenuItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Item Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.SubMenuItem
        fields = (
            'id',
            'title',
            'url',
            'action',
            'created_at',
            'modified_at',
        )
        read_only_fields = (
            'created_at',
            'modified_at',
        )


class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Item Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.MenuItem
        fields = (
            'id',
            'title',
            'url',
            'action',
            'sub_menu_items',
            'created_at',
            'modified_at',
        )
        read_only_fields = (
            'created_at',
            'modified_at',
        )


class MenuSerializer(serializers.ModelSerializer):
    """Serializer to map the Menu Model instance into JSON format."""
    menu_items = MenuItemSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Menu
        fields = (
            'owner',
            'id',
            'name',
            'menu_items',
            'created_at',
            'modified_at',
        )
        read_only_fields = (
            'created_at',
            'modified_at',
        )
