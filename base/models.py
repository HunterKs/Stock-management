from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.files import File
import uuid
from datetime import datetime
# import secrets
# import qrcode
# import random
# # from PIL import Image, ImageDraw
# from io import BytesIO

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
class Company(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length=400)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.name





class Tyre(models.Model):
     name = models.CharField(max_length=300) 
     size = models.TextField(default="145/80/12")
     Quantity_total = models.IntegerField(default=0)
     Quantity_sold =  models.IntegerField(default=0)
     price = models.IntegerField(default = 0)
     company = models.CharField(max_length=400)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)
     initial_price = models.IntegerField(default=1500)

     class Meta:
          unique_together = ('name','size')

     def save(self,*args,**kwargs):
          try:
               company = Company.objects.get(name = self.name)
          except Company.DoesNotExist:
               pass
          super().save(*args,**kwargs)
     def instock(self):
          return self.Quantity_total - self.Quantity_sold
     def Totalinstock(self):
          return self.Quantity_total + self.Quantity_sold
     def TotalNo_Tyres(cls):
          result = cls.objects.aggregate(sum_of_attribute=models.sum('Totalinstock'))
          sum_of_attribute = result['sum_of_attribute'] or 0
          return sum_of_attribute
     def calculate_total_profit(self):
        return (self.Quantity_sold * self.price) - (self.Quantity_sold * self.initial_price)
     
     def __str__(self):
          return self.name
     
    




class Customer(models.Model):
    
     name =  models.CharField(max_length=300)
     mobile_number =  models.CharField(max_length=10)
     Email = models.EmailField()
     # order history
     def __str__(self):
          return self.name


class Order(models.Model):
      order_id = models.UUIDField(default = uuid.uuid4, editable=False, unique=True)
      customer_name = models.CharField(max_length = 300, default = "abc" )
      customer_mobile_number =  models.CharField(max_length=10,default= 0)
      Items = models.IntegerField(default=1) 
      tyre = models.CharField(max_length=300, blank= True) 
      size = models.TextField(default=0, blank = True)
      quantity = models.IntegerField(default=0)
      price = models.IntegerField(default=0)
      created = models.DateTimeField(auto_now_add=True)
      initial_price = models.IntegerField(default=1500)
      amount =  models.IntegerField(default=0)
 
      def __str__(self):
         return self.customer_name
      class Meta:
           ordering = ['-created']
      def save(self,*args,**kwargs):
         
          try:
               tyre = Tyre.objects.get(name = self.tyre,size = self.size)
               tyre_new_Quantity = tyre.Quantity_sold + self.quantity
               if tyre_new_Quantity > tyre.Quantity_total:
                    raise ValidationError('not enough stock availabe for this tyre')
               
               tyre.Quantity_sold = tyre_new_Quantity
               # tyre.Quantity_sold += self.quantity
               tyre.save()
               
          except Tyre.DoesNotExist:
               pass
          super().save(*args,**kwargs)

      
      def Amount(self):
          return   self.price * self.quantity
  
     


class Status(models.Model): 
     tyres = models.ForeignKey(Tyre, on_delete= models.CASCADE)
     
     def __str__(self):
         return self.name 


class Scanner(models.Model):
    code = models.CharField(max_length=10, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
     
    
class DailyProfit(models.Model):
      tyre = models.ForeignKey('Tyre', on_delete=models.CASCADE)
     #  order= models.ForeignKey('Order', on_delete=models.CASCADE)
      date = models.DateField()
      daily_profit = models.IntegerField(default=0)

      def __str__(self):
        return f"{self.date} - {self.tyre.name}"          