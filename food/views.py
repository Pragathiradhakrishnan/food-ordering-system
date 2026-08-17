from .forms import OrderForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodItem, Category, Order


# Create your views here.

def home(request):
    foods = FoodItem.objects.filter(available=True)
    return render(request,'food/home.html',{'foods':foods})

def menu(request):
    categories = Category.objects.all()
    foods = FoodItem.objects.filter(available=True)
    category_id = request.GET.get('category')
    if category_id:
        foods = foods.filter(category_id=category_id)

    return render(request,'food/menu.html',{'foods':foods,'categories':categories,})

def food_detail(request,food_id):
    food = get_object_or_404(FoodItem,id=food_id,available=True)
    return render(request,'food/food_detail.html',{'food':food})

def add_to_cart(request, food_id):
    cart = request.session.get('cart', {})
    food_id = str(food_id)
    if food_id in cart:
        cart[food_id] += 1
    else:
        cart[food_id] = 1
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for food_id, quantity in cart.items():
        food = get_object_or_404(FoodItem,id=food_id)
        subtotal = food.price * quantity
        cart_items.append({'food': food,'quantity': quantity,'subtotal': subtotal,})
        total += subtotal
    return render(request,'food/cart.html',{'cart_items': cart_items,'total': total,})

def update_cart(request, food_id, action):
    cart = request.session.get('cart', {})
    food_id = str(food_id)
    if food_id in cart:
        if action == 'increase':
            cart[food_id] += 1
        elif action == 'decrease':
            cart[food_id] -= 1
            if cart[food_id] <= 0:
                del cart[food_id]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')

def remove_from_cart(request, food_id):
    cart = request.session.get('cart', {})
    food_id = str(food_id)
    if food_id in cart:
        del cart[food_id]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
    cart_items = []
    total = 0
    for food_id, quantity in cart.items():
        food = get_object_or_404(FoodItem,id=food_id)
        subtotal = food.price * quantity
        cart_items.append({
            'food': food,
            'quantity': quantity,
            'subtotal': subtotal,
        })
        total += subtotal
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            food_details = []
            for item in cart_items:
                food_details.append(
                    f"{item['food'].name} x {item['quantity']}"
                )
            order.food_items = ", ".join(food_details)
            order.total_amount = total
            order.save()
            request.session['cart'] = {}
            return redirect(
                'order_success',
                order_id=order.id
            )
    else:
        form = OrderForm()
    return render(
        request,
        'food/checkout.html',
        {
            'form': form,
            'cart_items': cart_items,
            'total': total,
        }
    )

def order_success(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id
    )
    return render(
        request,
        'food/order_success.html',
        {'order': order}
    )