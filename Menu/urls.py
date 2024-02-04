from django.urls import path

from .views import main_menu_display, submenu_display


urlpatterns = [
    path('', main_menu_display, name='page_menu'),
    path('menu/<path:path>/', submenu_display , name='submenu')
]