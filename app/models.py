from django.db import models

from datetime import datetime
from django.contrib import admin #добавили использование административного модуля
from django.shortcuts import reverse
from django.core.urlresolvers import reverse 
from decimal import Decimal

from django.contrib.auth.models import User

from django.conf import settings





# Create your models here.



# Модель данных Блога
class Post(models.Model):
    title = models.CharField(max_length = 120, db_index=True, verbose_name = "Заголовок:")
    description = models.TextField(verbose_name = "Краткое содержание:")
    content = models.TextField(verbose_name = "Полное содержание:")
    date_posted = models.DateTimeField(default = datetime.now(), verbose_name = "Опубликована:")
    image = models.FileField(default = 'temp.jpg', verbose_name ="Путь к картинке:")


    def get_absolute_url(self): # метод возвращает строку с уникальным интернет-адресом записи
        return reverse('blogpost', kwargs = {'id': self.id})

    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.title

    class Meta: # метаданные – вложенный класс, который задает дополнительные параметры модели:
        db_table = "Posts" # имя таблицы для модели
        ordering = ["-date_posted"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "Cтатья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "Cтатьи блога" # тоже для всех статей


class Comment(models.Model):
    text = models.TextField(verbose_name = "Текст комментария")
    date_posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата комментария")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = "Статья")

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям блога"
        ordering = ["-date_posted"]




class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Имя")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})



def image_folder(instance, filename):
        filename = instance.slug + '.' + filename.split('.')[1]
        return "{0}/{1}".format(instance.slug, filename)



class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)



class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})



class CartItem(models.Model):
    product = models.ForeignKey(Product)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product {0}".format(self.product.title)



class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self 
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
    
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()
        


    def remove_from_cart(self, product_slug):
        cart = self 
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()
        
    def change_qty(self,qty,item_id):
        cart = self
        cart_item = CartItem.objects.get(id=int(item_id))
        cart_item.qty = int(qty)
        cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
        cart_item.save()
        new_cart_total = 0.00
        for item in cart.items.all():
            new_cart_total += float(item.item_total)
        cart.cart_total = new_cart_total
        cart.save()



ORDER_STATUS_CHOICES = (
    ('Принят в обработку', 'Принят в обработку'),
    ('Выполняется', 'Выполняется'),
    ('Готов', 'Готов'),
    ('Оплачен', 'Оплачен')
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    items = models.ManyToManyField(Cart)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    buying_type = models.CharField(max_length=40, choices=(('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')))
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES)
    size = models.CharField(max_length=20)

    def __str__(self):
        return "Заказ №{0}".format(str(self.id))
    








admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)

