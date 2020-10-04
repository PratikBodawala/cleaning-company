from datetime import timedelta

from django.contrib.auth.models import AbstractUser, User
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils import timezone


class City(models.Model):
    name = models.CharField(unique=True, max_length=35)

    class Meta:
        verbose_name_plural = 'Cities'

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(City, self).save_base(True)

    def __str__(self):
        return self.name


class Cleaner(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} - {self.city}'


class Customer(models.Model):
    phone = models.BigIntegerField(unique=True, validators=[
        validators.MaxValueValidator(9_999_999_999),
        validators.MinValueValidator(6_000_000_000)  # update minvalue when new series number available

    ])
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)


class Appointment(models.Model):
    start_datetime = models.DateTimeField(validators=[
        validators.MinValueValidator(timezone.now() + timedelta(hours=1)),  # at least 1 hour before
        # validators.MaxValueValidator(timezone.now()+timedelta(days=30))  # when only 30 days prior booking
    ])
    end_datetime = models.DateTimeField(validators=[
        validators.MinValueValidator(timezone.now() + timedelta(minutes=15)),
        # suppose we have min 15 min of appointment
        # validators.MaxValueValidator(timezone.now()+timedelta(days=30))  # when only 30 days prior booking
    ])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cleaner = models.ForeignKey(Cleaner, on_delete=models.PROTECT)

    def clean(self):
        if self.start_datetime > self.end_datetime:
            raise ValidationError({'end_datetime': ['End date should not be less than start date.']})

    # TODO start end validation
