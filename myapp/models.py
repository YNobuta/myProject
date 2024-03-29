from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Currency(models.Model):
    iso = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)
    def __repr__(self):
        return self.iso + " " + self.long_name
    def __str__(self):
        return self.iso + " " + self.long_name

class Holding(models.Model):
    iso = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    buy_date = models.DateField()

    def __repr__(self):
            return self.iso.iso + " " + str(self.value) + " " + str(self.buy_date)

    def __str__(self):
        return self.iso.long_name + " " + str(self.value) + " " + str(self.buy_date)

class Rates(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    x_currency = models.CharField(max_length=3)
    rate = models.FloatField(default=1.0)
    last_update_time = models.DateTimeField()

    def __repr__(self):

        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)

    def __str__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)

class Whisky(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __repr__(self):
        return self.item_name + " " + self.price

    def __str__(self):
        return self.item_name + " " + self.price

class WhiskyBooze(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __repr__(self):
        return self.item_name + " " + self.price

    def __str__(self):
        return self.item_name + " " + self.price

class AccountHolder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    currencies_visited = models.ManyToManyField(Currency)
    def __str__(self):
        return self.user.username
    def __repr__(self):
        return self.user.username

class Whisky2(models.Model):
    item_name = models.CharField(max_length=300)
    price = models.CharField(max_length=10)
    url = models.CharField(max_length=300)

    def __repr__(self):
        return self.item_name + " " + self.price + " " + self.url

    def __str__(self):
        return self.item_name + " " + self.price + " " + self.url

class WhiskyBooze2(models.Model):
    item_name = models.CharField(max_length=300,default="")
    price = models.CharField(max_length=20,default=0)
    url = models.CharField(max_length=300,default="")

    def __repr__(self):
        return self.item_name + " " + self.price + " " + self.url

    def __str__(self):
        return self.item_name + " " + self.price + " " + self.url