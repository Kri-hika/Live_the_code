from django.db import models
# import os

class Config(models.Model):
  
    api_key = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200,choices = [("email","Email"),("phone_number_sms","Phone")])


# class Customize(models.Model):

class Info(models.Model):
    name = models.CharField( max_length=30)  # Field name made lowercase.
    email = models.EmailField(max_length=254) # field name for email in lowercase



