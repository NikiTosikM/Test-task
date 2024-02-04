# Generated by Django 4.2.1 on 2024-02-02 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Field name')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Submenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Field name')),
                ('url', models.CharField(blank=True, max_length=50, verbose_name='URL')),
                ('main_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_menu', to='Menu.mainmenu')),
                ('parent_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Menu.submenu')),
            ],
            options={
                'verbose_name': 'Menu items',
                'verbose_name_plural': 'Menu items',
                'ordering': ['id'],
            },
        ),
    ]