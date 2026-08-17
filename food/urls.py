from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('menu/', views.menu, name='menu'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/update/<int:food_id>/<str:action>/',views.update_cart,name='update_cart'),
    path('cart/remove/<int:food_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/',views.order_success,name='order_success'),
]