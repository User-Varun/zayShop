from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

class Customer(models.Model):
    cname = models.CharField(max_length=30)
    cadd = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    unm = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)


class ImageUploader(models.Model):
    photo = models.ImageField(upload_to='AllImages')
    name = models.CharField(max_length=30 , default="")
    price = models.FloatField(default=0.0)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=now)



class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=30, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.product.title}"