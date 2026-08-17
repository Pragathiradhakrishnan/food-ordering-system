from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(upload_to='food/')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Preparing','Preparing'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    ]
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    food_items = models.TextField()
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='Pending')
    def __str__(self):
        return self.customer_name
