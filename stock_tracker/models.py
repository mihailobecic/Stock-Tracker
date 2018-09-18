# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# User Table



# Keeps Track of Users Portfolios
class Portfolios(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    portfolio_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('Stox-Home', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.portfolio_name

# Keeps Track of Stocks Within a Users Portfolio
class StockPortfolio(models.Model):
    portfolio_name = models.ForeignKey(Portfolios,on_delete=models.CASCADE)
    ticker = models.CharField(max_length=7)

    def get_absolute_url(self):
        return reverse('Portfolio', kwargs={'pk':self.pk})

    def __str__(self):
        return  self.ticker

# Historical Data of Stock Prices
class HistoricData(models.Model):
    stock_id = models.AutoField(primary_key=True)
    ticker = models.ForeignKey('TickerList', models.DO_NOTHING, db_column='ticker', blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historic_data'

# List of All Tickers
class TickerList(models.Model):
    ticker = models.CharField(primary_key=True, max_length=10)
    company_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ticker_list'
