# Generated by Django 3.2.16 on 2023-01-21 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_whiskybooze2_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whiskybooze2',
            name='item_name',
        ),
    ]
