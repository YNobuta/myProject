# Generated by Django 3.2.16 on 2023-01-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_holding_rates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whisky_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=1.0)),
            ],
        ),
    ]
