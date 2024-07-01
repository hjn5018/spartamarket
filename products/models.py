from django.db import models
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='product',
    )
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like',
    )

    def __str__(self):
        return self.title