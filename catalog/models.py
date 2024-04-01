from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Seller(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Promocode(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    is_cumulative = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    description = models.TextField()
    count_on_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.article}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f'Image for {self.product.name}'


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class Order(models.Model):
    STATUSES = (
        ('In Process', 'In Process'),
        ('Packed', 'Packed'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Received', 'Received'),
        ('Refused', 'Refused')
    )
    DELIVERY_METHODS = (
        ('Courier', 'Courier'),
        ('Post', 'Post'),
        ('Self-delivery', 'Self-delivery')
    )
    PAYMENT_METHODS = (
        ('Card Online', 'Card Online'),
        ('Card Offline', 'Card Offline'),
        ('Cash', 'Cash')
    )
    PAYMENT_STATUSES = (
        ('Paid', 'Paid'),
        ('In Process', 'In Process'),
        ('Canceled', 'Canceled')
    )
    NOTIF_TIMES = (
        (24, 24),
        (6, 6),
        (1, 1)
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUSES)

    delivery_address = models.CharField(max_length=250, null=True, blank=True)
    delivery_methods = models.CharField(choices=DELIVERY_METHODS, max_length=100, null=True, blank=True)

    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=100)
    payment_status = models.CharField(choices=PAYMENT_STATUSES, max_length=100,
                                      default='In Process')
    delivery_notification_before = models.PositiveIntegerField(choices=NOTIF_TIMES, default=6)

    def __str__(self):
        return f'{self.user.name} - {self.id}'


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class CashBack(models.Model):
    percent = models.PositiveIntegerField()
    treshold = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.percent}%'
