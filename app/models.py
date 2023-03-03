from django.contrib.auth.models import AbstractUser
from django.db import models

# # Create your models here.
class district(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Area(models.Model):
    district_name=models.ForeignKey(district,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    def __str__(self):
        template='{0.district_name},{0.name}'
        return template.format(self)


class Login(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_dealer=models.BooleanField(default=False)
    name=models.CharField(max_length=25,null=True)
    phone=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True)
    district_name=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='profile',null=True)

class BookCatogeory(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    type=models.ForeignKey(BookCatogeory,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='gallery')
    price=models.FloatField(null=True)


class Feedback(models.Model):
    customer=models.ForeignKey(Login,on_delete=models.CASCADE)
    title=models.CharField(max_length=30,null=True)
    feedback=models.TextField(null=True)
    reply=models.TextField(null=True)
    date=models.DateField(null=True)

class Payment(models.Model):
    name=models.ForeignKey(Login,on_delete=models.CASCADE)
    bill_date=models.DateField(null=True)
    amount=models.IntegerField()
    paid_on=models.DateField(null=True)
    status=models.IntegerField(default=True)

class creditcard(models.Model):
    Payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    card_no=models.CharField(max_length=30)
    Card_cvv=models.CharField(max_length=30)
    expiry_date=models.DateField(max_length=300)
