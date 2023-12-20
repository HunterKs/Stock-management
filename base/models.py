from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.files import File
import uuid
from datetime import datetime
import secrets
import qrcode
import random
from PIL import Image, ImageDraw
from io import BytesIO

# Create your models here.
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
     # size_width = models.IntegerField(default=0)
     # size_depth = models.IntegerField(default=0)
     Quantity_total = models.IntegerField(default=0)
     Quantity_sold =  models.IntegerField(default=0)
     price = models.IntegerField(default = 0)
     company = models.CharField(max_length=400)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)

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
     #  Items = models.IntegerField(default=1)
     #  size_width = models.IntegerField(default=0,blank= True)
     #  size_depth = models.IntegerField(default=0,blank= True)
      quantity = models.IntegerField(default=0)
      price = models.IntegerField(default=0)
      created = models.DateTimeField(auto_now_add=True)
      # tyre name , size, price , Quantity, amount
      # order date and time 
     #  scanner_code = models.CharField(max_length=10, unique=True, default="DEFAULT")
     #  qr_code = models.ImageField(blank=True, null=True,upload_to='qr_codes')
      def __str__(self):
         return self.customer_name
      class Meta:
           ordering = ['-created']
      def save(self,*args,**kwargs):
          # qrcode_img = qrcode.make(self.order_id)
          # canvas = Image.new('RGB',(290,290),'white')
          # draw = ImageDraw.Draw(canvas) 
          # canvas.paste(qrcode_img)
          # fname = f'qr_code-{self.order_id}.png'
          # buffer = BytesIO()
          # canvas.save(buffer,'PNG')
          # self.qr_code.save(fname,File(buffer),save=True)
          # canvas.close()
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
     #  def generate_qr_code_content(self):
     #    unique_string = str(uuid.uuid4())  # Generate a unique string
     #    timestamp = datetime.now().timestamp()  # Get the current timestamp
     #    return f'Order ID: {self.id}, Unique: {unique_string}, Timestamp: {timestamp}'

     #  def generate_qr_code(self):
     #    qr = qrcode.QRCode(
     #        version=1,
     #        error_correction=qrcode.constants.ERROR_CORRECT_L,
     #        box_size=10,
     #        border=4,
     #    )
     #    qr.add_data(self.generate_qr_code_content())
     #    qr.make(fit=True)
     #    img = qr.make_image(fill_color="black", back_color="white")
     #    img.save(self.qr_code.path, "PNG")

     #  def generate_qr_code(self):
     #    # Create a QR code instance
     #    qr = qrcode.QRCode(
     #        version=1,
     #        error_correction=qrcode.constants.ERROR_CORRECT_L,
     #        box_size=10,
     #        border=4,
     #    )

     #    # Add data to the QR code (in this case, the invoice ID)
     #    qr.add_data(str(self.id))
     #    qr.make(fit=True)

     #    # Create an image from the QR code
     #    img = qr.make_image(fill_color="black", back_color="white")

     #    # Save the image to a BytesIO object
     #    img_buffer = BytesIO()
     #    img.save(img_buffer)
     #    img_buffer.seek(0)

     #    return img_buffer

     #  def save(self, *args, **kwargs):
     #    super().save(*args, **kwargs)
     #    if not self.qr_code:
     #        self.generate_qr_code()
      
     #  def generate_scanner_code():
     #    # Generate a random 10-character scanner code
     #    return secrets.token_hex(5)
     #  def save(self,*args,**kwargs):
     #        while not self.order_id:
     #        # Generate a random 6-digit order ID
     #         order_id = ''.join(random.choice('0123456789') for _ in range(6))

     #        # Check if the order ID already exists in the database
     #        if not Order.objects.filter(order_id=order_id).exists():
     #            self.order_id = order_id

     #        super(Order, self).save(*args, **kwargs)
     


class Status(models.Model): # it is for shop
     tyres = models.ForeignKey(Tyre, on_delete= models.CASCADE)
     # options for time period
     # options for search by size or name or both
     # overall stock, sold, bought info
     #   
     def __str__(self):
         return self.name 


class Scanner(models.Model):
    code = models.CharField(max_length=10, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
     
    
          