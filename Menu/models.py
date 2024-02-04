from django.db import models

# Create your models here.
class MainMenu(models.Model):
    name = models.CharField(verbose_name='Field name', max_length=100, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self) -> str:
        return self.name


class Submenu(models.Model):
    name = models.CharField(verbose_name='Field name', max_length=100)
    url = models.CharField(verbose_name='URL', max_length=50, blank=True)
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, related_name='items_menu')

    class Meta:
        ordering = ['id']
        verbose_name = 'Menu items'
        verbose_name_plural = 'Menu items'

    def __str__(self) -> str:
        return self.name