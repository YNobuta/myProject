# Generated by Django 3.2.16 on 2023-01-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_whisky2_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhiskyBooze2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
    ]
