from django.db import models

# Create your models here.


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

