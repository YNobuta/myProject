# Generated by Django 3.2.16 on 2023-01-18 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_holding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_currency', models.CharField(max_length=3)),
                ('rate', models.FloatField(default=1.0)),
                ('last_update_time', models.DateTimeField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0)),
                ('buy_date', models.DateField()),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.currency')),
            ],
        ),
    ]
