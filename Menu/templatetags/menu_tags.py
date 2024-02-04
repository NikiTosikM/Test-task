from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import MainMenu, Submenu



register = template.Library()


@register.inclusion_tag('Menu/menu.html')
def draw_menu(main_menu: str = None):
    main_menu = main_menu.split('/')

    menu_items = main_menu[-1]

    if len(main_menu) > 1:
        menu = [main_menu[0]]
        for item in main_menu[1:]:
            try:
                submenu = Submenu.objects.get(url=item)
                menu.append(submenu.name)
            except Submenu.DoesNotExist:
                menu.append(item)
        main_menu = menu
    else:
        main_menu = main_menu[0]

    if menu_items != main_menu:
        try:
            submenu = Submenu.objects.get(name=menu_items)
        except:
            submenu = Submenu.objects.get(url=menu_items)

        menu_items = Submenu.objects.filter(parent_menu=submenu)

        return {'main_menu': main_menu, 'menu_items': menu_items}
    else:
        main_menu = MainMenu.objects.get(name=main_menu)
        menu_items = Submenu.objects.filter(parent_menu=None, main_menu=main_menu)
    
        return {'main_menu': main_menu, 'menu_items': menu_items}