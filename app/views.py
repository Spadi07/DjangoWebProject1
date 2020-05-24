from django.shortcuts import render,redirect
from datetime import datetime


#3работа
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

#4работа
from django.db import models
from .models import Post

#5работа
from .models import Comment
from .forms import CommentForm, PostFormfrom .models import Category, Product, CartItem, Cart, Orderfrom django.contrib.auth.models import User, Group#Для корзиныfrom django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

#Для динамического изменения цены в корзине
from decimal import Decimal

from .forms import OrderForm


def home(request):
    return render(
        request,
        'app/index.html'
    )

def about(request):
    return render(
        request,
        'app/about.html'
    )

def contact(request):
    return render(
        request,
        'app/contact.html'
    )

def links(request):
    return render(
        request,
        'app/links.html'
    )

def xxx(request):
    return render(
        request,
        'app/xxx.html'
    )

def summer(request):
    return render(
        request,
        'app/summer.html'
    )

def winter(request):
    return render(
        request,
        'app/winter.html'
    )

def off_season(request):
    return render(
        request,
        'app/off_season.html'
    )




def menu(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(
        request,
        'app/menu.html',
        context = { 'categories': categories, 'products': products, 'cart': cart}
    )



def product_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()

    return render(
        request,
        'app/product.html',
        context = {'product': product, 'categories': categories, 'cart': cart}
    )



def category_view(request, category_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)

    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    categories = Category.objects.all()

    return render(
        request,
        'app/category.html',
        context = {'category': category, 'products_of_category': products_of_category, 'categories': categories, 'cart': cart}
    )

def cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    

    return render(
        request,
        'app/cart.html',
        context = {'cart': cart, 'categories': categories}
    )


def add_to_cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})




def remove_from_cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})

    

def change_item_qty(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart.change_qty(qty, item_id)
    cart_item = CartItem.objects.get(id=int(item_id))
    return JsonResponse({"cart_total": cart.items.count(), 
                         "item_total": cart_item.item_total,
                         'cart_total_price': cart.cart_total})

def checkout_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()

    return render(
        request,
        'app/checkout.html',
        context = {'cart': cart, 'categories': categories}
    )


def order_create_view(request):
    if request.method == "POST":
        cart_id = request.session['cart_id']
        form = OrderForm(request.POST)
        if form.is_valid:
            order_f = form.save(commit=False)
            order_f.user = request.user    
            order_f.status = 'Принят в обработку'
            order_f.save()
            cart = Cart.objects.filter(id = cart_id)
            order_f.items = cart
            order_f.total = Cart.objects.get(id=cart_id).cart_total
            order_f.save()
            del request.session['cart_id']
        return redirect('menu')
    else:
        try:
            cart_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            request.session['total'] = cart.items.count()
        except:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            request.session['cart_id'] = cart_id
            cart = Cart.objects.get(id=cart_id)
        categories = Category.objects.all()
        form = OrderForm()

        return render(
            request,
            'app/order.html',
            context = {'cart': cart, 'categories': categories, 'form': form}
        )



def client_orders(request):
    orders = Order.objects.filter(user = request.user)
    return render(
        request,
        'app/orders.html',
        context = {'orders': orders}
    )

   
def manager_orders(request):
    orders = Order.objects.all()
    return render(
        request,
        'app/orders.html',
        context = {'orders': orders}
    )


def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('menu')


def edit_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid:
            order_f = form.save(commit=False)
            order_f.save()
        return redirect('menu')
    else:
        form = OrderForm(instance=order)
        return render(
            request,
            'app/edit-order.html',
            context = {'form': form}
        )





 






#3работа

def registration(request):
    if request.method == "POST": #вызов метода POST (происходит при отправке формы)
        regform = UserCreationForm(request.POST) #создание формы
        if regform.is_valid(): #проверка на валидность
            reg_f = regform.save(commit=False) #получение данных из формы регистрации
            reg_f.is_staff = False #заполнение данных для пользователей в БД
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            user = User.objects.get(username = request.POST['username']);
            group = Group.objects.get(name = 'Client')
            user.groups.add(group)
            user.save()
            return redirect('home')
        else: #при неверном заполнении
            regform = UserCreationForm()
            return render(
            request,
            'app/registration.html',
            {
             'error': 'Пожалуйста, введите корректные данные!', #передача ошибки в шаблон
             'regform': regform, #передача формы в шаблон
            })
    else: #если вызывается не метод POST
        regform = UserCreationForm() #создание формы
        return render(
            request,
            'app/registration.html',
            {
             'regform': regform, #передача формы в шаблон
            })


 #4работа
def blog(request):
    posts = Post.objects.order_by('-date_posted') # запрос на выбор всех статей из модели, отсортированных по убыванию даты опубликования
    return render(
        request,
        'app/blog.html',
        context={'posts': posts}
        )def blogpost(request,id):
    post = Post.objects.get(id=id) ##тоже самое, но не все посты, а один, id которого равен id из адресной строки
    comments = Comment.objects.filter(post=post) 
    if request.method == "POST": #создание формы для оставления комментов (как в регистрации)
        form = CommentForm(request.POST)
        if form.is_valid:
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = post
            comment_f.save()
            return redirect('blogpost',id = post.id)
    else:
        form = CommentForm()
        return render(
            request,
            'app/blogpost.html',
            context={'post': post, 'form': form, 'comments': comments}
            )

#6работа
def newpost(request):
    if request.method == "POST": ##аналогично для создания постов
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post_f = form.save(commit=False)
            post_f.date_posted = datetime.now()
            post_f.save()
            return redirect('blogpost',id = post_f.id)
    else:
        form = PostForm()
        return render(
            request,
            'app/newpost.html',
            context={'form': form }
            )