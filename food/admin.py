from django.contrib import admin
from .models import Category,FoodItem,Order

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','price','available')
    list_filter = ('category','available')
    search_fields = ('name'),

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name','total_amount','order_date','status')
    list_filter = ('status'),
