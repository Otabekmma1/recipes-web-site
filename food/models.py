from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategoriya")
    photo = models.ImageField(upload_to='img/', verbose_name="Rasm")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['name']


class Recipes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Retsept nomi")
    content = models.TextField(verbose_name="Matni")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya", related_name='post')
    photo = models.ImageField(verbose_name="Rasmi", upload_to='img/', null=True, blank=True)
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Retsept'
        verbose_name_plural = 'Retseptlar'
        ordering = ['-created', 'name']



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    addres = models.CharField(max_length=100, verbose_name="Manzil", null=True, blank=True)
    phone = models.CharField(max_length=14, verbose_name="Telefon raqam", null=True, blank=True)
    chrome = models.CharField(max_length=150, verbose_name="Sayt", null=True, blank=True)
    instagram = models.CharField(max_length=150, null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    photo = models.ImageField(upload_to='profile/', null=True, blank=True)



    def __str__(self):
        return f"{self.user.username}"



