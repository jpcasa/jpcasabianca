from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from . import views


urlpatterns = {
    path('auth/',
        include('rest_framework.urls',
        namespace='rest_framework')
    ),
    path(
        'menus/',
        views.ListCreateMenuView.as_view(),
        name="ListCreateMenu"
    ),
    path(
        'menus/<int:pk>/',
        views.MenuDetailsView.as_view(),
        name="MenuDetails"
    ),
    path(
        'menu-items/',
        views.ListCreateMenuItemView.as_view(),
        name="ListCreateMenuItem"
    ),
    path(
        'menu-items/<int:pk>/',
        views.MenuItemDetailsView.as_view(),
        name="MenuItemDetails"
    ),
    path(
        'sub-menu-items/',
        views.ListCreateSubMenuItemView.as_view(),
        name="ListCreateSubMenuItem"
    ),
    path(
        'sub-menu-items/<int:pk>/',
        views.SubMenuItemDetailsView.as_view(),
        name="SubMenuItemDetails"
    ),
    path(
        'get-token/',
        obtain_auth_token
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
