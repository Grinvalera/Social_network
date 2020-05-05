from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=128)
    _password = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=32)
    _password2 = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Люди'
# Create your models here.
