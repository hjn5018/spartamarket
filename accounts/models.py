from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    follow = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='follower',
    )
    image = models.ImageField(
        upload_to='User_images/',
        blank=True,
    )